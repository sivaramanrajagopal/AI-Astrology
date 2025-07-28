#!/bin/bash

echo "🌟 Vedic Astrology Application - Quick Start"
echo "================================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed or not in PATH"
    echo "Please install Python from https://python.org/"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed or not in PATH"
    echo "Please install Node.js from https://nodejs.org/"
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed or not in PATH"
    exit 1
fi

echo "✅ All prerequisites are available!"

# Install backend dependencies
echo "📦 Installing backend dependencies..."
cd astro-backend/astro-backend
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Failed to install backend dependencies"
    exit 1
fi
cd ../..

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
cd astro-frontend
npm install
if [ $? -ne 0 ]; then
    echo "❌ Failed to install frontend dependencies"
    exit 1
fi
cd ..

# Setup API key
echo "🔑 Setting up OpenAI API key..."
cd astro-backend/astro-backend
python3 setup_api_key.py
cd ../..

# Start backend server
echo "🚀 Starting backend server..."
cd astro-backend
python3 main.py &
BACKEND_PID=$!
cd ..

# Wait a moment for backend to start
sleep 3

# Start frontend server
echo "🚀 Starting frontend server..."
cd astro-frontend
npm run dev &
FRONTEND_PID=$!
cd ..

# Wait a moment for frontend to start
sleep 5

# Open browser
echo "🌐 Opening application in browser..."
if command -v open &> /dev/null; then
    open http://localhost:3000
elif command -v xdg-open &> /dev/null; then
    xdg-open http://localhost:3000
elif command -v sensible-browser &> /dev/null; then
    sensible-browser http://localhost:3000
else
    echo "⚠️  Could not open browser automatically"
    echo "Please open http://localhost:3000 manually"
fi

echo ""
echo "🎉 Application is ready!"
echo "📱 Frontend: http://localhost:3000"
echo "🔧 Backend: http://127.0.0.1:8000"
echo ""
echo "💡 To stop the servers, press Ctrl+C"

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Stopping servers..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    echo "✅ Servers stopped"
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

# Keep the script running
while true; do
    sleep 1
done 