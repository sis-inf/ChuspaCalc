"""
Calculadora de variación porcentual entre dos valores.
"""

import math


def calcular_variacion_porcentual(valor_inicial, valor_final):
    """
    Calcula el cambio porcentual entre un valor inicial y uno final.

    Fórmula:
        ((valor_final - valor_inicial) / valor_inicial) * 100

    Returns:
        Variación porcentual calculada.

    Raises:
        TypeError: Si los valores no son numéricos.
        ValueError: Si el valor inicial es cero o los valores
            no son finitos.
    """
    valores = (valor_inicial, valor_final)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Los valores deben ser numéricos.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Los valores deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Los valores deben ser finitos.") from error

    if valor_inicial == 0:
        raise ValueError("El valor inicial no puede ser cero.")

    variacion = ((valor_final - valor_inicial) / valor_inicial) * 100

    if not math.isfinite(variacion):
        raise ValueError("El resultado debe ser finito.")

    return variacion
