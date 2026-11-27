"""
Operaciones básicas con números complejos.

Utiliza el tipo ``complex`` nativo de Python para realizar operaciones
aritméticas y conversiones entre forma rectangular y polar.
"""

import cmath
import math
from fractions import Fraction

from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
    validar_rango,
)

_MSG_RANGO = "El resultado excede el rango representable."


class ErrorDivisionPorCero(ErrorValidacion, ZeroDivisionError):
    """División entre cero.

    Es a la vez ``ErrorValidacion`` y ``ZeroDivisionError``, para mantener
    compatible el código que ya capturaba ``ZeroDivisionError``.
    """


def _a_complejo(valor: object, nombre: str) -> complex:
    """Valida que valor sea int, float o complex finito y lo devuelve complex."""
    if isinstance(valor, bool) or not isinstance(valor, (int, float, complex)):
        raise ErrorValidacion(
            f"El valor de '{nombre}' debe ser un número entero, decimal o complejo."
        )

    try:
        numero = complex(valor)
    except OverflowError as exc:
        raise ErrorValidacion(
            f"El valor de '{nombre}' está fuera del rango permitido."
        ) from exc

    if not (math.isfinite(numero.real) and math.isfinite(numero.imag)):
        raise ErrorValidacion(
            f"El valor de '{nombre}' debe tener parte real e imaginaria "
            f"finitas: {valor}"
        )

    return numero


def _resultado_complejo(valor: complex) -> complex:
    """Verifica que el resultado tenga componentes finitas."""
    if not (math.isfinite(valor.real) and math.isfinite(valor.imag)):
        raise ErrorValidacion(_MSG_RANGO)
    return valor


def sumar(a: complex, b: complex) -> complex:
    """
    Retorna la suma de dos números complejos.

    Raises:
        ErrorValidacion: Si algún operando es inválido o el resultado
            excede el rango representable.
    """
    return _resultado_complejo(_a_complejo(a, "a") + _a_complejo(b, "b"))


def restar(a: complex, b: complex) -> complex:
    """
    Retorna la resta de dos números complejos.

    Raises:
        ErrorValidacion: Si algún operando es inválido o el resultado
            excede el rango representable.
    """
    return _resultado_complejo(_a_complejo(a, "a") - _a_complejo(b, "b"))


def multiplicar(a: complex, b: complex) -> complex:
    """
    Retorna el producto de dos números complejos.

    Raises:
        ErrorValidacion: Si algún operando es inválido o el resultado
            excede el rango representable.
    """
    return _resultado_complejo(_a_complejo(a, "a") * _a_complejo(b, "b"))


def dividir(a: complex, b: complex) -> complex:
    """
    Retorna la división de dos números complejos.

    Raises:
        ErrorDivisionPorCero: Si el divisor es cero (también es
            ZeroDivisionError y ErrorValidacion).
        ErrorValidacion: Si algún operando es inválido o el resultado
            excede el rango representable.
    """
    dividendo = _a_complejo(a, "a")
    divisor = _a_complejo(b, "b")

    if divisor == 0:
        raise ErrorDivisionPorCero("No es posible dividir entre cero.")

    real_a, imag_a = Fraction(dividendo.real), Fraction(dividendo.imag)
    real_b, imag_b = Fraction(divisor.real), Fraction(divisor.imag)
    denominador = real_b * real_b + imag_b * imag_b
    try:
        resultado = complex(
            float((real_a * real_b + imag_a * imag_b) / denominador),
            float((imag_a * real_b - real_a * imag_b) / denominador),
        )
    except OverflowError as error:
        raise ErrorValidacion(_MSG_RANGO) from error
    return _resultado_complejo(resultado)


def modulo(z: complex) -> float:
    """
    Retorna el módulo de un número complejo.

    Raises:
        ErrorValidacion: Si z es inválido o el módulo excede el rango.
    """
    numero = _a_complejo(z, "z")

    try:
        resultado = abs(numero)
    except OverflowError as exc:
        raise ErrorValidacion(_MSG_RANGO) from exc

    if not math.isfinite(resultado):
        raise ErrorValidacion(_MSG_RANGO)
    return resultado


def conjugado(z: complex) -> complex:
    """
    Retorna el conjugado de un número complejo.

    Raises:
        ErrorValidacion: Si z no es un número complejo finito.
    """
    return _a_complejo(z, "z").conjugate()


def rectangular_a_polar(z: complex) -> tuple[float, float]:
    """
    Convierte un número complejo desde forma rectangular
    a forma polar.

    Retorna:
        (r, theta)
        r = módulo
        theta = ángulo en radianes.

    Raises:
        ErrorValidacion: Si z es inválido o el módulo excede el rango.
    """
    numero = _a_complejo(z, "z")

    try:
        r, theta = cmath.polar(numero)
    except OverflowError as exc:
        raise ErrorValidacion(_MSG_RANGO) from exc

    if not math.isfinite(r):
        raise ErrorValidacion(_MSG_RANGO)
    return r, theta


def polar_a_rectangular(r: float, theta: float) -> complex:
    """
    Convierte un número complejo desde forma polar
    a forma rectangular.

    Parámetros:
        r: módulo (no negativo)
        theta: ángulo en radianes

    Raises:
        ErrorValidacion: Si r o theta no son reales finitos, o si r es
            negativo.
    """
    modulo_r = validar_rango(r, "módulo", minimo=0)
    angulo = validar_numero(theta, "ángulo")

    return complex(
        modulo_r * math.cos(angulo),
        modulo_r * math.sin(angulo),
    )
