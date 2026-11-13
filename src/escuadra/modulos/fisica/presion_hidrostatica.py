
"""
Calculadora de presión hidrostática.

Fórmula:
    P = densidad * gravedad * profundidad

Unidades:
    Densidad: kg/m³
    Gravedad: m/s²
    Profundidad: m
    Presión: Pa
"""

import math


def calcular_presion_hidrostatica(densidad, gravedad, profundidad):
    """
    Calcula la presión hidrostática ejercida por un líquido.

    Args:
        densidad: Densidad del líquido en kg/m³.
        gravedad: Aceleración de la gravedad en m/s².
        profundidad: Profundidad en metros.

    Returns:
        Presión hidrostática en pascales (Pa).

    Raises:
        TypeError: Si algún argumento no es numérico.
        ValueError: Si algún valor es negativo, no finito
            o si el resultado no es finito.
    """
    valores = (densidad, gravedad, profundidad)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Todos los argumentos deben ser números.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Todos los valores deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Todos los valores deben ser finitos.") from error

        if valor < 0:
            raise ValueError("Los valores no pueden ser negativos.")

    try:
        presion = densidad * gravedad * profundidad
    except OverflowError as error:
        raise ValueError("El resultado está fuera del rango permitido.") from error

    if not math.isfinite(presion):
        raise ValueError("La presión calculada debe ser finita.")

    return presion
