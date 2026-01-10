import { Container, Typography } from "@mui/material";
import type React from "react";
import { useCallback, useEffect, useRef, useState } from "react";
import {API_BASE, type ChatMessage, type Source} from "./api";
import { streamCompletion } from "./api";
import { ChatWindow } from "./components/ChatWindow.tsx";
import { InputBar } from "./components/InputBar.tsx";

export const App: React.FC = () => {
    const [history, setHistory] = useState<ChatMessage[]>([]);
    const [current, setCurrent] = useState<{
        content: string;
        sources?: Source[];
    } | null>(null);
    const currentRef = useRef<{ content: string; sources?: Source[] } | null>(null); // new
    const [input, setInput] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const abortRef = useRef<AbortController | null>(null);

    useEffect(() => {
        return () => {
            // cleanup on unmount
            abortRef.current?.abort();
        };
    }, []);

    const sendQuestion = useCallback(async (question: string) => {
        setError(null);
        setLoading(true);
        setHistory((s) => [...s, { role: "user", content: question }]);
        const initialCurrent = { content: "", sources: [] as Source[] };
        setCurrent(initialCurrent);
        currentRef.current = initialCurrent;

        const controller = new AbortController();
        abortRef.current = controller;

        try {
            await streamCompletion(
                question,
                {
                    onToken: (token) => {
                        setCurrent((prev) => {
                            const next = prev ? { ...prev, content: prev.content + token } : { content: token, sources: [] };
                            currentRef.current = next;
                            return next;
                        });
                    },
                    onDone: (sources) => {
                        const content = currentRef.current?.content ?? "";
                        setHistory(h => [
                            ...h,
                            {
                                role: "assistant",
                                content,
                                sources,
                            },
                        ]);
                        setCurrent(null);
                        setLoading(false);
                    },
                    onError: (err) => {
                        setError(err.message);
                        setLoading(false);
                        setCurrent(null);
                        currentRef.current = null;
                    },
                },
                controller.signal,
            );
        } catch (err) {
            // errors already handled in onError; guard fallback
            setError((err as Error)?.message ?? String(err));
            setLoading(false);
            setCurrent(null);
        } finally {
            abortRef.current = null;
        }
    }, []);

    const onSend = useCallback(() => {
        const q = input.trim();
        if (!q || loading) return;
        setInput("");
        void sendQuestion(q);
    }, [input, loading, sendQuestion]);

    const onKeyDown = useCallback(
        (e: React.KeyboardEvent<HTMLDivElement>) => {
            if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                onSend();
            }
        },
        [onSend],
    );

    return (
        <Container maxWidth="md" sx={{ pt: 3, pb: 3 }}>
            <Typography variant="h5" sx={{ mb: 2 }}>
                notes.mgarbowski.pl - RAG
            </Typography>

            <ChatWindow
                history={history}
                current={current}
                loading={loading}
                error={error}
                height={480}
            />

            <InputBar
                value={input}
                onChange={setInput}
                onSend={onSend}
                disabled={loading}
                onKeyDown={onKeyDown}
            />

            <Typography variant="caption" color="text.secondary" sx={{ mt: 1 }}>
                API: {API_BASE}
            </Typography>
        </Container>
    );
};
