
"""
Calculadora del porcentaje en masa de un componente en una mezcla.

Fórmula:
    porcentaje = (masa_soluto / masa_total) * 100

Unidades:
    Ambas masas deben utilizar la misma unidad.
"""


import math


def calcular_porcentaje_masa(masa_soluto, masa_total):
    """
    Calcula el porcentaje en masa de un soluto dentro de una mezcla.

    Args:
        masa_soluto: Masa del componente o soluto.
        masa_total: Masa total de la mezcla.

    Returns:
        Porcentaje en masa expresado entre 0 y 100.

    Raises:
        TypeError: Si los argumentos no son números.
        ValueError: Si las masas no son finitas, positivas,
            si el soluto supera la masa total o si el resultado
            no es finito.
    """
    masas = (masa_soluto, masa_total)

    for masa in masas:
        if isinstance(masa, bool) or not isinstance(masa, (int, float)):
            raise TypeError("Las masas deben ser valores numéricos.")

        try:
            if not math.isfinite(masa):
                raise ValueError("Las masas deben ser valores finitos.")
        except OverflowError as error:
            raise ValueError("Las masas deben ser valores finitos.") from error

        if masa <= 0:
            raise ValueError("Las masas deben ser positivas.")

    if masa_soluto > masa_total:
        raise ValueError("La masa del soluto no puede superar la masa total.")

    try:
        porcentaje = (masa_soluto / masa_total) * 100
    except OverflowError as error:
        raise ValueError("El resultado está fuera del rango permitido.") from error

    if not math.isfinite(porcentaje):
        raise ValueError("El porcentaje calculado debe ser finito.")

    return porcentaje
