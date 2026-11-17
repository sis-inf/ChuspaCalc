"""
Calculadora de amplitud de intervalos estadísticos.
"""

import math


def calcular_amplitud_intervalo(valor_minimo, valor_maximo, numero_intervalos):
    """
    Calcula la amplitud de cada intervalo de clase.

    Args:
        valor_minimo: Valor mínimo del conjunto de datos.
        valor_maximo: Valor máximo del conjunto de datos.
        numero_intervalos: Cantidad de intervalos de clase.

    Returns:
        Amplitud calculada de los intervalos.
    """
    valores = (valor_minimo, valor_maximo)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Los valores deben ser numericos.")

        if not math.isfinite(valor):
            raise ValueError("Los valores deben ser finitos.")

    if valor_maximo <= valor_minimo:
        raise ValueError("El valor maximo debe ser mayor que el minimo.")

    if isinstance(numero_intervalos, bool) or not isinstance(numero_intervalos, int):
        raise TypeError("El numero de intervalos debe ser un entero.")

    if numero_intervalos <= 0:
        raise ValueError("El numero de intervalos debe ser positivo.")

    rango = valor_maximo - valor_minimo
    amplitud = rango / numero_intervalos

    if not math.isfinite(amplitud):
        raise ValueError("El resultado debe ser finito.")

    return amplitud
