# 🎬 Extraction de Vidéo

Script Python simple pour extraire une section d'une vidéo et l'optimiser pour le web (Google Storage).

## 📋 Prérequis

- Python 3
- ffmpeg

### Installation de ffmpeg

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
Téléchargez depuis https://ffmpeg.org/download.html

## 🚀 Utilisation

```bash
python3 extract_video.py
```

Le script vous demandera :
1. Le chemin vers votre vidéo
2. Le timestamp de début (en secondes ou format HH:MM:SS)
3. Le timestamp de fin (en secondes ou format HH:MM:SS)
4. Le nom du fichier de sortie (optionnel)

### Exemples de timestamps

- En secondes: `30` pour 30 secondes, `90` pour 1 minute 30
- Format temps: `00:00:30` pour 30 secondes, `00:01:30` pour 1 minute 30

## ⚙️ Optimisations

Le script applique automatiquement :
- **Codec H.264** : Compatible avec tous les navigateurs web
- **Compression intelligente** : Réduit la taille sans perte visible de qualité
- **Audio AAC 128kbps** : Audio optimisé
- **Fast start** : Optimisation pour le streaming web

## 📦 Exemple complet

```
📁 Chemin vers la vidéo: /home/user/ma_video.mp4
⏱️  Timestamps (format: secondes ou HH:MM:SS)
   Début: 00:01:30
   Fin: 00:03:45
💾 Nom du fichier de sortie: extrait.mp4

✅ Extraction réussie!
📦 Taille du fichier: 5.23 MB
```

## 💡 Conseils

- Pour une vidéo encore plus légère, éditez le script et modifiez le paramètre `-crf` (augmentez jusqu'à 28)
- Le format HH:MM:SS accepte aussi les millisecondes: `00:01:30.500`
