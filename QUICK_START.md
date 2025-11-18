# Quick Start - Platter Compiler Webapp

## 🚀 One-Click Server Management

### Start Everything
**Option 1:** Double-click → `start-servers.bat`  
**Option 2:** Run in terminal → `node server-manager.js start`  
**Option 3:** From frontend dir → `npm run start:dev`

### Stop Everything  
**Option 1:** Double-click → `stop-servers.bat`  
**Option 2:** Run in terminal → `node server-manager.js stop`  
**Option 3:** From frontend dir → `npm run stop:dev`

## 📍 URLs (after starting)
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000

## 🛠️ First Time Setup

**Automatic Setup (Recommended):**
```bash
# The server manager handles everything automatically!
node server-manager.js start
```

**Manual Setup (if needed):**
```bash
# Install frontend dependencies  
cd frontend
npm install

# Python virtual environment is created automatically
# Or create manually: python -m venv backend/.venv
```

## ✨ Features
- **Auto Virtual Environment**: Creates and manages Python venv automatically
- **Dependency Management**: Installs requirements.txt automatically
- **Port Management**: Checks and handles port conflicts
- **Single Terminal**: No multiple windows, everything in one place
- **Graceful Shutdown**: Ctrl+C stops everything cleanly

That's it! The server manager handles all the complexity. 🎉