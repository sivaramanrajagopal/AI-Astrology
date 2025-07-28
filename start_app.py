#!/usr/bin/env python3
"""
Quick start script for the Vedic Astrology Application
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

def check_python():
    """Check if Python is available"""
    try:
        subprocess.run([sys.executable, '--version'], capture_output=True, check=True)
        return True
    except:
        return False

def check_node():
    """Check if Node.js is available"""
    try:
        subprocess.run(['node', '--version'], capture_output=True, check=True)
        return True
    except:
        return False

def check_npm():
    """Check if npm is available"""
    try:
        subprocess.run(['npm', '--version'], capture_output=True, check=True)
        return True
    except:
        return False

def install_backend_dependencies():
    """Install backend Python dependencies"""
    print("📦 Installing backend dependencies...")
    try:
        subprocess.run([
            sys.executable, '-m', 'pip', 'install', '-r', 
            'astro-backend/astro-backend/requirements.txt'
        ], check=True)
        print("✅ Backend dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing backend dependencies: {e}")
        return False

def install_frontend_dependencies():
    """Install frontend Node.js dependencies"""
    print("📦 Installing frontend dependencies...")
    try:
        os.chdir('astro-frontend')
        subprocess.run(['npm', 'install'], check=True)
        os.chdir('..')
        print("✅ Frontend dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing frontend dependencies: {e}")
        return False

def setup_api_key():
    """Setup OpenAI API key"""
    print("🔑 Setting up OpenAI API key...")
    try:
        os.chdir('astro-backend/astro-backend')
        subprocess.run([sys.executable, 'setup_api_key.py'], check=True)
        os.chdir('../..')
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error setting up API key: {e}")
        return False

def start_backend():
    """Start the backend server"""
    print("🚀 Starting backend server...")
    try:
        os.chdir('astro-backend')
        # Start backend in background
        backend_process = subprocess.Popen([
            sys.executable, 'main.py'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait a bit for server to start
        time.sleep(3)
        
        # Check if server is running
        try:
            import requests
            response = requests.get('http://127.0.0.1:8000/', timeout=5)
            if response.status_code == 200:
                print("✅ Backend server is running at http://127.0.0.1:8000")
                return backend_process
        except:
            print("⚠️  Backend server might not be ready yet. Please check manually.")
            return backend_process
            
    except Exception as e:
        print(f"❌ Error starting backend: {e}")
        return None

def start_frontend():
    """Start the frontend server"""
    print("🚀 Starting frontend server...")
    try:
        os.chdir('astro-frontend')
        # Start frontend in background
        frontend_process = subprocess.Popen([
            'npm', 'run', 'dev'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait a bit for server to start
        time.sleep(5)
        
        print("✅ Frontend server is running at http://localhost:3000")
        return frontend_process
        
    except Exception as e:
        print(f"❌ Error starting frontend: {e}")
        return None

def main():
    """Main setup and start function"""
    print("🌟 Vedic Astrology Application - Quick Start")
    print("=" * 50)
    
    # Check prerequisites
    print("🔍 Checking prerequisites...")
    
    if not check_python():
        print("❌ Python is not installed or not in PATH")
        return
    
    if not check_node():
        print("❌ Node.js is not installed or not in PATH")
        print("Please install Node.js from https://nodejs.org/")
        return
    
    if not check_npm():
        print("❌ npm is not installed or not in PATH")
        return
    
    print("✅ All prerequisites are available!")
    
    # Install dependencies
    if not install_backend_dependencies():
        print("❌ Failed to install backend dependencies")
        return
    
    if not install_frontend_dependencies():
        print("❌ Failed to install frontend dependencies")
        return
    
    # Setup API key
    setup_api_key()
    
    # Start servers
    print("\n🚀 Starting application servers...")
    
    backend_process = start_backend()
    if not backend_process:
        print("❌ Failed to start backend server")
        return
    
    frontend_process = start_frontend()
    if not frontend_process:
        print("❌ Failed to start frontend server")
        backend_process.terminate()
        return
    
    # Open browser
    print("\n🌐 Opening application in browser...")
    try:
        webbrowser.open('http://localhost:3000')
    except:
        print("⚠️  Could not open browser automatically")
        print("Please open http://localhost:3000 manually")
    
    print("\n🎉 Application is ready!")
    print("📱 Frontend: http://localhost:3000")
    print("🔧 Backend: http://127.0.0.1:8000")
    print("\n💡 To stop the servers, press Ctrl+C")
    
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping servers...")
        if backend_process:
            backend_process.terminate()
        if frontend_process:
            frontend_process.terminate()
        print("✅ Servers stopped")

if __name__ == "__main__":
    main() 