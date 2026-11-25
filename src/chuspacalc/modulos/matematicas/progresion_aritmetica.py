import math
from numbers import Real

from .error_validacion import ErrorValidacion


def _es_real_finito(valor: object) -> bool:
    """Indica si el valor es un número real finito (sin contar bool)."""
    if isinstance(valor, bool) or not isinstance(valor, Real):
        return False

    try:
        return math.isfinite(valor)
    except OverflowError:
        return False


def calcular_termino_aritmetico(
    primer_termino: int | float, diferencia: int | float, posicion: int
) -> float:
    """
    Calcula un término de una progresión aritmética.

    Fórmula:
        an = a1 + (n - 1) * d

    Args:
        primer_termino: Primer término de la progresión.
        diferencia: Diferencia común.
        posicion: Posición del término que se desea calcular.

    Returns:
        float: Término correspondiente a la posición indicada.

    Raises:
        ErrorValidacion: Si los argumentos son inválidos o si el
            resultado no es finito.
    """

    if not _es_real_finito(primer_termino):
        raise ErrorValidacion("El primer término debe ser un número real finito.")

    if not _es_real_finito(diferencia):
        raise ErrorValidacion("La diferencia debe ser un número real finito.")

    if isinstance(posicion, bool) or not isinstance(posicion, int) or posicion <= 0:
        raise ErrorValidacion("La posición debe ser un entero positivo.")

    try:
        resultado = primer_termino + (posicion - 1) * diferencia
    except OverflowError as error:
        raise ErrorValidacion("El resultado calculado no es finito.") from error

    if not math.isfinite(resultado):
        raise ErrorValidacion("El resultado calculado no es finito.")

    return resultado
