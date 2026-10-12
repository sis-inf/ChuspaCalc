import math


def volumen_cubo(lado):
    """Volumen de un cubo: lado³"""
    if lado <= 0:
        raise ValueError("La dimensión debe ser mayor que 0")
    return float(lado**3)


def volumen_esfera(radio):
    """Volumen de una esfera: (4/3)πr³"""
    if radio <= 0:
        raise ValueError("La dimensión debe ser mayor que 0")
    return float((4 / 3) * math.pi * radio**3)


def volumen_cilindro(radio, altura):
    """Volumen de un cilindro: πr²h"""
    if radio <= 0 or altura <= 0:
        raise ValueError("Las dimensiones deben ser mayores que 0")
    return float(math.pi * radio**2 * altura)


def volumen_cono(radio, altura):
    """Volumen de un cono: (1/3)πr²h"""
    if radio <= 0 or altura <= 0:
        raise ValueError("Las dimensiones deben ser mayores que 0")
    return float((1 / 3) * math.pi * radio**2 * altura)


def volumen_paralelepipedo(largo, ancho, alto):
    """Volumen de un paralelepípedo: largo × ancho × alto"""
    if largo <= 0 or ancho <= 0 or alto <= 0:
        raise ValueError("Las dimensiones deben ser mayores que 0")
    return float(largo * ancho * alto)
