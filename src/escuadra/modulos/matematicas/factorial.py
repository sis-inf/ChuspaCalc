"""Factorial de un número entero no negativo."""


def calcular_factorial(numero: int) -> int:
    """Calcula el factorial de un entero no negativo.

    Fórmula: n! = 1 * 2 * ... * n, con 0! = 1.

    Args:
        numero: entero mayor o igual que 0.

    Returns:
        El factorial de numero, como entero.

    Raises:
        ValueError: si numero no es un entero, es un booleano o es
            negativo.
    """
    if isinstance(numero, bool) or not isinstance(numero, int):
        raise ValueError(f"numero debe ser un entero, se recibió {numero!r}")
    if numero < 0:
        raise ValueError(f"el factorial no existe para negativos: {numero}")

    resultado = 1
    for factor in range(2, numero + 1):
        resultado *= factor
    return resultado
