import math


def calcular_volumen_excavacion(longitud, ancho, profundidad):
    """
    Calcula el volumen de una excavación rectangular.

    Args:
        longitud: Longitud de la excavación.
        ancho: Ancho de la excavación.
        profundidad: Profundidad de la excavación.

    Returns:
        Volumen calculado.

    Raises:
        ValueError: Si alguna dimensión no es positiva o finita.
        TypeError: Si alguna dimensión no es numérica.
    """
    dimensiones = (longitud, ancho, profundidad)

    for dimension in dimensiones:
        if isinstance(dimension, bool) or not isinstance(dimension, (int, float)):
            raise TypeError("Las dimensiones deben ser valores numéricos.")

        if not math.isfinite(dimension) or dimension <= 0:
            raise ValueError("Las dimensiones deben ser positivas y finitas.")

    return longitud * ancho * profundidad
