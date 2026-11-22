"""
Identificador de reactivo limitante en una reaccion quimica.
"""

import math


def identificar_reactivo_limitante(cantidades, coeficientes):
    """
    Identifica el reactivo que se consume primero.

    Args:
        cantidades: Lista de cantidades disponibles de cada reactivo.
        coeficientes: Lista de coeficientes estequiometricos.

    Returns:
        Indice del reactivo limitante (comenzando desde cero).
    """
    if not isinstance(cantidades, (list, tuple)):
        raise TypeError("Las cantidades deben ser una lista o tupla.")

    if not isinstance(coeficientes, (list, tuple)):
        raise TypeError("Los coeficientes deben ser una lista o tupla.")

    if not cantidades or not coeficientes:
        raise ValueError("Las listas no pueden estar vacias.")

    if len(cantidades) != len(coeficientes):
        raise ValueError("Ambas listas deben tener la misma longitud.")

    for cantidad in cantidades:
        if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)):
            raise TypeError("Las cantidades deben ser numericas.")

        if not math.isfinite(cantidad):
            raise ValueError("Las cantidades deben ser finitas.")

        if cantidad < 0:
            raise ValueError("Las cantidades no pueden ser negativas.")

    for coeficiente in coeficientes:
        if isinstance(coeficiente, bool) or not isinstance(coeficiente, (int, float)):
            raise TypeError("Los coeficientes deben ser numericos.")

        if not math.isfinite(coeficiente):
            raise ValueError("Los coeficientes deben ser finitos.")

        if coeficiente <= 0:
            raise ValueError("Los coeficientes deben ser mayores que cero.")

    proporciones = [
        cantidad / coeficiente
        for cantidad, coeficiente in zip(cantidades, coeficientes)
    ]

    return proporciones.index(min(proporciones))
