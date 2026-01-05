import sys
import threading
from dataclasses import dataclass, field

import torch
from transformers import Pipeline, pipeline, TextIteratorStreamer

from notes_rag.core.models import load_generator_model
from notes_rag.core.schema import NoteChunk

DEFAULT_SYSTEM_PROMPT = "Jesteś pomocnym asystentem, odpowiadaj krótko po polsku na podstawie kontekstu. Cytuj źródła w nawiasach kwadratowych [...]."


@dataclass(frozen=True)
class GenerationRequest:
    user_prompt: str
    context: list[NoteChunk]
    message_history: list[dict[str, str]] = field(default_factory=list)
    max_new_tokens: int = 256
    temperature: float = 0.7
    top_p: float = 0.95


class Generator:
    def __init__(self, llm: Pipeline, system_prompt: str):
        self.llm = llm
        self.system_prompt = system_prompt

    @classmethod
    def default(cls, system_prompt: str = DEFAULT_SYSTEM_PROMPT):
        return cls(
            llm=load_generator_model(),
            system_prompt=system_prompt,
        )

    def generate(self, generation_request: GenerationRequest) -> str:
        prompt = self.build_prompt(
            generation_request.user_prompt,
            generation_request.context,
            generation_request.message_history,
        )

        generation_output = self.llm(
            prompt,
            max_new_tokens=generation_request.max_new_tokens,
            do_sample=True,
            temperature=generation_request.temperature,
            top_p=generation_request.top_p,
            eos_token_id=self.llm.tokenizer.eos_token_id,
            pad_token_id=self.llm.tokenizer.eos_token_id,
            return_full_text=False,
        )

        return generation_output[0]["generated_text"].strip()

    def generate_stream(
        self, generation_request: "GenerationRequest", on_token=None
    ) -> str:
        """
        Stream tokens in real time. `on_token` is a callable that receives each text chunk.
        If `on_token` is None the chunks are printed to stdout.
        Returns the complete generated string at the end.
        """
        prompt = self.build_prompt(
            generation_request.user_prompt,
            generation_request.context,
            generation_request.message_history,
        )

        # tokenize and move to model device
        inputs = self.llm.tokenizer(prompt, return_tensors="pt")
        model_device = next(self.llm.model.parameters()).device
        input_ids = inputs["input_ids"].to(model_device)
        attention_mask = inputs.get("attention_mask")
        if attention_mask is not None:
            attention_mask = attention_mask.to(model_device)

        streamer = TextIteratorStreamer(
            self.llm.tokenizer, skip_prompt=True, skip_special_tokens=True
        )

        gen_kwargs = {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "max_new_tokens": generation_request.max_new_tokens,
            "do_sample": True,
            "temperature": generation_request.temperature,
            "top_p": generation_request.top_p,
            "eos_token_id": self.llm.tokenizer.eos_token_id,
            "pad_token_id": self.llm.tokenizer.eos_token_id,
            "streamer": streamer,
        }

        thread = threading.Thread(target=self.llm.model.generate, kwargs=gen_kwargs)
        thread.start()

        parts = []
        for chunk in streamer:
            parts.append(chunk)
            if on_token:
                on_token(chunk)
            else:
                print(chunk, end="", flush=True, file=sys.stdout)

        thread.join()
        return "".join(parts).strip()

    def build_prompt(
        self,
        user_prompt: str,
        context: list[NoteChunk],
        message_history: list[dict[str, str]],
    ):
        context_text = (
            "\n\n".join(
                [
                    f"[{i + 1}] {d.title}, {d.course}\n{d.content}"
                    for i, d in enumerate(context)
                ]
            )
            if context
            else ""
        )

        messages = [
            {"role": "system", "content": self.system_prompt},
            *message_history,
            {
                "role": "assistant",
                "content": f"Źródła do kolejnej odpowiedzi:\n{context_text}",
            },
            {"role": "user", "content": user_prompt},
        ]

        return self.llm.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
