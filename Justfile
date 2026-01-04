gather-notes SOURCE:
    uv run -m notes_rag.scripts.gather_notes {{SOURCE}}

chunk *ARGS:
    uv run -m notes_rag.scripts.document_chunking {{ARGS}}

index *ARGS:
    uv run -m notes_rag.scripts.index_documents {{ARGS}}

seed *ARGS:
    uv run -m notes_rag.scripts.seed {{ARGS}}

drop_db:
    docker compose down -v

create_db:
    docker compose up -d

fmt:
    uvx ruff format