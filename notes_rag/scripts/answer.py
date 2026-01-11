"""CLI to answer a single question using a RAG approach."""

from argparse import ArgumentParser

from notes_rag.core.generation import Generator
from notes_rag.core.pipeline import Pipeline, PipelineRequest
from notes_rag.core.retrieval import FulltextRetriever, SemanticRetriever, Reranker
from notes_rag.core.notes_repository import (
    NoteChunkRepository,
)
from notes_rag.core.db.connection import DbConfig, get_engine, create_session_factory


def main():
    parser = ArgumentParser()
    parser.add_argument("question", type=str, help="The question to answer.")

    args = parser.parse_args()
    question = args.question

    engine = get_engine(DbConfig.local())
    session_factory = create_session_factory(engine)
    with session_factory() as session:
        repository = NoteChunkRepository(session)
        retriever_fulltext = FulltextRetriever(repository)
        retriever_semantic = SemanticRetriever.default_model(repository)
        reranker = Reranker.with_default_model()
        generator = Generator.default()
        pipeline = Pipeline(
            retrievers=[retriever_fulltext, retriever_semantic],
            reranker=reranker,
            generator=generator,
        )

        answer_parts = []

        def on_token(chunk: str):
            print(chunk, end="", flush=True)
            answer_parts.append(chunk)

        print("Odpowiedź:")
        _, context = pipeline.answer_stream(
            PipelineRequest(question), on_token=on_token
        )
        print("\nKontekst:")
        for i, chunk in enumerate(context):
            print(f"[{i + 1}] {chunk.title}, {chunk.course} ...")


if __name__ == "__main__":
    main()
