@echo off
REM Platter Compiler Webapp - Stop Script (Batch version)
REM This script invokes the Node.js server manager to stop servers

echo.
echo Stopping Platter Compiler Webapp servers...
echo =============================================
echo.

REM Get the directory where this batch file is located
set PROJECT_ROOT=%~dp0

REM Check if Node.js server manager exists
if not exist "%PROJECT_ROOT%server-manager.js" (
    echo ❌ Server manager not found: %PROJECT_ROOT%server-manager.js
    echo Please make sure server-manager.js is in the project root.
    pause
    exit /b 1
)

REM Change to project directory and run the Node.js server manager
cd /d "%PROJECT_ROOT%"
node server-manager.js force-stop

REM Additional aggressive cleanup for Windows
echo.
echo Performing additional cleanup...

REM Kill any remaining processes by name
echo Stopping Python processes...
taskkill /F /IM python.exe /T >nul 2>&1
taskkill /F /IM uvicorn.exe /T >nul 2>&1

echo Stopping Node processes...
taskkill /F /IM node.exe /T >nul 2>&1

REM Kill processes on specific ports
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000 2^>nul') do (
    echo Killing process %%a on port 8000...
    taskkill /PID %%a /F >nul 2>&1
)

for /f "tokens=5" %%a in ('netstat -aon ^| findstr :5173 2^>nul') do (
    echo Killing process %%a on port 5173...
    taskkill /PID %%a /F >nul 2>&1
)

echo ✅ Aggressive cleanup complete!
echo.
echo Press any key to exit...
pause > nul