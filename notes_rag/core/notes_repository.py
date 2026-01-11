import re

from sqlalchemy import (
    func,
    select,
)
from sqlalchemy.orm import Session

from notes_rag.core.config import POSTGRES_TEXT_SEARCH_CONFIG
from notes_rag.core.db.model import NoteChunk


class NoteChunkRepository:
    def __init__(
        self, session: Session, text_search_config: str = POSTGRES_TEXT_SEARCH_CONFIG
    ):
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
