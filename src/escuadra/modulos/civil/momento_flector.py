
import math


def calcular_momento_maximo(carga, longitud):
    """
    Calcula el momento flector máximo de una viga simplemente
    apoyada sometida a una carga puntual central.

    Fórmula:
        Mmax = (carga * longitud) / 4

    Args:
        carga: Carga puntual aplicada (N).
        longitud: Longitud de la viga (m).

    Returns:
        float: Momento flector máximo (N·m).

    Raises:
        ValueError: Si los valores no son numéricos,
                    positivos o finitos.
    """

    if isinstance(carga, bool) or not isinstance(carga, (int, float)):
        raise ValueError("La carga debe ser un número válido.")

    if isinstance(longitud, bool) or not isinstance(longitud, (int, float)):
        raise ValueError("La longitud debe ser un número válido.")

    if not math.isfinite(carga) or not math.isfinite(longitud):
        raise ValueError("La carga y la longitud deben ser finitas.")

    if carga <= 0:
        raise ValueError("La carga debe ser mayor que cero.")

    if longitud <= 0:
        raise ValueError("La longitud debe ser mayor que cero.")

    momento_maximo = (carga * longitud) / 4

    return momento_maximo
