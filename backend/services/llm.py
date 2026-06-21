from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config import LLM_MODEL, HF_TOKEN

# Built once per process and reused. Previously a fresh local torch model was
# loaded on every request, which was slow and memory-heavy; the hosted
# Inference API only needs a lightweight client.
_llm = None


def get_llm(model: str = None, temperature: float = 0.7):
    """
    Return a Hugging Face Inference API text-generation LLM.

    Uses the hosted Inference API instead of a local transformers/torch
    pipeline, so the service stays small enough for a free cloud tier.
    """
    global _llm
    if _llm is not None:
        return _llm

    if not HF_TOKEN:
        raise RuntimeError(
            "HF_TOKEN is not set. Create a free token at "
            "https://huggingface.co/settings/tokens and set HF_TOKEN in the "
            "environment."
        )

    _llm = HuggingFaceEndpoint(
        repo_id=model or LLM_MODEL,
        task="text-generation",
        huggingfacehub_api_token=HF_TOKEN,
        max_new_tokens=256,
        temperature=temperature,
        do_sample=True,
    )
    return _llm


def make_summary_chain():
    prompt = PromptTemplate(
        input_variables=["transcript"],
        template=(
            "Please summarize the following meeting transcript into 5-7 clear bullet points:\n\n"
            "Transcript: {transcript}\n\n"
            "Summary:"
        )
    )
    return prompt | get_llm() | StrOutputParser()


def make_action_item_chain():
    prompt = PromptTemplate(
        input_variables=["transcript"],
        template=(
            "Extract all clear action items from the following meeting transcript:\n\n"
            "Transcript: {transcript}\n\n"
            "Action Items:"
        )
    )

    chain = prompt | get_llm() | StrOutputParser()
    return chain
