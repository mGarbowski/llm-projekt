import React, { useCallback, useMemo, useState } from "react";
import Markdown from "react-markdown";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";

type Role = "user" | "assistant";
type Source = {
  id: string;
  content: string;
  course: string;
  title: string;
  filename?: string | null;
};
const API_BASE: string = "http://localhost:8000";

type ChatMessage = {
  role: Role;
  content: string;
  sources?: Source[];
};

export const App: React.FC = () => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const canSend = useMemo(() => input.trim().length > 0 && !loading, [input, loading]);

  const sendQuestionStream = useCallback(
    async (question: string) => {
      setError(null);
      setLoading(true);

      // append an empty assistant message that we will update incrementally
      setMessages((prev) => [...prev, { role: "assistant", content: "", sources: [] }]);

      try {
        const res = await fetch(`${API_BASE}/completion/stream`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ question }),
        });
        if (!res.ok) {
          const text = await res.text().catch(() => "");
          throw new Error(text || `HTTP ${res.status}`);
        }

        const reader = res.body?.getReader();
        if (!reader) throw new Error("No streaming body");

        const decoder = new TextDecoder();
        let buffer = "";

        while (true) {
          const { value, done } = await reader.read();
          if (done) break;
          buffer += decoder.decode(value, { stream: true });

          let idx: number;
          while ((idx = buffer.indexOf("\n\n")) !== -1) {
            const raw = buffer.slice(0, idx);
            buffer = buffer.slice(idx + 2);

            // parse SSE block
            const lines = raw.split(/\r?\n/);
            let event = "message";
            const dataLines: string[] = [];
            for (const line of lines) {
              if (line.startsWith("event:")) event = line.slice(6).trim();
              else if (line.startsWith("data:")) dataLines.push(line.slice(5).trim());
            }
            const dataStr = dataLines.join("\n");

            if (event === "done") {
              try {
                const parsed = JSON.parse(dataStr);
                setMessages((prev) => {
                  const next = [...prev];
                  const last = next[next.length - 1];
                  next[next.length - 1] = { ...last, sources: parsed.sources };
                  return next;
                });
              } catch (err) {
                // ignore parse errors for done payload
              }
            } else {
              // normal token message: data contains a json-encoded token string
              try {
                const token = JSON.parse(dataStr);
                setMessages((prev) => {
                  const next = [...prev];
                  const last = next[next.length - 1];
                  next[next.length - 1] = { ...last, content: last.content + token };
                  return next;
                });
              } catch (err) {
                // if not JSON, append raw chunk
                setMessages((prev) => {
                  const next = [...prev];
                  const last = next[next.length - 1];
                  next[next.length - 1] = { ...last, content: last.content + dataStr };
                  return next;
                });
              }
            }
          }
        }

        // flush any leftover buffer (unlikely if server uses \n\n terminator)
        if (buffer.length > 0) {
          // attempt to parse leftover as final JSON done or token
          if (buffer.startsWith("event: done")) {
            const rest = buffer.slice("event: done".length).trim();
            const dataMatch = rest.match(/data:\s*(.*)/s);
            if (dataMatch) {
              try {
                const parsed = JSON.parse(dataMatch[1].trim());
                setMessages((prev) => {
                  const next = [...prev];
                  const last = next[next.length - 1];
                  next[next.length - 1] = { ...last, sources: parsed.sources };
                  return next;
                });
              } catch {}
            }
          } else {
            setMessages((prev) => {
              const next = [...prev];
              const last = next[next.length - 1];
              next[next.length - 1] = { ...last, content: last.content + buffer };
              return next;
            });
          }
        }
      } catch (err: unknown) {
        const message = err instanceof Error ? err.message : String(err);
        setError(message || "Request failed");
      } finally {
        setLoading(false);
      }
    },
    []
  );

  const onSubmit = useCallback(
    async (e: React.FormEvent) => {
      e.preventDefault();
      if (!canSend) return;
      const question = input.trim();
      setMessages((prev) => [...prev, { role: "user", content: question }]);
      setInput("");
      await sendQuestionStream(question);
    },
    [canSend, input, sendQuestionStream]
  );

  const onKeyDown = useCallback(
    (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        if (canSend) {
          const form = (e.currentTarget.closest("form") as HTMLFormElement | null);
          form?.dispatchEvent(new Event("submit", { cancelable: true, bubbles: true }));
        }
      }
    },
    [canSend]
  );

  return (
    <div style={{ maxWidth: 820, margin: "0 auto", padding: 16, fontFamily: "system-ui, sans-serif" }}>
      <h1 style={{ marginBottom: 12 }}>RAG Chat (streaming)</h1>
      <div style={{ border: "1px solid #ddd", borderRadius: 8, padding: 12, height: 480, overflowY: "auto", background: "#fafafa" }}>
        {messages.length === 0 && <div style={{ color: "#666" }}>Ask a question to start the conversation.</div>}
        {messages.map((m, idx) => (
          <div key={idx} style={{ marginBottom: 14 }}>
            <div style={{ fontSize: 12, color: "#666", marginBottom: 4 }}>{m.role === "user" ? "You" : "Assistant"}</div>
            <div style={{ whiteSpace: "pre-wrap", background: m.role === "user" ? "#e9f2ff" : "#fff", border: "1px solid #e5e5e5", borderRadius: 6, padding: 10 }}>
              <Markdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>{m.content}</Markdown>
            </div>
            {m.role === "assistant" && m.sources && m.sources.length > 0 && (
              <div style={{ marginTop: 6 }}>
                <div style={{ fontSize: 12, color: "#888", marginBottom: 4 }}>Sources:</div>
                <ul style={{ margin: 0, paddingLeft: 18 }}>
                  {m.sources.map((s, i) => (
                    <li key={s.id ?? i} style={{ fontSize: 13 }}>
                      <span style={{ color: "#333" }}>[{i + 1}] {s.title ?? s.id ?? "source"}</span>
                      <div style={{ color: "#666" }}><Markdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>{s.content.length > 220 ? `${s.content.slice(0, 220)}…` : s.content}</Markdown></div>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ))}
        {loading && <div style={{ color: "#666" }}>Generating…</div>}
        {error && <div style={{ color: "crimson" }}>Error: {error}</div>}
      </div>

      <form onSubmit={onSubmit} style={{ marginTop: 12, display: "grid", gap: 8 }}>
        <textarea value={input} onChange={(e) => setInput(e.target.value)} onKeyDown={onKeyDown} rows={3} placeholder="Type your question…" style={{ resize: "vertical", padding: 10, borderRadius: 6, border: "1px solid #ccc", fontFamily: "inherit", fontSize: 14 }} />
        <div style={{ display: "flex", justifyContent: "flex-end", gap: 8 }}>
          <button type="submit" disabled={!canSend} style={{ padding: "8px 14px", borderRadius: 6, border: "1px solid #0a66c2", background: canSend ? "#0a66c2" : "#9cbfe3", color: "#fff", cursor: canSend ? "pointer" : "not-allowed" }}>Send</button>
        </div>
      </form>

      <div style={{ marginTop: 8, fontSize: 12, color: "#777" }}>Using API: {API_BASE || "/completion (same-origin)"}</div>
    </div>
  );
};