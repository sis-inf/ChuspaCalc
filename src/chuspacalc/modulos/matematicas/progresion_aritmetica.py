
import math
from numbers import Real


def calcular_termino_aritmetico(primer_termino, diferencia, posicion):
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
        ValueError: Si los argumentos son inválidos.
    """

    if (
        isinstance(primer_termino, bool)
        or not isinstance(primer_termino, Real)
        or not math.isfinite(primer_termino)
    ):
        raise ValueError("El primer término debe ser un número real finito.")

    if (
        isinstance(diferencia, bool)
        or not isinstance(diferencia, Real)
        or not math.isfinite(diferencia)
    ):
        raise ValueError("La diferencia debe ser un número real finito.")

    if (
        isinstance(posicion, bool)
        or not isinstance(posicion, int)
        or posicion <= 0
    ):
        raise ValueError("La posición debe ser un entero positivo.")

    resultado = primer_termino + (posicion - 1) * diferencia

    if not math.isfinite(resultado):
        raise ValueError("El resultado calculado no es finito.")

    return resultado
