import { Box, Paper, Typography } from "@mui/material";
import type React from "react";
import type { Role, Source } from "./api";
import { MarkdownText } from "./components/MarkdownText.tsx";
import { Sources } from "./components/Sources.tsx";

type Props = {
    chatRole: Role;
    content: string;
    sources?: Source[];
};

export const MessageBubble: React.FC<Props> = ({
    chatRole,
    content,
    sources,
}) => {
    const bg = chatRole === "user" ? "#e9f2ff" : "#fff";
    return (
        <Box sx={{ mb: 2 }}>
            <Typography
                variant="caption"
                color="text.secondary"
                sx={{ mb: 0.5 }}
            >
                {chatRole === "user" ? "You" : "Assistant"}
            </Typography>
            <Paper elevation={1} sx={{ p: 1.5, background: bg }}>
                <MarkdownText text={content} />
            </Paper>

            {chatRole === "assistant" && sources && sources.length > 0 && (
                <Sources sources={sources} />
            )}
        </Box>
    );
};
