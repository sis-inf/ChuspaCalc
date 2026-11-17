"""
Calculadora del número de partículas a partir de la cantidad de moles.

Relación:
    N = n * NA

Constante de Avogadro:
    NA = 6.02214076e23 partículas/mol
"""

import math

CONSTANTE_AVOGADRO = 6.02214076e23


def calcular_numero_particulas(moles):
    """
    Calcula el número de partículas presentes en una muestra.

    Args:
        moles: Cantidad de sustancia expresada en moles.

    Returns:
        Número de partículas calculado.

    Raises:
        TypeError: Si la cantidad de moles no es numérica.
        ValueError: Si los moles son negativos o no finitos.
    """
    if isinstance(moles, bool) or not isinstance(moles, (int, float)):
        raise TypeError("La cantidad de moles debe ser numérica.")

    try:
        if not math.isfinite(moles):
            raise ValueError("La cantidad de moles debe ser finita.")
    except OverflowError as error:
        raise ValueError("La cantidad de moles debe ser finita.") from error

    if moles < 0:
        raise ValueError("La cantidad de moles no puede ser negativa.")

    try:
        numero_particulas = float(moles) * CONSTANTE_AVOGADRO
    except OverflowError as error:
        raise ValueError("El resultado está fuera del rango permitido.") from error

    if not math.isfinite(numero_particulas):
        raise ValueError("El resultado debe ser finito.")

    return numero_particulas
