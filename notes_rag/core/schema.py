import uuid
from dataclasses import dataclass

from sqlalchemy import (
    UUID,
    Column,
    Text,
    Integer,
    create_engine,
    Engine,
    func,
    Index,
    literal_column,
    text,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class NoteChunk(Base):
    __tablename__ = "note_chunks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = Column(Text)
    course = Column(Text)
    filename = Column(Text)
    title = Column(Text)
    number = Column(Integer)


def create_fulltext_index(engine: Engine):
    sql = (
        "CREATE INDEX IF NOT EXISTS content_idx "
        "ON note_chunks USING GIN (to_tsvector('simple', content));"
    )
    with engine.begin() as conn:
        conn.execute(text(sql))


@dataclass(frozen=True)
class DbConfig:
    username: str
    password: str
    db_name: str
    host: str
    port: int

    @classmethod
    def local(cls):
        return cls(
            username="postgres",
            password="postgres",
            db_name="rag_db",
            host="localhost",
            port=5432,
        )


def get_engine(cfg: DbConfig) -> Engine:
    return create_engine(
        f"postgresql+psycopg2://{cfg.username}:{cfg.password}@{cfg.host}:{cfg.port}/{cfg.db_name}",
        echo=False,
    )
