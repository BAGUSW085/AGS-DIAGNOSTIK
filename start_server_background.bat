@echo off
setlocal
cd /d "c:\project bengkel masa depan ai antigravity\backend"

:: Jika port 8000 sudah aktif (server sudah jalan), jangan jalankan duplikat
netstat -ano | findstr ":8000 " | findstr "LISTENING" >nul 2>nul
if %errorlevel%==0 exit /b 0

if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" -m uvicorn app.main:app --host 0.0.0.0 --port 8000
) else (
    python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
)
