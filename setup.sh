#!/bin/bash
# Script de configuration automatique pour Linux/macOS

echo "============================================================"
echo "    Configuration de l'environnement - Linux/macOS"
echo "============================================================"
echo

# Vérifier si Python est disponible
if ! command -v python3 &> /dev/null; then
    echo "[ERREUR] Python 3 n'est pas installé"
    echo
    echo "Installez Python 3:"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-venv"
    echo "  macOS: brew install python3"
    exit 1
fi

echo "[1/3] Création de l'environnement virtuel..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "[ERREUR] Impossible de créer l'environnement virtuel"
    exit 1
fi

echo "[2/3] Activation de l'environnement virtuel..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "[ERREUR] Impossible d'activer l'environnement virtuel"
    exit 1
fi

echo "[3/3] Installation des dépendances..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "[ERREUR] Impossible d'installer les dépendances"
    exit 1
fi

echo
echo "============================================================"
echo "    Configuration terminée avec succès !"
echo "============================================================"
echo
echo "Prochaines étapes:"
echo "  1. Installez ffmpeg (voir README.md)"
echo "  2. Activez l'environnement: source venv/bin/activate"
echo "  3. Lancez: python3 extract_video.py"
echo
