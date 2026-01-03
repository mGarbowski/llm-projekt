import uuid

from sqlalchemy import UUID, Column, Text, Integer, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class NoteChunk(Base):
    __tablename__ = 'note_chunks'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = Column(Text)
    course = Column(Text)
    filename = Column(Text)
    title = Column(Text)
    number = Column(Integer)


def get_engine():
    return create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/rag_db", echo=False)
