from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request

from notes_rag.core import (
    NoteChunkRepository,
    FulltextRetriever,
    SemanticRetriever,
    Reranker,
    Generator,
    Pipeline,
)
from notes_rag.core.config import DEFAULT_SYSTEM_PROMPT

from notes_rag.core.db import DbConfig, get_engine, create_session_factory
from notes_rag.core.models import (
    load_bi_encoder_model,
    load_reranker_model,
    load_generator_model,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load ML models and database engine at startup."""
    db_config = DbConfig.local()
    engine = get_engine(db_config)

    app.state.engine = engine
    app.state.session_factory = create_session_factory(engine)

    app.state.bi_encoder_model = load_bi_encoder_model()
    app.state.reranker_model = load_reranker_model()
    app.state.generator_model = load_generator_model()

    yield


def get_db(request: Request):
    session_factory = request.app.state.session_factory
    with session_factory() as session:
        yield session


def get_pipeline(request: Request, db: Session = Depends(get_db)):
    state = request.app.state

    repository = NoteChunkRepository(db)
    retriever_fulltext = FulltextRetriever(repository)
    retriever_semantic = SemanticRetriever(repository, state.bi_encoder_model)
    reranker = Reranker(state.reranker_model)
    generator = Generator(state.generator_model, DEFAULT_SYSTEM_PROMPT)

    return Pipeline(
        retrievers=[retriever_semantic, retriever_fulltext],
        reranker=reranker,
        generator=generator,
    )
