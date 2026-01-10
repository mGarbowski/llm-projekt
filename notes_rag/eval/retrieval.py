from dataclasses import dataclass
from statistics import mean
from uuid import UUID

from tqdm import tqdm

from notes_rag.core.retrieval import Retriever
from notes_rag.eval.dataset import TestDataset, DatasetItem


@dataclass(frozen=True)
class ResultItem:
    expected_ids: list[UUID]
    retrieved: list[UUID]


@dataclass(frozen=True)
class RetrievalEvaluationResult:
    items: list[ResultItem]
    max_k: int

    def recall_at_k(self, k: int) -> float:
        if k > self.max_k:
            raise ValueError(f"k={k} cannot be greater than max_k={self.max_k}")

        return mean(self._item_recall_at_k(item, k) for item in self.items)

    def mrr_at_k(self, k: int) -> float:
        if k > self.max_k:
            raise ValueError(f"k={k} cannot be greater than max_k={self.max_k}")

        return mean(self._item_mrr_at_k(item, k) for item in self.items)

    @staticmethod
    def _item_recall_at_k(item: ResultItem, k: int) -> float:
        retrieved_at_k = set(item.retrieved[:k])
        expected = set(item.expected_ids)
        return len(retrieved_at_k & expected) / len(expected)

    @staticmethod
    def _item_mrr_at_k(item: ResultItem, k: int) -> float:
        retrieved_at_k = item.retrieved[:k]
        expected = set(item.expected_ids)
        for rank, doc_id in enumerate(retrieved_at_k, start=1):
            if doc_id in expected:
                return 1.0 / rank
        return 0.0


class RetrievalEvaluation:
    def __init__(self, dataset: TestDataset):
        self.dataset = dataset

    def evaluate(self, retriever: Retriever, max_k: int) -> RetrievalEvaluationResult:
        return RetrievalEvaluationResult(
            items=[
                self._process_item(item, retriever, max_k)
                for item in tqdm(self.dataset.items)
            ],
            max_k=max_k,
        )

    @staticmethod
    def _process_item(item: DatasetItem, retriever: Retriever, max_k: int) -> ResultItem:
        retrieved_chunks = retriever.retrieve(item.query, top_k=max_k)
        retrieved_ids = [chunk.id for chunk in retrieved_chunks]
        return ResultItem(expected_ids=item.relevant_docs, retrieved=retrieved_ids)
