
import math


def calcular_reacciones_carga_distribuida(carga_distribuida, longitud):
    """
    Calcula las reacciones en los apoyos de una viga simplemente
    apoyada sometida a una carga uniformemente distribuida.

    Args:
        carga_distribuida: Carga distribuida en N/m.
        longitud: Longitud de la viga en metros.

    Returns:
        tuple: (reaccion_izquierda, reaccion_derecha), en N.

    Raises:
        ValueError: Si los parámetros no son numéricos,
                    positivos o finitos.
    """

    if isinstance(carga_distribuida, bool) or not isinstance(
        carga_distribuida, (int, float)
    ):
        raise ValueError("La carga distribuida debe ser numérica.")

    if isinstance(longitud, bool) or not isinstance(longitud, (int, float)):
        raise ValueError("La longitud debe ser numérica.")

    if not math.isfinite(carga_distribuida):
        raise ValueError("La carga distribuida debe ser finita.")

    if not math.isfinite(longitud):
        raise ValueError("La longitud debe ser finita.")

    if carga_distribuida <= 0:
        raise ValueError("La carga distribuida debe ser mayor que cero.")

    if longitud <= 0:
        raise ValueError("La longitud debe ser mayor que cero.")

    carga_total = carga_distribuida * longitud

    reaccion_izquierda = carga_total / 2
    reaccion_derecha = carga_total / 2

    return reaccion_izquierda, reaccion_derecha
