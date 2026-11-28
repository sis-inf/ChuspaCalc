import math
from collections.abc import Callable
from numbers import Real

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def _validar_finitos(**parametros: float) -> None:
    """Rechaza valores no numéricos, NaN e infinitos indicando el parámetro inválido."""
    for nombre, valor in parametros.items():
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


def _resultado_finito(calculo: Callable[[], float]) -> float:
    """Ejecuta el cálculo y verifica que el resultado sea un float finito."""
    try:
        resultado = float(calculo())
    except (OverflowError, ZeroDivisionError) as error:
        raise ErrorValidacion("El resultado excede el rango numérico") from error

    if not math.isfinite(resultado):
        raise ErrorValidacion("El resultado excede el rango numérico")

    return resultado


def potencia_vi(voltaje: float, corriente: float) -> float:
    """
    Calcula la potencia eléctrica usando la fórmula P = V·I.

    Fórmula:
        P = V·I

    Unidades:
        - V: voltaje en Volts (V)
        - I: corriente en Amperes (A)
        - P: potencia en Watts (W)

    Raises:
        ErrorValidacion: Si algún argumento no es un número real finito,
            si no es mayor que cero o si el resultado excede el rango numérico.
    """
    _validar_finitos(voltaje=voltaje, corriente=corriente)

    if voltaje <= 0:
        raise ErrorValidacion("voltaje debe ser mayor que 0")

    if corriente <= 0:
        raise ErrorValidacion("corriente debe ser mayor que 0")

    return _resultado_finito(lambda: voltaje * corriente)


def potencia_ir(corriente: float, resistencia: float) -> float:
    """
    Calcula la potencia eléctrica usando la fórmula P = I²·R.

    Fórmula:
        P = I²·R

    Unidades:
        - I: corriente en Amperes (A)
        - R: resistencia en Ohms (Ω)
        - P: potencia en Watts (W)

    Raises:
        ErrorValidacion: Si algún argumento no es un número real finito,
            si no es mayor que cero o si el resultado excede el rango numérico.
    """
    _validar_finitos(corriente=corriente, resistencia=resistencia)

    if corriente <= 0:
        raise ErrorValidacion("corriente debe ser mayor que 0")

    if resistencia <= 0:
        raise ErrorValidacion("resistencia debe ser mayor que 0")

    return _resultado_finito(lambda: (corriente**2) * resistencia)


def potencia_vr(voltaje: float, resistencia: float) -> float:
    """
    Calcula la potencia eléctrica usando la fórmula P = V²/R.

    Fórmula:
        P = V²/R

    Unidades:
        - V: voltaje en Volts (V)
        - R: resistencia en Ohms (Ω)
        - P: potencia en Watts (W)

    Raises:
        ErrorValidacion: Si algún argumento no es un número real finito,
            si no es mayor que cero o si el resultado excede el rango numérico.
    """
    _validar_finitos(voltaje=voltaje, resistencia=resistencia)

    if voltaje <= 0:
        raise ErrorValidacion("voltaje debe ser mayor que 0")

    if resistencia <= 0:
        raise ErrorValidacion("resistencia debe ser mayor que 0")

    return _resultado_finito(lambda: (voltaje**2) / resistencia)
