import math


def area_rectangular(base, altura):
    """Calcula el área de una sección rectangular."""
    if base <= 0 or altura <= 0:
        raise ValueError("Las dimensiones deben ser mayores que 0")

    return base * altura


def area_circular(radio):
    """Calcula el área de una sección circular maciza."""
    if radio <= 0:
        raise ValueError("El radio debe ser mayor que 0")

    return math.pi * radio**2


def area_circular_hueca(radio_ext, radio_int):
    """Calcula el área de una sección circular hueca."""
    if radio_ext <= 0 or radio_int <= 0:
        raise ValueError("Los radios deben ser mayores que 0")

    if radio_int >= radio_ext:
        raise ValueError("El radio interior debe ser menor que el radio exterior")

    return math.pi * (radio_ext**2 - radio_int**2)


def area_perfil_i(
    ancho_ala,
    espesor_ala,
    altura_alma,
    espesor_alma,
):
    """Calcula el área de una sección tipo I."""
    dimensiones = [
        ancho_ala,
        espesor_ala,
        altura_alma,
        espesor_alma,
    ]

    if any(d <= 0 for d in dimensiones):
        raise ValueError("Las dimensiones deben ser mayores que 0")

    return 2 * ancho_ala * espesor_ala + altura_alma * espesor_alma


def area_perfil_t(
    ancho_ala,
    espesor_ala,
    altura_alma,
    espesor_alma,
):
    """Calcula el área de una sección tipo T."""
    dimensiones = [
        ancho_ala,
        espesor_ala,
        altura_alma,
        espesor_alma,
    ]

    if any(d <= 0 for d in dimensiones):
        raise ValueError("Las dimensiones deben ser mayores que 0")

    return ancho_ala * espesor_ala + altura_alma * espesor_alma
