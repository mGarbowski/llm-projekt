gather-notes SOURCE:
    uv run -m notes_rag.scripts.gather_notes {{SOURCE}}

chunk *ARGS:
    uv run -m notes_rag.scripts.document_chunking {{ARGS}}

index *ARGS:
    uv run -m notes_rag.scripts.index_documents {{ARGS}}

seed *ARGS:
    uv run -m notes_rag.scripts.seed {{ARGS}}

fmt:
    uvx ruff format