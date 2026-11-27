"""
Módulo para cálculo de corrección del factor de potencia
mediante banco de capacitores.
"""

import math
from fractions import Fraction

from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
)


def calcular_capacitancia_correccion(
    potencia_activa: float,
    fp_actual: float,
    fp_deseado: float,
    voltaje: float,
    frecuencia: float = 60,
) -> float:
    """
    Calcula la capacitancia necesaria para corregir el factor
    de potencia de un sistema.

    Parámetros
    ----------
    potencia_activa : float
        Potencia activa en Watts.

    fp_actual : float
        Factor de potencia actual.

    fp_deseado : float
        Factor de potencia deseado.

    voltaje : float
        Voltaje RMS del sistema.

    frecuencia : float
        Frecuencia en Hz.

    Retorna
    -------
    float
        Capacitancia en Faradios.
    """

    parametros = {
        "potencia_activa": potencia_activa,
        "fp_actual": fp_actual,
        "fp_deseado": fp_deseado,
        "voltaje": voltaje,
        "frecuencia": frecuencia,
    }
    valores = {
        nombre: validar_numero(valor, nombre) for nombre, valor in parametros.items()
    }
    potencia_activa = valores["potencia_activa"]
    fp_actual = valores["fp_actual"]
    fp_deseado = valores["fp_deseado"]
    voltaje = valores["voltaje"]
    frecuencia = valores["frecuencia"]

    if not (0 < fp_actual <= 1):
        raise ErrorValidacion("fp_actual debe estar entre 0 y 1")

    if not (0 < fp_deseado <= 1):
        raise ErrorValidacion("fp_deseado debe estar entre 0 y 1")

    if fp_deseado <= fp_actual:
        raise ErrorValidacion("El factor de potencia deseado debe ser mayor al actual")

    if potencia_activa <= 0:
        raise ErrorValidacion("La potencia debe ser positiva")

    if voltaje <= 0:
        raise ErrorValidacion("El voltaje debe ser positivo")

    if frecuencia <= 0:
        raise ErrorValidacion("La frecuencia debe ser positiva")

    actual = Fraction(fp_actual)
    deseado = Fraction(fp_deseado)
    seno_actual = Fraction(math.sqrt((1 - fp_actual) * (1 + fp_actual)))
    seno_deseado = Fraction(math.sqrt((1 - fp_deseado) * (1 + fp_deseado)))
    diferencia = ((deseado - actual) * (deseado + actual)) / (
        actual * deseado * (deseado * seno_actual + actual * seno_deseado)
    )

    try:
        capacitancia = float(
            Fraction(potencia_activa)
            * diferencia
            / (Fraction(2 * math.pi) * Fraction(frecuencia) * Fraction(voltaje) ** 2)
        )
    except OverflowError as error:
        raise ErrorValidacion("La capacitancia excede el rango numérico") from error
    if not math.isfinite(capacitancia) or capacitancia <= 0:
        raise ErrorValidacion("La capacitancia debe ser positiva y finita")
    return capacitancia
