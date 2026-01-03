import json
from pathlib import Path

from sqlalchemy.orm import Session

from notes_rag.core.schema import get_engine, Base, NoteChunk


def main():
    engine = get_engine()
    Base.metadata.create_all(engine)
    chunks = json.loads(Path("data/processed/chunked_notes/chunked_notes.json").read_text())

    records = [
        NoteChunk(
            content=chunk["content"],
            course=chunk["course"],
            filename=chunk["filename"],
            title=chunk["title"],
            number=chunk["number"],
        ) for chunk in chunks]
    with Session(engine) as session:
        session.add_all(records)
        session.commit()


if __name__ == "__main__":
    main()