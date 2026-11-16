
"""
Calculadora de dilatacion lineal de materiales.
"""

import math


def calcular_dilatacion_lineal(longitud_inicial, coeficiente, cambio_temperatura):
    """
    Calcula la variacion de longitud usando la formula:
    delta_L = L0 * alfa * delta_T.

    Args:
        longitud_inicial: Longitud inicial del material.
        coeficiente: Coeficiente de dilatacion lineal.
        cambio_temperatura: Variacion de temperatura.

    Returns:
        Variacion de longitud calculada.
    """
    valores = (longitud_inicial, coeficiente, cambio_temperatura)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Todos los valores deben ser numericos.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Todos los valores deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Todos los valores deben ser finitos.") from error

    if longitud_inicial <= 0:
        raise ValueError("La longitud inicial debe ser positiva.")

    if coeficiente <= 0:
        raise ValueError("El coeficiente debe ser positivo.")

    try:
        dilatacion = longitud_inicial * coeficiente * cambio_temperatura
    except OverflowError as error:
        raise ValueError("El resultado no es finito.") from error

    if not math.isfinite(dilatacion):
        raise ValueError("El resultado debe ser finito.")

    return dilatacion
