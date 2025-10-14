#!/usr/bin/env pwsh
# Platter Compiler Webapp - Start Script
# This script starts both the Python backend and Svelte frontend servers

Write-Host "🍽️  Starting Platter Compiler Webapp..." -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan

# Check if ports are already in use
$backendPort = 8000
$frontendPort = 5173

# Function to check if port is in use
function Test-Port {
    param($Port)
    try {
        $connection = Test-NetConnection -ComputerName "localhost" -Port $Port -InformationLevel Quiet -WarningAction SilentlyContinue
        return $connection
    }
    catch {
        return $false
    }
}

# Check backend port
if (Test-Port $backendPort) {
    Write-Host "⚠️  Port $backendPort is already in use. Backend may already be running." -ForegroundColor Yellow
} else {
    Write-Host "✅ Port $backendPort is available for backend" -ForegroundColor Green
}

# Check frontend port
if (Test-Port $frontendPort) {
    Write-Host "⚠️  Port $frontendPort is already in use. Frontend may already be running." -ForegroundColor Yellow
} else {
    Write-Host "✅ Port $frontendPort is available for frontend" -ForegroundColor Green
}

Write-Host ""
Write-Host "🚀 Starting servers..." -ForegroundColor Green

# Get the script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$projectRoot = $scriptDir
$backendDir = Join-Path $projectRoot "backend"
$frontendDir = Join-Path $projectRoot "frontend"

# Verify directories exist
if (-not (Test-Path $backendDir)) {
    Write-Host "❌ Backend directory not found: $backendDir" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $frontendDir)) {
    Write-Host "❌ Frontend directory not found: $frontendDir" -ForegroundColor Red
    exit 1
}

# Create a new PowerShell window for the backend
Write-Host "🐍 Starting Python backend server..." -ForegroundColor Yellow
$backendCmd = "cd '$backendDir'; uvicorn main:app --reload --host 0.0.0.0 --port $backendPort"
Start-Process pwsh -ArgumentList "-NoExit", "-Command", $backendCmd -WindowStyle Normal

# Wait a moment for backend to start
Start-Sleep -Seconds 3

# Create a new PowerShell window for the frontend
Write-Host "⚡ Starting Svelte frontend server..." -ForegroundColor Yellow
$frontendCmd = "cd '$frontendDir'; npm run dev"
Start-Process pwsh -ArgumentList "-NoExit", "-Command", $frontendCmd -WindowStyle Normal

# Wait a moment for frontend to start
Start-Sleep -Seconds 5

Write-Host ""
Write-Host "🎉 Servers started successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "📍 Backend API:  http://localhost:$backendPort" -ForegroundColor Cyan
Write-Host "📍 Frontend UI:  http://localhost:$frontendPort" -ForegroundColor Cyan
Write-Host ""
Write-Host "💡 Tip: Use 'stop-servers.ps1' to stop all servers" -ForegroundColor Gray
Write-Host ""

# Optionally open the browser
$openBrowser = Read-Host "🌐 Open browser to frontend? (y/N)"
if ($openBrowser.ToLower() -eq 'y' -or $openBrowser.ToLower() -eq 'yes') {
    Start-Process "http://localhost:$frontendPort"
}

Write-Host "✨ Setup complete! Happy coding!" -ForegroundColor Green