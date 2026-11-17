
"""
Calculadora del porcentaje en masa de un componente en una mezcla.

Fórmula:
    porcentaje = (masa_soluto / masa_total) * 100

Unidades:
    Ambas masas deben utilizar la misma unidad.
"""


import math

from ..matematicas.error_validacion import ErrorValidacion


def calcular_porcentaje_masa(
    masa_soluto: int | float, masa_total: int | float
) -> float:
    """
    Calcula el porcentaje en masa de un soluto dentro de una mezcla.

    Args:
        masa_soluto: Masa del componente o soluto.
        masa_total: Masa total de la mezcla.

    Returns:
        Porcentaje en masa expresado entre 0 y 100.

    Raises:
        ErrorValidacion: Si los argumentos no son números, si las masas no
            son finitas ni positivas, si el soluto supera la masa total o
            si el resultado no es finito.
    """
    masas = (masa_soluto, masa_total)

    for masa in masas:
        if isinstance(masa, bool) or not isinstance(masa, (int, float)):
            raise ErrorValidacion("Las masas deben ser valores numéricos.")

        try:
            if not math.isfinite(masa):
                raise ErrorValidacion("Las masas deben ser valores finitos.")
        except OverflowError as error:
            raise ErrorValidacion("Las masas deben ser valores finitos.") from error

        if masa <= 0:
            raise ErrorValidacion("Las masas deben ser positivas.")

    if masa_soluto > masa_total:
        raise ErrorValidacion("La masa del soluto no puede superar la masa total.")

    try:
        porcentaje = (masa_soluto / masa_total) * 100
    except OverflowError as error:
        raise ErrorValidacion(
            "El resultado está fuera del rango permitido."
        ) from error

    if not math.isfinite(porcentaje):
        raise ErrorValidacion("El porcentaje calculado debe ser finito.")

    return porcentaje
