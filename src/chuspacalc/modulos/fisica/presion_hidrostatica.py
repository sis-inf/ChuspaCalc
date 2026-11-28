"""
Calculadora de presión hidrostática.

Fórmula:
    P = densidad * gravedad * profundidad

Unidades:
    Densidad: kg/m³
    Gravedad: m/s²
    Profundidad: m
    Presión: Pa
"""

import math

from ..matematicas.error_validacion import ErrorValidacion, validar_rango


def calcular_presion_hidrostatica(
    densidad: int | float, gravedad: int | float, profundidad: int | float
) -> float:
    """
    Calcula la presión hidrostática ejercida por un líquido.

    Args:
        densidad: Densidad del líquido en kg/m³. Debe ser un número finito
            no negativo.
        gravedad: Aceleración de la gravedad en m/s². Debe ser un número
            finito no negativo.
        profundidad: Profundidad en metros. Debe ser un número finito no
            negativo.

    Returns:
        Presión hidrostática en pascales (Pa).

    Raises:
        ErrorValidacion: Si algún argumento no es numérico, no es finito,
            está fuera del rango representable o es negativo, o si la
            presión calculada no es finita.
    """
    densidad_kg_m3 = validar_rango(densidad, "densidad", minimo=0)
    gravedad_ms2 = validar_rango(gravedad, "gravedad", minimo=0)
    profundidad_m = validar_rango(profundidad, "profundidad", minimo=0)

    presion = densidad_kg_m3 * gravedad_ms2 * profundidad_m

    if not math.isfinite(presion):
        raise ErrorValidacion("La presión calculada debe ser finita.")

    return presion
