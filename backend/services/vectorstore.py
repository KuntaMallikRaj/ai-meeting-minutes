from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEndpointEmbeddings

from config import EMBED_MODEL, HF_TOKEN, CHROMA_DIR

# Reuse a single store/embeddings client per process instead of rebuilding it
# (and re-loading a local model) on every request.
_store = None


def get_chroma_store():
    """
    Initialize a Chroma vector store backed by Hugging Face Inference API
    embeddings. No local sentence-transformers/torch model is loaded.
    """
    global _store
    if _store is not None:
        return _store

    if not HF_TOKEN:
        raise RuntimeError(
            "HF_TOKEN is not set. Create a free token at "
            "https://huggingface.co/settings/tokens and set HF_TOKEN in the "
            "environment."
        )

    embeddings = HuggingFaceEndpointEmbeddings(
        model=EMBED_MODEL,
        huggingfacehub_api_token=HF_TOKEN,
    )

    _store = Chroma(
        collection_name="meeting_chunks",
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )
    return _store
