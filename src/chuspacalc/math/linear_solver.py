"""
Módulo para solucionar sistemas de ecuaciones lineales 2x2
"""

import math
from numbers import Real
from typing import Optional, Tuple

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

_MENSAJE_RESULTADO = "El resultado calculado no es finito."


def _validar_real_finito(nombre: str, valor: object) -> None:
    """
    Comprueba que el valor sea un número real finito (sin contar bool).

    Raises:
        ErrorValidacion: Si el valor no es numérico o no es finito.
    """
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(
            f"El valor de {nombre} debe ser un número real: {valor!r}."
        )
    try:
        es_finito = math.isfinite(valor)
    except OverflowError:
        es_finito = False
    if not es_finito:
        raise ErrorValidacion(f"El valor de {nombre} debe ser finito: {valor}.")


def solve_linear_2x2(
    a11: float, a12: float, a21: float, a22: float, b1: float, b2: float
) -> Optional[Tuple[float, float]]:
    """
    Resuelve un sistema de ecuaciones lineales 2x2 usando la regla de Cramer.

    Sistema representado como:
    a11*x + a12*y = b1
    a21*x + a22*y = b2

    Args:
        a11, a12: Coeficientes de la primera ecuación
        a21, a22: Coeficientes de la segunda ecuación
        b1, b2: Términos independientes

    Returns:
        Tupla (x, y) solución del sistema, o None si el determinante es cero

    Raises:
        ErrorValidacion: Si algún coeficiente o término independiente no es un
            número real (por ejemplo None, texto o bool), no es finito (NaN, inf
            o -inf), o si el determinante o la solución calculados no son
            finitos. Es subclase de ValueError.

    Examples:
        >>> solve_linear_2x2(2, 3, 1, 4, 5, 6)
        (0.4, 1.4)

        >>> solve_linear_2x2(1, 1, 1, 1, 2, 3)
        None
    """
    datos = {"a11": a11, "a12": a12, "a21": a21, "a22": a22, "b1": b1, "b2": b2}
    for nombre, valor in datos.items():
        _validar_real_finito(nombre, valor)

    try:
        # Calcular el determinante principal
        det = a11 * a22 - a12 * a21
        if not math.isfinite(det):
            raise ErrorValidacion(_MENSAJE_RESULTADO)

        # Si el determinante es cero, no hay solución única
        if abs(det) < 1e-10:
            return None

        # Calcular determinantes para x e y
        det_x = b1 * a22 - a12 * b2
        det_y = a11 * b2 - b1 * a21

        # Calcular x e y
        x = det_x / det
        y = det_y / det
    except OverflowError as error:
        raise ErrorValidacion(_MENSAJE_RESULTADO) from error

    if not (math.isfinite(x) and math.isfinite(y)):
        raise ErrorValidacion(_MENSAJE_RESULTADO)

    return (x, y)
