@echo off
REM Platter Compiler Webapp - Start Script (Batch version)
REM This script starts both the Python backend and Svelte frontend servers

echo.
echo 🍽️  Starting Platter Compiler Webapp...
echo =======================================
echo.

REM Get the directory where this batch file is located
set PROJECT_ROOT=%~dp0
set BACKEND_DIR=%PROJECT_ROOT%backend
set FRONTEND_DIR=%PROJECT_ROOT%frontend

REM Check if directories exist
if not exist "%BACKEND_DIR%" (
    echo ❌ Backend directory not found: %BACKEND_DIR%
    pause
    exit /b 1
)

if not exist "%FRONTEND_DIR%" (
    echo ❌ Frontend directory not found: %FRONTEND_DIR%
    pause
    exit /b 1
)

echo 🚀 Starting servers...
echo.

REM Start backend server in a new window
echo 🐍 Starting Python backend server...
start "Platter Backend" cmd /k "cd /d "%BACKEND_DIR%" && uvicorn main:app --reload --host 0.0.0.0 --port 8000"

REM Wait a moment
timeout /t 3 /nobreak > nul

REM Start frontend server in a new window
echo ⚡ Starting Svelte frontend server...
start "Platter Frontend" cmd /k "cd /d "%FRONTEND_DIR%" && npm run dev"

REM Wait a moment
timeout /t 5 /nobreak > nul

echo.
echo 🎉 Servers started successfully!
echo.
echo 📍 Backend API:  http://localhost:8000
echo 📍 Frontend UI:  http://localhost:5173
echo.
echo 💡 Tip: Use 'stop-servers.bat' to stop all servers
echo.

REM Ask if user wants to open browser
set /p OPEN_BROWSER=🌐 Open browser to frontend? (y/N): 
if /i "%OPEN_BROWSER%"=="y" start http://localhost:5173
if /i "%OPEN_BROWSER%"=="yes" start http://localhost:5173

echo.
echo ✨ Setup complete! Happy coding!
pause