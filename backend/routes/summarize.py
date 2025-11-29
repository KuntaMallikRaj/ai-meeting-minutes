from flask import Blueprint, request, jsonify
from services.llm import make_summary_chain, make_action_item_chain




def summarize():
    payload = request.json or request.form
    content = payload.get("content") if isinstance(payload, dict) else None
    if not content:
        return jsonify({"error": "missing content"}), 400

    try:
        # Generate summary using Hugging Face model
        summary_chain = make_summary_chain()
        summary = summary_chain.invoke({"transcript": content})

        # Generate action items using Hugging Face model
        action_item_chain = make_action_item_chain()
        action_items = action_item_chain.invoke({"transcript": content})

        return jsonify({
            "summary": summary,
            "action_items": action_items,
            "status": "success"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
