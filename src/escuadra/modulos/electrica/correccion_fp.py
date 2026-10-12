"""
Módulo para cálculo de corrección del factor de potencia
mediante banco de capacitores.
"""

import math


def calcular_capacitancia_correccion(
    potencia_activa,
    fp_actual,
    fp_deseado,
    voltaje,
    frecuencia=60,
):
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

    if not (0 < fp_actual <= 1):
        raise ValueError("fp_actual debe estar entre 0 y 1")

    if not (0 < fp_deseado <= 1):
        raise ValueError("fp_deseado debe estar entre 0 y 1")

    if fp_deseado <= fp_actual:
        raise ValueError("El factor de potencia deseado debe ser mayor al actual")

    if potencia_activa <= 0:
        raise ValueError("La potencia debe ser positiva")

    if voltaje <= 0:
        raise ValueError("El voltaje debe ser positivo")

    if frecuencia <= 0:
        raise ValueError("La frecuencia debe ser positiva")

    theta_actual = math.acos(fp_actual)
    theta_deseado = math.acos(fp_deseado)

    potencia_reactiva = potencia_activa * (
        math.tan(theta_actual) - math.tan(theta_deseado)
    )

    omega = 2 * math.pi * frecuencia

    capacitancia = potencia_reactiva / (omega * voltaje**2)

    return capacitancia
