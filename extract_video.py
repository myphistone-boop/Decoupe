#!/usr/bin/env python3
"""
Script simple pour extraire une section d'une vidéo et l'optimiser pour le web
"""
import subprocess
import sys
import os


def format_timestamp(seconds):
    """Convertit les secondes en format HH:MM:SS"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:06.3f}"


def extract_video(input_path, start_time, end_time, output_path="output.mp4"):
    """
    Extrait une section de vidéo et l'optimise pour le web

    Args:
        input_path: Chemin vers la vidéo source
        start_time: Timestamp de début (en secondes ou format HH:MM:SS)
        end_time: Timestamp de fin (en secondes ou format HH:MM:SS)
        output_path: Chemin de sortie (par défaut: output.mp4)
    """

    # Vérifier si le fichier d'entrée existe
    if not os.path.exists(input_path):
        print(f"❌ Erreur: Le fichier '{input_path}' n'existe pas")
        return False

    # Calculer la durée
    try:
        if isinstance(start_time, str) and ":" in start_time:
            start = start_time
        else:
            start = format_timestamp(float(start_time))

        if isinstance(end_time, str) and ":" in end_time:
            end = end_time
        else:
            end = format_timestamp(float(end_time))
    except ValueError:
        print("❌ Erreur: Format de timestamp invalide")
        return False

    print(f"\n📹 Extraction de {start} à {end}")
    print(f"📁 Fichier source: {input_path}")
    print(f"💾 Fichier de sortie: {output_path}")
    print("\n⏳ Traitement en cours...\n")

    # Commande ffmpeg optimisée pour le web
    # -ss: timestamp de début
    # -to: timestamp de fin
    # -i: fichier d'entrée
    # -c:v libx264: codec vidéo H.264 (compatible web)
    # -preset fast: compromis vitesse/compression
    # -crf 23: qualité (18-28, 23 = bonne qualité)
    # -c:a aac: codec audio AAC
    # -b:a 128k: bitrate audio 128kbps
    # -movflags +faststart: optimisation pour streaming web
    # -vf scale=-2:720: redimensionner à 720p (optionnel)

    cmd = [
        'ffmpeg',
        '-ss', start,
        '-to', end,
        '-i', input_path,
        '-c:v', 'libx264',
        '-preset', 'fast',
        '-crf', '23',
        '-c:a', 'aac',
        '-b:a', '128k',
        '-movflags', '+faststart',
        '-y',  # Écraser le fichier de sortie s'il existe
        output_path
    ]

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)

        # Afficher la taille du fichier
        if os.path.exists(output_path):
            size_mb = os.path.getsize(output_path) / (1024 * 1024)
            print(f"\n✅ Extraction réussie!")
            print(f"📦 Taille du fichier: {size_mb:.2f} MB")
            print(f"📍 Emplacement: {os.path.abspath(output_path)}")
            return True

    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erreur lors de l'extraction:")
        print(e.stderr)
        return False
    except FileNotFoundError:
        print("\n❌ Erreur: ffmpeg n'est pas installé")
        print("Installez-le avec: sudo apt-get install ffmpeg (Linux) ou brew install ffmpeg (Mac)")
        return False


def main():
    print("=" * 60)
    print("🎬 EXTRACTION DE VIDÉO - Optimisée pour le web")
    print("=" * 60)

    # Demander le chemin de la vidéo
    video_path = input("\n📁 Chemin vers la vidéo: ").strip()

    # Demander les timestamps
    print("\n⏱️  Timestamps (format: secondes ou HH:MM:SS)")
    start = input("   Début: ").strip()
    end = input("   Fin: ").strip()

    # Demander le nom du fichier de sortie (optionnel)
    output = input("\n💾 Nom du fichier de sortie (Enter = output.mp4): ").strip()
    if not output:
        output = "output.mp4"

    # Ajouter l'extension .mp4 si elle n'est pas présente
    if not output.endswith('.mp4'):
        output += '.mp4'

    # Extraire la vidéo
    success = extract_video(video_path, start, end, output)

    if success:
        print("\n" + "=" * 60)
        print("🎉 Terminé! Votre vidéo est prête pour Google Storage.")
        print("=" * 60)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
