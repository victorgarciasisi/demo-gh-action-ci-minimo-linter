"""Demo repo para CI con lint.

Código deliberadamente pequeño para centrar el vídeo en calidad básica.
"""

from __future__ import annotations


def normalize_name(name: str) -> str:
    """Normaliza un nombre para mostrarlo de forma consistente."""
    return " ".join(name.strip().split())


def greeting(name: str) -> str:
    clean = normalize_name(name)
    return f"Hola, {clean}!"
