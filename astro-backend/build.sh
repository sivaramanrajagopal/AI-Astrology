#!/usr/bin/env bash
# Build script for Render deployment

echo "🐍 Checking Python version..."
python --version

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "🚀 Starting server..."
python start_minimal.py 