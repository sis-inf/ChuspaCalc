"""Cálculo de resistencia equivalente en serie y paralelo."""

import math
from collections.abc import Sequence

from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
)


def _normalizar_componentes(
    componentes: tuple[object, ...],
    nombre: str,
) -> tuple[float, ...]:
    """Normaliza y valida los componentes eléctricos recibidos."""

    if len(componentes) == 1 and isinstance(componentes[0], (list, tuple)):
        componentes = tuple(componentes[0])

    if len(componentes) < 2:
        raise ErrorValidacion(f"Se requieren al menos 2 {nombre.lower()}.")

    valores: list[float] = []

    for posicion, componente in enumerate(componentes, start=1):
        valor = validar_numero(componente, f"{nombre} {posicion}")

        if valor <= 0:
            raise ErrorValidacion(
                f"{nombre} {posicion} debe ser mayor que 0; " f"se recibió: {valor}."
            )

        valores.append(valor)

    return tuple(valores)


def _validar_resultado(resultado: float, nombre: str) -> float:
    """Comprueba que el resultado calculado sea finito y positivo."""

    if not math.isfinite(resultado) or resultado <= 0:
        raise ErrorValidacion(
            f"El resultado de {nombre} debe ser finito y positivo; "
            f"se obtuvo: {resultado}."
        )

    return resultado


def resistencia_serie(
    *resistencias: float | Sequence[float],
) -> float:
    """
    Args:
        resistencias: Resistencias individuales o una lista/tupla.

    Returns:
        Resistencia equivalente en ohmios.

    Raises:
        ErrorValidacion: Si los valores son inválidos o el resultado
            no puede representarse como un número finito positivo.

    """
    valores = _normalizar_componentes(resistencias, "La resistencia")

    try:
        resultado = math.fsum(valores)
    except OverflowError as exc:
        raise ErrorValidacion(
            "La resistencia equivalente en serie excede el rango numérico"
        ) from exc
    return _validar_resultado(resultado, "La resistencia equivalente en serie")


def resistencia_paralelo(
    *resistencias: float | Sequence[float],
) -> float:
    """
    Calcula la resistencia equivalente en paralelo.

    Args:
        resistencias: Resistencias individuales o una lista/tupla.

    Returns:
        Resistencia equivalente en ohmios.

    Raises:
        ErrorValidacion: Si los valores son inválidos o el resultado
            no puede representarse como un número finito positivo.
    """
    valores = _normalizar_componentes(resistencias, "La resistencia")

    menor = min(valores)

    try:
        suma_relativa = math.fsum(menor / valor for valor in valores)
        resultado = menor / suma_relativa
    except (OverflowError, ZeroDivisionError) as exc:
        raise ErrorValidacion(
            "No fue posible calcular la resistencia equivalente en paralelo."
        ) from exc

    return _validar_resultado(resultado, "La resistencia equivalente en paralelo")


def capacitancia_paralelo(*capacitancias):
    """
    Calcula la capacitancia equivalente en paralelo.

    Args:
        capacitancias: Capacitancias individuales en faradios.

    Returns:
        Capacitancia equivalente en faradios.

    Raises:
        ErrorValidacion: Si los valores son inválidos o el resultado
            no puede representarse como un número finito positivo.
    """
    valores = _normalizar_componentes(capacitancias, "La capacitancia")

    try:
        resultado = math.fsum(valores)
    except OverflowError as exc:
        raise ErrorValidacion(
            "La capacitancia equivalente en paralelo excede el rango numérico."
        ) from exc

    return _validar_resultado(resultado, "La capacitancia equivalente en paralelo")


def capacitancia_serie(*capacitancias):
    """
    Calcula la capacitancia equivalente en serie.


    Args:
        capacitancias: Capacitancias individuales en faradios.

    Returns:
        Capacitancia equivalente en faradios.

    Raises:
        ErrorValidacion: Si los valores son inválidos o el resultado
            no puede representarse como un número finito positivo.
    """
    valores = _normalizar_componentes(capacitancias, "La capacitancia")

    menor = min(valores)

    try:
        suma_relativa = math.fsum(menor / valor for valor in valores)
        resultado = menor / suma_relativa
    except (OverflowError, ZeroDivisionError) as exc:
        raise ErrorValidacion(
            "No fue posible calcular la capacitancia equivalente en serie."
        ) from exc

    return _validar_resultado(resultado, "La capacitancia equivalente en serie")
