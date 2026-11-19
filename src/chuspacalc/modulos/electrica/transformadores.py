"""
Herramientas para cálculo de transformadores monofásicos.
"""

import math


def calcular_transformador_monofasico(v_primario, v_secundario, potencia_aparente):
    """
    Calcula la relación de transformación y las corrientes nominales
    de un transformador monofásico ideal.

    Asume un transformador ideal: sin pérdidas, por lo que la potencia
    aparente es la misma en el primario y en el secundario.

    Fórmulas:
        a = V1 / V2
        I1 = S / V1
        I2 = S / V2

    Args:
        v_primario: Voltaje primario V1, en V.
        v_secundario: Voltaje secundario V2, en V.
        potencia_aparente: Potencia aparente S, en VA.

    Returns:
        Diccionario con la relación de transformación (adimensional)
        y las corrientes primaria y secundaria, en A.

    Raises:
        ValueError: Si algún valor no es finito o no es positivo.
    """

    valores = (v_primario, v_secundario, potencia_aparente)

    if not all(math.isfinite(v) for v in valores):
        raise ValueError("Los valores deben ser finitos")

    if v_primario <= 0 or v_secundario <= 0:
        raise ValueError("Los voltajes deben ser positivos")

    if potencia_aparente <= 0:
        raise ValueError("La potencia aparente debe ser positiva")

    return {
        "relacion_transformacion": v_primario / v_secundario,
        "corriente_primaria": potencia_aparente / v_primario,
        "corriente_secundaria": potencia_aparente / v_secundario,
        "unidad_corriente": "A",
    }
