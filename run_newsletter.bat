@echo off
REM Windows Batch Script to Run Newsletter Generator
REM Double-click this file to run the newsletter generator

echo ========================================
echo AI-Powered News Newsletter Generator
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

REM Run the newsletter generator
python newsletter_generator.py

echo.
echo ========================================
echo.
pause


