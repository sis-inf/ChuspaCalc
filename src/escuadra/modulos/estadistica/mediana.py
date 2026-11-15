
"""
Calculadora de la mediana de un conjunto de datos numéricos.
"""

import math


def calcular_mediana(datos):
    """
    Calcula la mediana de una colección de datos numéricos.

    Args:
        datos: Lista de valores numéricos.

    Returns:
        La mediana del conjunto de datos.

    Raises:
        TypeError: Si los datos no son una lista o contienen
            valores no numéricos.
        ValueError: Si la lista está vacía o contiene valores
            no finitos.
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
            raise ValueError("Los datos deben ser valores finitos.") from error

    valores_ordenados = sorted(datos)
    cantidad = len(valores_ordenados)
    medio = cantidad // 2

    if cantidad % 2 == 1:
        return valores_ordenados[medio]

    try:
        mediana = (
            valores_ordenados[medio - 1] + valores_ordenados[medio]
        ) / 2
    except OverflowError as error:
        raise ValueError("No se pudo calcular una mediana finita.") from error

    if not math.isfinite(mediana):
        raise ValueError("El resultado debe ser finito.")

    return mediana
