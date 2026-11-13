
"""
Calculadora del discriminante de una ecuación cuadrática.

Fórmula:
    D = b² - 4ac
"""


import math


def calcular_discriminante(a, b, c):
    """
    Calcula el discriminante de una ecuación cuadrática.

    Args:
        a: Coeficiente cuadrático.
        b: Coeficiente lineal.
        c: Término independiente.

    Returns:
        El valor del discriminante.

    Raises:
        TypeError: Si algún coeficiente no es numérico.
        ValueError: Si algún coeficiente no es finito o si a es cero.
    """
    coeficientes = (a, b, c)

    for valor in coeficientes:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Los coeficientes deben ser números reales.")

        if isinstance(valor, float) and not math.isfinite(valor):
            raise ValueError("Los coeficientes deben ser números finitos.")

    if a == 0:
        raise ValueError("El coeficiente principal a no puede ser cero.")

    try:
        discriminante = b ** 2 - 4 * a * c
    except OverflowError as error:
        raise ValueError("El resultado está fuera del rango permitido.") from error

    if isinstance(discriminante, float) and not math.isfinite(discriminante):
        raise ValueError("El resultado debe ser un número finito.")

    return discriminante
