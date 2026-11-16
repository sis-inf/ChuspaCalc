
import math


def calcular_reacciones_carga_central(carga, longitud):
    """
    Calcula las reacciones en los apoyos de una viga
    simplemente apoyada con una carga puntual central.

    Args:
        carga: Magnitud de la carga aplicada.
        longitud: Longitud total de la viga.

    Returns:
        tuple: (reaccion_izquierda, reaccion_derecha)

    Raises:
        ValueError: Si la carga o longitud no son positivas
                    o no son valores numéricos finitos.
    """

    if isinstance(carga, bool) or not isinstance(carga, (int, float)):
        raise ValueError("La carga debe ser un número válido.")

    if isinstance(longitud, bool) or not isinstance(longitud, (int, float)):
        raise ValueError("La longitud debe ser un número válido.")

    if not math.isfinite(carga) or not math.isfinite(longitud):
        raise ValueError("La carga y la longitud deben ser valores finitos.")

    if carga <= 0:
        raise ValueError("La carga debe ser mayor que cero.")

    if longitud <= 0:
        raise ValueError("La longitud debe ser mayor que cero.")

    reaccion_izquierda = carga / 2
    reaccion_derecha = carga / 2

    return reaccion_izquierda, reaccion_derecha
