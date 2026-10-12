"""
Resolución de triángulos mediante ley de senos y cosenos.
"""

import math


def resolver_triangulo_lados(a: float, b: float, c: float):
    """
    Resuelve un triángulo conociendo sus tres lados usando ley de cosenos.

    Retorna los tres ángulos en grados.
    """

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Los lados deben ser mayores a cero")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Los lados no forman un triángulo válido")

    angulo_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))

    angulo_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))

    angulo_c = 180 - angulo_a - angulo_b

    return angulo_a, angulo_b, angulo_c


def resolver_triangulo_lado_angulo(
    a: float,
    angulo_a: float,
    angulo_b: float,
):
    """
    Resuelve un triángulo usando ley de senos.

    Recibe un lado y dos ángulos.
    """

    if a <= 0:
        raise ValueError("El lado debe ser mayor a cero")

    if angulo_a + angulo_b >= 180:
        raise ValueError("La suma de ángulos es inválida")

    angulo_c = 180 - angulo_a - angulo_b

    b = a * math.sin(math.radians(angulo_b)) / math.sin(math.radians(angulo_a))

    c = a * math.sin(math.radians(angulo_c)) / math.sin(math.radians(angulo_a))

    return b, c, angulo_c
