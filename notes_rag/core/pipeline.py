from __future__ import annotations

import gc
from dataclasses import dataclass, field

import torch

from notes_rag.core.generation import Generator, GenerationRequest, Message
from notes_rag.core.retrieval import Retriever, Reranker
from notes_rag.core.db.model import NoteChunk


class Pipeline:
    def __init__(
        self, retrievers: list[Retriever], reranker: Reranker, generator: Generator
    ):
        self.retrievers = retrievers
        self.reranker = reranker
        self.generator = generator

    @torch.no_grad()
    def answer(self, request: PipelineRequest) -> tuple[str, list[NoteChunk]]:
        top_context = self.retrieve_context(
            question=request.question, top_k=request.top_k
        )
        generation_request = request.to_generation_request(top_context)
        answer = self.generator.generate(generation_request)
        torch.cuda.empty_cache()
        gc.collect()
        return answer, top_context

    @torch.no_grad()
    def answer_stream(self, request: PipelineRequest, on_token=None):
        top_context = self.retrieve_context(request.question, top_k=request.top_k)
        generation_request = request.to_generation_request(top_context)
        final = self.generator.generate_stream(generation_request, on_token=on_token)
        torch.cuda.empty_cache()
        gc.collect()
        return final, top_context

    def retrieve_context(self, question: str, top_k: int) -> list[NoteChunk]:
        candidates = [
            candidate
            for retriever in self.retrievers
            for candidate in retriever.retrieve(question, top_k=top_k)
        ]
        reranked = self.reranker.rerank(question, candidates)
        top_context = reranked[:top_k]
        return top_context


@dataclass(frozen=True)
class PipelineRequest:
    question: str
    top_k: int = 5
    message_history: list[Message] = field(default_factory=list)
    max_new_tokens: int = 256
    temperature: float = 0.7
    top_p: float = 0.95

    def to_generation_request(self, context: list[NoteChunk]) -> GenerationRequest:
        return GenerationRequest(
            user_prompt=self.question,
            context=context,
            message_history=self.message_history,
            max_new_tokens=self.max_new_tokens,
            temperature=self.temperature,
            top_p=self.top_p,
        )
