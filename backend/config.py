import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # loads .env

BASE_DIR = Path(__file__).resolve().parent
CHROMA_DIR = os.environ.get("CHROMA_DIR", str(BASE_DIR / "chroma_store"))
SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")

# Hosted inference via the Hugging Face Inference API (no local torch needed).
# Create a free token at https://huggingface.co/settings/tokens and set HF_TOKEN.
HF_TOKEN = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACEHUB_API_TOKEN")

# Chat model used for summaries / Q&A. Optional: when unset, the service tries a
# built-in list of common ungated chat models and uses the first one your token's
# inference providers can serve. Set this to pin a specific model.
LLM_MODEL = os.environ.get("LLM_MODEL", "")
# Embedding model used for the Chroma vector store (feature-extraction API).
EMBED_MODEL = os.environ.get("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./meetings.db")
