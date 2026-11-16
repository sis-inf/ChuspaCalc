
"""
Calculadora de trabajo mecanico realizado por una fuerza constante.
"""

import math


def calcular_trabajo_mecanico(fuerza, desplazamiento, angulo):
    """
    Calcula el trabajo mecanico usando W = F * d * cos(theta).

    Args:
        fuerza: Magnitud de la fuerza en newtons.
        desplazamiento: Magnitud del desplazamiento en metros.
        angulo: Angulo entre la fuerza y el desplazamiento, en grados.

    Returns:
        Trabajo mecanico expresado en julios.

    Raises:
        TypeError: Si los argumentos no son numericos.
        ValueError: Si los valores no son finitos o validos.
    """
    valores = (fuerza, desplazamiento, angulo)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Todos los valores deben ser numericos.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Todos los valores deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Todos los valores deben ser finitos.") from error

    if fuerza < 0 or desplazamiento < 0:
        raise ValueError("La fuerza y el desplazamiento no pueden ser negativos.")

    try:
        angulo_radianes = math.radians(angulo)
        trabajo = fuerza * desplazamiento * math.cos(angulo_radianes)
    except (OverflowError, ValueError) as error:
        raise ValueError("No se pudo calcular el trabajo mecanico.") from error

    if not math.isfinite(trabajo):
        raise ValueError("El resultado debe ser finito.")

    return trabajo
