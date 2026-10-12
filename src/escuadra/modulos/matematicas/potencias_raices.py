import math


def potencia(base, exponente):
    """
    Calcula una potencia.

    Fórmula:
        resultado = base ** exponente
    """
    return float(base**exponente)


def raiz_n(valor, n):
    """
    Calcula la raíz n-ésima de un número.

    Lanza ValueError si:
    - n <= 0
    - valor es negativo y n es par
    """
    if n <= 0:
        raise ValueError("n debe ser mayor que 0")

    if valor < 0 and n % 2 == 0:
        raise ValueError("No existe raíz par real de un número negativo")

    return float(valor ** (1 / n))


def raiz_cuadrada(valor):
    """
    Calcula la raíz cuadrada.

    Fórmula:
        sqrt(valor)
    """
    if valor < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")

    return float(math.sqrt(valor))


def logaritmo_natural(valor):
    """
    Calcula el logaritmo natural.

    Fórmula:
        ln(valor)
    """
    if valor <= 0:
        raise ValueError("El valor debe ser mayor que 0")

    return float(math.log(valor))


def logaritmo_base10(valor):
    """
    Calcula el logaritmo en base 10.

    Fórmula:
        log10(valor)
    """
    if valor <= 0:
        raise ValueError("El valor debe ser mayor que 0")

    return float(math.log10(valor))


def logaritmo_base(valor, base):
    """
    Calcula el logaritmo en una base arbitraria.

    Fórmula:
        log(valor, base)
    """
    if valor <= 0:
        raise ValueError("El valor debe ser mayor que 0")

    if base <= 0 or base == 1:
        raise ValueError("La base debe ser positiva y distinta de 1")

    return float(math.log(valor, base))
