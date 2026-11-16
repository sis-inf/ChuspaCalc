import math


def calcular_energia_cinetica(masa, velocidad):
    """
    Calcula la energia cinetica de un cuerpo.

    Args:
        masa: Masa del cuerpo en kilogramos.
        velocidad: Velocidad del cuerpo en metros por segundo.

    Returns:
        Energia cinetica en joules.

    Raises:
        TypeError: Si los argumentos no son numericos.
        ValueError: Si la masa no es positiva o los valores no son finitos.
    """
    if isinstance(masa, bool) or isinstance(velocidad, bool):
        raise TypeError("La masa y la velocidad deben ser numericas.")

    if not isinstance(masa, (int, float)) or not isinstance(velocidad, (int, float)):
        raise TypeError("La masa y la velocidad deben ser numericas.")

    if not math.isfinite(masa) or not math.isfinite(velocidad):
        raise ValueError("Los valores deben ser finitos.")

    if masa <= 0:
        raise ValueError("La masa debe ser un numero positivo.")

    energia = (masa * velocidad ** 2) / 2

    if not math.isfinite(energia):
        raise ValueError("El resultado debe ser finito.")

    return energia
