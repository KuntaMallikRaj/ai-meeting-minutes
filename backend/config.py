import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # loads .env

BASE_DIR = Path(__file__).resolve().parent
CHROMA_DIR = os.environ.get("CHROMA_DIR", str(BASE_DIR / "chroma_store"))
SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")
# Using free Hugging Face models instead of OpenAI
LLM_MODEL = os.environ.get("LLM_MODEL", "microsoft/DialoGPT-medium")
EMBED_MODEL = os.environ.get("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./meetings.db")
