@echo off
cd /d "%~dp0"
echo === GG Den: setup ===
where py >nul 2>nul
if errorlevel 1 (
  echo Python launcher "py" not found. Install Python 3.11+ from python.org and tick "Add Python to PATH".
  pause
  exit /b 1
)
if not exist ".venv\Scripts\python.exe" py -m venv .venv
call ".venv\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 goto error
call ".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto error
call ".venv\Scripts\python.exe" manage.py migrate
if errorlevel 1 goto error
echo.
echo Setup completed. Double-click run.bat to start the website.
pause
exit /b 0
:error
echo Setup failed. Check the error above and make sure internet access is available.
pause
exit /b 1
