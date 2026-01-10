import gc
import sys

import torch

from notes_rag.core.generation import Generator, GenerationRequest
from notes_rag.core.retrieval import Retriever, Reranker
from notes_rag.core.schema import NoteChunk


class Pipeline:
    def __init__(
        self, retrievers: list[Retriever], reranker: Reranker, generator: Generator
    ):
        self.retrievers = retrievers
        self.reranker = reranker
        self.generator = generator

    @torch.no_grad()
    def answer(self, question: str) -> tuple[str, list[NoteChunk]]:
        top_context = self.retrieve_context(question)
        print("Generuję odpowiedź...", file=sys.stderr)
        generation_request = GenerationRequest(
            user_prompt=question, context=top_context
        )
        answer = self.generator.generate(generation_request)
        torch.cuda.empty_cache()
        gc.collect()
        return answer, top_context

    @torch.no_grad()
    def answer_stream(self, question: str, on_token=None):
        top_context = self.retrieve_context(question)
        print("Generuję odpowiedź...", file=sys.stderr)
        generation_request = GenerationRequest(
            user_prompt=question, context=top_context
        )
        final = self.generator.generate_stream(generation_request, on_token=on_token)
        torch.cuda.empty_cache()
        gc.collect()
        return final, top_context

    def retrieve_context(self, question: str) -> list[NoteChunk]:
        print("Wyszukuję istotne dokumenty...", file=sys.stderr)
        candidates = []
        for retriever in self.retrievers:
            candidates.extend(retriever.retrieve(question, top_k=5))
        print(
            f"Znaleziono {len(candidates)} dokumentów. Oceniam ich istotność...",
            file=sys.stderr,
        )
        reranked = self.reranker.rerank(question, candidates)
        top_context = reranked[:5]
        return top_context
