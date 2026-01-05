// `frontend/src/components/ChatWindow.tsx`

import { Box, Divider, Typography } from "@mui/material";
import type React from "react";
import { useEffect, useRef } from "react";
import type { ChatMessage } from "./api";
import { MessageBubble } from "./MessageBubble";

type Props = {
	history: ChatMessage[]; // finished messages
	current?: { content: string; sources?: any[] } | null; // generating assistant message
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

	useEffect(() => {
		scrollerRef.current?.scrollTo({
			top: scrollerRef.current.scrollHeight,
			behavior: "smooth",
		});
	}, [history.length, current?.content, loading]);

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
					key={i}
					role={m.role}
					content={m.content}
					sources={m.sources}
				/>
			))}

			{current && (
				<MessageBubble
					role="assistant"
					content={current.content}
					sources={current.sources}
				/>
			)}

			{loading && <Typography color="text.secondary">Generating…</Typography>}
			{error && (
				<>
					<Divider sx={{ my: 1 }} />
					<Typography color="error">Error: {error}</Typography>
				</>
			)}
		</Box>
	);
};
