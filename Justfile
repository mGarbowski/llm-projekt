gather-notes SOURCE:
    uv run -m scripts.gather_notes {{SOURCE}}

chunk *ARGS:
    uv run -m scripts.document_chunking {{ARGS}}

fmt:
    uvx ruff format