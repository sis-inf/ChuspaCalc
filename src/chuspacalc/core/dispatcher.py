"""
Despachador de comandos que mapea subcomandos a funciones ejecutables
consultando dinámicamente al registry.
"""

import importlib
import json
import sys

from chuspacalc.core import registry

FORMATOS_VALIDOS = ("dict", "json", "texto")


def _cargar_modulos_dinamicos() -> None:
    """Carga dinámicamente los módulos de la carpeta 'modulos'."""
    if registry.MODULOS_DIR.exists():
        for archivo in registry.MODULOS_DIR.glob("*.py"):
            if archivo.name != "__init__.py":
                nombre_modulo = f"chuspacalc.modulos.{archivo.stem}"
                try:
                    importlib.import_module(nombre_modulo)
                except (ImportError, ModuleNotFoundError):
                    pass


def _formatear_resultado(resultado, formato: str):
    """Convierte el resultado de un handler al formato solicitado."""
    if formato == "dict" or not isinstance(resultado, dict):
        return resultado
    if formato == "json":
        return json.dumps(resultado, indent=2, ensure_ascii=False)
    return "\n".join(f"{clave}: {valor}" for clave, valor in resultado.items())


def dispatch(subcommand: str, formato: str = "dict") -> int | dict | str:
    """
    Despacha un subcomando a su función ejecutable correspondiente.

    Args:
        subcommand: Nombre del subcomando a ejecutar.
        formato: Formato de salida: 'dict' (por defecto), 'json' o 'texto'.
            Solo se aplica cuando el handler devuelve un diccionario.

    Returns:
        Código de salida entero (0 para éxito), o el resultado del handler
        en el formato solicitado si este devuelve un diccionario.

    Raises:
        ValueError: Si el formato no es 'dict', 'json' ni 'texto'.

    Examples:
        >>> dispatch("convert")
        Ejecutando conversión...
        0
        >>> dispatch("desconocido")
        Error: subcomando desconocido 'desconocido'
        1
    """
    if formato not in FORMATOS_VALIDOS:
        raise ValueError(
            f"Formato '{formato}' no soportado. Use uno de: {', '.join(FORMATOS_VALIDOS)}"
        )

    # Forzamos el descubrimiento automático de submódulos antes de consultar
    _cargar_modulos_dinamicos()

    tools = registry.get_tools()
    handler = tools.get(subcommand)

    if handler is None:
        print(
            f"Error: subcomando desconocido '{subcommand}'",
            file=sys.stderr,
        )
        return 1

    try:
        resultado = handler()
    except (ImportError, ModuleNotFoundError):
        print(
            "Error: El módulo solicitado no está disponible o no existe.",
            file=sys.stderr,
        )
        return 1

    return _formatear_resultado(resultado, formato)
