#!/usr/bin/env python3
"""
Simple HTTP server for the AI Meeting Minutes Frontend
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 3000

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)

    def end_headers(self):
        # Add CORS headers to allow frontend to communicate with backend
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"🚀 AI Meeting Minutes Frontend Server")
            print(f"📡 Serving at: http://localhost:{PORT}")
            print(f"🌐 Opening browser...")
            print(f"📁 Serving from: {os.path.dirname(os.path.abspath(__file__))}")
            print(f"\n💡 Make sure your backend is running on port 8001!")
            print(f"⌨️  Press Ctrl+C to stop the server\n")
            
            # Open browser automatically
            webbrowser.open(f'http://localhost:{PORT}')
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"\n👋 Shutting down the server...")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Port already in use
            print(f"❌ Port {PORT} is already in use.")
            print(f"💡 Try using a different port or stop the process using port {PORT}")
            print(f"🔧 To kill process on port {PORT}: lsof -ti:{PORT} | xargs kill -9")
        else:
            print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
