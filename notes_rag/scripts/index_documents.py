"""Calculate embeddings for processed note chunks

Calculates mmlw-retrieval-roberta-large embeddings
Stores them in a JSON file
"""

import argparse
import json
import string
from pathlib import Path

from dataclasses import dataclass

from sentence_transformers import SentenceTransformer
from tqdm import tqdm


@dataclass(frozen=True)
class Config:
    chunks_file: Path
    output_dir: Path


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
    bi_encoder_model = SentenceTransformer("sdadas/mmlw-retrieval-roberta-base")
    embeddings_map = {
        chunk["id"]: bi_encoder_model.encode(chunk["content"]).tolist()
        for chunk in tqdm(chunks)
    }
    cfg.output_dir.mkdir(parents=True, exist_ok=True)
    embeddings_file = cfg.output_dir / "note_chunk_embeddings.json"
    embeddings_file.write_text(json.dumps(embeddings_map))


if __name__ == "__main__":
    main()
