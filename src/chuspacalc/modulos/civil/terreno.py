"""
Cálculo de volúmenes de movimiento de tierras.
"""

import math

from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
)


def volumen_areas_extremas(area_1: float, area_2: float, longitud: float) -> float:
    """
    Calcula el volumen de corte o relleno entre dos secciones
    transversales consecutivas por el método de áreas extremas promedio:

        V = ((A1 + A2) / 2) * L

    Args:
        area_1: Área de la primera sección transversal, en m². Debe ser
            finita y no negativa.
        area_2: Área de la segunda sección transversal, en m². Debe ser
            finita y no negativa.
        longitud: Distancia entre ambas secciones, en m. Debe ser finita
            y mayor que cero.

    Returns:
        Volumen entre las dos secciones, en m³.

    Raises:
        ErrorValidacion: Si algún valor no es un número real finito, si
            es booleano, si un área es negativa, si la longitud no es
            mayor que cero o si el volumen resultante se desborda.
    """

    areas = (("area_1", area_1), ("area_2", area_2))
    validadas: list[float] = []

    for nombre, area in areas:
        numero = validar_numero(area, nombre)

        if numero < 0:
            raise ErrorValidacion(
                f"El valor de '{nombre}' no puede ser negativo "
                f"(valor recibido: {numero})."
            )

        validadas.append(numero)

    distancia = validar_numero(longitud, "longitud")

    if distancia <= 0:
        raise ErrorValidacion(
            f"El valor de 'longitud' debe ser mayor que cero "
            f"(valor recibido: {distancia})."
        )

    volumen = ((validadas[0] + validadas[1]) / 2) * distancia

    if not math.isfinite(volumen):
        raise ErrorValidacion(
            "El volumen calculado está fuera del rango representable."
        )

    return volumen
