"""
Excepción personalizada y validadores numéricos del módulo de matemáticas.
"""

import math


class ErrorValidacion(ValueError):
    """Excepción para errores de validación de rangos físicos.

    Se usa cuando un valor de entrada no está dentro del rango
    físicamente permitido (ej. temperatura bajo cero absoluto,
    masa o longitud negativas).
    """


def validar_numero(valor: object, nombre: str) -> float:
    """Valida que un valor sea un número real finito.

    Args:
        valor: Valor a validar. Se rechazan los booleanos y los tipos
            no numéricos.
        nombre: Nombre del parámetro, usado en el mensaje de error.

    Returns:
        El valor convertido a float.

    Raises:
        ErrorValidacion: Si el valor no es int ni float, si es NaN o
            infinito, o si está fuera del rango representable.
    """
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise ErrorValidacion(
            f"El valor de '{nombre}' debe ser un número entero o decimal."
        )

    try:
        numero = float(valor)
    except OverflowError as exc:
        raise ErrorValidacion(
            f"El valor de '{nombre}' está fuera del rango permitido."
        ) from exc

    if not math.isfinite(numero):
        raise ErrorValidacion(f"El valor de '{nombre}' debe ser finito: {valor}")

    return numero


def validar_no_cero(valor: object, nombre: str) -> float:
    """Valida que un valor sea un número finito distinto de cero.

    Pensada para divisores y otros parámetros donde el cero provocaría
    una división por cero.

    Args:
        valor: Valor a validar.
        nombre: Nombre del parámetro, usado en el mensaje de error.

    Returns:
        El valor convertido a float.

    Raises:
        ErrorValidacion: Si el valor no es un número finito válido o
            es igual a cero.
    """
    numero = validar_numero(valor, nombre)

    if numero == 0:
        raise ErrorValidacion(
            f"El valor de '{nombre}' no puede ser cero (división por cero)."
        )

    return numero


def validar_rango(
    valor: object,
    nombre: str,
    minimo: float | None = None,
    maximo: float | None = None,
) -> float:
    """Valida que un valor sea finito y esté dentro de un rango inclusivo.

    Args:
        valor: Valor a validar.
        nombre: Nombre del parámetro, usado en el mensaje de error.
        minimo: Límite inferior inclusivo, o None si no hay límite.
        maximo: Límite superior inclusivo, o None si no hay límite.

    Returns:
        El valor convertido a float.

    Raises:
        ErrorValidacion: Si el valor no es un número finito válido, si
            está fuera del rango, o si minimo es mayor que maximo.
    """
    if minimo is not None and maximo is not None and minimo > maximo:
        raise ErrorValidacion(
            f"Rango inválido para '{nombre}': el mínimo ({minimo}) "
            f"es mayor que el máximo ({maximo})."
        )

    numero = validar_numero(valor, nombre)

    if minimo is not None and numero < minimo:
        raise ErrorValidacion(
            f"El valor de '{nombre}' no puede ser menor que {minimo} "
            f"(valor recibido: {numero})."
        )

    if maximo is not None and numero > maximo:
        raise ErrorValidacion(
            f"El valor de '{nombre}' no puede ser mayor que {maximo} "
            f"(valor recibido: {numero})."
        )

    return numero
