"""
Cálculo de volúmenes de movimiento de tierras.
"""

import math


def volumen_areas_extremas(area_1, area_2, longitud):
    """
    Calcula el volumen de corte o relleno entre dos secciones
    transversales consecutivas por el método de áreas extremas promedio:

        V = ((A1 + A2) / 2) * L

    Args:
        area_1: Área de la primera sección transversal, en m².
        area_2: Área de la segunda sección transversal, en m².
        longitud: Distancia entre ambas secciones, en m.

    Returns:
        Volumen entre las dos secciones, en m³.

    Raises:
        ValueError: Si algún valor no es finito, si un área es negativa
            o si la longitud no es positiva.
    """

    if not all(math.isfinite(v) for v in (area_1, area_2, longitud)):
        raise ValueError("Los valores deben ser finitos")

    if area_1 < 0 or area_2 < 0:
        raise ValueError("Las áreas no pueden ser negativas")

    if longitud <= 0:
        raise ValueError("La longitud debe ser positiva")

    return ((area_1 + area_2) / 2) * longitud
