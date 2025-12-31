@echo off
REM Script de configuration automatique pour Windows

echo ============================================================
echo     Configuration de l'environnement - Windows
echo ============================================================
echo.

REM Vérifier si Python est disponible
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] Python n'est pas installe
    echo.
    echo Installez Python depuis: https://www.python.org/downloads/
    echo Assurez-vous de cocher "Add Python to PATH" lors de l'installation
    echo.
    pause
    exit /b 1
)

echo [1/3] Creation de l'environnement virtuel...
python -m venv venv
if %errorlevel% neq 0 (
    echo [ERREUR] Impossible de creer l'environnement virtuel
    pause
    exit /b 1
)

echo [2/3] Activation de l'environnement virtuel...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERREUR] Impossible d'activer l'environnement virtuel
    pause
    exit /b 1
)

echo [3/3] Installation des dependances...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERREUR] Impossible d'installer les dependances
    pause
    exit /b 1
)

echo.
echo ============================================================
echo     Configuration terminee avec succes !
echo ============================================================
echo.
echo Prochaines etapes:
echo   1. Installez ffmpeg (voir README.md)
echo   2. Lancez: extract_video.bat
echo.
pause
