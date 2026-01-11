from enum import Enum

from pydantic import BaseModel, Field

from notes_rag.core import PipelineRequest, Message


class MessageHistoryRole(str, Enum):
    user = "user"
    assistant = "assistant"


class MessageHistoryItem(BaseModel):
    role: MessageHistoryRole
    content: str


class CompletionRequest(BaseModel):
    question: str
    message_history: list[MessageHistoryItem] = Field(default_factory=list)
    retrieval_top_k: int = 5
    max_new_tokens: int = 256
    temperature: float = 0.7
    generator_top_p: float = 0.95

    def to_pipeline_request(self) -> PipelineRequest:
        return PipelineRequest(
            question=self.question,
            top_k=self.retrieval_top_k,
            message_history=[
                Message(role=msg.role, content=msg.content)
                for msg in self.message_history
            ],
            max_new_tokens=self.max_new_tokens,
            temperature=self.temperature,
            top_p=self.generator_top_p,
        )


class SourceItem(BaseModel):
    id: str
    content: str
    course: str
    title: str
    filename: str


class CompletionResponse(BaseModel):
    answer: str
    sources: list[SourceItem]
