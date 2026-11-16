
"""
Calculadora del área de un rombo.
"""

import math


def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    """
    Calcula el área de un rombo a partir de sus diagonales.

    Fórmula:
        A = (diagonal_mayor * diagonal_menor) / 2

    Args:
        diagonal_mayor: Longitud de la diagonal mayor.
        diagonal_menor: Longitud de la diagonal menor.

    Returns:
        Área calculada del rombo.

    Raises:
        TypeError: Si las diagonales no son numéricas.
        ValueError: Si las diagonales no son positivas, finitas
            o si la diagonal mayor es menor que la menor.
    """
    diagonales = (diagonal_mayor, diagonal_menor)

    for valor in diagonales:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Las diagonales deben ser numéricas.")

        if not math.isfinite(valor):
            raise ValueError("Las diagonales deben ser finitas.")

        if valor <= 0:
            raise ValueError("Las diagonales deben ser positivas.")

    if diagonal_mayor < diagonal_menor:
        raise ValueError(
            "La diagonal mayor no puede ser menor que la diagonal menor."
        )

    area = (diagonal_mayor * diagonal_menor) / 2

    if not math.isfinite(area):
        raise ValueError("El resultado debe ser finito.")

    return area
