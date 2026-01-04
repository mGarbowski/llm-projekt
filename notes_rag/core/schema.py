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
from sqlalchemy.orm import declarative_base, Session, sessionmaker

Base = declarative_base()


class NoteChunk(Base):
    __tablename__ = "note_chunks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = Column(Text)
    course = Column(Text)
    filename = Column(Text)
    title = Column(Text)
    number = Column(Integer)

    def __str__(self):
        return f"NoteChunk(id={self.id}, title={self.title}, course={self.course}, number={self.number})"


class NoteChunkRepository:
    def __init__(self, session: Session):
        self.session = session

    def search_fulltext(self, query: str, limit: int = 10):
        stmt = (
            select(NoteChunk)
            .where(
                func.to_tsvector("simple", NoteChunk.content).op("@@")(
                    func.phraseto_tsquery("simple", query)
                )
            )
            .order_by(
                func.ts_rank(
                    func.to_tsvector("simple", NoteChunk.content),
                    func.phraseto_tsquery("simple", query),
                ).desc()
            )
            .limit(limit)
        )
        return self.session.execute(stmt).scalars().all()


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
