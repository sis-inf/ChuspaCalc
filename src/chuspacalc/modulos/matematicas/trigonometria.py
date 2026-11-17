import math

from .error_validacion import ErrorValidacion


def _validar_numero_finito(valor: int | float) -> int | float:
    """
    Comprueba que el valor sea un número real finito.

    Raises:
        ErrorValidacion: Si el valor no es numérico o no es finito.
    """
    try:
        if not math.isfinite(valor):
            raise ErrorValidacion("El valor debe ser un número finito")
    except (TypeError, OverflowError) as error:
        raise ErrorValidacion("El valor debe ser un número finito") from error
    return valor


def seno(angulo_grados: int | float) -> float:
    """
    Calcula el seno de un ángulo en grados.

    Raises:
        ErrorValidacion: Si el ángulo no es un número finito.
    """
    _validar_numero_finito(angulo_grados)
    return math.sin(math.radians(angulo_grados))


def coseno(angulo_grados: int | float) -> float:
    """
    Calcula el coseno de un ángulo en grados.

    Raises:
        ErrorValidacion: Si el ángulo no es un número finito.
    """
    _validar_numero_finito(angulo_grados)
    return math.cos(math.radians(angulo_grados))


def tangente(angulo_grados: int | float) -> float:
    """
    Calcula la tangente de un ángulo en grados.

    Raises:
        ErrorValidacion: Si el ángulo no es un número finito o si la
            tangente no está definida para ese ángulo.
    """
    _validar_numero_finito(angulo_grados)
    angulo_normalizado = angulo_grados % 180

    if math.isclose(angulo_normalizado, 90.0, abs_tol=1e-9):
        raise ErrorValidacion("Tangente indefinida para este ángulo")

    return math.tan(math.radians(angulo_grados))


def arcoseno(valor: int | float) -> float:
    """
    Calcula el arcoseno y devuelve el resultado en grados.

    Raises:
        ErrorValidacion: Si el valor no es finito o está fuera de [-1, 1].
    """
    _validar_numero_finito(valor)
    if valor < -1 or valor > 1:
        raise ErrorValidacion("El valor debe estar en el rango [-1, 1]")

    return math.degrees(math.asin(valor))


def arcocoseno(valor: int | float) -> float:
    """
    Calcula el arcocoseno y devuelve el resultado en grados.

    Raises:
        ErrorValidacion: Si el valor no es finito o está fuera de [-1, 1].
    """
    _validar_numero_finito(valor)
    if valor < -1 or valor > 1:
        raise ErrorValidacion("El valor debe estar en el rango [-1, 1]")

    return math.degrees(math.acos(valor))


def arcotangente(valor: int | float) -> float:
    """
    Calcula el arcotangente y devuelve el resultado en grados.

    Raises:
        ErrorValidacion: Si el valor no es un número finito.
    """
    _validar_numero_finito(valor)
    return math.degrees(math.atan(valor))
