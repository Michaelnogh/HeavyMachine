# Start both backend and frontend in separate terminals

Write-Host "Starting Heavy Machinery Catalog..." -ForegroundColor Yellow

# Backend (Flask)
Start-Process powershell -ArgumentList "-NoExit", "-Command", `
  "cd '$PSScriptRoot\backend'; python main.py"

# Frontend (Vite + React)
Start-Process powershell -ArgumentList "-NoExit", "-Command", `
  "cd '$PSScriptRoot\frontend'; npm install; npm run dev"

Write-Host ""
Write-Host "Backend  -> http://localhost:8000" -ForegroundColor Cyan
Write-Host "Frontend -> http://localhost:5173" -ForegroundColor Cyan
