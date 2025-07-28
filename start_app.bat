@echo off
echo 🌟 Vedic Astrology Application - Quick Start
echo ================================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://python.org/
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)

echo ✅ All prerequisites are available!

REM Install backend dependencies
echo 📦 Installing backend dependencies...
cd astro-backend\astro-backend
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install backend dependencies
    pause
    exit /b 1
)
cd ..\..

REM Install frontend dependencies
echo 📦 Installing frontend dependencies...
cd astro-frontend
npm install
if errorlevel 1 (
    echo ❌ Failed to install frontend dependencies
    pause
    exit /b 1
)
cd ..

REM Setup API key
echo 🔑 Setting up OpenAI API key...
cd astro-backend\astro-backend
python setup_api_key.py
cd ..\..

REM Start backend server
echo 🚀 Starting backend server...
start "Backend Server" cmd /k "cd astro-backend && python main.py"

REM Wait a moment for backend to start
timeout /t 3 /nobreak >nul

REM Start frontend server
echo 🚀 Starting frontend server...
start "Frontend Server" cmd /k "cd astro-frontend && npm run dev"

REM Wait a moment for frontend to start
timeout /t 5 /nobreak >nul

REM Open browser
echo 🌐 Opening application in browser...
start http://localhost:3000

echo.
echo 🎉 Application is ready!
echo 📱 Frontend: http://localhost:3000
echo 🔧 Backend: http://127.0.0.1:8000
echo.
echo 💡 Close the command windows to stop the servers
pause 