import { Container, Typography } from "@mui/material";
import type React from "react";
import { useCallback, useEffect, useRef, useState } from "react";
import type { ChatMessage, Source } from "./api";
import { streamCompletion } from "./api";
import { ChatWindow } from "./ChatWindow";
import { InputBar } from "./InputBar";

export const App: React.FC = () => {
	const [history, setHistory] = useState<ChatMessage[]>([]);
	const [current, setCurrent] = useState<{
		content: string;
		sources?: Source[];
	} | null>(null);
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
		// append user message to history
		setHistory((s) => [...s, { role: "user", content: question }]);
		setCurrent({ content: "", sources: [] });

		const controller = new AbortController();
		abortRef.current = controller;

		try {
			await streamCompletion(
				question,
				{
					onToken: (token) => {
						setCurrent((prev) => {
							if (!prev) return { content: token, sources: [] };
							return { ...prev, content: prev.content + token };
						});
					},
					onDone: (sources) => {
						setCurrent((prev) => {
							const final = { content: prev?.content ?? "", sources };
							// push finished assistant message into history
							setHistory((h) => [
								...h,
								{
									role: "assistant",
									content: final.content,
									sources: final.sources,
								},
							]);
							return null;
						});
						setLoading(false);
					},
					onError: (err) => {
						setError(err.message);
						setLoading(false);
						setCurrent(null);
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
		(e: React.KeyboardEvent<HTMLTextAreaElement>) => {
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
				RAG Chat (streaming)
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
				Using API: http://localhost:8000
			</Typography>
		</Container>
	);
};
