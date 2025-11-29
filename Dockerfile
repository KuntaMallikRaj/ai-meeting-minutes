FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy backend requirements and install Python dependencies
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy the entire application
COPY . .

# Create directories for data persistence
RUN mkdir -p /app/data /app/backend/chroma_db

# Expose ports
EXPOSE 8001 3000

# Create startup script
RUN echo '#!/bin/bash\n\
echo "🚀 Starting AI Meeting Minutes in Docker..."\n\
cd /app/backend && python app.py &\n\
BACKEND_PID=$!\n\
sleep 5\n\
cd /app/frontend && python3 -m http.server 3000 &\n\
FRONTEND_PID=$!\n\
echo "✅ Backend: http://localhost:8001"\n\
echo "✅ Frontend: http://localhost:3000"\n\
echo "📱 Open http://localhost:3000 in your browser"\n\
wait $BACKEND_PID $FRONTEND_PID' > /app/start.sh && chmod +x /app/start.sh

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8001/ || exit 1

CMD ["/app/start.sh"]
