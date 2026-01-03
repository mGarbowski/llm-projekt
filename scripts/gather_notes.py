#!/usr/bin/env python3

import shutil
from pathlib import Path
import argparse
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    source_dir: Path
    output_dir: Path

def gather_notes(config: Config):
    source_dir = config.source_dir
    output_dir = config.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    for semester_dir in source_dir.iterdir():
        if not semester_dir.is_dir():
            continue

        for course_dir in semester_dir.iterdir():
            if course_dir.is_dir():
                process_course_dir(course_dir, output_dir)

def process_course_dir(course_dir: Path, output_dir: Path):

    notes_dir = course_dir / "notatki"
    if not notes_dir.is_dir():
        return

    items_to_copy = [item for item in notes_dir.iterdir() if item.is_file() and item.suffix == ".md"]
    if not items_to_copy:
        return

    course_name = course_dir.name
    target_dir = output_dir / course_name
    target_dir.mkdir(parents=True, exist_ok=True)
    for item in items_to_copy:
        shutil.copy2(item, target_dir / item.name)


def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "source",
        type=str,
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="data/raw/notes",
        help="Output directory for organized notes (default: data/raw/notes)"
    )

    args = parser.parse_args()
    config = Config(
        source_dir=Path(args.source),
        output_dir=Path(args.output)
    )

    gather_notes(
        config
    )


if __name__ == "__main__":
    main()

