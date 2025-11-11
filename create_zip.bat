@echo off
echo ========================================
echo Creating Blogify Project Zip Archive
echo ========================================
echo.

REM Run the PowerShell script
powershell.exe -ExecutionPolicy Bypass -File "%~dp0create_zip.ps1"

echo.
echo Press any key to exit...
pause >nul
