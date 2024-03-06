#settings.py
from pathlib import Path
import os

def get_desktop_directory():
    # Lista de posibles ubicaciones del escritorio en diferentes idiomas.
    desktop_candidates = [
        Path.home() / "Escritorio",  # Español
        Path.home() / "Desktop"  # Inglés
    ]
    # Itera sobre las ubicaciones candidatas para encontrar el escritorio.
    for candidate in desktop_candidates:
        if candidate.exists():
            # Retorna la primera ubicación del escritorio que exista.
            return candidate
    # Si ninguna ubicación existe, retorna None.
    return None

def setup_directory():
    desktop_directory = get_desktop_directory()
    # Obtiene la dirección del escritorio.
    media_directory = desktop_directory / "MEDIA" / "Vendetta" #Cambiar nombre de Grupo

    try:
        # Verifica si el directorio ya existe
        media_directory.mkdir(parents=True, exist_ok=True)

        # Establece los permisos del directorio
        os.chmod(media_directory, 0o777)

    except OSError as e:
       print(f"Error en main.py: {e}")
       print("La función main no se ejecutó correctamente.")

#j4rin4