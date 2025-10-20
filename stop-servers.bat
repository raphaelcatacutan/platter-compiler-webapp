@echo off
REM Platter Compiler Webapp - Stop Script (Batch version)
REM This script stops both the Python backend and Svelte frontend servers

echo.
echo 🛑 Stopping Platter Compiler Webapp servers...
echo =============================================
echo.

echo 🐍 Stopping Python backend server...
REM Kill processes on port 8000 (backend)
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000') do (
    echo Stopping process %%a on port 8000...
    taskkill /PID %%a /F > nul 2>&1
)

echo ⚡ Stopping Svelte frontend server...
REM Kill processes on port 5173 (frontend)
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :5173') do (
    echo Stopping process %%a on port 5173...
    taskkill /PID %%a /F > nul 2>&1
)

echo 🪟 Closing development server windows...
REM Close command windows with our titles
taskkill /FI "WindowTitle eq Platter Backend*" /F > nul 2>&1
taskkill /FI "WindowTitle eq Platter Frontend*" /F > nul 2>&1

REM Also try to kill by process name (more aggressive)
echo 🔪 Stopping remaining Python and Node processes...
taskkill /IM python.exe /F > nul 2>&1
taskkill /IM node.exe /F > nul 2>&1
taskkill /IM uvicorn.exe /F > nul 2>&1

echo.
echo 🎉 All servers stopped successfully!
echo.
echo 💡 Tip: Use 'start-servers.bat' to start servers again
echo ✨ Cleanup complete!
echo.
pause