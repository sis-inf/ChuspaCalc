
"""
Calculadora de impulso mecánico.
"""


import math


def calcular_impulso(fuerza, tiempo):
    """
    Calcula el impulso producido por una fuerza constante.

    Args:
        fuerza: Fuerza aplicada en newtons.
        tiempo: Intervalo de tiempo en segundos.

    Returns:
        Impulso mecánico en N·s.
    """
    valores = {
        "fuerza": fuerza,
        "tiempo": tiempo,
    }

    for nombre, valor in valores.items():
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError(f"La {nombre} debe ser numérica.")

        if not math.isfinite(valor):
            raise ValueError(f"La {nombre} debe ser finita.")

    if tiempo < 0:
        raise ValueError("El tiempo no puede ser negativo.")

    impulso = fuerza * tiempo

    if not math.isfinite(impulso):
        raise ValueError("El resultado no es finito.")

    return impulso
