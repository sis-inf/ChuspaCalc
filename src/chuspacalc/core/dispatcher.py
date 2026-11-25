"""
Despachador de comandos que mapea subcomandos a funciones ejecutables
consultando dinámicamente al registry.
"""

import json
import sys
from typing import Protocol, runtime_checkable

from chuspacalc.core import registry

FORMATOS_VALIDOS = ("dict", "json", "texto")
Resultado = int | dict[str, object] | str


@runtime_checkable
class HerramientaEjecutable(Protocol):
    def ejecutar(self) -> Resultado: ...


def _formatear_resultado(resultado: Resultado, formato: str) -> Resultado:
    """
    Convierte el resultado de un handler al formato solicitado.

    Args:
        resultado: Valor devuelto por el handler. Solo se formatea si es un diccionario.
        formato: Formato de salida: 'dict', 'json' o 'texto'.

    Returns:
        El mismo resultado si el formato es 'dict' o si no es un diccionario.
        En otro caso, una cadena JSON ('json') o una cadena con una linea
        'clave: valor' por entrada ('texto').
    """
    if formato == "dict" or not isinstance(resultado, dict):
        return resultado
    if formato == "json":
        return json.dumps(resultado, indent=2, ensure_ascii=False)
    return "\n".join(f"{clave}: {valor}" for clave, valor in resultado.items())


def dispatch(subcommand: str, formato: str = "dict") -> Resultado:
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

    herramienta = registry.buscar_por_nombre(subcommand)
    if herramienta is None:
        print(
            f"Error: subcomando desconocido '{subcommand}'",
            file=sys.stderr,
        )
        return 1

    try:
        instancia = herramienta()
    except (ImportError, ModuleNotFoundError):
        print(
            "Error: El módulo solicitado no está disponible o no existe.",
            file=sys.stderr,
        )
        return 1

    if not isinstance(instancia, HerramientaEjecutable):
        print(
            f"Error: la herramienta '{subcommand}' no es ejecutable.",
            file=sys.stderr,
        )
        return 1

    resultado = instancia.ejecutar()
    return _formatear_resultado(resultado, formato)
