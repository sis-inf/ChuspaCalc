"""
Calculadora de vida media radiactiva.
"""

import math


def calcular_cantidad_restante(cantidad_inicial, tiempo, vida_media):
    """
    Calcula la cantidad restante de una sustancia radiactiva.

    Args:
        cantidad_inicial: Cantidad inicial de la sustancia.
        tiempo: Tiempo transcurrido.
        vida_media: Tiempo necesario para reducir la cantidad a la mitad.

    Returns:
        Cantidad restante de la sustancia.
    """
    valores = {
        "cantidad inicial": cantidad_inicial,
        "tiempo": tiempo,
        "vida media": vida_media,
    }

    for nombre, valor in valores.items():
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError(f"El {nombre} debe ser numerico.")

        if not math.isfinite(valor):
            raise ValueError(f"El {nombre} debe ser finito.")

    if cantidad_inicial < 0:
        raise ValueError("La cantidad inicial no puede ser negativa.")

    if tiempo < 0:
        raise ValueError("El tiempo no puede ser negativo.")

    if vida_media <= 0:
        raise ValueError("La vida media debe ser positiva.")

    cantidad_restante = cantidad_inicial * (0.5 ** (tiempo / vida_media))

    if not math.isfinite(cantidad_restante):
        raise ValueError("El resultado no es finito.")

    return cantidad_restante
