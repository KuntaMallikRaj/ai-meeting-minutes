import os

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from routes.ingest import upload_meeting
from routes.search import search
from routes.summarize import summarize
from services.splitter import split_text
from db import init_db

# The single-page frontend lives alongside the backend. Serving it from Flask
# means one deployed service hosts both the UI and the API on the same origin.
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontend")


def create_app():
    # static_url_path="" serves frontend/style.css, frontend/script.js, etc. at
    # the root path (e.g. GET /script.js).
    app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")
    CORS(app)

    # Create database tables on startup. Without this the `meetings` table
    # never exists and the first /ingest/upload fails with "no such table".
    init_db()

    @app.route("/", methods=["GET"])
    def home():
        # Serve the web UI at the root. The JSON status moved to /health.
        return send_from_directory(FRONTEND_DIR, "index.html")

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({
            "service": "AI Meeting Minutes Generator (Flask)",
            "status": "ok"
        }), 200

    @app.route("/ingest/upload", methods=["POST"])
    def ingest_upload():
        return upload_meeting()
    
    @app.route("/search", methods=["POST"]) 
    def search_route():
        return search()
    @app.route("/summarize", methods=["POST"])
    def summarize_route():
        return summarize()
    
    @app.route("/split", methods=["POST"])
    def split_route():
        try:
            data = request.get_json()
            if not data or 'text' not in data:
                return jsonify({"error": "Text field is required"}), 400
            
            text = data['text']
            chunks = split_text(text)
            
            return jsonify({
                "chunks": chunks,
                "total_chunks": len(chunks)
            }), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8001))
    app.run(host="0.0.0.0", port=port, debug=False)
