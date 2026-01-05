import { Box, List, ListItem, Paper, Typography } from "@mui/material";
import type React from "react";
import Markdown from "react-markdown";
import rehypeKatex from "rehype-katex";
import remarkMath from "remark-math";
import type { Role, Source } from "./api";

type Props = {
	role: Role;
	content: string;
	sources?: Source[];
};

export const MessageBubble: React.FC<Props> = ({ role, content, sources }) => {
	const bg = role === "user" ? "#e9f2ff" : "#fff";
	return (
		<Box sx={{ mb: 2 }}>
			<Typography variant="caption" color="text.secondary" sx={{ mb: 0.5 }}>
				{role === "user" ? "You" : "Assistant"}
			</Typography>
			<Paper elevation={1} sx={{ p: 1.5, background: bg }}>
				<Markdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>
					{content}
				</Markdown>
			</Paper>

			{role === "assistant" && sources && sources.length > 0 && (
				<Box sx={{ mt: 1 }}>
					<Typography variant="caption" color="text.secondary">
						Sources:
					</Typography>
					<List sx={{ pl: 2, mt: 0 }}>
						{sources.map((s, i) => (
							<ListItem key={s.id ?? i} sx={{ py: 0 }}>
								<Box>
									<Typography variant="body2" sx={{ fontWeight: 500 }}>
										[{i + 1}] {s.title ?? s.id ?? "source"}
									</Typography>
									<Typography variant="body2" color="text.secondary">
										{s.content.length > 220
											? `${s.content.slice(0, 220)}…`
											: s.content}
									</Typography>
								</Box>
							</ListItem>
						))}
					</List>
				</Box>
			)}
		</Box>
	);
};
