# Library scripts

gather-notes SOURCE:
    uv run -m notes_rag.scripts.gather_notes {{SOURCE}}

chunk *ARGS:
    uv run -m notes_rag.scripts.document_chunking {{ARGS}}

index *ARGS:
    uv run -m notes_rag.scripts.index_documents {{ARGS}}

seed *ARGS:
    uv run -m notes_rag.scripts.seed {{ARGS}}

answer PROMPT:
    uv run -m notes_rag.scripts.answer "{{PROMPT}}"

# Database management

drop_db:
    docker compose down -v

create_db:
    docker compose up -d

# Developer tools

fmt:
    uvx ruff format

# App management

# Start backend development server
devb:
    fastapi dev notes_rag/api/main.py --reload

# Start frontend development server
devf:
    cd frontend && npm run dev