@echo off
setlocal enabledelayedexpansion
title AGOS SMART DIAGNOSTIK by Agos Corporation - Backend Server
echo ============================================================================
echo   AGOS SMART DIAGNOSTIK by Agos Corporation - ONE-CLICK BACKEND LAUNCHER
echo   FastAPI + Async SQLAlchemy 2.0 + SQLite + RAG Manual Grand Vitara JB420
echo ============================================================================
echo.

cd /d "%~dp0backend"

:: Deteksi Perintah Python yang Tersedia
set "PY_CMD="
where python >nul 2>nul && set "PY_CMD=python"
if "%PY_CMD%"=="" (
    where py >nul 2>nul && set "PY_CMD=py"
)
if "%PY_CMD%"=="" (
    where python3 >nul 2>nul && set "PY_CMD=python3"
)

if "%PY_CMD%"=="" (
    echo [ERROR] Python tidak terdeteksi di sistem PATH Windows Anda!
    echo Silakan install Python 3.11 atau 3.12 dari https://www.python.org/
    echo Pastikan centang "Add Python to PATH" saat instalasi.
    echo.
    pause
    exit /b 1
)

echo [INFO] Menggunakan executable: %PY_CMD%
echo.

if not exist ".venv" (
    echo [1/4] Membuat Python Virtual Environment (.venv)...
    %PY_CMD% -m venv .venv
    if errorlevel 1 (
        echo [WARNING] Gagal membuat virtual environment, mencoba menjalankan secara langsung...
    )
)

if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
    set "RUN_PY=python"
) else (
    set "RUN_PY=%PY_CMD%"
)

echo [2/4] Menginstal dependensi FastAPI, SQLAlchemy 2.0, aiosqlite, dan pypdf...
%RUN_PY% -m pip install -r requirements.txt

echo.
echo [3/4] Menjalankan Database Seeder & Ingest Manual Suzuki Grand Vitara JB420...
%RUN_PY% -m app.db.seed_data
%RUN_PY% -m app.db.ingest_vitara_manuals --dir "../manual repair suzuki vitara"

echo.
echo ============================================================================
echo [4/4] Server FastAPI aktif!
echo   - Web App Dashboard : http://localhost:8000/
echo   - Swagger Docs UI   : http://localhost:8000/docs
echo   - ReDoc UI          : http://localhost:8000/redoc
echo   - Endpoint Health   : http://localhost:8000/health
echo ============================================================================
echo.
echo Membuka browser ke Web Dashboard (http://localhost:8000/)...
start "" http://localhost:8000/
%RUN_PY% -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

pause

