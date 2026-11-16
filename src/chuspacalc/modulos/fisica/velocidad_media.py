
"""
Calculadora de velocidad media.
"""

import math


def calcular_velocidad_media(desplazamiento, tiempo):
    """
    Calcula la velocidad media a partir del desplazamiento y el tiempo.

    Fórmula:
        velocidad_media = desplazamiento / tiempo

    Args:
        desplazamiento: Desplazamiento del objeto.
        tiempo: Tiempo transcurrido.

    Returns:
        Velocidad media calculada.

    Raises:
        TypeError: Si los argumentos no son numéricos.
        ValueError: Si los valores no son finitos, el tiempo no es
            positivo o el resultado no es finito.
    """
    valores = (desplazamiento, tiempo)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Los argumentos deben ser numéricos.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Los argumentos deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Los argumentos deben ser finitos.") from error

    if tiempo <= 0:
        raise ValueError("El tiempo debe ser positivo.")

    try:
        velocidad = desplazamiento / tiempo
    except OverflowError as error:
        raise ValueError("El resultado está fuera del rango permitido.") from error

    if not math.isfinite(velocidad):
        raise ValueError("El resultado debe ser finito.")

    return velocidad
