@echo off
setlocal enabledelayedexpansion

echo.
echo ==============================================
echo   Quiz Application - One-Click Setup ^& Run
echo ==============================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/
    pause
    exit /b
)

:: Step 1: Virtual Environment
if not exist "venv" (
    echo [1/4] Creating virtual environment...
    python -m venv venv
    if !errorlevel! neq 0 (
        echo [ERROR] Failed to create virtual environment.
        pause
        exit /b
    )
    echo [OK] Virtual environment created.
) else (
    echo [1/4] Virtual environment already exists. Skipping creation.
)

:: Step 2: Install Dependencies
echo [2/4] Installing/Updating dependencies...
venv\Scripts\python.exe -m pip install --upgrade pip >nul
venv\Scripts\pip.exe install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies.
    pause
    exit /b
)
echo [OK] Dependencies ready.

:: Step 3: Database Migrations
echo [3/4] Checking and applying database migrations...
venv\Scripts\python.exe manage.py migrate
if %errorlevel% neq 0 (
    echo [ERROR] Failed to run migrations.
    pause
    exit /b
)
echo [OK] Database is up to date.

:: Step 4: Run Server
echo [4/4] Starting the Quiz Application server...
echo.
echo ----------------------------------------------
echo   URL: http://127.0.0.1:8000
echo   Admin: http://127.0.0.1:8000/admin/
echo ----------------------------------------------
echo.
echo Press Ctrl+C to stop the server.
echo.

venv\Scripts\python.exe manage.py runserver

pause
