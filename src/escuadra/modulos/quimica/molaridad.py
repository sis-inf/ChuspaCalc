
import math


def calcular_molaridad(moles, volumen_litros):
    """
    Calcula la molaridad de una solución química.

    Args:
        moles: Cantidad de moles de soluto.
        volumen_litros: Volumen de la solución expresado en litros.

    Returns:
        Concentración de la solución en mol/L.

    Raises:
        TypeError: Si los argumentos no son números reales.
        ValueError: Si los moles son negativos o el volumen
                    no es positivo y finito.
    """
    if isinstance(moles, bool) or not isinstance(moles, (int, float)):
        raise TypeError("Los moles deben ser un número real.")

    if isinstance(volumen_litros, bool) or not isinstance(
        volumen_litros, (int, float)
    ):
        raise TypeError("El volumen debe ser un número real.")

    if not math.isfinite(moles):
        raise ValueError("Los moles deben ser un valor finito.")

    if not math.isfinite(volumen_litros):
        raise ValueError("El volumen debe ser un valor finito.")

    if moles < 0:
        raise ValueError("Los moles no pueden ser negativos.")

    if volumen_litros <= 0:
        raise ValueError("El volumen debe ser mayor que cero.")

    molaridad = moles / volumen_litros

    return molaridad
