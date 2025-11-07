@echo off
REM Windows Batch Script to Test Components
REM Double-click this file to test all components

echo ========================================
echo AI Newsletter - Component Testing
echo ========================================
echo.

REM Check if .env exists
if not exist .env (
    echo ERROR: .env file not found!
    echo Please copy config.env.example to .env and fill in your API keys.
    echo.
    pause
    exit /b 1
)

REM Run the component tests
python test_components.py

echo.
pause


