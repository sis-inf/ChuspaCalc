
import math
from numbers import Real


def calcular_densidad(masa, volumen):
    """
    Calcula la densidad de un cuerpo a partir de su masa y volumen.

    Args:
        masa: Masa del cuerpo, valor no negativo.
        volumen: Volumen del cuerpo, valor positivo.

    Returns:
        float: Densidad calculada (masa / volumen).

    Raises:
        TypeError: Si algún argumento no es numérico.
        ValueError: Si los valores no son finitos, la masa es negativa
                    o el volumen no es positivo.
    """
    valores = (masa, volumen)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, Real):
            raise TypeError("La masa y el volumen deben ser numéricos.")

        if not math.isfinite(valor):
            raise ValueError("La masa y el volumen deben ser finitos.")

    if masa < 0:
        raise ValueError("La masa no puede ser negativa.")

    if volumen <= 0:
        raise ValueError("El volumen debe ser positivo.")

    densidad = masa / volumen

    return densidad
