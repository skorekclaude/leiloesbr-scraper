@echo off
chcp 65001 >nul
echo ============================================
echo   ART COLLECTION BROWSER
echo   Otworz w Chrome: http://localhost:8080
echo   Zamknij: Ctrl+C
echo ============================================

cd /d "C:\Users\skore\leiloesbr-scraper"
python server.py
