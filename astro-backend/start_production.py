#!/usr/bin/env python3
"""
Production startup script for Render deployment
"""

import os
import sys
import uvicorn

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Try to import pyswisseph with error handling
try:
    import pyswisseph as swe
    print("✅ Successfully imported pyswisseph")
except ImportError as e:
    print(f"❌ Error importing pyswisseph: {e}")
    print("Attempting to install pyswisseph...")
    import subprocess
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyswisseph==2.8.0.post1"])
        import pyswisseph as swe
        print("✅ Successfully installed and imported pyswisseph")
    except Exception as install_error:
        print(f"❌ Failed to install pyswisseph: {install_error}")
        sys.exit(1)

# Now import the main app
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
    print(f"📁 Working directory: {os.getcwd()}")
    print(f"🐍 Python path: {sys.path}")
    
    uvicorn.run(app, host=host, port=port) 