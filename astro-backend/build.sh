#!/usr/bin/env bash
# Build script for Render deployment

echo "🐍 Checking Python version..."
python --version

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "🔍 Verifying pyswisseph installation..."
python -c "import pyswisseph; print('✅ pyswisseph imported successfully')"

echo "🚀 Starting server..."
python start_simple.py 