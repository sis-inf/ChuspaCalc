"""
Calculadora de concentración de una sustancia en partes por millón (ppm).

Fórmula:
    ppm = (masa_soluto / masa_total) * 1_000_000
"""

import math


def calcular_concentracion_ppm(masa_soluto, masa_total):
    """
    Calcula la concentración de una sustancia en partes por millón.

    Args:
        masa_soluto: Masa del soluto.
        masa_total: Masa total de la mezcla.

    Returns:
        La concentración expresada en ppm.

    Raises:
        TypeError: Si algún valor no es numérico.
        ValueError: Si las masas no son finitas o válidas.
    """
    valores = (masa_soluto, masa_total)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Las masas deben ser números reales.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Las masas deben ser finitas.")
        except OverflowError as error:
            raise ValueError("Las masas deben ser finitas.") from error

    if masa_total <= 0:
        raise ValueError("La masa total debe ser positiva.")

    if masa_soluto < 0:
        raise ValueError("La masa del soluto no puede ser negativa.")

    if masa_soluto > masa_total:
        raise ValueError("La masa del soluto no puede superar la masa total.")

    concentracion = (masa_soluto / masa_total) * 1_000_000

    if not math.isfinite(concentracion):
        raise ValueError("El resultado debe ser finito.")

    return concentracion
