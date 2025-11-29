from flask import Blueprint, request, jsonify
from services.splitter import split_text
from services.vectorstore import get_chroma_store
from db import SessionLocal
from models import Meeting


def upload_meeting():
    db = SessionLocal()
    try:
        file = request.files.get("file")
        raw = None
        title = request.form.get("title") or "untitled_meeting"
        if file:
            raw = file.read().decode("utf-8")
        else:
            # try JSON body or form field 'text' or 'transcript'
            if request.is_json:
                raw = request.json.get("text") or request.json.get("transcript")
            else:
                raw = request.form.get("text") or request.form.get("transcript")
        if not raw:
            return jsonify({"error": "no text uploaded"}), 400

        chunks = split_text(raw)
        m = Meeting(title=title, raw_text=raw, chunks_count=len(chunks))
        db.add(m)
        db.commit()
        db.refresh(m)

        store = get_chroma_store()
        texts = chunks
        metadatas = [{"meeting_id": m.id, "chunk_index": i} for i in range(len(texts))]
        ids = [f"{m.id}_{i}" for i in range(len(texts))]
        store.add_texts(texts=texts, metadatas=metadatas, ids=ids)
        # Note: Chroma automatically persists data in newer versions

        return jsonify({"status": "uploaded", "meeting_id": m.id, "chunks": len(chunks)})
    finally:
        db.close()
