
import math
from numbers import Real


def _validar_dimension(valor, nombre):
    """Verifica que una dimensión sea real y finita."""
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ValueError(f"{nombre} debe ser un numero real finito")

    if not isinstance(valor, int) and not math.isfinite(valor):
        raise ValueError(f"{nombre} debe ser un numero real finito")



def perimetro_circulo(radio):
    _validar_dimension(radio, "radio")

    if radio <= 0:
        raise ValueError("El radio debe ser mayor que cero")

    return 2 * math.pi * radio


def perimetro_cuadrado(lado):
    _validar_dimension(lado, "lado")

    if lado <= 0:
        raise ValueError("El lado debe ser mayor que cero")

    return 4 * lado


def perimetro_rectangulo(largo, ancho):
    _validar_dimension(largo, "largo")
    _validar_dimension(ancho, "ancho")

    if largo <= 0 or ancho <= 0:
        raise ValueError("Las dimensiones deben ser mayores que cero")

    return 2 * (largo + ancho)


def perimetro_triangulo(a, b, c):
    _validar_dimension(a, "a")
    _validar_dimension(b, "b")
    _validar_dimension(c, "c")

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Los lados deben ser mayores que cero")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("El triángulo no cumple la desigualdad triangular")

    return a + b + c


def perimetro_hexagono_regular(lado):
    _validar_dimension(lado, "lado")

    if lado <= 0:
        raise ValueError("El lado debe ser mayor que cero")

    return 6 * lado


def perimetro_poligono_regular(n_lados: int, longitud_lado: float):
    if isinstance(n_lados, bool) or not isinstance(n_lados, int):
        raise ValueError("El numero de lados debe ser un entero")

    if n_lados < 3:
        raise ValueError("El polígono debe tener al menos 3 lados")

    _validar_dimension(longitud_lado, "longitud_lado")

    if longitud_lado <= 0:
        raise ValueError("El lado debe ser mayor que cero")

    return n_lados * longitud_lado


def perimetro_trapecio(lado_a: float, lado_b: float, lado_c: float, lado_d: float):
    _validar_dimension(lado_a, "lado_a")
    _validar_dimension(lado_b, "lado_b")
    _validar_dimension(lado_c, "lado_c")
    _validar_dimension(lado_d, "lado_d")

    if lado_a <= 0 or lado_b <= 0 or lado_c <= 0 or lado_d <= 0:
        raise ValueError("Los lados deben ser mayores que cero")

    return lado_a + lado_b + lado_c + lado_d
