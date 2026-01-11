import asyncio
import json
from typing import Any

from fastapi import APIRouter
from fastapi import Body, Depends
from fastapi.responses import StreamingResponse

from notes_rag.api.di import get_pipeline
from notes_rag.api.schema import CompletionRequest, SourceItem, CompletionResponse
from notes_rag.core.pipeline import Pipeline

api_router = APIRouter()


@api_router.post("/completion", response_model=CompletionResponse)
def completion(
    body: CompletionRequest = Body(...), rag: Pipeline = Depends(get_pipeline)
):
    """Returns a generated answer and the sources used after generation finishes."""
    answer, context = rag.answer(body.to_pipeline_request())

    return CompletionResponse(
        answer=answer,
        sources=[
            SourceItem(
                id=str(chunk.id),
                content=chunk.content,
                course=chunk.course,
                title=chunk.title,
                filename=chunk.filename,
            )
            for chunk in context
        ],
    )


@api_router.post("/completion/stream")
async def completion_stream(
    body: CompletionRequest = Body(...), pipeline: Pipeline = Depends(get_pipeline)
):
    """Streaming answer for a chatbot-style interface.
    Streams tokens as SSE events:
      - event 'message' (default) with `data: "<token text>"`
      - event 'done' with `data: { "sources": [...] }` when generation finishes
    """

    loop = asyncio.get_event_loop()
    q: asyncio.Queue = asyncio.Queue()
    result: dict[str, Any] = {}

    def on_token(tok: str):
        # called from blocking generator thread
        loop.call_soon_threadsafe(q.put_nowait, tok)

    def run_streaming():
        # runs in a threadpool — call blocking pipeline streaming method
        final, context = pipeline.answer_stream(
            body.to_pipeline_request(), on_token=on_token
        )
        result["context"] = context
        # signal end
        loop.call_soon_threadsafe(q.put_nowait, None)

    # start blocking stream in executor
    task = loop.run_in_executor(None, run_streaming)

    async def event_generator():
        # emit tokens as SSE data events
        while True:
            token = await q.get()
            if token is None:
                break
            # emit token as JSON string in `data:` line (SSE)
            # escape token via json.dumps so clients receive exact text
            yield f"data: {json.dumps(token)}\n\n"

        # ensure worker finished
        await task

        # send done event with sources
        ctx = result.get("context", [])
        sources = [
            {
                "id": str(c.id),
                "title": c.title,
                "course": c.course,
                "content": c.content,
                "filename": getattr(c, "filename", None),
            }
            for c in ctx
        ]
        yield f"event: done\ndata: {json.dumps({'sources': sources})}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")
