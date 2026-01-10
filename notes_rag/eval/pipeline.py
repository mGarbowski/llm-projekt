"""Evaluate the performance of full RAG pipeline."""

from dataclasses import dataclass
from statistics import mean

from bert_score import score
from rouge_score import rouge_scorer
from sacrebleu import corpus_bleu
from tqdm import tqdm

from notes_rag.core.pipeline import Pipeline
from notes_rag.core.schema import NoteChunk
from notes_rag.eval.dataset import TestDataset, DatasetItem


@dataclass(frozen=True)
class PipelineEvaluationResultItem:
    test_item: DatasetItem
    answer: str
    context: list[NoteChunk]


@dataclass(frozen=True)
class PipelineEvaluationResult:
    items: list[PipelineEvaluationResultItem]

    def bert_score(self):
        precision, recall, f1_score = score(
            cands=self._predictions(), refs=self._references(), lang="pl"
        )
        return {
            "precision": precision.mean().item(),
            "recall": recall.mean().item(),
            "f1": f1_score.mean().item(),
        }

    def rouge_score(self):
        variant = "rougeL"
        scorer = rouge_scorer.RougeScorer(rouge_types=[variant], use_stemmer=True)
        scores = [
            scorer.score(target=refs[0], prediction=pred)
            for refs, pred in zip(self._references(), self._predictions())
        ]
        return {
            "precision": mean(sc[variant].precision for sc in scores),
            "recall": mean(sc[variant].recall for sc in scores),
            "f1": mean(sc[variant].fmeasure for sc in scores),
        }

    def bleu_score(self):
        return corpus_bleu(
            hypotheses=self._predictions(), references=self._references()
        ).score

    def _references(self) -> list[list[str]]:
        return [item.test_item.reference_answers for item in self.items]

    def _predictions(self) -> list[str]:
        return [item.answer for item in self.items]


class PipelineEvaluation:
    def __init__(self, dataset: TestDataset):
        self.dataset = dataset

    def evaluate(self, pipeline: Pipeline):
        return PipelineEvaluationResult(
            items=[
                self._response_for_single_item(item, pipeline)
                for item in tqdm(self.dataset.items)
            ]
        )

    @staticmethod
    def _response_for_single_item(item: DatasetItem, pipeline: Pipeline):
        answer, context = pipeline.answer(item.query)
        return PipelineEvaluationResultItem(
            test_item=item,
            answer=answer,
            context=context,
        )
