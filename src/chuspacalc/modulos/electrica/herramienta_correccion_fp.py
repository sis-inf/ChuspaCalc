"""
Herramienta para cálculo de corrección
del factor de potencia.
"""

from ..matematicas.error_validacion import ErrorValidacion, validar_numero
from .correccion_fp import calcular_capacitancia_correccion


def herramienta_correccion_fp(
    potencia_activa: float,
    fp_actual: float,
    fp_deseado: float,
    voltaje: float,
    frecuencia: float = 60,
) -> float:
    """
    Wrapper para calcular la capacitancia de corrección.

    Valida los parámetros de entrada antes de delegar el cálculo.

    Args:
        potencia_activa: Potencia activa en Watts (mayor que cero).
        fp_actual: Factor de potencia actual (mayor que 0 y hasta 1).
        fp_deseado: Factor de potencia deseado (mayor que 0 y hasta 1, y
            mayor que fp_actual).
        voltaje: Voltaje RMS del sistema en Volts (mayor que cero).
        frecuencia: Frecuencia en Hz (mayor que cero). Por defecto 60.

    Returns:
        Capacitancia necesaria en Faradios.

    Raises:
        ErrorValidacion: Si algún parámetro no es un número real finito o
            está fuera del rango permitido.
    """
    potencia_activa = validar_numero(potencia_activa, "potencia_activa")
    fp_actual = validar_numero(fp_actual, "fp_actual")
    fp_deseado = validar_numero(fp_deseado, "fp_deseado")
    voltaje = validar_numero(voltaje, "voltaje")
    frecuencia = validar_numero(frecuencia, "frecuencia")

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

    capacitancia: float = calcular_capacitancia_correccion(
        potencia_activa,
        fp_actual,
        fp_deseado,
        voltaje,
        frecuencia,
    )
    return capacitancia
