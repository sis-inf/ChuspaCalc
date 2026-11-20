import math
from numbers import Real

from chuspacalc.modulos.matematicas.conversor_longitud import (
    UNIDADES_A_METROS as UNIDADES_BASE,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

UNIDADES_A_METROS: dict[str, float] = {
    **UNIDADES_BASE,
    "ua": 1.496e11,
    "al": 9.461e15,
    "mn": 1852.0,
    "pc": 3.086e16,
}


def convertir_longitud(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    Convierte unidades de longitud extendidas usando metros como base.

    Args:
        valor (float): Valor a convertir.
        unidad_origen (str): Unidad origen.
        unidad_destino (str): Unidad destino.

    Returns:
        float: Valor convertido a la unidad destino.

    Raises:
        ErrorValidacion: Si el valor no es numérico, no es finito o es
            negativo, si alguna unidad no es texto o no existe, o si el
            resultado no es finito.
    """
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(
            f"El valor de entrada debe ser un número real: {valor!r}",
        )

    if not isinstance(valor, int) and not math.isfinite(valor):
        raise ErrorValidacion(f"El valor de entrada debe ser finito: {valor}")

    if valor < 0:
        raise ErrorValidacion("El valor no puede ser negativo")

    if not isinstance(unidad_origen, str) or not isinstance(unidad_destino, str):
        raise ErrorValidacion("Las unidades deben ser texto")

    de_unidad = unidad_origen.strip().lower()
    a_unidad = unidad_destino.strip().lower()

    if de_unidad not in UNIDADES_A_METROS:
        raise ErrorValidacion(f"Unidad origen no reconocida: {de_unidad}")

    if a_unidad not in UNIDADES_A_METROS:
        raise ErrorValidacion(f"Unidad destino no reconocida: {a_unidad}")

    valor_en_metros = valor * UNIDADES_A_METROS[de_unidad]
    resultado = valor_en_metros / UNIDADES_A_METROS[a_unidad]

    if not math.isfinite(resultado):
        raise ErrorValidacion(
            f"El resultado de la conversión no es finito: {resultado}"
        )

    return resultado
