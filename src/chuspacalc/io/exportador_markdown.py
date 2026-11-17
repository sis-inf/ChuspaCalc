"""
Módulo para exportar resultados de cálculos a formato Markdown.
"""

import re
from typing import Any, Dict, List, Optional


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
    """
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
    """
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
    """
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
    """
    markdown = f"## {titulo}\n\n"

    for i, elemento in enumerate(elementos, 1):
        if ordenada:
            markdown += f"{i}. {elemento}\n"
        else:
            markdown += f"- {elemento}\n"

    return markdown + "\n"
