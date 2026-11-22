"""Módulo para la conversión de unidades de velocidad.

Implementa conversiones entre m/s, km/h, mph, nudos y ft/s.
"""

import math
from numbers import Real

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

FACTORES_A_MS: dict[str, float] = {
    "m/s": 1.0,
    "km/h": 1 / 3.6,
    "mph": 0.44704,
    "nudos": 0.514444,
    "ft/s": 0.3048,
}


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


def _validar_unidad(unidad: object, nombre: str) -> str:
    """Verifica que la unidad sea un texto conocido y la devuelve."""
    if not isinstance(unidad, str):
        raise ErrorValidacion(
            f"El parámetro '{nombre}' debe ser un texto, "
            f"se recibió {type(unidad).__name__}",
        )
    if unidad not in FACTORES_A_MS:
        raise ErrorValidacion(
            f"Unidad desconocida: {unidad}. "
            f"Unidades válidas: {list(FACTORES_A_MS.keys())}",
        )
    return unidad


def convertir_velocidad(
    valor: float,
    unidad_origen: str,
    unidad_destino: str,
) -> float:
    """Convierte una velocidad entre unidades.

    Args:
        valor: Velocidad a convertir (número real finito, no negativo).
        unidad_origen: Unidad de entrada (m/s, km/h, mph, nudos, ft/s).
        unidad_destino: Unidad de salida (m/s, km/h, mph, nudos, ft/s).

    Returns:
        La velocidad expresada en la unidad de destino.

    Raises:
        ErrorValidacion: Si el valor no es un número finito, es negativo,
            o si alguna unidad no es válida.
    """
    numero = _validar_numero(valor, "valor")
    if numero < 0:
        raise ErrorValidacion("La velocidad no puede ser negativa")
    origen = _validar_unidad(unidad_origen, "unidad_origen")
    destino = _validar_unidad(unidad_destino, "unidad_destino")

    valor_ms = numero * FACTORES_A_MS[origen]
    return valor_ms / FACTORES_A_MS[destino]
