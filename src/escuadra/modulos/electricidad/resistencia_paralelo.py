
"""
Calculadora de resistencia equivalente en paralelo.

La resistencia equivalente se calcula mediante:
    1 / Req = 1/R1 + 1/R2 + ... + 1/Rn
"""

import math


def calcular_resistencia_paralelo(resistencias):
    """
    Calcula la resistencia equivalente de varias resistencias
    conectadas en paralelo.

    Args:
        resistencias: Lista de valores de resistencia en ohmios.

    Returns:
        La resistencia equivalente en ohmios.

    Raises:
        TypeError: Si la entrada no es una lista o contiene
            valores que no son números.
        ValueError: Si la lista está vacía, contiene valores
            no positivos o no finitos, o el resultado no es finito.
    """
    if not isinstance(resistencias, list):
        raise TypeError("Las resistencias deben proporcionarse en una lista.")

    if not resistencias:
        raise ValueError("La lista de resistencias no puede estar vacía.")

    for resistencia in resistencias:
        if isinstance(resistencia, bool) or not isinstance(resistencia, (int, float)):
            raise TypeError("Todas las resistencias deben ser números.")

        try:
            if not math.isfinite(resistencia):
                raise ValueError("Las resistencias deben ser valores finitos.")
        except OverflowError as error:
            raise ValueError("Las resistencias deben ser valores finitos.") from error

        if resistencia <= 0:
            raise ValueError("Las resistencias deben ser mayores que cero.")

    try:
        conductancia_total = sum(1 / resistencia for resistencia in resistencias)
        equivalente = 1 / conductancia_total
    except (OverflowError, ZeroDivisionError) as error:
        raise ValueError("No se pudo calcular la resistencia equivalente.") from error

    if not math.isfinite(equivalente):
        raise ValueError("El resultado debe ser un número finito.")

    return equivalente
