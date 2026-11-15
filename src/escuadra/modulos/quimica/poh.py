
"""
Calculadora del pOH de una solución.

Fórmula:
    pOH = -log10(concentracion_oh)
"""

import math


def calcular_poh(concentracion_oh):
    """
    Calcula el pOH a partir de la concentración de iones hidróxido.

    Args:
        concentracion_oh: Concentración de iones OH- en mol/L.

    Returns:
        El valor calculado del pOH.

    Raises:
        TypeError: Si la concentración no es numérica.
        ValueError: Si la concentración no es positiva o finita.
    """
    if isinstance(concentracion_oh, bool) or not isinstance(
        concentracion_oh, (int, float)
    ):
        raise TypeError("La concentración debe ser un valor numérico.")

    if not math.isfinite(concentracion_oh):
        raise ValueError("La concentración debe ser finita.")

    if concentracion_oh <= 0:
        raise ValueError("La concentración debe ser positiva y mayor que cero.")

    resultado = -math.log10(concentracion_oh)

    if not math.isfinite(resultado):
        raise ValueError("El resultado debe ser finito.")

    return resultado
