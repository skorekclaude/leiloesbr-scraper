@echo off
chcp 65001 >nul
echo ============================================
echo   USTAWIANIE TYGODNIOWEGO SKANOWANIA
echo ============================================
echo.
echo To doda zadanie do Windows Task Scheduler:
echo   - Nazwa: LeiloesBR Art Scraper
echo   - Kiedy: Co niedziele o 10:00
echo   - Co robi: Uruchamia scraper automatycznie
echo.

schtasks /create /tn "LeiloesBR Art Scraper" /tr "\"C:\Users\skore\leiloesbr-scraper\run_scraper.bat\"" /sc weekly /d SUN /st 10:00 /f

if %errorlevel% equ 0 (
    echo.
    echo ============================================
    echo   GOTOWE! Scraper bedzie sie uruchamial
    echo   automatycznie w kazda niedziele o 10:00.
    echo.
    echo   Zeby zobaczyc/zmienic:
    echo   1. Otworz "Task Scheduler" w Windows
    echo   2. Znajdz "LeiloesBR Art Scraper"
    echo ============================================
) else (
    echo.
    echo   BLAD: Nie udalo sie utworzyc zadania.
    echo   Sprobuj uruchomic ten plik jako Administrator:
    echo   Kliknij prawym na setup_schedule.bat
    echo   i wybierz "Uruchom jako administrator"
)

echo.
pause
