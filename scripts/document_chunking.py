"""Script to split all documents in notes dataset into chunks with relevant metadata."""

import argparse
import re
import json
import uuid
from pathlib import Path
from dataclasses import dataclass, asdict
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter


@dataclass(frozen=True)
class Config:
    input_dir: Path
    output_dir: Path
    chunk_size: int
    chunk_overlap: int


@dataclass(frozen=True)
class DocumentChunk:
    id: str
    content: str
    filename: str
    course: str
    title: str
    number: int



class DocumentChunker:
    def __init__(self, config: Config):
        self.config = config

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.config.chunk_size,
            chunk_overlap=self.config.chunk_overlap,
        )

    def generate_id(self) -> str:
        return str(uuid.uuid4())

    def extract_title(self, content: str) -> str | None:
        """Extract from first H1 header or fallback to first line."""
        md_title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
        if md_title_match:
            return md_title_match.group(1).strip()

        first_line = content.splitlines()[0].strip()
        if first_line:
            return first_line

        return None

    def chunk_document(self, doc_path: Path) -> list[DocumentChunk]:
        print("Chunking document:", doc_path)

        with open(doc_path, "r", encoding="utf-8") as f:
            content = f.read()

        filename = doc_path.stem
        course = doc_path.parent.name
        title = self.extract_title(content) or filename

        text_splits = self.text_splitter.split_text(content)
        print(f"Generated {len(text_splits)} chunks for document: {filename}")
        return [
            DocumentChunk(
                id=self.generate_id(),
                content=chunk,
                filename=filename,
                course=course,
                title=title,
                number=idx,
            )
            for idx, chunk in enumerate(text_splits)
        ]

    def process_course_dir(self, course_dir: Path) -> list[DocumentChunk]:
        print("Processing course directory:", course_dir)
        all_chunks = []
        for doc_path in course_dir.glob("*.md"):
            doc_chunks = self.chunk_document(doc_path)
            all_chunks.extend(doc_chunks)

        print(f"Processed {len(all_chunks)} chunks from {course_dir.name}")
        return all_chunks

    def process_dataset(self) -> list[DocumentChunk]:
        all_chunks = []
        for course_dir in self.config.input_dir.iterdir():
            if course_dir.is_dir():
                course_chunks = self.process_course_dir(course_dir)
                all_chunks.extend(course_chunks)
        return all_chunks


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input",
        type=str,
        nargs="?",
        default="data/raw/notes",
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
        default=700,
        help="Size of each text chunk (default: 250 characters)"
    )

    parser.add_argument(
        "--chunk_overlap",
        type=int,
        default=20,
        help="Overlap between text chunks (default: 20 characters)"
    )

    args = parser.parse_args()
    config = Config(
        input_dir=Path(args.input),
        output_dir=Path(args.output),
        chunk_size=args.chunk_size,
        chunk_overlap=args.chunk_overlap
    )

    chunker = DocumentChunker(config)
    all_chunks = chunker.process_dataset()
    config.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = config.output_dir / "chunked_notes.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump([asdict(chunk) for chunk in all_chunks], f, ensure_ascii=False, indent=2)
    print(f"Chunked {len(all_chunks)} document chunks saved to {output_path}")


if __name__ == "__main__":
    main()
