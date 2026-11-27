"""
Cálculo del volumen de excavaciones rectangulares.
"""

import math

from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
)


def calcular_volumen_excavacion(
    longitud: float, ancho: float, profundidad: float
) -> float:
    """
    Calcula el volumen de una excavación rectangular.

    Args:
        longitud: Longitud de la excavación, en metros. Debe ser finita y
            mayor que cero.
        ancho: Ancho de la excavación, en metros. Debe ser finito y mayor
            que cero.
        profundidad: Profundidad de la excavación, en metros. Debe ser
            finita y mayor que cero.

    Returns:
        Volumen calculado, en metros cúbicos.

    Raises:
        ErrorValidacion: Si alguna dimensión no es un número real finito,
            si es booleana, si no es mayor que cero o si el volumen
            resultante se desborda.
    """
    dimensiones = (
        ("longitud", longitud),
        ("ancho", ancho),
        ("profundidad", profundidad),
    )

    validadas: list[float] = []

    for nombre, dimension in dimensiones:
        numero = validar_numero(dimension, nombre)

        if numero <= 0:
            raise ErrorValidacion(
                f"El valor de '{nombre}' debe ser mayor que cero "
                f"(valor recibido: {numero})."
            )

        validadas.append(numero)

    volumen = validadas[0] * validadas[1] * validadas[2]

    if not math.isfinite(volumen):
        raise ErrorValidacion(
            "El volumen calculado está fuera del rango representable."
        )

    return volumen
