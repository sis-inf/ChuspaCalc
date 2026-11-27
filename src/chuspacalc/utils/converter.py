"""Funciones de conversion de unidades de uso general.

Incluye conversiones de temperatura y de longitud.
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit.

    Args:
        celsius: Temperatura en grados Celsius.

    Returns:
        Temperatura equivalente en grados Fahrenheit.

    Example:
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return (celsius * 9 / 5) + 32


def km_to_miles(km: float) -> float:
    """Convierte kilómetros a millas.

    Args:
        km: Distancia en kilómetros.

    Returns:
        Distancia equivalente en millas.

    Example:
        >>> km_to_miles(4)
        2.485484
    """
    return km * 0.621371
