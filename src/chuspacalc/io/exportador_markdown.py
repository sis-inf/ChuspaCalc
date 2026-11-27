"""
Módulo para exportar resultados de cálculos a formato Markdown.
"""

import re
from typing import Any, Dict, List, Optional

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def _validar_texto(valor: str, nombre: str, permitir_vacio: bool = False) -> None:
    if not isinstance(valor, str) or (not permitir_vacio and not valor.strip()):
        raise ErrorValidacion(f"{nombre} debe ser texto válido")


def _validar_secuencia(valor: object, nombre: str) -> None:
    if not isinstance(valor, (list, tuple)):
        raise ErrorValidacion(f"{nombre} debe ser una lista o tupla")


def _escapar_celda(valor: Any) -> str:
    """
    Convierte un valor a texto seguro para una celda de tabla Markdown.

    Escapa las barras verticales anteponiéndoles una barra invertida y reemplaza
    los saltos de línea por un espacio, para que la fila conserve sus columnas.
    """
    texto = str(valor).replace("|", r"\|")
    return re.sub(r"\r\n|\r|\n", " ", texto)


def exportar_markdown(
    titulo: str,
    parametros: Dict[str, Any],
    resultado: Any,
    descripcion: Optional[str] = None,
    unidad: Optional[str] = None,
) -> str:
    """
    Genera un bloque Markdown estructurado a partir de los resultados de una herramienta.

    Args:
        titulo: Título del cálculo o herramienta.
        parametros: Diccionario con los parámetros de entrada.
        resultado: Resultado del cálculo (puede ser número, str, lista, etc.).
        descripcion: Descripción opcional del resultado.
        unidad: Unidad opcional del resultado.

    Returns:
        str: Bloque Markdown con la información formateada.

    Raises:
        ErrorValidacion: Si una entrada es nula, tiene tipo incorrecto o
            sus dimensiones no son compatibles con el formato.
    """
    _validar_texto(titulo, "titulo")
    if not isinstance(parametros, dict):
        raise ErrorValidacion("parametros debe ser un diccionario")
    if resultado is None:
        raise ErrorValidacion("resultado no puede ser nulo")
    if descripcion is not None:
        _validar_texto(descripcion, "descripcion", permitir_vacio=True)
    if unidad is not None:
        _validar_texto(unidad, "unidad", permitir_vacio=True)
    # Encabezado
    markdown = f"# {titulo}\n\n"

    # Tabla de parámetros de entrada
    markdown += "## 📥 Parámetros de entrada\n\n"
    markdown += "| Parámetro | Valor |\n"
    markdown += "|-----------|-------|\n"
    for clave, valor in parametros.items():
        markdown += f"| {_escapar_celda(clave)} | {_escapar_celda(valor)} |\n"
    markdown += "\n"

    # Resultado
    markdown += "## 📤 Resultado\n\n"
    if descripcion:
        markdown += f"**{descripcion}**\n\n"

    if unidad:
        markdown += f"```\n{resultado} {unidad}\n```\n\n"
    else:
        markdown += f"```\n{resultado}\n```\n\n"

    return markdown


def exportar_tabla(
    titulo: str,
    encabezados: List[str],
    filas: List[List[Any]],
) -> str:
    """
    Genera una tabla en formato Markdown.

    Args:
        titulo: Título de la tabla.
        encabezados: Lista de nombres de columnas.
        filas: Lista de filas (cada fila es una lista de valores).

    Returns:
        str: Tabla en formato Markdown.

    Raises:
        ErrorValidacion: Si una entrada es nula, tiene tipo incorrecto o
            sus dimensiones no son compatibles con el formato.
    """
    _validar_texto(titulo, "titulo")
    _validar_secuencia(encabezados, "encabezados")
    _validar_secuencia(filas, "filas")
    if not encabezados:
        raise ErrorValidacion("La tabla necesita al menos un encabezado")
    for encabezado in encabezados:
        _validar_texto(encabezado, "encabezado")
    for indice, fila in enumerate(filas, 1):
        _validar_secuencia(fila, f"fila {indice}")
        if len(fila) != len(encabezados):
            raise ErrorValidacion(f"La fila {indice} no coincide con los encabezados")
    markdown = f"## {titulo}\n\n"

    # Encabezados
    markdown += "| " + " | ".join(_escapar_celda(h) for h in encabezados) + " |\n"
    markdown += "| " + " | ".join(["---"] * len(encabezados)) + " |\n"

    # Filas
    for fila in filas:
        markdown += "| " + " | ".join(_escapar_celda(valor) for valor in fila) + " |\n"

    return markdown + "\n"


def exportar_codigo(
    titulo: str,
    codigo: str,
    lenguaje: str = "python",
) -> str:
    """
    Genera un bloque de código en formato Markdown.

    Args:
        titulo: Título del bloque.
        codigo: Código o texto a mostrar.
        lenguaje: Lenguaje de programación (para resaltado de sintaxis).

    Returns:
        str: Bloque de código en Markdown.

    Raises:
        ErrorValidacion: Si una entrada es nula, tiene tipo incorrecto o
            sus dimensiones no son compatibles con el formato.
    """
    _validar_texto(titulo, "titulo")
    _validar_texto(codigo, "codigo", permitir_vacio=True)
    _validar_texto(lenguaje, "lenguaje", permitir_vacio=True)
    if any(caracter in lenguaje for caracter in (chr(96), "\r", "\n")):
        raise ErrorValidacion(
            "lenguaje no puede contener delimitadores ni saltos de línea"
        )
    markdown = f"## {titulo}\n\n"
    markdown += f"```{lenguaje}\n{codigo}\n```\n\n"
    return markdown


def exportar_lista(
    titulo: str,
    elementos: List[str],
    ordenada: bool = False,
) -> str:
    """
    Genera una lista en formato Markdown.

    Args:
        titulo: Título de la lista.
        elementos: Lista de elementos.
        ordenada: Si es True, genera lista numerada; si es False, lista con viñetas.

    Returns:
        str: Lista en formato Markdown.

    Raises:
        ErrorValidacion: Si una entrada es nula, tiene tipo incorrecto o
            sus dimensiones no son compatibles con el formato.
    """
    _validar_texto(titulo, "titulo")
    _validar_secuencia(elementos, "elementos")
    if not isinstance(ordenada, bool):
        raise ErrorValidacion("ordenada debe ser un booleano")
    for elemento in elementos:
        _validar_texto(elemento, "elemento", permitir_vacio=True)
    markdown = f"## {titulo}\n\n"

    for i, elemento in enumerate(elementos, 1):
        if ordenada:
            markdown += f"{i}. {elemento}\n"
        else:
            markdown += f"- {elemento}\n"

    return markdown + "\n"
