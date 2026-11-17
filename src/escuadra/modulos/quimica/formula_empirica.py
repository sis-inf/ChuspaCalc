
"""
Calculadora de formula empirica de un compuesto.
"""

import math
from fractions import Fraction
from functools import reduce
from math import gcd, lcm


def calcular_formula_empirica(moles_elementos):
    """
    Obtiene la proporcion entera mas sencilla de los moles.

    Args:
        moles_elementos: Lista o tupla con las cantidades molares.

    Returns:
        Lista con las proporciones enteras de cada elemento.
    """
    if not isinstance(moles_elementos, (list, tuple)):
        raise TypeError("Los moles deben proporcionarse en una lista o tupla.")

    if not moles_elementos:
        raise ValueError("La coleccion de moles no puede estar vacia.")

    for cantidad in moles_elementos:
        if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)):
            raise TypeError("Las cantidades molares deben ser numericas.")

        if not math.isfinite(cantidad):
            raise ValueError("Las cantidades molares deben ser finitas.")

        if cantidad <= 0:
            raise ValueError("Las cantidades molares deben ser positivas.")

    menor_cantidad = min(moles_elementos)

    proporciones = [
        Fraction(str(cantidad / menor_cantidad)).limit_denominator(1000)
        for cantidad in moles_elementos
    ]

    denominador_comun = reduce(
        lcm, (proporcion.denominator for proporcion in proporciones)
    )

    proporciones_enteras = [
        proporcion.numerator * (denominador_comun // proporcion.denominator)
        for proporcion in proporciones
    ]

    divisor_comun = reduce(gcd, proporciones_enteras)

    resultado = [
        proporcion // divisor_comun
        for proporcion in proporciones_enteras
    ]

    return resultado
