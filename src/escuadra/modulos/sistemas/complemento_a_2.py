"""
Funciones para convertir entre decimal y complemento a 2.
"""


def decimal_a_complemento(numero: int, bits: int) -> str:
    minimo = -(2 ** (bits - 1))
    maximo = (2 ** (bits - 1)) - 1

    if numero < minimo or numero > maximo:
        raise ValueError(f"El número debe estar entre {minimo} y {maximo}.")

    if numero >= 0:
        return f"{numero:0{bits}b}"

    return f"{(2 ** bits + numero):0{bits}b}"


def complemento_a_decimal(binario: str, bits: int) -> int:
    if len(binario) != bits:
        raise ValueError(f"Debe ingresar exactamente {bits} bits.")

    if any(c not in "01" for c in binario):
        raise ValueError("Solo se permiten 0 y 1.")

    valor = int(binario, 2)

    if binario[0] == "1":
        return valor - (2**bits)

    return valor
