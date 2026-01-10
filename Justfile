# Library scripts

# Gather the notes from SOURCE directory
gather-notes SOURCE:
    uv run -m notes_rag.scripts.gather_notes {{SOURCE}}

# Split documents into chunks
chunk *ARGS:
    uv run -m notes_rag.scripts.document_chunking {{ARGS}}

# Compute embeddings for documents
index *ARGS:
    uv run -m notes_rag.scripts.index_documents {{ARGS}}

# Populate the database
seed *ARGS:
    uv run -m notes_rag.scripts.seed {{ARGS}}

# Answer the promp using RAG
answer PROMPT:
    uv run -m notes_rag.scripts.answer "{{PROMPT}}"

# Evaluate retrieval component
eval-retriever *ARGS:
    uv run -m notes_rag.scripts.evaluate_retrieval {{ARGS}}

# Database management

# Delete database container and volumes
drop_db:
    docker compose down -v

# Start database container
create_db:
    docker compose up -d

# Developer tools

# Run auto formatter
fmt:
    uvx ruff format

# Install dependencies
install:
    uv sync

# Setup Hugging Face credentials (required for downloading gated models)
setup-hf:
    hf auth login

# App management

# Start backend development server
devb:
    fastapi dev notes_rag/api/main.py --reload

# Start frontend development server
devf:
    cd frontend && npm run dev