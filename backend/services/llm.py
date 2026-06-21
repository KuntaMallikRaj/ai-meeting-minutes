from huggingface_hub import InferenceClient

from config import LLM_MODEL, HF_TOKEN

# Hugging Face now serves most instruct models through the chat-completion
# ("conversational") task rather than plain text-generation, so we call
# chat_completion directly. The client is built once per process and reused.
_client = None


def _get_client():
    global _client
    if not HF_TOKEN:
        raise RuntimeError(
            "HF_TOKEN is not set. Create a free token at "
            "https://huggingface.co/settings/tokens and set HF_TOKEN in the "
            "environment."
        )
    if _client is None:
        _client = InferenceClient(token=HF_TOKEN)
    return _client


def _chat(prompt: str, temperature: float = 0.7, max_tokens: int = 256) -> str:
    """Send a single-turn prompt to the configured chat model and return text."""
    resp = _get_client().chat_completion(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return (resp.choices[0].message.content or "").strip()


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
