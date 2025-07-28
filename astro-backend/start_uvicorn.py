#!/usr/bin/env python3
"""
Alternative startup script using uvicorn directly
"""

import os
import sys
import subprocess

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