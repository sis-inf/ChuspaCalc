
def es_numero_primo(numero):
    """
    Determina si un número entero es primo.

    Args:
        numero: Número entero que se desea comprobar.

    Returns:
        bool: True si es primo, False si no es primo.

    Raises:
        ValueError: Si el argumento no es un número entero
                    o si es un valor booleano.
    """

    if isinstance(numero, bool) or not isinstance(numero, int):
        raise ValueError("El argumento debe ser un número entero.")

    if numero < 2:
        return False

    divisor = 2

    while divisor <= numero // divisor:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True
