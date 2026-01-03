gather-notes SOURCE:
    uv run -m notes_rag.scripts.gather_notes {{SOURCE}}

chunk *ARGS:
    uv run -m notes_rag.scripts.document_chunking {{ARGS}}

fmt:
    uvx ruff format