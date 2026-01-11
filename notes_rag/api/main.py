from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from notes_rag.api.di import lifespan
from notes_rag.api.endpoints import api_router

app = FastAPI(lifespan=lifespan)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
    allow_credentials=False,
)
app.include_router(api_router)
