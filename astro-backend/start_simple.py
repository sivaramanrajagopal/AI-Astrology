#!/usr/bin/env python3
"""
Simple startup script for Render deployment
"""

import os
import sys
import uvicorn

# Check Python version
python_version = sys.version_info
print(f"🐍 Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")

# Try to import the required modules
try:
    import pyswisseph as swe
    print("✅ Successfully imported pyswisseph")
except ImportError as e:
    print(f"❌ Error importing pyswisseph: {e}")
    print("💡 This might be due to Python version incompatibility")
    sys.exit(1)

try:
    from main import app
    print("✅ Successfully imported main app")
except Exception as e:
    print(f"❌ Error importing main app: {e}")
    sys.exit(1)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    
    print(f"🚀 Starting server on {host}:{port}")
    uvicorn.run(app, host=host, port=port) 