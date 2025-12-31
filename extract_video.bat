@echo off
REM Script batch pour lancer l'extraction de vidéo sur Windows
REM Active automatiquement l'environnement virtuel si disponible

echo ============================================================
echo     Extraction de Video - Optimisee pour le Web
echo ============================================================
echo.

REM Vérifier si l'environnement virtuel existe
if exist "venv\Scripts\activate.bat" (
    echo [INFO] Activation de l'environnement virtuel...
    call venv\Scripts\activate.bat
    echo.
)

REM Vérifier si Python est disponible
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] Python n'est pas installe ou n'est pas dans le PATH
    echo.
    echo Installez Python depuis: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM Vérifier si ffmpeg est disponible
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ATTENTION] ffmpeg n'est pas installe ou n'est pas dans le PATH
    echo.
    echo Installez ffmpeg avec chocolatey: choco install ffmpeg
    echo Ou telechargez depuis: https://www.gyan.dev/ffmpeg/builds/
    echo.
    pause
    exit /b 1
)

REM Lancer le script Python
python extract_video.py

echo.
pause
