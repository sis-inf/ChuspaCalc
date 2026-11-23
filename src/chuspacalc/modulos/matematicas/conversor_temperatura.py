"""Módulo para la conversión de temperaturas.

Implementa conversiones entre Celsius, Fahrenheit y Kelvin.
"""

import math
from numbers import Real

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def _validar_numero(valor: object, nombre: str) -> float:
    """Verifica que el valor sea un número real finito y lo devuelve como float.

    Lanza ErrorValidacion si el tipo no es numérico (incluye bool),
    o si el valor es NaN o infinito.
    """
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(
            f"El parámetro '{nombre}' debe ser un número real, "
            f"se recibió {type(valor).__name__}",
        )
    try:
        numero = float(valor)
    except OverflowError:
        raise ErrorValidacion(
            f"El parámetro '{nombre}' es demasiado grande para ser procesado",
        ) from None
    if not math.isfinite(numero):
        raise ErrorValidacion(
            f"El parámetro '{nombre}' debe ser finito (no NaN ni infinito): {numero}",
        )
    return numero


def celsius_a_fahrenheit(c: float) -> float:
    """Convierte grados Celsius a Fahrenheit.

    Fórmula utilizada: F = C * (9/5) + 32
    """
    c = _validar_numero(c, "c")
    if c < -273.15:
        raise ErrorValidacion(
            f"La temperatura {c}°C está por debajo del cero absoluto (-273.15°C)",
        )
    return c * (9 / 5) + 32


def fahrenheit_a_celsius(f: float) -> float:
    """Convierte grados Fahrenheit a Celsius.

    Fórmula utilizada: C = (F - 32) * (5/9)
    """
    f = _validar_numero(f, "f")
    if f < -459.67:
        raise ErrorValidacion(
            f"La temperatura {f}°F está por debajo del cero absoluto (-459.67°F)",
        )
    return (f - 32) * (5 / 9)


def celsius_a_kelvin(c: float) -> float:
    """Convierte grados Celsius a Kelvin.

    Fórmula utilizada: K = C + 273.15
    """
    c = _validar_numero(c, "c")
    if c < -273.15:
        raise ErrorValidacion(
            f"La temperatura {c}°C está por debajo del cero absoluto (-273.15°C)",
        )
    return c + 273.15


def kelvin_a_celsius(k: float) -> float:
    """Convierte Kelvin a grados Celsius.

    Fórmula utilizada: C = K - 273.15
    """
    k = _validar_numero(k, "k")
    if k < 0:
        raise ErrorValidacion(
            f"La temperatura {k}K no puede ser negativa (cero absoluto es 0K)",
        )
    return k - 273.15
