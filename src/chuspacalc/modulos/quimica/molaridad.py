
import math

from ..matematicas.error_validacion import ErrorValidacion


def calcular_molaridad(moles: int | float, volumen_litros: int | float) -> float:
    """
    Calcula la molaridad de una solución química.

    Args:
        moles: Cantidad de moles de soluto.
        volumen_litros: Volumen de la solución expresado en litros.

    Returns:
        Concentración de la solución en mol/L.

    Raises:
        ErrorValidacion: Si los argumentos no son números reales, si los
            moles son negativos, si el volumen no es positivo y finito o
            si el resultado no es finito.
    """
    if isinstance(moles, bool) or not isinstance(moles, (int, float)):
        raise ErrorValidacion("Los moles deben ser un número real.")

    if isinstance(volumen_litros, bool) or not isinstance(
        volumen_litros, (int, float)
    ):
        raise ErrorValidacion("El volumen debe ser un número real.")

    try:
        moles_finitos = math.isfinite(moles)
    except OverflowError as error:
        raise ErrorValidacion("Los moles deben ser un valor finito.") from error

    if not moles_finitos:
        raise ErrorValidacion("Los moles deben ser un valor finito.")

    try:
        volumen_finito = math.isfinite(volumen_litros)
    except OverflowError as error:
        raise ErrorValidacion("El volumen debe ser un valor finito.") from error

    if not volumen_finito:
        raise ErrorValidacion("El volumen debe ser un valor finito.")

    if moles < 0:
        raise ErrorValidacion("Los moles no pueden ser negativos.")

    if volumen_litros <= 0:
        raise ErrorValidacion("El volumen debe ser mayor que cero.")

    molaridad = moles / volumen_litros

    if not math.isfinite(molaridad):
        raise ErrorValidacion("La molaridad calculada debe ser finita.")

    return molaridad
