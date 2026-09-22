@echo off
setlocal EnableExtensions

cd /d "%~dp0"

set "PYTHON_EXE=python"
if exist ".venv\Scripts\python.exe" (
    set "PYTHON_EXE=.venv\Scripts\python.exe"
)

set "PYTHONPATH=%CD%\src"
set "HOST=127.0.0.1"
set "PORT=5000"

echo.
echo FortiGate Excel Report
echo ----------------------
echo Local UI: http://%HOST%:%PORT%/
echo Output: Excel workbook (.xlsx)
echo Press Ctrl+C to stop the server.
echo.

"%PYTHON_EXE%" -c "import flask, openpyxl, pydantic, yaml" >nul 2>&1
if errorlevel 1 (
    echo Required Python packages are not available.
    echo Run: "%PYTHON_EXE%" -m pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

start "" cmd /c "timeout /t 2 /nobreak >nul && start http://%HOST%:%PORT%/"

"%PYTHON_EXE%" -c "from fortigate_extract.web import create_app; create_app().run(host='%HOST%', port=%PORT%, debug=False)"

set "EXIT_CODE=%ERRORLEVEL%"
echo.
if not "%EXIT_CODE%"=="0" (
    echo Server exited with code %EXIT_CODE%.
    pause
)

exit /b %EXIT_CODE%
