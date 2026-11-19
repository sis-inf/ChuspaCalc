"""
Calculadora de aceleración centrípeta.
"""

import math


def calcular_aceleracion_centripeta(velocidad, radio):
    """
    Calcula la aceleración centrípeta de un cuerpo en movimiento circular.

    Args:
        velocidad: Velocidad del cuerpo en m/s.
        radio: Radio de la trayectoria circular en metros.

    Returns:
        Aceleración centrípeta en m/s².
    """
    valores = {
        "velocidad": velocidad,
        "radio": radio,
    }

    for nombre, valor in valores.items():
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError(f"La {nombre} debe ser numérica.")

        if not math.isfinite(valor):
            raise ValueError(f"La {nombre} debe ser finita.")

    if radio <= 0:
        raise ValueError("El radio debe ser positivo.")

    aceleracion = velocidad**2 / radio

    if not math.isfinite(aceleracion):
        raise ValueError("El resultado no es finito.")

    return aceleracion
