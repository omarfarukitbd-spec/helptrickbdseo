@echo off
chcp 65001 > nul
setlocal

cd /d "%~dp0\..\.."
echo ========================================================
echo   HELPTRICKBD 3-TIMES-DAILY EXAM RADAR MONITOR
echo ========================================================
python tools\trend_forecaster\auto_radar_daemon.py

endlocal
