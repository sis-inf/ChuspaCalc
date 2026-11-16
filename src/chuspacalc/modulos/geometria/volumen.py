
import math
from numbers import Real


def _validar_dimension(valor, nombre):
    """Verifica que una dimension sea real y finita."""
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ValueError(f"{nombre} debe ser un numero real finito")

    if not isinstance(valor, int) and not math.isfinite(valor):
        raise ValueError(f"{nombre} debe ser un numero real finito")


def volumen_cubo(lado):
    """Volumen de un cubo: lado³"""
    _validar_dimension(lado, "lado")

    if lado <= 0:
        raise ValueError("La dimensión debe ser mayor que 0")

    return float(lado ** 3)


def volumen_esfera(radio):
    """Volumen de una esfera: (4/3)πr³"""
    _validar_dimension(radio, "radio")

    if radio <= 0:
        raise ValueError("La dimensión debe ser mayor que 0")

    return float((4 / 3) * math.pi * radio ** 3)


def volumen_cilindro(radio, altura):
    """Volumen de un cilindro: πr²h"""
    _validar_dimension(radio, "radio")
    _validar_dimension(altura, "altura")

    if radio <= 0 or altura <= 0:
        raise ValueError("Las dimensiones deben ser mayores que 0")

    return float(math.pi * radio ** 2 * altura)


def volumen_cono(radio, altura):
    """Volumen de un cono: (1/3)πr²h"""
    _validar_dimension(radio, "radio")
    _validar_dimension(altura, "altura")

    if radio <= 0 or altura <= 0:
        raise ValueError("Las dimensiones deben ser mayores que 0")

    return float((1 / 3) * math.pi * radio ** 2 * altura)


def volumen_paralelepipedo(largo, ancho, alto):
    """Volumen de un paralelepípedo: largo × ancho × alto"""
    _validar_dimension(largo, "largo")
    _validar_dimension(ancho, "ancho")
    _validar_dimension(alto, "alto")

    if largo <= 0 or ancho <= 0 or alto <= 0:
        raise ValueError("Las dimensiones deben ser mayores que 0")

    return float(largo * ancho * alto)
