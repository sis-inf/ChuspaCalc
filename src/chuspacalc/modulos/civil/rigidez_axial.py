"""Cálculo de rigidez axial de elementos estructurales."""

import math
from fractions import Fraction

from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
)


def calcular_rigidez_axial(elasticidad: float, area: float, longitud: float) -> float:
    """Calcula E * A / L, en N/m.

    Args:
        elasticidad: Módulo de elasticidad en Pa.
        area: Área transversal en m².
        longitud: Longitud del elemento en m.

    Raises:
        ErrorValidacion: Si una entrada no es real, positiva y finita,
            o la rigidez está fuera del rango numérico representable.
    """
    parametros = {"elasticidad": elasticidad, "area": area, "longitud": longitud}
    valores = {}
    for nombre, valor in parametros.items():
        numero = validar_numero(valor, nombre)
        if numero <= 0:
            raise ErrorValidacion(f"{nombre} debe ser positivo y finito.")
        valores[nombre] = numero
    elasticidad, area, longitud = (
        valores["elasticidad"],
        valores["area"],
        valores["longitud"],
    )
    rigidez = elasticidad * area / longitud
    if not math.isfinite(rigidez) or rigidez <= 0:
        try:
            rigidez = float(Fraction(elasticidad) * Fraction(area) / Fraction(longitud))
        except OverflowError as error:
            raise ErrorValidacion("La rigidez excede el rango numérico") from error
        if not math.isfinite(rigidez) or rigidez <= 0:
            raise ErrorValidacion("La rigidez debe ser positiva y finita")
    return rigidez
