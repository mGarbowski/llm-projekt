import Markdown from "react-markdown";
import rehypeKatex from "rehype-katex";
import remarkMath from "remark-math";

type Props = {
    text: string;
};

export const MarkdownText = ({ text }: Props) => (
    <Markdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>
        {text}
    </Markdown>
);
