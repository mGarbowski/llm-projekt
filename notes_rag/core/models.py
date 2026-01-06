"""Functions for loading the default ML models."""

import torch
from sentence_transformers import CrossEncoder, SentenceTransformer
from transformers import pipeline


def load_reranker_model():
    return CrossEncoder(
        "sdadas/polish-reranker-roberta-v3",
        default_activation_function=torch.nn.Identity(),
        max_length=8192,
        trust_remote_code=True,
        model_kwargs={"torch_dtype": torch.bfloat16},
    )


def load_bi_encoder_model():
    return SentenceTransformer("sdadas/mmlw-retrieval-roberta-base")


def load_generator_model():
    return pipeline(
        "text-generation",
        model="speakleash/Bielik-1.5B-v3.0-Instruct",
        dtype=torch.bfloat16,
        device_map="auto",
    )
