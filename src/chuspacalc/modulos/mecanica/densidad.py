import math
from numbers import Real

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def calcular_densidad(masa: float, volumen: float) -> float:
    """
    Calcula la densidad de un cuerpo a partir de su masa y volumen.

    Args:
        masa: Masa del cuerpo, valor no negativo.
        volumen: Volumen del cuerpo, valor positivo.

    Returns:
        Densidad calculada (masa / volumen).

    Raises:
        ErrorValidacion: Si algún argumento no es numérico o no es finito,
            si la masa es negativa, si el volumen no es positivo o si el
            resultado no es finito.
    """
    valores = (masa, volumen)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, Real):
            raise ErrorValidacion("La masa y el volumen deben ser numéricos.")

        if not math.isfinite(valor):
            raise ErrorValidacion("La masa y el volumen deben ser finitos.")

    if masa < 0:
        raise ErrorValidacion("La masa no puede ser negativa.")

    if volumen <= 0:
        raise ErrorValidacion("El volumen debe ser positivo.")

    densidad = masa / volumen

    if not math.isfinite(densidad):
        raise ErrorValidacion("La densidad calculada no es finita.")

    return densidad
