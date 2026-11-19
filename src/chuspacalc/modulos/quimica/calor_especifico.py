"""
Calculadora del calor específico de una sustancia.

Fórmula:
    c = Q / (m * ΔT)
"""

import math


def calcular_calor_especifico(calor, masa, cambio_temperatura):
    """
    Calcula el calor específico de una sustancia.

    Args:
        calor: Calor intercambiado en julios.
        masa: Masa de la sustancia.
        cambio_temperatura: Variación de temperatura.

    Returns:
        El calor específico calculado.

    Raises:
        TypeError: Si algún valor no es numérico.
        ValueError: Si la masa no es positiva, algún valor no es finito,
                    el cambio de temperatura es cero o el resultado no es finito.
    """
    valores = (calor, masa, cambio_temperatura)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Los parámetros deben ser números reales.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Los parámetros deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Los parámetros deben ser finitos.") from error

    if masa <= 0:
        raise ValueError("La masa debe ser positiva.")

    if cambio_temperatura == 0:
        raise ValueError("El cambio de temperatura no puede ser cero.")

    try:
        calor_especifico = float(calor) / (float(masa) * float(cambio_temperatura))
    except OverflowError as error:
        raise ValueError("El resultado está fuera del rango permitido.") from error

    if not math.isfinite(calor_especifico):
        raise ValueError("El resultado debe ser finito.")

    return calor_especifico
