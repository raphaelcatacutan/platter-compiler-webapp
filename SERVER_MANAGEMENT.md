# 🍽️ Platter Compiler Webapp - Server Management

This directory contains convenient scripts to start and stop both the Python backend and Svelte frontend servers with a single command.

## 📁 Available Scripts

### PowerShell Scripts (Recommended for Windows)
- **`start-servers.ps1`** - Starts both backend and frontend servers
- **`stop-servers.ps1`** - Stops all running servers and cleans up processes

### Batch Scripts (Alternative for Windows)
- **`start-servers.bat`** - Starts both servers (simpler version)
- **`stop-servers.bat`** - Stops all servers (simpler version)

## 🚀 How to Use

### Starting Servers

**Option 1: PowerShell (Recommended)**
```powershell
# Right-click on start-servers.ps1 and select "Run with PowerShell"
# OR run from PowerShell terminal:
.\start-servers.ps1
```

**Option 2: Batch File**
```cmd
# Double-click start-servers.bat
# OR run from Command Prompt:
start-servers.bat
```

### Stopping Servers

**Option 1: PowerShell (Recommended)**
```powershell
# Right-click on stop-servers.ps1 and select "Run with PowerShell"
# OR run from PowerShell terminal:
.\stop-servers.ps1
```

**Option 2: Batch File**
```cmd
# Double-click stop-servers.bat
# OR run from Command Prompt:
stop-servers.bat
```

## 🎯 What the Scripts Do

### Start Scripts
- ✅ Check if ports 8000 and 5173 are available
- 🐍 Start Python FastAPI backend on `http://localhost:8000`
- ⚡ Start Svelte frontend on `http://localhost:5173`
- 🪟 Open each server in a separate terminal window
- 🌐 Optionally open browser to the frontend
- 📍 Display URLs for easy access

### Stop Scripts
- 🛑 Find and terminate processes running on ports 8000 and 5173
- 🔪 Kill Python and Node.js processes related to the servers
- 🪟 Close the terminal windows opened by start scripts
- 🧹 Clean up any remaining development server processes

## 🔧 Requirements

Before running the scripts, ensure you have:
- Python with FastAPI and Uvicorn installed
- Node.js with npm installed
- All dependencies installed in both `backend/` and `frontend/` directories

## 💡 Tips

1. **First Time Setup**: Make sure to install dependencies first:
   ```bash
   # In backend directory
   pip install fastapi uvicorn
   
   # In frontend directory
   npm install
   ```

2. **PowerShell Execution Policy**: If you get an execution policy error, run:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

3. **Port Conflicts**: If ports are already in use, the scripts will warn you and may not start properly.

4. **Manual Cleanup**: If scripts don't stop everything, you can manually kill processes:
   ```powershell
   # Kill by port
   netstat -ano | findstr :8000
   taskkill /PID <process_id> /F
   ```

## 🎉 One-Click Development

With these scripts, you can now:
- **Start**: Double-click `start-servers.ps1` → Both servers running!
- **Stop**: Double-click `stop-servers.ps1` → Everything cleaned up!
- **Develop**: Open `http://localhost:5173` and start coding!

Happy coding! 🚀