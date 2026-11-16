"""Módulo para exportar resultados de cálculo a archivos JSON."""

import json
import os


def exportar_resultado(resultado: dict, ruta_archivo: str, sobreescribir: bool = False) -> None:
    """Exporta un diccionario a un archivo JSON con indentación de 2 espacios."""
    if not isinstance(resultado, dict):
        raise TypeError(f"Se esperaba un dict, se recibió {type(resultado).__name__}")

    if os.path.exists(ruta_archivo) and not sobreescribir:
        raise FileExistsError(ruta_archivo)

    directorio = os.path.dirname(ruta_archivo)
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio, exist_ok=True)

    with open(ruta_archivo, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)


def exportar_lista(resultados: list, ruta_archivo: str, sobreescribir: bool = False) -> None:
    """Exporta una lista de resultados a un archivo JSON con indentación de 2 espacios."""
    if not isinstance(resultados, list):
        raise TypeError(f"Se esperaba una list, se recibió {type(resultados).__name__}")

    if os.path.exists(ruta_archivo) and not sobreescribir:
        raise FileExistsError(ruta_archivo)

    directorio = os.path.dirname(ruta_archivo)
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio, exist_ok=True)

    with open(ruta_archivo, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False)
