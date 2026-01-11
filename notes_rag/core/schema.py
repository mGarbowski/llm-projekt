import re
import uuid
from dataclasses import dataclass
from typing import Generator, Any, Callable

from sqlalchemy import (
    UUID,
    Column,
    Text,
    Integer,
    create_engine,
    Engine,
    func,
    text,
    select,
)
from sqlalchemy.orm import declarative_base, Session, sessionmaker, mapped_column
from pgvector.sqlalchemy import Vector

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


class NoteChunkRepository:
    def __init__(self, session: Session, text_search_config: str = "polish"):
        self.session = session
        self.text_search_config = text_search_config

    def search_fulltext(self, query: str, limit: int = 10):
        stmt = (
            select(NoteChunk)
            .where(
                self._make_ts_vector(NoteChunk.content).op("@@")(
                    self._make_or_ts_query(query)
                )
            )
            .order_by(
                func.ts_rank(
                    self._make_ts_vector(NoteChunk.content),
                    self._make_or_ts_query(query),
                ).desc()
            )
            .limit(limit)
        )
        return self.session.execute(stmt).scalars().all()

    def search_semantic(self, query_embedding: list[float], limit: int = 10):
        stmt = (
            select(NoteChunk)
            .order_by(NoteChunk.embedding.l2_distance(query_embedding))
            .limit(limit)
        )
        return self.session.execute(stmt).scalars().all()

    def _make_ts_vector(self, document):
        return func.to_tsvector(self.text_search_config, document)

    def _make_or_ts_query(self, query: str):
        """Text search query with alternative of the tokens"""
        tokens = re.findall(r"\w+", query.lower())
        ts_query_text = " | ".join(tokens)
        return func.to_tsquery(self.text_search_config, ts_query_text)

    def _make_websearch_ts_query(self, query: str):
        """Text search query in websearch format
        https://www.postgresql.org/docs/current/textsearch-controls.html#TEXTSEARCH-PARSING-QUERIES
        """
        return func.websearch_to_tsquery(self.text_search_config, query)


def create_fulltext_index(engine: Engine):
    sql = (
        "CREATE INDEX IF NOT EXISTS content_idx "
        "ON note_chunks USING GIN (to_tsvector('polish', content));"
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


def create_session_factory(engine: Engine):
    return sessionmaker(bind=engine, expire_on_commit=False, future=True)


def make_get_db(session_factory) -> Callable[[], Generator[Session, Any, None]]:
    def get_db():
        db: Session = session_factory()
        try:
            yield db
        finally:
            db.close()

    return get_db
