import { Box, Divider, Typography } from "@mui/material";
import type React from "react";
import { useEffect, useRef } from "react";
import type { ChatMessage } from "./api";
import { MessageBubble } from "./MessageBubble";

type Props = {
    history: ChatMessage[];
    // biome-ignore lint/suspicious/noExplicitAny: <TODO specify request and response types>
    current?: { content: string; sources?: any[] } | null;
    loading: boolean;
    error?: string | null;
    height?: number;
};

export const ChatWindow: React.FC<Props> = ({
    history,
    current,
    loading,
    error,
    height = 480,
}) => {
    const scrollerRef = useRef<HTMLDivElement | null>(null);

    // biome-ignore lint/correctness/useExhaustiveDependencies: <scroll when content changes>
    useEffect(() => {
        scrollerRef.current?.scrollTo({
            top: scrollerRef.current.scrollHeight,
            behavior: "smooth",
        });
    }, [current]);

    return (
        <Box
            sx={{
                border: "1px solid #ddd",
                borderRadius: 1,
                p: 2,
                height,
                overflowY: "auto",
                bgcolor: "#fafafa",
            }}
            ref={scrollerRef}
        >
            {history.length === 0 && (
                <Typography color="text.secondary">
                    Ask a question to start the conversation.
                </Typography>
            )}
            {history.map((m, i) => (
                <MessageBubble
                    // biome-ignore lint/suspicious/noArrayIndexKey: <no suitable identifier>
                    key={i}
                    chatRole={m.role}
                    content={m.content}
                    sources={m.sources}
                />
            ))}

            {current && (
                <MessageBubble
                    chatRole="assistant"
                    content={current.content}
                    sources={current.sources}
                />
            )}

            {loading && (
                <Typography color="text.secondary">Generating…</Typography>
            )}
            {error && (
                <>
                    <Divider sx={{ my: 1 }} />
                    <Typography color="error">Error: {error}</Typography>
                </>
            )}
        </Box>
    );
};
