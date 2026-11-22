"""
Calculadora de resistencia equivalente en paralelo.

La resistencia equivalente se calcula mediante:
    1 / Req = 1/R1 + 1/R2 + ... + 1/Rn
"""

import math

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def calcular_resistencia_paralelo(resistencias: list[float]) -> float:
    """
    Calcula la resistencia equivalente de varias resistencias
    conectadas en paralelo.

    Args:
        resistencias: Lista de valores de resistencia en ohmios.

    Returns:
        La resistencia equivalente en ohmios.

    Raises:
        ErrorValidacion: Si la entrada no es una lista, contiene valores
            que no son números, la lista está vacía, hay valores no
            positivos o no finitos, o el resultado no es finito.
    """
    if not isinstance(resistencias, list):
        raise ErrorValidacion("Las resistencias deben proporcionarse en una lista.")

    if not resistencias:
        raise ErrorValidacion("La lista de resistencias no puede estar vacía.")

    for resistencia in resistencias:
        if isinstance(resistencia, bool) or not isinstance(resistencia, (int, float)):
            raise ErrorValidacion("Todas las resistencias deben ser números.")

        try:
            es_finita = math.isfinite(resistencia)
        except OverflowError:
            es_finita = False

        if not es_finita:
            raise ErrorValidacion("Las resistencias deben ser valores finitos.")

        if resistencia <= 0:
            raise ErrorValidacion("Las resistencias deben ser mayores que cero.")

    try:
        conductancia_total = sum(1 / resistencia for resistencia in resistencias)
    except (OverflowError, ZeroDivisionError) as error:
        raise ErrorValidacion(
            "No se pudo calcular la resistencia equivalente."
        ) from error

    if not math.isfinite(conductancia_total) or conductancia_total <= 0:
        raise ErrorValidacion("No se pudo calcular la resistencia equivalente.")

    equivalente = 1 / conductancia_total

    if not math.isfinite(equivalente):
        raise ErrorValidacion("El resultado debe ser un número finito.")

    return equivalente
