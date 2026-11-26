"""
Cálculo de reacciones en los apoyos de una viga simplemente apoyada.
"""

import math

from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
)


def calcular_reacciones_carga_central(
    carga: float, longitud: float
) -> tuple[float, float]:
    """
    Calcula las reacciones en los apoyos de una viga
    simplemente apoyada con una carga puntual central.

    Args:
        carga: Magnitud de la carga aplicada. Debe ser finita y mayor
            que cero.
        longitud: Longitud total de la viga. Debe ser finita y mayor
            que cero.

    Returns:
        Tupla (reaccion_izquierda, reaccion_derecha), cada una igual a
        la mitad de la carga.

    Raises:
        ErrorValidacion: Si la carga o la longitud no son números reales
            finitos, si son booleanas o si no son mayores que cero.
    """

    parametros = (("carga", carga), ("longitud", longitud))
    validados: list[float] = []

    for nombre, valor in parametros:
        numero = validar_numero(valor, nombre)

        if numero <= 0:
            raise ErrorValidacion(
                f"El valor de '{nombre}' debe ser mayor que cero "
                f"(valor recibido: {numero})."
            )

        validados.append(numero)

    carga_validada = validados[0]

    reaccion_izquierda = carga_validada / 2
    reaccion_derecha = carga_validada / 2

    if not math.isfinite(reaccion_izquierda) or not math.isfinite(reaccion_derecha):
        raise ErrorValidacion(
            "Las reacciones calculadas están fuera del rango representable."
        )

    return reaccion_izquierda, reaccion_derecha
