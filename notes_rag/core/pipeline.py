import sys

from notes_rag.core.generation import Generator, GenerationRequest
from notes_rag.core.retrieval import Retriever, Reranker


class Pipeline:
    def __init__(
            self,
            retrievers: list[Retriever],
            reranker: Reranker,
            generator: Generator
    ):
        self.retrievers = retrievers
        self.reranker = reranker
        self.generator = generator

    def answer(self, question: str):
        print("Wyszukuję istotne dokumenty...", file=sys.stderr)
        candidates = []
        for retriever in self.retrievers:
            candidates.extend(retriever.retrieve(question, top_k=5))
        print(f"Znaleziono {len(candidates)} dokumentów. Oceniam ich istotność...", file=sys.stderr)
        reranked = self.reranker.rerank(question, candidates)
        top_context = reranked[:5]
        print("Generuję odpowiedź...", file=sys.stderr)
        generation_request = GenerationRequest(
            user_prompt=question,
            context=top_context
        )
        answer = self.generator.generate(generation_request)
        return answer, top_context