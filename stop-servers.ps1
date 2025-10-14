#!/usr/bin/env pwsh
# Platter Compiler Webapp - Stop Script
# This script stops both the Python backend and Svelte frontend servers

Write-Host "🛑 Stopping Platter Compiler Webapp servers..." -ForegroundColor Red
Write-Host "=============================================" -ForegroundColor Red

# Function to kill processes by port
function Stop-ProcessByPort {
    param($Port, $ServiceName)
    
    try {
        # Find processes using the port
        $processes = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue | 
                    Select-Object -ExpandProperty OwningProcess -Unique
        
        if ($processes) {
            foreach ($processId in $processes) {
                try {
                    $process = Get-Process -Id $processId -ErrorAction SilentlyContinue
                    if ($process) {
                        Write-Host "🔪 Stopping $ServiceName (PID: $processId, Name: $($process.ProcessName))" -ForegroundColor Yellow
                        Stop-Process -Id $processId -Force
                        Write-Host "✅ $ServiceName stopped successfully" -ForegroundColor Green
                    }
                }
                catch {
                    Write-Host "⚠️  Could not stop process $processId for $ServiceName" -ForegroundColor Yellow
                }
            }
        }
        else {
            Write-Host "ℹ️  No process found running on port $Port for $ServiceName" -ForegroundColor Gray
        }
    }
    catch {
        Write-Host "⚠️  Error checking port $Port for $ServiceName : $($_.Exception.Message)" -ForegroundColor Yellow
    }
}

# Function to kill processes by name pattern
function Stop-ProcessByName {
    param($ProcessNamePattern, $ServiceName)
    
    try {
        $processes = Get-Process | Where-Object { $_.ProcessName -like $ProcessNamePattern }
        
        if ($processes) {
            foreach ($process in $processes) {
                # Check if it's likely our development server by looking at command line
                try {
                    $commandLine = (Get-CimInstance Win32_Process -Filter "ProcessId = $($process.Id)").CommandLine
                    if ($commandLine -and ($commandLine -like "*uvicorn*" -or $commandLine -like "*vite*" -or $commandLine -like "*npm*dev*")) {
                        Write-Host "🔪 Stopping $ServiceName (PID: $($process.Id), Name: $($process.ProcessName))" -ForegroundColor Yellow
                        Stop-Process -Id $process.Id -Force
                        Write-Host "✅ $ServiceName process stopped" -ForegroundColor Green
                    }
                }
                catch {
                    # If we can't get command line, just check if it's our port
                    continue
                }
            }
        }
    }
    catch {
        Write-Host "⚠️  Error stopping $ServiceName processes: $($_.Exception.Message)" -ForegroundColor Yellow
    }
}

# Stop backend server (port 8000)
Write-Host "🐍 Stopping Python backend server..." -ForegroundColor Yellow
Stop-ProcessByPort -Port 8000 -ServiceName "Backend (FastAPI/Uvicorn)"

# Stop frontend server (port 5173)
Write-Host "⚡ Stopping Svelte frontend server..." -ForegroundColor Yellow
Stop-ProcessByPort -Port 5173 -ServiceName "Frontend (Vite)"

# Also try to stop by process name patterns
Stop-ProcessByName -ProcessNamePattern "*python*" -ServiceName "Python Backend"
Stop-ProcessByName -ProcessNamePattern "*node*" -ServiceName "Node.js Frontend"

# Close any PowerShell windows that might have been opened by start script
Write-Host "🪟 Closing development server windows..." -ForegroundColor Yellow
try {
    # Look for PowerShell windows with our specific titles or commands
    $powershellProcesses = Get-Process -Name "pwsh" -ErrorAction SilentlyContinue
    foreach ($ps in $powershellProcesses) {
        try {
            $commandLine = (Get-CimInstance Win32_Process -Filter "ProcessId = $($ps.Id)").CommandLine
            if ($commandLine -and ($commandLine -like "*uvicorn*" -or $commandLine -like "*npm*dev*")) {
                Write-Host "🔪 Closing PowerShell window (PID: $($ps.Id))" -ForegroundColor Yellow
                Stop-Process -Id $ps.Id -Force
            }
        }
        catch {
            # Skip if we can't access command line
            continue
        }
    }
}
catch {
    Write-Host "⚠️  Could not check PowerShell processes: $($_.Exception.Message)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🎉 All servers stopped successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "💡 Tip: Use 'start-servers.ps1' to start servers again" -ForegroundColor Gray
Write-Host "✨ Cleanup complete!" -ForegroundColor Green

# Wait for user input before closing
Write-Host ""
Read-Host "Press Enter to close this window"