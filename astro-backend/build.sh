#!/usr/bin/env bash
# Build script for Render deployment

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setting up environment..."
cd astro-backend

echo "Starting server..."
uvicorn main:app --host 0.0.0.0 --port $PORT 