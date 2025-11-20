@echo off
REM Platter Compiler Webapp - Start Script (Batch version)
REM This script invokes the Node.js server manager

echo.
echo Starting Platter Compiler Webapp...
echo =======================================
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

REM Run the Node.js server manager
node "%PROJECT_ROOT%server-manager.js" start

echo.
echo Press any key to exit...
pause > nul