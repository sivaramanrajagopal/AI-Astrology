#!/usr/bin/env python3
"""
Simple startup script for Render deployment
"""

import os
import sys
import uvicorn

# Get environment variables
port = int(os.environ.get("PORT", 8000))
host = os.environ.get("HOST", "0.0.0.0")

print(f"🚀 Starting server on {host}:{port}")
print(f"🐍 Python version: {sys.version}")

# Start uvicorn directly
uvicorn.run("main:app", host=host, port=port) 