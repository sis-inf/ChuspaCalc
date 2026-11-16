import math


def _validar_numero_finito(valor):
    """Comprueba que el valor sea un número real finito."""
    try:
        if not math.isfinite(valor):
            raise ValueError("El valor debe ser un número finito")
    except TypeError as error:
        raise ValueError("El valor debe ser un número finito") from error
    return valor


def seno(angulo_grados):
    """Calcula el seno de un ángulo en grados."""
    _validar_numero_finito(angulo_grados)
    return math.sin(math.radians(angulo_grados))


def coseno(angulo_grados):
    """Calcula el coseno de un ángulo en grados."""
    _validar_numero_finito(angulo_grados)
    return math.cos(math.radians(angulo_grados))


def tangente(angulo_grados):
    """Calcula la tangente de un ángulo en grados."""
    _validar_numero_finito(angulo_grados)
    angulo_normalizado = angulo_grados % 180

    if math.isclose(angulo_normalizado, 90.0, abs_tol=1e-9):
        raise ValueError("Tangente indefinida para este ángulo")

    return math.tan(math.radians(angulo_grados))


def arcoseno(valor):
    """Calcula el arcoseno y devuelve el resultado en grados."""
    _validar_numero_finito(valor)
    if valor < -1 or valor > 1:
        raise ValueError("El valor debe estar en el rango [-1, 1]")

    return math.degrees(math.asin(valor))


def arcocoseno(valor):
    """Calcula el arcocoseno y devuelve el resultado en grados."""
    _validar_numero_finito(valor)
    if valor < -1 or valor > 1:
        raise ValueError("El valor debe estar en el rango [-1, 1]")

    return math.degrees(math.acos(valor))


def arcotangente(valor):
    """Calcula el arcotangente y devuelve el resultado en grados."""
    _validar_numero_finito(valor)
    return math.degrees(math.atan(valor))
