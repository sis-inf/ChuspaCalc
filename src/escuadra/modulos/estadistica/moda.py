
"""
Calculadora de la moda estadística de un conjunto de datos.
"""

import math
from collections import Counter


def calcular_moda(datos):
    """
    Identifica el valor o los valores con mayor frecuencia.

    Args:
        datos: Lista o tupla de valores numéricos.

    Returns:
        Lista ordenada con los valores que tienen mayor frecuencia.

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

    frecuencias = Counter(datos)
    frecuencia_maxima = max(frecuencias.values())

    moda = [
        valor
        for valor, frecuencia in frecuencias.items()
        if frecuencia == frecuencia_maxima
    ]

    return sorted(moda)
