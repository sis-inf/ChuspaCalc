
"""
Calculadora del rango estadístico de un conjunto de datos.
"""


import math


def calcular_rango(datos):
    """
    Calcula el rango mediante la diferencia entre el máximo
    y el mínimo de un conjunto de datos.

    Args:
        datos: Lista o tupla de valores numéricos.

    Returns:
        Diferencia entre el valor máximo y el mínimo.

    Raises:
        TypeError: Si los datos no son una lista o contienen
            valores no numéricos.
        ValueError: Si la colección está vacía o contiene
            valores no finitos.
    """
    if not isinstance(datos, (list, tuple)):
        raise TypeError("Los datos deben ser una lista o tupla.")

    if not datos:
        raise ValueError("La lista de datos no puede estar vacía.")

    for valor in datos:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Todos los datos deben ser numéricos.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Todos los datos deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Los datos deben ser finitos.") from error

    try:
        rango = max(datos) - min(datos)
    except OverflowError as error:
        raise ValueError("El rango está fuera del límite permitido.") from error

    if not math.isfinite(rango):
        raise ValueError("El resultado debe ser finito.")

    return rango
