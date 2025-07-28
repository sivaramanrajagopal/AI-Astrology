#!/usr/bin/env bash
# Build script for Render deployment

echo "Installing system dependencies..."
# Install build dependencies for Swiss Ephemeris
apt-get update -qq && apt-get install -y build-essential

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Setting up environment..."
cd astro-backend

echo "Starting server..."
python start_production.py 