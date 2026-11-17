
"""
Calculadora de puntuacion Z.
"""

import math


def calcular_puntuacion_z(valor, media, desviacion_estandar):
    """
    Calcula la puntuacion Z de una observacion.

    Args:
        valor: Valor de la observacion.
        media: Media de la poblacion.
        desviacion_estandar: Desviacion estandar poblacional.

    Returns:
        Puntuacion Z calculada.
    """
    parametros = (valor, media, desviacion_estandar)

    for parametro in parametros:
        if isinstance(parametro, bool) or not isinstance(parametro, (int, float)):
            raise TypeError("Todos los parametros deben ser numericos.")

        try:
            if not math.isfinite(parametro):
                raise ValueError("Todos los parametros deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Todos los parametros deben ser finitos.") from error

    if desviacion_estandar <= 0:
        raise ValueError("La desviacion estandar debe ser mayor que cero.")

    try:
        puntuacion = (valor - media) / desviacion_estandar
    except (OverflowError, ZeroDivisionError) as error:
        raise ValueError("No se pudo calcular la puntuacion Z.") from error

    if not math.isfinite(puntuacion):
        raise ValueError("El resultado debe ser finito.")

    return puntuacion
