import math
from numbers import Real
from typing import Any

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def _validar_valor(nombre: str, valor: float | None) -> None:
    """Valida que un valor, si fue proporcionado, sea un número real finito."""
    if valor is None:
        return

    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(
            f"{nombre} debe ser un número real, se recibió: {valor!r}"
        )

    try:
        es_finito = math.isfinite(valor)
    except OverflowError:
        es_finito = False

    if not es_finito:
        raise ErrorValidacion(f"{nombre} debe ser finito, se recibió: {valor}")


def _resultado_finito(resultado: float) -> float:
    """Verifica que un resultado calculado sea finito."""
    try:
        es_finito = math.isfinite(resultado)
    except OverflowError:
        es_finito = False

    if not es_finito:
        raise ErrorValidacion("El resultado excede el rango numérico")

    return resultado


def calcular_ohm(
    voltaje: float | None = None,
    corriente: float | None = None,
    resistencia: float | None = None,
) -> dict[str, Any]:
    """
    Calcula la magnitud faltante de la Ley de Ohm (V = I·R).

    Se deben proporcionar dos de las tres magnitudes; la que se deja en
    ``None`` es la que se calcula.

    Args:
        voltaje: Voltaje en Volts (V), o ``None`` para calcularlo.
        corriente: Corriente en Amperes (A), o ``None`` para calcularla.
        resistencia: Resistencia en Ohms (Ω), o ``None`` para calcularla.

    Returns:
        Diccionario con ``voltaje``, ``corriente`` y ``resistencia`` y sus
        unidades (``unidad_v``, ``unidad_i`` y ``unidad_r``).

    Raises:
        ErrorValidacion: Si no se deja exactamente una magnitud sin valor,
            si algún valor no es un número real finito, si se divide entre
            una resistencia o corriente igual a cero, o si el resultado
            excede el rango numérico.
    """
    valores = [voltaje, corriente, resistencia]

    if valores.count(None) != 1:
        raise ErrorValidacion("Debe proporcionar exactamente dos parámetros")

    _validar_valor("voltaje", voltaje)
    _validar_valor("corriente", corriente)
    _validar_valor("resistencia", resistencia)

    if resistencia == 0:
        raise ErrorValidacion("La resistencia no puede ser cero")

    try:
        if voltaje is None and corriente is not None and resistencia is not None:
            voltaje = _resultado_finito(corriente * resistencia)

        elif corriente is None and voltaje is not None and resistencia is not None:
            corriente = _resultado_finito(voltaje / resistencia)

        elif resistencia is None and voltaje is not None and corriente is not None:
            if corriente == 0:
                raise ErrorValidacion("La corriente no puede ser cero")

            resistencia = _resultado_finito(voltaje / corriente)

    except OverflowError as error:
        raise ErrorValidacion("El resultado excede el rango numérico") from error

    return {
        "voltaje": voltaje,
        "unidad_v": "V",
        "corriente": corriente,
        "unidad_i": "A",
        "resistencia": resistencia,
        "unidad_r": "Ω",
    }
