"""
Calculadora del rendimiento porcentual de una reacción química.

Fórmula:
    rendimiento = (rendimiento_real / rendimiento_teorico) * 100
"""

import math


def calcular_rendimiento_porcentual(rendimiento_real, rendimiento_teorico):
    """
    Calcula el rendimiento porcentual de una reacción química.

    Args:
        rendimiento_real: Cantidad de producto obtenida.
        rendimiento_teorico: Cantidad máxima de producto esperada.

    Returns:
        El rendimiento expresado en porcentaje.

    Raises:
        TypeError: Si los valores no son numéricos.
        ValueError: Si los valores no son finitos, el rendimiento
                    teórico no es positivo o el real es negativo.
    """
    valores = (rendimiento_real, rendimiento_teorico)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Los rendimientos deben ser valores numéricos.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Los rendimientos deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Los rendimientos deben ser finitos.") from error

    if rendimiento_teorico <= 0:
        raise ValueError("El rendimiento teórico debe ser mayor que cero.")

    if rendimiento_real < 0:
        raise ValueError("El rendimiento real no puede ser negativo.")

    try:
        resultado = (float(rendimiento_real) / float(rendimiento_teorico)) * 100
    except (OverflowError, ZeroDivisionError) as error:
        raise ValueError("No se pudo calcular un resultado válido.") from error

    if not math.isfinite(resultado):
        raise ValueError("El resultado debe ser finito.")

    return resultado
