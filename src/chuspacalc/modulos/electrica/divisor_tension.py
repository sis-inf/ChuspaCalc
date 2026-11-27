"""Herramientas para cálculo de divisor de tensión resistivo."""

import math
from fractions import Fraction

from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
)


def _validar_positivo(valor: float, nombre: str) -> float:
    numero = validar_numero(valor, nombre)
    if numero <= 0:
        raise ErrorValidacion(f"{nombre} debe ser positivo")
    return numero


def _resultado_finito(valor: float | Fraction) -> float:
    try:
        resultado = float(valor)
    except OverflowError as error:
        raise ErrorValidacion("El resultado excede el rango numérico") from error
    if not math.isfinite(resultado) or resultado <= 0:
        raise ErrorValidacion("El resultado debe ser positivo y finito")
    return resultado


def calcular_tension_salida(
    v_entrada: float, r1: float, r2: float
) -> dict[str, float | str]:
    """Calcula Vout = Vin * R2 / (R1 + R2).

    Raises:
        ErrorValidacion: Si una entrada no es real, positiva y finita o
            el resultado está fuera del rango representable.
    """
    v_entrada = _validar_positivo(v_entrada, "v_entrada")
    r1 = _validar_positivo(r1, "r1")
    r2 = _validar_positivo(r2, "r2")
    v_salida = v_entrada * r2 / (r1 + r2)
    if not math.isfinite(v_salida) or v_salida <= 0:
        v_salida = _resultado_finito(
            Fraction(v_entrada) * Fraction(r2) / (Fraction(r1) + Fraction(r2))
        )
    return {
        "v_entrada": v_entrada,
        "r1": r1,
        "r2": r2,
        "v_salida": v_salida,
        "unidad": "V",
    }


def calcular_r2_para_tension(
    v_entrada: float, v_salida: float, r1: float
) -> dict[str, float | str]:
    """Calcula R2 = Vout * R1 / (Vin - Vout).

    Raises:
        ErrorValidacion: Si los valores no son reales positivos y finitos,
            Vout no es menor que Vin o R2 no es representable.
    """
    v_entrada = _validar_positivo(v_entrada, "v_entrada")
    v_salida = _validar_positivo(v_salida, "v_salida")
    r1 = _validar_positivo(r1, "r1")
    if v_salida >= v_entrada:
        raise ErrorValidacion("v_salida debe ser positiva y menor que v_entrada")
    r2 = v_salida * r1 / (v_entrada - v_salida)
    if not math.isfinite(r2) or r2 <= 0:
        r2 = _resultado_finito(
            Fraction(v_salida)
            * Fraction(r1)
            / (Fraction(v_entrada) - Fraction(v_salida))
        )
    return {
        "v_entrada": v_entrada,
        "v_salida": v_salida,
        "r1": r1,
        "r2": r2,
        "unidad": "ohm",
    }
