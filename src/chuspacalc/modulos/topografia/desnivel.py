import math
from numbers import Real

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def calcular_desnivel(cota_inicial: float, cota_final: float) -> float:
    """
    Calcula el desnivel entre dos puntos topográficos.

    Args:
        cota_inicial: Elevación inicial del primer punto.
        cota_final: Elevación final del segundo punto.

    Returns:
        Diferencia entre la cota final y la inicial.

    Raises:
        ErrorValidacion: Si alguna cota no es numérica o no es finita, o si
            el resultado no es finito.
    """
    cotas = (cota_inicial, cota_final)

    for cota in cotas:
        if isinstance(cota, bool) or not isinstance(cota, Real):
            raise ErrorValidacion("Las cotas deben ser valores numéricos.")

        if not math.isfinite(cota):
            raise ErrorValidacion("Las cotas deben ser valores finitos.")

    desnivel = cota_final - cota_inicial

    if not math.isfinite(desnivel):
        raise ErrorValidacion("El desnivel calculado no es finito.")

    return desnivel
