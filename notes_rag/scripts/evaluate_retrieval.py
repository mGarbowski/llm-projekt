import argparse
from pathlib import Path

import pandas as pd

from notes_rag.core.retrieval import FulltextRetriever, SemanticRetriever, Retriever, Reranker
from notes_rag.core.schema import get_engine, DbConfig, create_session_factory, NoteChunkRepository, NoteChunk
from notes_rag.eval.dataset import TestDataset
from notes_rag.eval.retrieval import RetrievalEvaluation, RetrievalEvaluationResult


class RerankingRetrieverAdapter(Retriever):
    def __init__(self, reranker, retrievers: list[Retriever]):
        self.reranker = reranker
        self.retrievers = retrievers

    def retrieve(self, query: str, top_k: int = 5) -> list[NoteChunk]:
        candidates = [
            candidate
            for retriever in self.retrievers
            for candidate in retriever.retrieve(query, top_k=top_k)
        ]

        reranked = self.reranker.rerank(query, candidates)
        return reranked[:top_k]


def _make_table_column(result: RetrievalEvaluationResult, k_values: list[int]) -> list[float]:
    return [
        *(result.recall_at_k(k) for k in k_values),
        *(result.mrr_at_k(k) for k in k_values),
    ]

def make_table(results: dict[str, RetrievalEvaluationResult], k_values: list[int]) -> pd.DataFrame:
    row_index = [
        *[f"Recall@{k}" for k in k_values],
        *[f"MRR@{k}" for k in k_values],
    ]

    data = {
        name: _make_table_column(result, k_values)
        for name, result in results.items()
    }

    return pd.DataFrame(index=row_index, data=data)

def main():
    parser = argparse.ArgumentParser(description="Evaluate retrieval performance using various metrics.")
    parser.add_argument("--dataset-path", type=Path, default=Path("data/eval/test.jsonl"),
                        help="Path to the evaluation dataset in JSONL format.")
    parser.add_argument("--output", type=Path, default=Path("reports/results/retrieval_results.csv"),
                        help="Path to the CSV file containing retrieval results.")
    args = parser.parse_args()

    dataset = TestDataset.load(args.dataset_path)
    evaluation = RetrievalEvaluation(dataset)

    engine = get_engine(DbConfig.local())
    session_factory = create_session_factory(engine)
    with session_factory() as db:
        repo = NoteChunkRepository(db)
        fulltext_retriever = FulltextRetriever(repo)
        semantic_retriever = SemanticRetriever.default_model(repo)
        reranker = Reranker.with_default_model()
        reranking_retriever = RerankingRetrieverAdapter(reranker, [semantic_retriever, fulltext_retriever])

        results = {
            "Fulltext Retriever": evaluation.evaluate(fulltext_retriever, max_k=10),
            "Semantic Retriever": evaluation.evaluate(semantic_retriever, max_k=10),
            "Reranking Retriever": evaluation.evaluate(reranking_retriever, max_k=10),
        }

    results_df = make_table(results, k_values=[1, 3, 5, 10])
    print(results_df.to_markdown())
    results_df.to_csv(args.output)


if __name__ == "__main__":
    main()
