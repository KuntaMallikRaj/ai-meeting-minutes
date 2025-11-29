from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os

def get_chroma_store():
    """
    Initialize Chroma vector store with Hugging Face embeddings
    Using a free, high-quality sentence transformer model
    """
    # Use a free, high-quality embedding model from Hugging Face
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",  # Free, lightweight, and effective
        model_kwargs={'device': 'cpu'},  # Force CPU for compatibility
        encode_kwargs={'normalize_embeddings': True}  # Normalize for better similarity search
    )

    store = Chroma(
        collection_name="meeting_chunks",
        embedding_function=embeddings,
        persist_directory="chroma_db"
    )

    return store
