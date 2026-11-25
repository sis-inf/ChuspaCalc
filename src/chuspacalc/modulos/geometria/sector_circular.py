"""
Calculadora del área de un sector circular.
"""

import math


def calcular_area_sector(radio, angulo):
    """
    Calcula el área de un sector circular usando el ángulo en grados.

    Fórmula:
        A = (angulo / 360) * pi * radio²

    Args:
        radio: Radio del círculo.
        angulo: Ángulo central expresado en grados.

    Returns:
        Área del sector circular.

    Raises:
        TypeError: Si los argumentos no son numéricos.
        ValueError: Si el radio no es positivo, los valores no son
            finitos o el ángulo está fuera del intervalo permitido.
    """
    valores = (radio, angulo)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("El radio y el ángulo deben ser numéricos.")

        if not math.isfinite(valor):
            raise ValueError("Los valores deben ser finitos.")

    if radio <= 0:
        raise ValueError("El radio debe ser positivo.")

    if not 0 <= angulo <= 360:
        raise ValueError("El ángulo debe estar entre 0 y 360 grados.")

    area = (angulo / 360) * math.pi * radio**2

    if not math.isfinite(area):
        raise ValueError("El resultado debe ser finito.")

    return area
