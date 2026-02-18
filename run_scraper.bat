@echo off
chcp 65001 >nul
echo ============================================
echo   LEILOESBR SCRAPER — TYGODNIOWY SKAN
echo   %date% %time%
echo ============================================

cd /d "C:\Users\skore\leiloesbr-scraper"
python scraper.py

echo.
echo Skan zakonczony.
echo ============================================
