"""
Módulo para cargar configuración desde archivos YAML.
"""

from pathlib import Path
from typing import Any

import yaml

FONT_SCALE_OPTIONS: list[float] = [1.0, 1.25, 1.5]

DEFAULT_FONT_SCALE: float = 1.0


def _get_config_dir() -> Path:
    """Retorna el directorio de configuración del usuario."""
    config_dir = Path.home() / ".config" / "chuspacalc"
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir


def _get_config_path() -> Path:
    """Retorna la ruta al archivo de configuración del usuario."""
    return _get_config_dir() / "config.yaml"


def load(path: str) -> dict[str, Any]:
    """
    Carga un archivo YAML y retorna su contenido como diccionario.

    Args:
        path: Ruta al archivo YAML.

    Returns:
        Diccionario con la configuración cargada.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        yaml.YAMLError: Si el archivo tiene formato YAML inválido, está vacío
            o su raíz no es un mapa.

    Examples:
        >>> config = load("config.yaml")
        >>> print(config)
        {'nombre': 'ChuspaCalc', 'version': '1.0'}
    """
    archivo = Path(path)

    if not archivo.exists():
        raise FileNotFoundError(f"Archivo de configuración no encontrado: {path}")

    with archivo.open("r", encoding="utf-8") as f:
        try:
            contenido = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error al parsear el archivo YAML: {e}")

    if not isinstance(contenido, dict):
        raise yaml.YAMLError(
            f"La raíz del archivo de configuración {path} debe ser un mapa, "
            f"se recibió {type(contenido).__name__}"
        )

    return contenido


def load_font_scale() -> float:
    """
    Carga la escala de fuente guardada en la configuración del usuario.

    Returns:
        La escala de fuente (1.0, 1.25 o 1.5). Default 1.0 si no existe configuración.
    """
    config_path = _get_config_path()
    if not config_path.exists():
        return DEFAULT_FONT_SCALE

    try:
        config = load(str(config_path))
        scale = config.get("font_scale", DEFAULT_FONT_SCALE)
        if scale in FONT_SCALE_OPTIONS:
            return float(scale)
        return DEFAULT_FONT_SCALE
    except (FileNotFoundError, yaml.YAMLError):
        return DEFAULT_FONT_SCALE


def save_font_scale(scale: float) -> None:
    """
    Guarda la escala de fuente en la configuración del usuario.

    Args:
        scale: Escala de fuente a guardar (1.0, 1.25 o 1.5).

    Raises:
        ValueError: Si la escala no es una de las opciones válidas.
    """
    if scale not in FONT_SCALE_OPTIONS:
        raise ValueError(
            f"Escala inválida: {scale}. Opciones válidas: {FONT_SCALE_OPTIONS}"
        )

    config_path = _get_config_path()
    config: dict[str, Any] = {}
    if config_path.exists():
        try:
            config = load(str(config_path))
        except (FileNotFoundError, yaml.YAMLError):
            config = {}

    config["font_scale"] = scale

    with config_path.open("w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
