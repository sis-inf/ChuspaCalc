
"""
Calculadora de torque producido por una fuerza.
"""

import math


def calcular_torque(fuerza, distancia, angulo):
    """
    Calcula el torque mediante la formula tau = F * r * sen(theta).

    Args:
        fuerza: Magnitud de la fuerza en newtons.
        distancia: Distancia al punto de giro en metros.
        angulo: Angulo entre la fuerza y el brazo de palanca, en grados.

    Returns:
        Torque expresado en newton-metro.
    """
    valores = (fuerza, distancia, angulo)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Todos los valores deben ser numericos.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Todos los valores deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Todos los valores deben ser finitos.") from error

    if fuerza <= 0:
        raise ValueError("La fuerza debe ser positiva.")

    if distancia <= 0:
        raise ValueError("La distancia debe ser positiva.")

    try:
        angulo_radianes = math.radians(angulo)
        torque = fuerza * distancia * math.sin(angulo_radianes)
    except (OverflowError, ValueError) as error:
        raise ValueError("No se pudo calcular el torque.") from error

    if not math.isfinite(torque):
        raise ValueError("El resultado debe ser finito.")

    return torque
