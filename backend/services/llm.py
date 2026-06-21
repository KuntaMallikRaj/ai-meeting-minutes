from huggingface_hub import InferenceClient

from config import LLM_MODEL, HF_TOKEN

# Hugging Face serves instruct models through the chat-completion
# ("conversational") task via Inference Providers. Which model a given token can
# call depends on the providers enabled on that account, so we try a list of
# common ungated chat models and cache the first one that works.
_FALLBACK_MODELS = [
    "Qwen/Qwen2.5-7B-Instruct",
    "mistralai/Mistral-7B-Instruct-v0.3",
    "meta-llama/Llama-3.2-3B-Instruct",
    "microsoft/Phi-3.5-mini-instruct",
    "google/gemma-2-2b-it",
    "HuggingFaceH4/zephyr-7b-beta",
]

_client = None
_working_model = None  # cached after the first successful call


def _get_client():
    if not HF_TOKEN:
        raise RuntimeError(
            "HF_TOKEN is not set. Create a free token at "
            "https://huggingface.co/settings/tokens and set HF_TOKEN in the "
            "environment."
        )
    global _client
    if _client is None:
        _client = InferenceClient(token=HF_TOKEN)
    return _client


def _candidate_models():
    """LLM_MODEL (if set) is tried first, then the ungated fallbacks."""
    models = []
    if LLM_MODEL:
        models.append(LLM_MODEL)
    for m in _FALLBACK_MODELS:
        if m not in models:
            models.append(m)
    return models


def _chat(prompt: str, temperature: float = 0.7, max_tokens: int = 256) -> str:
    """Send a single-turn prompt to the first chat model the token can serve."""
    client = _get_client()
    global _working_model

    # Once we've found a model that works, keep using it.
    models = [_working_model] if _working_model else _candidate_models()

    last_error = None
    for model in models:
        try:
            resp = client.chat_completion(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature,
            )
            _working_model = model
            return (resp.choices[0].message.content or "").strip()
        except Exception as e:  # noqa: BLE001 - try the next candidate
            last_error = e
            _working_model = None  # don't pin a model that just failed

    raise RuntimeError(
        "No configured chat model could be served by your Hugging Face token. "
        "Enable an Inference Provider at "
        "https://huggingface.co/settings/inference-providers or set LLM_MODEL to "
        f"a model your providers serve. Last error: {last_error}"
    )


class _LLM:
    """Minimal wrapper so callers can do get_llm().invoke(prompt_string)."""

    def invoke(self, prompt: str) -> str:
        return _chat(prompt)


def get_llm(model: str = None, temperature: float = 0.7):
    """Return a chat LLM exposing .invoke(str) -> str."""
    return _LLM()


class _PromptChain:
    """Mimics a LangChain `prompt | llm | parser` chain: .invoke(dict) -> str."""

    def __init__(self, template: str):
        self.template = template

    def invoke(self, variables: dict) -> str:
        return _chat(self.template.format(**variables))


def make_summary_chain():
    return _PromptChain(
        "Please summarize the following meeting transcript into 5-7 clear bullet points:\n\n"
        "Transcript: {transcript}\n\n"
        "Summary:"
    )


def make_action_item_chain():
    return _PromptChain(
        "Extract all clear action items from the following meeting transcript:\n\n"
        "Transcript: {transcript}\n\n"
        "Action Items:"
    )
