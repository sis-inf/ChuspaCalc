"""
Módulo para solucionar sistemas de ecuaciones lineales 2x2
"""

import math
from typing import Optional, Tuple


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
        ValueError: Si algún coeficiente o término independiente no es finito
            (NaN, inf o -inf).

    Examples:
        >>> solve_linear_2x2(2, 3, 1, 4, 5, 6)
        (0.4, 1.4)

        >>> solve_linear_2x2(1, 1, 1, 1, 2, 3)
        None
    """
    datos = {"a11": a11, "a12": a12, "a21": a21, "a22": a22, "b1": b1, "b2": b2}
    for nombre, valor in datos.items():
        if not math.isfinite(valor):
            raise ValueError(f"El valor de {nombre} debe ser finito: {valor}.")

    # Calcular el determinante principal
    det = a11 * a22 - a12 * a21

    # Si el determinante es cero, no hay solución única
    if abs(det) < 1e-10:
        return None

    # Calcular determinantes para x e y
    det_x = b1 * a22 - a12 * b2
    det_y = a11 * b2 - b1 * a21

    # Calcular x e y
    x = det_x / det
    y = det_y / det

    return (x, y)
