
import math
from numbers import Real


def calcular_desnivel(cota_inicial, cota_final):
    """
    Calcula el desnivel entre dos puntos topográficos.

    Args:
        cota_inicial: Elevación inicial del primer punto.
        cota_final: Elevación final del segundo punto.

    Returns:
        float: Diferencia entre la cota final y la inicial.

    Raises:
        TypeError: Si alguna cota no es numérica.
        ValueError: Si alguna cota no es finita.
    """
    cotas = (cota_inicial, cota_final)

    for cota in cotas:
        if isinstance(cota, bool) or not isinstance(cota, Real):
            raise TypeError("Las cotas deben ser valores numéricos.")

        if not math.isfinite(cota):
            raise ValueError("Las cotas deben ser valores finitos.")

    desnivel = cota_final - cota_inicial

    return desnivel
