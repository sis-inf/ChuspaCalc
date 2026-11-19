"""
Calculadora de fuerza peso de un cuerpo.

Fórmula:
    P = m * g
"""

import math


def calcular_fuerza_peso(masa, gravedad):
    """
    Calcula la fuerza peso a partir de la masa y la gravedad.

    Args:
        masa: Masa del cuerpo en kilogramos.
        gravedad: Aceleración gravitatoria en m/s².

    Returns:
        Fuerza peso expresada en newtons.

    Raises:
        TypeError: Si los argumentos no son numéricos.
        ValueError: Si los valores no son positivos o finitos.
    """
    valores = (masa, gravedad)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("La masa y la gravedad deben ser numéricas.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Los valores deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Los valores deben ser finitos.") from error

        if valor <= 0:
            raise ValueError("La masa y la gravedad deben ser positivas.")

    try:
        fuerza = masa * gravedad
    except OverflowError as error:
        raise ValueError("El resultado está fuera del rango permitido.") from error

    if not math.isfinite(fuerza):
        raise ValueError("El resultado debe ser finito.")

    return fuerza
