"""
Calculadora de distancia de un punto al origen de coordenadas.
"""

import math


def calcular_distancia_origen(x, y):
    """
    Calcula la distancia entre un punto (x, y) y el origen (0, 0).

    Fórmula:
        d = sqrt(x² + y²)

    Args:
        x: Coordenada horizontal.
        y: Coordenada vertical.

    Returns:
        Distancia calculada.

    Raises:
        TypeError: Si las coordenadas no son numéricas.
        ValueError: Si las coordenadas no son finitas o el resultado
            no es finito.
    """
    coordenadas = (x, y)

    for valor in coordenadas:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Las coordenadas deben ser numéricas.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Las coordenadas deben ser finitas.")
        except OverflowError as error:
            raise ValueError("Las coordenadas deben ser finitas.") from error

    distancia = math.hypot(x, y)

    if not math.isfinite(distancia):
        raise ValueError("El resultado debe ser finito.")

    return distancia
