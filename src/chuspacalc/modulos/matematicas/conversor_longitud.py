import math
from numbers import Real
from typing import TypedDict

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

UNIDADES_A_METROS: dict[str, float] = {
    "m": 1,
    "cm": 0.01,
    "mm": 0.001,
    "km": 1000,
    "in": 0.0254,
    "ft": 0.3048,
}


class ResultadoConversion(TypedDict):
    """Resultado de una conversión de longitud."""

    valor_original: float
    unidad_original: str
    valor_convertido: float
    unidad_destino: str


def convertir(valor: float, de_unidad: str, a_unidad: str) -> ResultadoConversion:
    """
    Convierte unidades de longitud usando metros como base.

    Args:
        valor (float): Valor a convertir.
        de_unidad (str): Unidad origen.
        a_unidad (str): Unidad destino.

    Returns:
        ResultadoConversion: Resultado de la conversión.

    Raises:
        ErrorValidacion: Si el valor no es numérico, no es finito o es
            negativo, o si alguna unidad no es texto o no existe.
    """

    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(
            f"El valor de entrada debe ser un número real: {valor!r}",
        )

    if not isinstance(valor, int) and not math.isfinite(valor):
        raise ErrorValidacion(f"El valor de entrada debe ser finito: {valor}")

    if valor < 0:
        raise ErrorValidacion(
            f"La longitud no puede ser negativa (valor recibido: {valor})",
        )

    if not isinstance(de_unidad, str) or not isinstance(a_unidad, str):
        raise ErrorValidacion("Las unidades deben ser texto")

    de_unidad = de_unidad.strip().lower()
    a_unidad = a_unidad.strip().lower()

    if de_unidad not in UNIDADES_A_METROS:
        raise ErrorValidacion(f"Unidad origen no reconocida: {de_unidad}")

    if a_unidad not in UNIDADES_A_METROS:
        raise ErrorValidacion(f"Unidad destino no reconocida: {a_unidad}")

    # Convertir a metros
    valor_en_metros = valor * UNIDADES_A_METROS[de_unidad]

    # Convertir desde metros a unidad destino
    valor_convertido = valor_en_metros / UNIDADES_A_METROS[a_unidad]

    return {
        "valor_original": valor,
        "unidad_original": de_unidad,
        "valor_convertido": valor_convertido,
        "unidad_destino": a_unidad,
    }
