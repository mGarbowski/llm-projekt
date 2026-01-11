from typing import Protocol

import torch
from sentence_transformers import SentenceTransformer, CrossEncoder

from notes_rag.core.config import SEMANTIC_RETRIEVER_QUERY_PREFIX
from notes_rag.core.models import load_reranker_model, load_bi_encoder_model
from notes_rag.core.schema import NoteChunk, NoteChunkRepository


class Retriever(Protocol):
    def retrieve(self, query: str, top_k: int = 5) -> list[NoteChunk]: ...


class FulltextRetriever:
    def __init__(self, notes_repository: NoteChunkRepository):
        self.notes_repository = notes_repository

    def retrieve(self, query: str, top_k: int = 5) -> list[NoteChunk]:
        return self.notes_repository.search_fulltext(query, limit=top_k)


class SemanticRetriever:
    def __init__(
        self,
        notes_repository: NoteChunkRepository,
        model,
        query_prefix: str = SEMANTIC_RETRIEVER_QUERY_PREFIX,
    ):
        self.notes_repository = notes_repository
        self.model = model
        self.query_prefix = query_prefix

    @classmethod
    def default_model(
        cls,
        notes_repository: NoteChunkRepository,
        query_prefix: str = SEMANTIC_RETRIEVER_QUERY_PREFIX,
    ):
        model = load_bi_encoder_model()
        return cls(notes_repository, model, query_prefix)

    def compute_embedding(self, text: str) -> list[float]:
        return self.model.encode(text).tolist()

    def retrieve(self, query: str, top_k: int = 5) -> list[NoteChunk]:
        model_query = f"{self.query_prefix}{query}"
        query_embedding = self.compute_embedding(model_query)
        return self.notes_repository.search_semantic(query_embedding, limit=top_k)


class Reranker:
    def __init__(self, model):
        self.model = model

    @classmethod
    def with_default_model(cls):
        return cls(load_reranker_model())

    def rerank(self, query: str, candidates: list[NoteChunk]) -> list[NoteChunk]:
        """Return the list of candidates sorted by relevance to the query."""
        scores = self.model.predict(
            [(query, candidate.content) for candidate in candidates]
        )
        ranked_candidates = [
            candidate
            for _, candidate in sorted(
                zip(scores, candidates), key=lambda pair: pair[0], reverse=True
            )
        ]
        return ranked_candidates
