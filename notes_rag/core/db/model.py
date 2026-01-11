import uuid

from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, UUID, Text, Integer, Engine, text
from sqlalchemy.orm import declarative_base, mapped_column

from notes_rag.core.config import POSTGRES_TEXT_SEARCH_CONFIG

Base = declarative_base()


class NoteChunk(Base):
    __tablename__ = "note_chunks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = Column(Text)
    course = Column(Text)
    filename = Column(Text)
    title = Column(Text)
    number = Column(Integer)
    embedding = mapped_column(Vector(768))

    def __str__(self):
        return f"NoteChunk(id={self.id}, title={self.title}, course={self.course}, number={self.number})"


def create_fulltext_index(engine: Engine):
    sql = (
        f"CREATE INDEX IF NOT EXISTS content_idx "
        f"ON note_chunks USING GIN (to_tsvector('{POSTGRES_TEXT_SEARCH_CONFIG}', content));"
    )
    with engine.begin() as conn:
        conn.execute(text(sql))
