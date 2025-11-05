"""Script to split all documents in notes dataset into chunks with relevant metadata."""

import argparse
import re
from pathlib import Path
from dataclasses import dataclass
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter

@dataclass(frozen=True)
class Config:
    input_dir: Path
    output_dir: Path
    chunk_size: int
    chunk_overlap: int

@dataclass(frozen=True)
class DocumentChunk:
    content: str
    filename: str
    course: str
    title: str
    other_metadata: dict[str, str]


class DocumentChunker:
    def __init__(self, config: Config):
        self.config = config
        self.markdown_split_headers = [
            ("#", "H1"),
            ("##", "H2"),
            ("###", "H3"),
            ("####", "H4"),
        ]

        self.md_splitter = MarkdownHeaderTextSplitter(
            self.markdown_split_headers,
            strip_headers=False,
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.config.chunk_size,
            chunk_overlap=self.config.chunk_overlap,
        )


    def extract_title(self, content: str) -> str | None:
        # Try to extract title from markdown headers
        md_title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
        if md_title_match:
            return md_title_match.group(1).strip()

        # Fallback: extract title from first line
        first_line = content.splitlines()[0].strip()
        if first_line:
            return first_line

        return None

    def chunk_document(self, doc_path: Path) -> list[DocumentChunk]:
        with open(doc_path, "r", encoding="utf-8") as f:
            content = f.read()

        filename = doc_path.stem
        course = doc_path.parent.name
        title = self.extract_title(content) or filename




def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input",
        type=str,
        help="Input directory containing notes to be chunked"
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        default="data/processed/chunked_notes",
        help="Output directory for chunked notes (default: data/processed/chunked_notes)"
    )

    parser.add_argument(
        "--chunk_size",
        type=int,
        default=1000,
        help="Size of each text chunk (default: 1000 characters)"
    )

    parser.add_argument(
        "--chunk_overlap",
        type=int,
        default=200,
        help="Overlap between text chunks (default: 200 characters)"
    )

    args = parser.parse_args()
    config = Config(
        input_dir=Path(args.input),
        output_dir=Path(args.output),
        chunk_size=args.chunk_size,
        chunk_overlap=args.chunk_overlap
    )

if __name__ == "__main__":
    main()
