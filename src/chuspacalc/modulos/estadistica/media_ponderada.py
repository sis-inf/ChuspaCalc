"""
Calculadora de la media ponderada de un conjunto de valores.
"""

import math


def calcular_media_ponderada(valores, pesos):
    """
    Calcula el promedio ponderado de una colección de valores.

    Args:
        valores: Lista de valores numéricos.
        pesos: Lista de pesos correspondientes a cada valor.

    Returns:
        La media ponderada calculada.

    Raises:
        TypeError: Si los argumentos no son listas o contienen
            valores no numéricos.
        ValueError: Si las listas están vacías, tienen distinta
            longitud, contienen valores no finitos o si los pesos
            son negativos o suman cero.
    """
    if not isinstance(valores, (list, tuple)):
        raise TypeError("Los valores deben ser una lista o tupla.")

    if not isinstance(pesos, (list, tuple)):
        raise TypeError("Los pesos deben ser una lista o tupla.")

    if not valores or not pesos:
        raise ValueError("Las listas no pueden estar vacías.")

    if len(valores) != len(pesos):
        raise ValueError("Las listas deben tener la misma longitud.")

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Todos los valores deben ser numéricos.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Los valores deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Los valores deben ser finitos.") from error

    for peso in pesos:
        if isinstance(peso, bool) or not isinstance(peso, (int, float)):
            raise TypeError("Todos los pesos deben ser numéricos.")

        try:
            if not math.isfinite(peso):
                raise ValueError("Los pesos deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Los pesos deben ser finitos.") from error

        if peso < 0:
            raise ValueError("Los pesos no pueden ser negativos.")

    try:
        suma_pesos = math.fsum(pesos)

        if not math.isfinite(suma_pesos) or suma_pesos <= 0:
            raise ValueError("La suma de los pesos debe ser mayor que cero.")

        productos = [valor * peso for valor, peso in zip(valores, pesos)]
        suma_ponderada = math.fsum(productos)
        resultado = suma_ponderada / suma_pesos

    except OverflowError as error:
        raise ValueError("El resultado está fuera del rango permitido.") from error

    if not math.isfinite(resultado):
        raise ValueError("El resultado debe ser finito.")

    return resultado
