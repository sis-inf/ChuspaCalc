"""
Operaciones básicas con números complejos.

Utiliza el tipo ``complex`` nativo de Python para realizar operaciones
aritméticas y conversiones entre forma rectangular y polar.
"""

import cmath
import math
import numbers


def sumar(a: complex, b: complex) -> complex:
    """
    Retorna la suma de dos números complejos.
    """
    return a + b


def restar(a: complex, b: complex) -> complex:
    """
    Retorna la resta de dos números complejos.
    """
    return a - b


def multiplicar(a: complex, b: complex) -> complex:
    """
    Retorna el producto de dos números complejos.
    """
    return a * b


def dividir(a: complex, b: complex) -> complex:
    """
    Retorna la división de dos números complejos.

    Lanza:
        ZeroDivisionError: Si el divisor es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No es posible dividir entre cero.")

    return a / b


def modulo(z: complex) -> float:
    """
    Retorna el módulo de un número complejo.
    """
    return abs(z)


def conjugado(z: complex) -> complex:
    """
    Retorna el conjugado de un número complejo.
    """
    return z.conjugate()


def rectangular_a_polar(z: complex) -> tuple[float, float]:
    """
    Convierte un número complejo desde forma rectangular
    a forma polar.

    Retorna:
        (r, theta)
    donde:
        r = módulo
        theta = ángulo en radianes.
    """
    return cmath.polar(z)


def polar_a_rectangular(r: float, theta: float) -> complex:
    """
    Convierte un número complejo desde forma polar
    a forma rectangular.

    Parámetros:
        r: módulo
        theta: ángulo en radianes
    """
    if isinstance(r, bool) or not isinstance(r, numbers.Real):
        raise ValueError("El módulo debe ser un número real.")
    if isinstance(theta, bool) or not isinstance(theta, numbers.Real):
        raise ValueError("El ángulo debe ser un número real.")

    if not math.isfinite(r):
        raise ValueError("El módulo debe ser un número finito.")
    if not math.isfinite(theta):
        raise ValueError("El ángulo debe ser un número finito.")
        
    if r < 0:
        raise ValueError("El módulo no puede ser negativo.")

    return complex(
        r * math.cos(theta),
        r * math.sin(theta),
    )
