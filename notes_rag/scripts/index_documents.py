"""Calculate embeddings for processed note chunks

Calculates BM25 and sdadas/mmlw-retrieval-roberta-large embeddings
Stores them separately in JSON files
"""

import argparse
import json
import string
from pathlib import Path

from dataclasses import dataclass

from rank_bm25 import BM25Okapi
from stop_words import get_stop_words


@dataclass(frozen=True)
class Config:
    chunks_file: Path
    output_dir: Path


class BM25Retriever:
    def __init__(self):
        self._stop_words = get_stop_words("polish")

    def tokenize(self, text: str) -> list[str]:
        tokens = []
        raw_tokens = text.lower().strip().split()
        for token in raw_tokens:
            for punc in string.punctuation:
                token = token.replace(punc, "")
            if token in self._stop_words:
                continue
            if token == "":
                continue
            tokens.append(token)
        return tokens

    def process_corpus(self, corpus: list[str]) -> None:
        tokenized_corpus = [self.tokenize(doc) for doc in corpus]
        bm25 = BM25Okapi(tokenized_corpus)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--chunks_file",
        type=Path,
        default=Path("data/processed/chunked_notes/chunked_notes.json"),
        help="Path to input JSON file",
    )
    parser.add_argument(
        "--output_dir",
        type=Path,
        default=Path("data/processed/index"),
        help="Directory to save computed indices",
    )

    args = parser.parse_args()
    cfg = Config(
        chunks_file=args.chunks_file,
        output_dir=args.output_dir,
    )

    chunks = json.loads(cfg.chunks_file.read_text())
    print(chunks[0])
    corpus = [chunk["content"] for chunk in chunks]
    bm25 = BM25Retriever()
    bm25.process_corpus(corpus)


if __name__ == "__main__":
    main()
