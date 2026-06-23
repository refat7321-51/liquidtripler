@echo off
chcp 65001 >nul 2>&1
setlocal enabledelayedexpansion

title Quiz App - Auto Setup

echo.
echo ╔══════════════════════════════════════════════════╗
echo ║     Quiz Application - One-Click Setup ^& Run     ║
echo ║     ডাবল ক্লিকেই সব অটো সেটআপ হবে!              ║
echo ╚══════════════════════════════════════════════════╝
echo.

:: ========================================================
:: Step 0: Check if Python is installed
:: ========================================================
echo [0/5] Python চেক করা হচ্ছে...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ╔══════════════════════════════════════════════════╗
    echo ║  [ERROR] Python ইনস্টল নেই অথবা PATH-এ নেই!    ║
    echo ║  Python ডাউনলোড করুন: https://www.python.org/   ║
    echo ║                                                  ║
    echo ║  ইনস্টলের সময় "Add Python to PATH" টিক দিন!    ║
    echo ╚══════════════════════════════════════════════════╝
    echo.
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PYVER=%%i
echo     [OK] %PYVER% পাওয়া গেছে।
echo.

:: ========================================================
:: Step 1: Create Virtual Environment (if not exists)
:: ========================================================
if exist "venv\Scripts\python.exe" (
    echo [1/5] Virtual environment আগে থেকেই আছে। স্কিপ করা হচ্ছে...
) else (
    if exist "venv" (
        echo [1/5] আগের venv ভাঙা মনে হচ্ছে। মুছে নতুন করে তৈরি হচ্ছে...
        rmdir /s /q venv
    ) else (
        echo [1/5] Virtual environment তৈরি হচ্ছে...
    )
    python -m venv venv
    if !errorlevel! neq 0 (
        echo     [ERROR] Virtual environment তৈরি করা যায়নি!
        echo     কারণ হতে পারে: Python ঠিকমতো ইনস্টল হয়নি।
        pause
        exit /b 1
    )
    echo     [OK] Virtual environment তৈরি হয়েছে!
)
echo.

:: ========================================================
:: Step 2: Upgrade pip & Install Dependencies
:: ========================================================
echo [2/5] Dependencies ইনস্টল হচ্ছে (কিছুক্ষণ সময় লাগতে পারে)...
echo     pip আপগ্রেড হচ্ছে...
venv\Scripts\python.exe -m pip install --upgrade pip >nul 2>&1

echo     requirements.txt থেকে প্যাকেজ ইনস্টল হচ্ছে...
venv\Scripts\pip.exe install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo     [ERROR] Dependencies ইনস্টল ব্যর্থ হয়েছে!
    echo     ইন্টারনেট কানেকশন চেক করুন এবং আবার চেষ্টা করুন।
    pause
    exit /b 1
)
echo     [OK] সব dependencies ইনস্টল হয়েছে!
echo.

:: ========================================================
:: Step 3: Database Migrations
:: ========================================================
echo [3/5] Database সেটআপ হচ্ছে (migrations)...
venv\Scripts\python.exe manage.py migrate --run-syncdb
if %errorlevel% neq 0 (
    echo     [ERROR] Database migration ব্যর্থ হয়েছে!
    pause
    exit /b 1
)
echo     [OK] Database প্রস্তুত!
echo.

:: ========================================================
:: Step 4: Collect Static Files
:: ========================================================
echo [4/5] Static files collect হচ্ছে...
venv\Scripts\python.exe manage.py collectstatic --noinput >nul 2>&1
if %errorlevel% neq 0 (
    echo     [WARNING] Static files collect-এ সমস্যা হয়েছে, তবে সার্ভার চলবে।
) else (
    echo     [OK] Static files প্রস্তুত!
)
echo.

:: ========================================================
:: Step 5: Run Server
:: ========================================================
echo [5/5] সার্ভার চালু হচ্ছে...
echo.
echo ╔══════════════════════════════════════════════════╗
echo ║                                                  ║
echo ║   সার্ভার চালু হয়েছে! ব্রাউজারে যান:           ║
echo ║                                                  ║
echo ║   URL:   http://127.0.0.1:8000                   ║
echo ║   Admin: http://127.0.0.1:8000/admin/            ║
echo ║                                                  ║
echo ║   বন্ধ করতে: Ctrl+C চাপুন                       ║
echo ║                                                  ║
echo ╚══════════════════════════════════════════════════╝
echo.

venv\Scripts\python.exe manage.py runserver

echo.
echo সার্ভার বন্ধ হয়েছে।
pause
