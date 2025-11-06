from typing import Any

import chromadb
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
import torch

gen = pipeline(
    "text-generation",
    model="speakleash/Bielik-1.5B-v3.0-Instruct",
    dtype=torch.bfloat16,
    device_map="auto",
)
chroma_client = chromadb.HttpClient(
    host="localhost",
    port=9000,
)
docs = chroma_client.get_collection(name="chunked_notes")

app = FastAPI()
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

def retrieve(question: str, top_k: int = 4) -> list[dict[str, Any]]:
    res = docs.query(query_texts=[question], n_results=top_k)
    out: list[dict[str, Any]] = []
    n = len(res.get("documents", [[]])[0]) if res.get("documents") else 0
    for i in range(n):
        out.append({
            "id": res["ids"][0][i] if "ids" in res else None,
            "text": res["documents"][0][i],
            "metadata": res["metadatas"][0][i] if "metadatas" in res else {},
            "score": res["distances"][0][i] if "distances" in res else None,
        })
    return out

def build_prompt(question: str, ctx_docs: list[dict[str, Any]]) -> str:
    tokenizer = gen.tokenizer
    ctx_text = "\n\n".join([f"[{i+1}] {d['text']}" for i, d in enumerate(ctx_docs)]) if ctx_docs else ""
    system = "Jesteś pomocnym asystentem, odpowiadaj krótko po polsku na podstawie kontekstu. Cytuj źródła w nawiasach kwadratowych [...]."
    if ctx_text:
        system += "\nKontekst:\n" + ctx_text
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": question},
    ]
    return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

@app.post("/completion")
def completion(body: dict[str, Any] = Body(...)):
    question = body.get("question")
    if not question:
        return JSONResponse({"error": "Missing field `question`."}, status_code=400)
    top_k = int(body.get("top_k", 4))
    max_new_tokens = int(body.get("max_new_tokens", 256))
    temperature = float(body.get("temperature", 0.7))

    # 1) Retrieve context
    sources = retrieve(question, top_k=top_k)

    # 2) Build chat prompt
    prompt = build_prompt(question, sources)

    # 3) Generate answer (non-streaming)
    outputs = gen(
        prompt,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=temperature,
        top_p=0.95,
        eos_token_id=gen.tokenizer.eos_token_id,
        pad_token_id=gen.tokenizer.eos_token_id,
        return_full_text=False,
    )
    answer = outputs[0]["generated_text"].strip()

    return {"answer": answer, "sources": sources}
