"""Cálculo de reacciones en vigas simplemente apoyadas con carga uniforme."""

import math
from numbers import Real

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def _validar_numero(valor: object, descripcion: str) -> float:
    """Verifica que el valor sea un número real finito y lo devuelve como float.

    Args:
        valor: Dato a validar.
        descripcion: Nombre descriptivo del parámetro para el mensaje de error.

    Returns:
        El valor convertido a ``float``.

    Raises:
        ErrorValidacion: Si el tipo no es numérico (incluye ``bool``), si es
            demasiado grande para convertirse a ``float`` o si no es finito.
    """
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(f"{descripcion} debe ser numérica.")
    try:
        numero = float(valor)
    except OverflowError:
        raise ErrorValidacion(f"{descripcion} es demasiado grande.") from None
    if not math.isfinite(numero):
        raise ErrorValidacion(f"{descripcion} debe ser finita.")
    return numero


def calcular_reacciones_carga_distribuida(
    carga_distribuida: float, longitud: float
) -> tuple[float, float]:
    """
    Calcula las reacciones en los apoyos de una viga simplemente
    apoyada sometida a una carga uniformemente distribuida.

    Args:
        carga_distribuida: Carga distribuida en N/m.
        longitud: Longitud de la viga en metros.

    Returns:
        tuple: (reaccion_izquierda, reaccion_derecha), en N.

    Raises:
        ErrorValidacion: Si los parámetros no son numéricos,
            positivos o finitos, o si el resultado se desborda.
    """
    carga = _validar_numero(carga_distribuida, "La carga distribuida")
    largo = _validar_numero(longitud, "La longitud")

    if carga <= 0:
        raise ErrorValidacion("La carga distribuida debe ser mayor que cero.")

    if largo <= 0:
        raise ErrorValidacion("La longitud debe ser mayor que cero.")

    carga_total = carga * largo
    if not math.isfinite(carga_total):
        raise ErrorValidacion(
            "El resultado se desborda: carga o longitud demasiado grandes."
        )

    reaccion_izquierda = carga_total / 2
    reaccion_derecha = carga_total / 2

    return reaccion_izquierda, reaccion_derecha
