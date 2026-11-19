"""
Funciones para convertir entre decimal y complemento a 2.
"""

from ..matematicas.error_validacion import ErrorValidacion


def _validar_bits(bits: int) -> None:
    """Valida que la cantidad de bits sea un entero positivo."""
    if isinstance(bits, bool) or not isinstance(bits, int) or bits < 1:
        raise ErrorValidacion("La cantidad de bits debe ser un entero positivo.")


def decimal_a_complemento(numero: int, bits: int) -> str:
    """
    Convierte un entero decimal a su representación en complemento a 2.

    Args:
        numero: Entero a convertir, dentro del rango que cabe en bits.
        bits: Cantidad de bits de la representación (entero positivo).

    Returns:
        Cadena de exactamente bits caracteres con el número en complemento a 2.

    Raises:
        ErrorValidacion: Si bits o numero no son enteros, si bits no es
            positivo o si numero no cabe en esa cantidad de bits.
    """
    _validar_bits(bits)

    if isinstance(numero, bool) or not isinstance(numero, int):
        raise ErrorValidacion("El número debe ser un entero.")

    minimo = -(2 ** (bits - 1))
    maximo = (2 ** (bits - 1)) - 1

    if numero < minimo or numero > maximo:
        raise ErrorValidacion(f"El número debe estar entre {minimo} y {maximo}.")

    if numero >= 0:
        return f"{numero:0{bits}b}"

    return f"{(2 ** bits + numero):0{bits}b}"


def complemento_a_decimal(binario: str, bits: int) -> int:
    """
    Convierte una cadena en complemento a 2 a su valor decimal.

    Args:
        binario: Cadena de ceros y unos de exactamente bits caracteres.
        bits: Cantidad de bits de la representación (entero positivo).

    Returns:
        El entero con signo que representa la cadena.

    Raises:
        ErrorValidacion: Si bits no es un entero positivo, si binario no es
            texto, si su longitud no es bits o si tiene caracteres distintos
            de 0 y 1.
    """
    _validar_bits(bits)

    if not isinstance(binario, str):
        raise ErrorValidacion("El valor binario debe ser una cadena de texto.")

    if len(binario) != bits:
        raise ErrorValidacion(f"Debe ingresar exactamente {bits} bits.")

    if any(c not in "01" for c in binario):
        raise ErrorValidacion("Solo se permiten 0 y 1.")

    valor: int = int(binario, 2)

    if binario[0] == "1":
        resultado: int = valor - (2**bits)
        return resultado

    return valor
