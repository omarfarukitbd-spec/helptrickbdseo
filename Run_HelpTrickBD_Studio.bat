@echo off
chcp 65001 >nul
title HelpTrickBD Autonomous Publishing Studio
cls
echo ======================================================================
echo 🚀 HELPTRICKBD AUTONOMOUS PUBLISHING STUDIO
echo ======================================================================
echo • Local Web Dashboard: http://localhost:8501
echo • Agent Constitution Rules 00–08 Active
echo • Blogger API v3, Google Indexing API & Thumbnail Engine Online
echo ======================================================================
echo.
echo [1/2] ব্রাউজারে স্টুডিও ড্যাশবোর্ড ওপেন করা হচ্ছে...
start http://localhost:8501
echo.
echo [2/2] লোকাল ব্যাকএন্ড সার্ভার চালু করা হচ্ছে (Press Ctrl+C to stop)...
echo ======================================================================
python tools/studio/backend/studio_server.py 8501
pause
