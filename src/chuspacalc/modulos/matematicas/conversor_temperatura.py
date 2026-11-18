"""Módulo para la conversión de temperaturas.

Implementa conversiones entre Celsius, Fahrenheit y Kelvin.
"""

import math

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def celsius_a_fahrenheit(c):
    """Convierte grados Celsius a Fahrenheit.

    Fórmula utilizada: F = C * (9/5) + 32
    """
    if not math.isfinite(c):
        raise ValueError(f"El valor de entrada debe ser finito: {c}")
    if c < -273.15:
        raise ErrorValidacion(
            f"La temperatura {c}°C está por debajo del cero absoluto (-273.15°C)",
        )
    return c * (9 / 5) + 32


def fahrenheit_a_celsius(f):
    """Convierte grados Fahrenheit a Celsius.

    Fórmula utilizada: C = (F - 32) * (5/9)
    """
    if not math.isfinite(f):
        raise ValueError(f"El valor de entrada debe ser finito: {f}")
    if f < -459.67:
        raise ErrorValidacion(
            f"La temperatura {f}°F está por debajo del cero absoluto (-459.67°F)",
        )
    return (f - 32) * (5 / 9)


def celsius_a_kelvin(c):
    """Convierte grados Celsius a Kelvin.

    Fórmula utilizada: K = C + 273.15
    """
    if not math.isfinite(c):
        raise ValueError(f"El valor de entrada debe ser finito: {c}")
    if c < -273.15:
        raise ErrorValidacion(
            f"La temperatura {c}°C está por debajo del cero absoluto (-273.15°C)",
        )
    return c + 273.15


def kelvin_a_celsius(k):
    """Convierte Kelvin a grados Celsius.

    Fórmula utilizada: C = K - 273.15
    """
    if not math.isfinite(k):
        raise ValueError(f"El valor de entrada debe ser finito: {k}")
    if k < 0:
        raise ErrorValidacion(
            f"La temperatura {k}K no puede ser negativa (cero absoluto es 0K)",
        )
    return k - 273.15
