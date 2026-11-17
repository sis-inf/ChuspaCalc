
import math
from numbers import Real

from ..matematicas.error_validacion import ErrorValidacion


def calcular_densidad(masa: int | float, volumen: int | float) -> float:
    """
    Calcula la densidad de un cuerpo a partir de su masa y volumen.

    Args:
        masa: Masa del cuerpo, valor no negativo.
        volumen: Volumen del cuerpo, valor positivo.

    Returns:
        float: Densidad calculada (masa / volumen).

    Raises:
        ErrorValidacion: Si algún argumento no es numérico, si los valores
            no son finitos, si la masa es negativa, si el volumen no es
            positivo o si el resultado no es finito.
    """
    valores = (masa, volumen)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, Real):
            raise ErrorValidacion("La masa y el volumen deben ser numéricos.")

        try:
            es_finito = math.isfinite(valor)
        except OverflowError as error:
            raise ErrorValidacion("La masa y el volumen deben ser finitos.") from error

        if not es_finito:
            raise ErrorValidacion("La masa y el volumen deben ser finitos.")

    if masa < 0:
        raise ErrorValidacion("La masa no puede ser negativa.")

    if volumen <= 0:
        raise ErrorValidacion("El volumen debe ser positivo.")

    densidad = masa / volumen

    if not math.isfinite(densidad):
        raise ErrorValidacion("La densidad calculada debe ser finita.")

    return densidad
