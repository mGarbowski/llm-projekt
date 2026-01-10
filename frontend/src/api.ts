export type Role = "user" | "assistant";
export type Source = {
    id: string;
    content: string;
    course: string;
    title: string;
    filename: string;
};
export type ChatMessage = {
    role: Role;
    content: string;
    sources?: Source[];
};

export const API_BASE = "http://localhost:8000";

type Callbacks = {
    onToken: (token: string) => void;
    onDone: (sources: Source[]) => void;
    onError: (err: Error) => void;
};

export async function streamCompletion(
    question: string,
    callbacks: Callbacks,
    signal?: AbortSignal,
): Promise<void> {
    const controller = new AbortController();
    const combinedSignal = signal ?? controller.signal;

    try {
        const res = await fetch(`${API_BASE}/completion/stream`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({question}),
            signal: combinedSignal,
        });
        if (!res.ok) {
            const text = await res.text().catch(() => "");
            throw new Error(text || `HTTP ${res.status}`);
        }

        const reader = res.body?.getReader();
        if (!reader) {
            throw new Error("No streaming body");
        }

        const decoder = new TextDecoder();
        let buffer = "";

        while (true) {
            const {value, done} = await reader.read();
            if (done) break;
            buffer += decoder.decode(value, {stream: true});

            let idx: number;
            // biome-ignore lint/suspicious/noAssignInExpressions: <TODO refactor>
            while ((idx = buffer.indexOf("\n\n")) !== -1) {
                const raw = buffer.slice(0, idx);
                buffer = buffer.slice(idx + 2);

                const lines = raw.split(/\r?\n/);
                let event = "message";
                const dataLines: string[] = [];
                for (const line of lines) {
                    if (line.startsWith("event:")) event = line.slice(6).trim();
                    else if (line.startsWith("data:"))
                        dataLines.push(line.slice(5).trim());
                }
                const dataStr = dataLines.join("\n");

                if (event === "done") {
                    try {
                        const parsed = JSON.parse(dataStr);
                        callbacks.onDone(parsed.sources ?? []);
                    } catch (e) {
                        // if parsing fails, just notify error
                        callbacks.onError?.(
                            e instanceof Error ? e : new Error(String(e)),
                        );
                    }
                } else {
                    // token message
                    try {
                        const tokenOrObj = JSON.parse(dataStr);
                        // if server sends JSON string tokens or objects containing text
                        if (typeof tokenOrObj === "string")
                            callbacks.onToken(tokenOrObj);
                        else if (
                            typeof tokenOrObj === "object" &&
                            tokenOrObj !== null &&
                            "text" in tokenOrObj
                        )
                            // biome-ignore lint/suspicious/noExplicitAny: <TODO refactor>
                            callbacks.onToken(String((tokenOrObj as any).text));
                        else callbacks.onToken(String(tokenOrObj));
                    } catch {
                        // raw text chunk
                        callbacks.onToken(dataStr);
                    }
                }
            }
        }


    } catch (err) {
        // biome-ignore lint/suspicious/noExplicitAny: <TODO refactor>
        if ((err as any)?.name === "AbortError") {
            callbacks.onError?.(new Error("Streaming aborted"));
            return;
        }
        callbacks.onError?.(
            err instanceof Error ? err : new Error(String(err)),
        );
        throw err;
    }
}
