import math


def calcular_mcm(a, b):
    """
    Calcula el minimo comun multiplo de dos numeros enteros.

    Args:
        a: Primer numero entero.
        b: Segundo numero entero.

    Returns:
        El minimo comun multiplo como entero no negativo.

    Raises:
        TypeError: Si los argumentos no son enteros o son booleanos.
    """
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Los argumentos deben ser numeros enteros.")

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Los argumentos deben ser numeros enteros.")

    if a == 0 or b == 0:
        return 0

    return abs((a * b) // math.gcd(a, b))
