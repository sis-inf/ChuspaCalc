
"""
Calculadora del volumen final de un gas mediante la ley de Charles.

Fórmula:
    V1 / T1 = V2 / T2
    V2 = (V1 * T2) / T1
"""


import math


def calcular_volumen_charles(volumen_inicial, temperatura_inicial, temperatura_final):
    """
    Calcula el volumen final de un gas aplicando la ley de Charles.

    Args:
        volumen_inicial: Volumen inicial del gas.
        temperatura_inicial: Temperatura inicial en kelvin.
        temperatura_final: Temperatura final en kelvin.

    Returns:
        El volumen final calculado.

    Raises:
        TypeError: Si algún valor no es numérico.
        ValueError: Si algún valor no es positivo o finito,
                    o si el resultado no es finito.
    """
    valores = (volumen_inicial, temperatura_inicial, temperatura_final)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Los valores deben ser números reales.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Los valores deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Los valores deben ser finitos.") from error

        if valor <= 0:
            raise ValueError("Los volúmenes y temperaturas deben ser positivos.")

    try:
        volumen_final = (
            float(volumen_inicial) * float(temperatura_final)
        ) / float(temperatura_inicial)
    except OverflowError as error:
        raise ValueError("El resultado está fuera del rango permitido.") from error

    if not math.isfinite(volumen_final):
        raise ValueError("El volumen final debe ser finito.")

    return volumen_final
