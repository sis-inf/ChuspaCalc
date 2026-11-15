
"""
Calculadora de varianza poblacional.
"""

import math


def calcular_varianza_poblacional(datos):
    """
    Calcula la varianza poblacional de un conjunto de datos.

    Args:
        datos: Lista de valores numericos.

    Returns:
        Varianza poblacional calculada.
    """
    if not isinstance(datos, (list, tuple)):
        raise TypeError("Los datos deben ser una lista o tupla.")

    if not datos:
        raise ValueError("La lista de datos no puede estar vacia.")

    for valor in datos:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Todos los datos deben ser numericos.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Todos los datos deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Todos los datos deben ser finitos.") from error

    try:
        media = math.fsum(datos) / len(datos)
        diferencias_cuadradas = [(valor - media) ** 2 for valor in datos]
        varianza = math.fsum(diferencias_cuadradas) / len(datos)
    except (OverflowError, ValueError) as error:
        raise ValueError("No se pudo calcular la varianza poblacional.") from error

    if not math.isfinite(varianza):
        raise ValueError("El resultado debe ser finito.")

    return varianza
