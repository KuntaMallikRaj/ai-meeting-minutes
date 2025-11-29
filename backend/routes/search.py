from flask import Blueprint, request, jsonify
from services.vectorstore import get_chroma_store
from services.llm import get_llm




def search():
    payload = request.json or request.form
    query = payload.get("query") if isinstance(payload, dict) else None
    top_k = int(payload.get("top_k", 3)) if isinstance(payload, dict) else 3
    if not query:
        return jsonify({"error": "missing query"}), 400

    store = get_chroma_store()
    docs = store.similarity_search(query, k=top_k)

    contexts = [d.page_content for d in docs]
    context_text = "\n\n---\n\n".join(contexts) if contexts else ""

    llm = get_llm()
    prompt = f"Use the following meeting excerpts to answer the query.\n\nContext:\n{context_text}\n\nQuery: {query}\n\nAnswer concisely."
    answer = llm.invoke(prompt)

    return jsonify({"answer": answer, "contexts": contexts})
