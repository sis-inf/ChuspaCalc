"""
Cálculo del esfuerzo normal producido por una fuerza axial.
"""

import math

from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
)


def calcular_esfuerzo_axial(fuerza: float, area: float) -> float:
    """
    Calcula el esfuerzo normal producido por una fuerza axial.

    Args:
        fuerza: Fuerza axial en Newtons (N). Debe ser finita. Positiva
            para tracción y negativa para compresión.
        area: Área transversal en metros cuadrados (m²). Debe ser finita
            y mayor que cero.

    Returns:
        Esfuerzo axial en Pascales (Pa).

    Raises:
        ErrorValidacion: Si la fuerza o el área no son números reales
            finitos, si son booleanas, si el área no es mayor que cero o
            si el esfuerzo resultante se desborda.
    """

    fuerza_validada = validar_numero(fuerza, "fuerza")
    area_validada = validar_numero(area, "area")

    if area_validada <= 0:
        raise ErrorValidacion(
            f"El valor de 'area' debe ser mayor que cero "
            f"(valor recibido: {area_validada})."
        )

    esfuerzo = fuerza_validada / area_validada

    if not math.isfinite(esfuerzo):
        raise ErrorValidacion(
            "El esfuerzo calculado está fuera del rango representable."
        )

    return esfuerzo
