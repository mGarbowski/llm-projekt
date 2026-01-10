import argparse
import gc
from pathlib import Path

import pandas as pd
import torch

from notes_rag.core.generation import Generator
from notes_rag.core.pipeline import Pipeline
from notes_rag.core.retrieval import FulltextRetriever, SemanticRetriever, Reranker
from notes_rag.core.schema import (
    get_engine,
    DbConfig,
    create_session_factory,
    NoteChunkRepository,
)
from notes_rag.eval.dataset import TestDataset
from notes_rag.eval.pipeline import PipelineEvaluation, PipelineEvaluationResult


def make_table(results: PipelineEvaluationResult) -> pd.DataFrame:
    row_index = [
        "BERT Score - Precision",
        "BERT Score - Recall",
        "BERT Score - F1",
        "ROUGE-L - Precision",
        "ROUGE-L - Recall",
        "ROUGE-L - F1",
        "BLEU Score",
    ]

    bert = results.bert_score()
    rouge = results.rouge_score()
    bleu = results.bleu_score()

    data = {
        "Pipeline": [
            bert["precision"],
            bert["recall"],
            bert["f1"],
            rouge["precision"],
            rouge["recall"],
            rouge["f1"],
            bleu,
        ]
    }

    return pd.DataFrame(index=row_index, data=data)


def main():
    parser = argparse.ArgumentParser(description="Evaluate pipeline performance.")
    parser.add_argument(
        "--dataset-path",
        type=Path,
        default=Path("data/eval/test.jsonl"),
        help="Path to the evaluation dataset in JSONL format.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("reports/results/pipeline_results.csv"),
        help="Path to the CSV file containing evaluation results.",
    )
    args = parser.parse_args()
    args.output.parent.mkdir(exist_ok=True, parents=True)

    dataset = TestDataset.load(args.dataset_path)
    evaluation = PipelineEvaluation(dataset)

    engine = get_engine(DbConfig.local())
    session_factory = create_session_factory(engine)
    with session_factory() as db:
        repo = NoteChunkRepository(db)
        fulltext_retriever = FulltextRetriever(repo)
        semantic_retriever = SemanticRetriever.default_model(repo)
        reranker = Reranker.with_default_model()
        generator = Generator.default()
        pipeline = Pipeline(
            retrievers=[semantic_retriever, fulltext_retriever],
            reranker=reranker,
            generator=generator,
        )
        result = evaluation.evaluate(pipeline)

    # Free GPU memory
    del pipeline
    del generator
    del reranker
    del semantic_retriever
    torch.cuda.empty_cache()
    gc.collect()

    table = make_table(result)
    print(table.to_markdown())
    table.to_csv(args.output)


if __name__ == "__main__":
    main()
