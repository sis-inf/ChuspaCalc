"""
Calculadora del volumen final de un gas mediante la ley de Boyle.

Fórmula:
    P1 * V1 = P2 * V2
    V2 = (P1 * V1) / P2
"""

import math


def calcular_volumen_boyle(presion_inicial, volumen_inicial, presion_final):
    """
    Calcula el volumen final de un gas aplicando la ley de Boyle.

    Args:
        presion_inicial: Presión inicial del gas.
        volumen_inicial: Volumen inicial del gas.
        presion_final: Presión final del gas.

    Returns:
        El volumen final calculado.

    Raises:
        TypeError: Si algún valor no es numérico.
        ValueError: Si algún valor no es positivo o finito,
                    o si el resultado no es finito.
    """
    valores = (presion_inicial, volumen_inicial, presion_final)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Las presiones y el volumen deben ser numéricos.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Los valores deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Los valores deben ser finitos.") from error

        if valor <= 0:
            raise ValueError("Las presiones y el volumen deben ser positivos.")

    try:
        volumen_final = (float(presion_inicial) * float(volumen_inicial)) / float(
            presion_final
        )
    except OverflowError as error:
        raise ValueError("El resultado está fuera del rango permitido.") from error

    if not math.isfinite(volumen_final):
        raise ValueError("El volumen final debe ser finito.")

    return volumen_final
