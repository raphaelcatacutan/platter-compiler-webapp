# 🚀 Development Server Manager

## Overview

The Platter Compiler Webapp now uses a modern, unified server management system built with Node.js that handles both the Python backend and Svelte frontend in a single terminal process.

## ✨ Key Features

- **🔄 Automatic Virtual Environment**: Creates and manages Python `.venv` automatically
- **📦 Smart Dependencies**: Auto-installs `requirements.txt` packages  
- **🖥️ Single Terminal**: No multiple windows, everything runs together
- **🔍 Port Management**: Detects and handles port conflicts intelligently
- **🛑 Graceful Shutdown**: Ctrl+C stops everything cleanly
- **🎨 Rich Output**: Colored logs with emojis for easy reading

## 🚀 Quick Start

### Start Development Environment
```bash
# From project root - starts both servers
node server-manager.js start

# Alternative: from frontend directory
npm run start:dev
```

### Stop Everything
```bash
# Keyboard shortcut (recommended)
Ctrl+C

# Or run stop command
node server-manager.js stop
```

## 📋 All Commands

```bash
node server-manager.js start    # Start both servers (default)
node server-manager.js stop     # Stop all servers  
node server-manager.js restart  # Restart all servers
node server-manager.js venv     # Setup virtual environment only
node server-manager.js          # Same as 'start'
```

## 🔧 NPM Scripts

From the `frontend/` directory:
```bash
npm run start:dev     # Start both servers
npm run stop:dev      # Stop all servers
npm run restart:dev   # Restart all servers  
npm run setup:venv    # Setup virtual environment
```

## 🖱️ One-Click Options

For users who prefer double-clicking:
- **`start-servers.bat`** - Starts the development environment
- **`stop-servers.bat`** - Stops all servers

## 🐍 Python Virtual Environment

The system automatically:
1. **Checks** if `.venv` exists in `backend/` directory
2. **Creates** virtual environment if missing
3. **Installs** all packages from `requirements.txt`
4. **Validates** that key packages (FastAPI, Uvicorn) are available
5. **Uses** the virtual environment for all Python operations

### Manual venv management:
```bash
# Setup/check venv only
node server-manager.js venv

# Check venv status
ls backend/.venv/  # Should contain Scripts/ (Windows) or bin/ (Unix)
```

## 🌐 Access URLs

After starting the servers:
- **Frontend Application**: http://localhost:5173
- **Backend API**: http://localhost:8000  
- **API Documentation**: http://localhost:8000/docs

## 🔍 Troubleshooting

### Port Conflicts
If ports 8000 or 5173 are in use:
- The manager will detect this and prompt you to stop conflicting processes
- Answer 'y' to automatically clean up ports

### Python Issues  
```bash
# Recreate virtual environment
rm -rf backend/.venv
node server-manager.js venv
```

### Node.js Issues
```bash
# Reinstall frontend dependencies
cd frontend && npm install
```

### Manual Cleanup
```bash
# Kill processes on specific ports (Windows)
netstat -ano | findstr :8000
taskkill /PID <process_id> /F

# Kill processes on specific ports (Unix/Mac)
lsof -ti :8000 | xargs kill -9
```

## 🔄 Migration from Old System

If you were using the old PowerShell scripts:

| Old Command | New Command |
|-------------|-------------|
| `start-servers.ps1` | `node server-manager.js start` |
| `stop-servers.ps1` | `Ctrl+C` or `node server-manager.js stop` |
| Multiple windows | Single terminal |
| Manual venv setup | Automatic venv management |

## 🏗️ Architecture

```
server-manager.js
├── VenvManager class
│   ├── Creates Python virtual environment
│   ├── Installs requirements.txt
│   └── Validates setup completeness
├── ServerManager class  
│   ├── Checks dependencies & ports
│   ├── Starts backend (Python/FastAPI)
│   ├── Starts frontend (Node.js/Vite)
│   └── Handles graceful shutdown
└── Main process
    ├── Command parsing
    ├── Signal handling (Ctrl+C)
    └── Error management
```

## 💡 Development Workflow

1. **One-time setup**: `node server-manager.js start` (creates venv, installs deps)
2. **Daily coding**: Same command starts everything instantly  
3. **During development**: All logs appear in one terminal
4. **End session**: `Ctrl+C` stops everything cleanly
5. **Restart if needed**: `node server-manager.js restart`

## 🎯 Benefits Over Old System

- ✅ **No multiple terminal windows** - everything in one place
- ✅ **Automatic Python venv** - no manual setup needed
- ✅ **Better error handling** - clear messages and recovery
- ✅ **Cross-platform** - works on Windows, Mac, Linux
- ✅ **Modern architecture** - Node.js based with proper async handling
- ✅ **Rich logging** - colored output with status indicators

Happy coding! 🎉