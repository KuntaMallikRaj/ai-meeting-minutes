#!/bin/bash

echo "🚀 Starting AI Meeting Minutes Server..."
echo "=================================="

# Check if we're in the right directory
if [ ! -f "README.md" ]; then
    echo "❌ Please run this script from the project root directory"
    exit 1
fi

# Start backend
echo "🤖 Starting AI Backend Server..."
cd backend
python app.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Start frontend  
echo "🌐 Starting Frontend Web Server..."
cd ../frontend
python3 -m http.server 3000 &
FRONTEND_PID=$!

# Display status
echo ""
echo "✅ Backend running on: http://127.0.0.1:8001"
echo "✅ Frontend running on: http://localhost:3000"
echo ""
echo "📱 Open http://localhost:3000 in your browser"
echo "⏹️  Press Ctrl+C to stop all servers"
echo ""

# Function to cleanup when script exits
cleanup() {
    echo ""
    echo "🛑 Stopping servers..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    echo "✅ All servers stopped"
}

# Set trap to cleanup on script exit
trap cleanup EXIT

# Wait for user to stop
wait
