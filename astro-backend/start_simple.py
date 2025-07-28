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

# Check if Python version is compatible
if python_version.major == 3 and python_version.minor >= 13:
    print("⚠️  Warning: Python 3.13+ may have compatibility issues with pyswisseph")
    print("💡 Consider using Python 3.10 for better compatibility")
elif python_version.major == 3 and python_version.minor == 10:
    print("✅ Using Python 3.10 - should be compatible with pyswisseph")
else:
    print(f"ℹ️  Using Python {python_version.major}.{python_version.minor}")

# Try to import the required modules
try:
    import pyswisseph as swe
    print("✅ Successfully imported pyswisseph")
except ImportError as e:
    print(f"❌ Error importing pyswisseph: {e}")
    print("💡 This might be due to Python version incompatibility")
    print("🔧 Try using Python 3.10 instead of Python 3.13")
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