from dataclasses import dataclass

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker


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
