"""
Despachador de comandos que mapea subcomandos a herramientas
consultando al registry real.
"""

from __future__ import annotations

import sys
from typing import Any

from escuadra.core.registry import buscar_por_nombre


def despacho(nombre: str) -> Any:
    """Despacha un subcomando a su herramienta."""
    herramienta_cls = buscar_por_nombre(nombre)
    if herramienta_cls is None:
        sys.stderr.write(f"Error: subcomando desconocido '{nombre}'\n")
        return None
    instancia = herramienta_cls()
    if hasattr(instancia, "ejecutar"):
        return instancia.ejecutar()
    if hasattr(instancia, "run"):
        return instancia.run()
    return instancia


def dispatch(subcommand: str) -> int:
    """Despacha un subcomando a su herramienta correspondiente."""
    result = despacho(subcommand)
    if result is None:
        return 1
    if isinstance(result, int):
        return result
    return 0
