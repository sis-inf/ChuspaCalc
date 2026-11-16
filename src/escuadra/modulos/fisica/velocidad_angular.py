
"""
Calculadora de velocidad angular.
"""

import math


def calcular_velocidad_angular(angulo, tiempo):
    """
    Calcula la velocidad angular a partir del desplazamiento angular
    y el tiempo empleado.

    Args:
        angulo: Desplazamiento angular en radianes.
        tiempo: Tiempo transcurrido en segundos.

    Returns:
        Velocidad angular en rad/s.
    """
    valores = {
        "angulo": angulo,
        "tiempo": tiempo,
    }

    for nombre, valor in valores.items():
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError(f"El {nombre} debe ser numérico.")

        if not math.isfinite(valor):
            raise ValueError(f"El {nombre} debe ser finito.")

    if tiempo <= 0:
        raise ValueError("El tiempo debe ser positivo.")

    velocidad_angular = angulo / tiempo

    if not math.isfinite(velocidad_angular):
        raise ValueError("El resultado no es finito.")

    return velocidad_angular
