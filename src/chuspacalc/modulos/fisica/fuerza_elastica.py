"""
Calculadora de fuerza elastica mediante la ley de Hooke.
"""

import math


def calcular_fuerza_elastica(constante_resorte, deformacion):
    """
    Calcula la fuerza elastica usando la ley de Hooke: F = -k * x.

    Args:
        constante_resorte: Constante elastica del resorte.
        deformacion: Deformacion del resorte en metros.

    Returns:
        Fuerza elastica expresada en newtons.

    Raises:
        TypeError: Si los argumentos no son numericos.
        ValueError: Si los valores no son validos o finitos.
    """
    valores = (constante_resorte, deformacion)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Los valores deben ser numericos.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Los valores deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Los valores deben ser finitos.") from error

    if constante_resorte <= 0:
        raise ValueError("La constante del resorte debe ser positiva.")

    try:
        fuerza = -constante_resorte * deformacion
    except OverflowError as error:
        raise ValueError("El resultado no es finito.") from error

    if not math.isfinite(fuerza):
        raise ValueError("El resultado debe ser finito.")

    return fuerza
