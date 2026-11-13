
"""
Calculadora de divisor de tensión.

Calcula la tensión de salida sobre la segunda resistencia
de dos resistencias conectadas en serie.

Fórmula:
    Vout = Vin * R2 / (R1 + R2)
"""

import math


def calcular_divisor_tension(tension_entrada, resistencia_1, resistencia_2):
    """
    Calcula la tensión de salida de un divisor resistivo.

    Args:
        tension_entrada: Tensión de entrada en voltios.
        resistencia_1: Primera resistencia en ohmios.
        resistencia_2: Segunda resistencia en ohmios.

    Returns:
        Tensión de salida sobre la segunda resistencia, en voltios.

    Raises:
        TypeError: Si algún argumento no es numérico.
        ValueError: Si los valores no son finitos o las resistencias
            no son positivas.
    """
    valores = (
        tension_entrada,
        resistencia_1,
        resistencia_2,
    )

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Todos los argumentos deben ser números.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Todos los valores deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Todos los valores deben ser finitos.") from error

    if resistencia_1 <= 0 or resistencia_2 <= 0:
        raise ValueError("Las resistencias deben ser mayores que cero.")

    try:
        mayor = max(resistencia_1, resistencia_2)
        proporcion = (resistencia_2 / mayor) / (
            resistencia_1 / mayor + resistencia_2 / mayor
        )
        tension_salida = tension_entrada * proporcion
    except (OverflowError, ZeroDivisionError) as error:
        raise ValueError("No se pudo calcular la tensión de salida.") from error

    if not math.isfinite(tension_salida):
        raise ValueError("La tensión de salida debe ser finita.")

    return tension_salida
