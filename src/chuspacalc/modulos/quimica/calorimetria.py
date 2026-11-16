
"""
Calculadora del calor absorbido o cedido por una sustancia.

Fórmula:
    Q = m * c * ΔT
"""


import math


def calcular_calor(masa, calor_especifico, cambio_temperatura):
    """
    Calcula el calor intercambiado por una sustancia.

    Args:
        masa: Masa de la sustancia.
        calor_especifico: Calor específico de la sustancia.
        cambio_temperatura: Variación de temperatura.

    Returns:
        El calor calculado en julios.

    Raises:
        TypeError: Si algún valor no es numérico.
        ValueError: Si la masa o el calor específico no son positivos,
                    si algún valor no es finito o si el resultado no es finito.
    """
    valores = (masa, calor_especifico, cambio_temperatura)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Los parámetros deben ser números reales.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Los parámetros deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Los parámetros deben ser finitos.") from error

    if masa <= 0 or calor_especifico <= 0:
        raise ValueError("La masa y el calor específico deben ser positivos.")

    try:
        calor = (
            float(masa)
            * float(calor_especifico)
            * float(cambio_temperatura)
        )
    except OverflowError as error:
        raise ValueError("El resultado está fuera del rango permitido.") from error

    if not math.isfinite(calor):
        raise ValueError("El calor calculado debe ser finito.")

    return calor
