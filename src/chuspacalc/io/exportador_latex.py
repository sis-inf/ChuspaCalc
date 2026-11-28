"""
Exportador de resultados a formato LaTeX.

Permite generar tablas y fórmulas listas para documentos académicos,
validando los tipos y las estructuras de entrada.
"""

import math
from collections.abc import Mapping

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

_REEMPLAZOS_LATEX: dict[str, str] = {
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
}


def escapar_latex(texto: str | int | float) -> str:
    """Escapa caracteres especiales de LaTeX.

    Acepta cadenas de texto y valores numéricos finitos.
    Rechaza valores nulos, booleanos y tipos no compatibles.

    Args:
        texto: Cadena o valor numérico que se desea escapar.

    Returns:
        Texto con los caracteres especiales de LaTeX escapados.

    Raises:
        ErrorValidacion: Si el valor es nulo, booleano, no compatible
            o contiene un número no finito.
    """
    if texto is None:
        raise ErrorValidacion("El texto que se desea escapar no puede ser None.")

    if isinstance(texto, bool):
        raise ErrorValidacion("El texto que se desea escapar no puede ser booleano.")

    if isinstance(texto, str):
        texto_validado = texto

    elif isinstance(texto, int):
        texto_validado = str(texto)

    elif isinstance(texto, float):
        if not math.isfinite(texto):
            raise ErrorValidacion(
                "El valor numérico que se desea escapar debe ser finito."
            )
        texto_validado = str(texto)

    else:
        raise ErrorValidacion(
            "El valor que se desea escapar debe ser texto o un número."
        )

    for caracter, reemplazo in _REEMPLAZOS_LATEX.items():
        texto_validado = texto_validado.replace(caracter, reemplazo)

    return texto_validado


def exportar_tabla(
    parametros: Mapping[str | int | float, str | int | float],
    resultado: str | int | float,
    formula: str | None = None,
) -> str:
    """Genera una tabla LaTeX con parámetros y resultado.

    Los parámetros deben proporcionarse como un diccionario o una
    estructura compatible con Mapping. Sus claves y valores deben
    ser cadenas o números finitos.

    La fórmula, cuando se proporciona, se conserva como código
    matemático LaTeX y no se escapa automáticamente.

    Args:
        parametros: Mapeo de nombres de parámetros y sus valores.
        resultado: Resultado del cálculo, como texto o número finito.
        formula: Expresión matemática LaTeX opcional.

    Returns:
        Código LaTeX de la tabla y, si corresponde, de la fórmula.

    Raises:
        ErrorValidacion: Si los parámetros no son un mapeo válido,
            alguno de sus elementos no es compatible, el resultado
            es inválido o la fórmula no es texto.
    """
    if not isinstance(parametros, Mapping):
        raise ErrorValidacion(
            "Los parámetros deben proporcionarse como un diccionario "
            "o una estructura de tipo Mapping."
        )

    if formula is not None and not isinstance(formula, str):
        raise ErrorValidacion("La fórmula debe ser una cadena de texto o None.")

    resultado_validado = escapar_latex(resultado)

    lineas = [
        r"\begin{tabular}{|l|l|}",
        r"\hline",
        "Parámetro & Valor \\\\",
        r"\hline",
    ]

    for clave, valor in parametros.items():
        clave_validada = escapar_latex(clave)
        valor_validado = escapar_latex(valor)

        lineas.append(f"{clave_validada} & {valor_validado} \\\\")

    lineas.extend(
        [
            r"\hline",
            f"Resultado & {resultado_validado} \\\\",
            r"\hline",
            r"\end{tabular}",
        ]
    )

    if formula:
        lineas.extend(
            [
                "",
                r"\[",
                formula,
                r"\]",
            ]
        )

    return "\n".join(lineas)
