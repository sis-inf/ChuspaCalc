"""
Calculadora del discriminante de una ecuación cuadrática.

Fórmula:
    D = b² - 4ac
"""

import math

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def calcular_discriminante(
    a: int | float,
    b: int | float,
    c: int | float,
) -> int | float:
    """
    Calcula el discriminante de una ecuación cuadrática.

    Args:
        a: Coeficiente cuadrático, distinto de cero.
        b: Coeficiente lineal.
        c: Término independiente.

    Returns:
        El valor del discriminante.

    Raises:
        ErrorValidacion: Si algún coeficiente es inválido,
            no finito o si ocurre un desbordamiento numérico.
    """
    coeficientes = (a, b, c)

    for nombre, valor in zip(("a", "b", "c"), coeficientes):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ErrorValidacion(
                f"El coeficiente {nombre} debe ser numérico: {valor!r}"
            )

        if isinstance(valor, float) and not math.isfinite(valor):
            raise ErrorValidacion(f"El coeficiente {nombre} debe ser finito: {valor}")

    if a == 0:
        raise ErrorValidacion("El coeficiente principal a no puede ser cero.")

    try:
        discriminante = b**2 - 4 * a * c
    except OverflowError as error:
        raise ErrorValidacion(
            "El resultado está fuera del rango numérico permitido."
        ) from error

    if isinstance(discriminante, float) and not math.isfinite(discriminante):
        raise ErrorValidacion("El resultado debe ser un número finito.")

    return discriminante
