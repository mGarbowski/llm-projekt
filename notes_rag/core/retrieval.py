from typing import Protocol
from sentence_transformers import SentenceTransformer
from notes_rag.core.schema import NoteChunk, NoteChunkRepository


class Retriever(Protocol):
    def retrieve(self, query: str, top_k: int = 5) -> list[NoteChunk]: ...


class FulltextRetriever:
    def __init__(self, notes_repository: NoteChunkRepository):
        self.notes_repository = notes_repository

    def retrieve(self, query: str, top_k: int = 5) -> list[NoteChunk]:
        return self.notes_repository.search_fulltext(query, limit=top_k)


class SemanticRetriever:
    def __init__(self, notes_repository: NoteChunkRepository, model):
        self.notes_repository = notes_repository
        self.model = model

    @classmethod
    def default_model(cls, notes_repository: NoteChunkRepository):
        model = SentenceTransformer("sdadas/mmlw-retrieval-roberta-base")
        return cls(notes_repository, model)

    def compute_embedding(self, text: str) -> list[float]:
        return self.model.encode(text).tolist()

    def retrieve(self, query: str, top_k: int = 5) -> list[NoteChunk]:
        query_embedding = self.compute_embedding(query)
        return self.notes_repository.search_semantic(query_embedding, limit=top_k)
