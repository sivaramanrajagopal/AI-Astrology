#!/usr/bin/env bash
# Build script for Render deployment

echo "🐍 Checking Python version..."
python --version

echo "📦 Installing Python dependencies..."
cd astro-backend

# Try to install pyswisseph with different methods
echo "📦 Installing pyswisseph..."
pip install --no-cache-dir pyswisseph==2.8.0.post1

# Install other dependencies
echo "📦 Installing other dependencies..."
pip install --no-cache-dir fastapi==0.95.2 uvicorn==0.22.0 python-dotenv==1.0.0 openai==0.28.1 requests==2.31.0 python-multipart==0.0.6

# Test pyswisseph import
echo "🧪 Testing pyswisseph import..."
python -c "import pyswisseph; print('✅ pyswisseph imported successfully')" || echo "❌ pyswisseph import failed"

echo "🚀 Starting server..."
python start_minimal.py 