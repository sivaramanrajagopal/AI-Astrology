#!/usr/bin/env python3
"""
Alternative startup script using uvicorn directly
"""

import os
import sys
import subprocess

# Add the astro-backend directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
astro_backend_dir = os.path.join(current_dir, "astro-backend")
sys.path.insert(0, astro_backend_dir)

# Change to the astro-backend directory
os.chdir(astro_backend_dir)

# Get environment variables
port = os.environ.get("PORT", "8000")
host = os.environ.get("HOST", "0.0.0.0")

print(f"🚀 Starting server on {host}:{port}")
print(f"📁 Working directory: {os.getcwd()}")

# Start uvicorn directly
subprocess.run([
    sys.executable, "-m", "uvicorn", 
    "main:app", 
    "--host", host, 
    "--port", port
]) 