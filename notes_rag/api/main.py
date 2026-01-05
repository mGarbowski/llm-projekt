from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, Body, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from notes_rag.core.generation import Generator, DEFAULT_SYSTEM_PROMPT
from notes_rag.core.models import load_bi_encoder_model, load_reranker_model, load_generator_model
from notes_rag.core.pipeline import Pipeline
from notes_rag.core.retrieval import FulltextRetriever, SemanticRetriever, Reranker
from notes_rag.core.schema import get_engine, DbConfig, create_session_factory, NoteChunkRepository



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

app = FastAPI(lifespan=lifespan)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
    allow_credentials=False,
)

@app.post("/completion")
def completion(body: dict[str, Any] = Body(...), rag: Pipeline = Depends(get_pipeline)):
    question = body.get("question")
    if not question:
        return JSONResponse({"error": "Missing field `question`."}, status_code=400)

    answer, context = rag.answer(question)

    return {"answer": answer, "sources": [
        {
            "id": chunk.id,
            "content": chunk.content,
            "course": chunk.course,
            "title": chunk.title,
            "filename": chunk.filename,
        }
        for chunk in context
    ]}
