"""
Calculadora de fraccion molar.
"""

import math


def calcular_fraccion_molar(moles_componente, moles_totales):
    """
    Calcula la fraccion molar de un componente en una mezcla.

    Args:
        moles_componente: Cantidad de moles del componente.
        moles_totales: Cantidad total de moles de la mezcla.

    Returns:
        Fraccion molar del componente.
    """
    valores = (moles_componente, moles_totales)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Los moles deben ser valores numericos.")

        if not math.isfinite(valor):
            raise ValueError("Los moles deben ser valores finitos.")

        if valor < 0:
            raise ValueError("Los moles no pueden ser negativos.")

    if moles_totales <= 0:
        raise ValueError("Los moles totales deben ser mayores que cero.")

    if moles_componente > moles_totales:
        raise ValueError("Los moles del componente no pueden superar el total.")

    fraccion = moles_componente / moles_totales

    return fraccion
