"""Módulo para la conversión de temperaturas.

Implementa conversiones entre Celsius, Fahrenheit y Kelvin.
"""

from escuadra.modulos.matematicas.error_validacion import ErrorValidacion


def celsius_a_fahrenheit(c):
    """Convierte grados Celsius a Fahrenheit.

    Fórmula utilizada: F = C * (9/5) + 32
    """
    if c < -273.15:
        raise ErrorValidacion(
            f"La temperatura {c}°C está por debajo del cero absoluto (-273.15°C)"
        )
    return c * (9 / 5) + 32


def fahrenheit_a_celsius(f):
    """Convierte grados Fahrenheit a Celsius.

    Fórmula utilizada: C = (F - 32) * (5/9)
    """
    if f < -459.67:
        raise ErrorValidacion(
            f"La temperatura {f}°F está por debajo del cero absoluto (-459.67°F)"
        )
    return (f - 32) * (5 / 9)


def celsius_a_kelvin(c):
    """Convierte grados Celsius a Kelvin.

    Fórmula utilizada: K = C + 273.15
    """
    if c < -273.15:
        raise ErrorValidacion(
            f"La temperatura {c}°C está por debajo del cero absoluto (-273.15°C)"
        )
    return c + 273.15


def kelvin_a_celsius(k):
    """Convierte Kelvin a grados Celsius.

    Fórmula utilizada: C = K - 273.15
    """
    if k < 0:
        raise ErrorValidacion(
            f"La temperatura {k}K no puede ser negativa (cero absoluto es 0K)"
        )
    return k - 273.15


def fahrenheit_a_kelvin(f):
    """Convierte grados Fahrenheit a Kelvin.

    Fórmula utilizada: K = (F - 32) * (5/9) + 273.15

    >>> fahrenheit_a_kelvin(32)
    273.15
    >>> abs(fahrenheit_a_kelvin(-459.67)) < 1e-10
    True
    >>> fahrenheit_a_kelvin(-500)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    escuadra.modulos.matematicas.error_validacion.ErrorValidacion: ...
    """
    if f < -459.67:
        raise ErrorValidacion(
            f"La temperatura {f}°F está por debajo del cero absoluto (-459.67°F)"
        )
    return (f - 32) * (5 / 9) + 273.15


def kelvin_a_fahrenheit(k):
    """Convierte Kelvin a grados Fahrenheit.

    Fórmula utilizada: F = (K - 273.15) * (9/5) + 32

    >>> round(kelvin_a_fahrenheit(273.15), 10)
    32.0
    >>> round(kelvin_a_fahrenheit(0), 10)
    -459.67
    >>> kelvin_a_fahrenheit(-1)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    escuadra.modulos.matematicas.error_validacion.ErrorValidacion: ...
    """
    if k < 0:
        raise ErrorValidacion(
            f"La temperatura {k}K no puede ser negativa (cero absoluto es 0K)"
        )
    return (k - 273.15) * (9 / 5) + 32
