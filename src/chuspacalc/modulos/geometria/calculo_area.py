
import math
from numbers import Real


def _validar_dimension(valor, nombre):
    """Verifica que una dimensión sea real, finita y positiva."""
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ValueError(f"{nombre} debe ser un numero real finito")

    if not isinstance(valor, int) and not math.isfinite(valor):
        raise ValueError(f"{nombre} debe ser un numero real finito")


def area_triangulo(base, altura):
    _validar_dimension(base, "base")
    _validar_dimension(altura, "altura")

    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser mayores que cero")

    return (base * altura) / 2


def area_circulo(radio):
    _validar_dimension(radio, "radio")

    if radio <= 0:
        raise ValueError("El radio debe ser mayor que cero")

    return 3.1416 * (radio ** 2)


def area_rectangulo(base, altura):
    _validar_dimension(base, "base")
    _validar_dimension(altura, "altura")

    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser mayores que cero")

    return base * altura
