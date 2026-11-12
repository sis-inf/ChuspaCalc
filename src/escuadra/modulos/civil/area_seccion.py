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

    if espesor_ala >= ancho_ala:
        raise ValueError(
            "El espesor del ala debe ser menor que el ancho del ala"
        )

    if espesor_alma >= altura_alma:
        raise ValueError(
            "El espesor del alma debe ser menor que la altura del alma"
        )

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


def _validar_positivos(*valores):
    """Lanza ValueError si algún valor no es finito o no es mayor que 0."""
    if any(not math.isfinite(v) or v <= 0 for v in valores):
        raise ValueError("Los valores deben ser finitos y mayores que 0")


def momento_inercia_rectangular(base, altura):
    """Calcula la inercia centroidal respecto al eje horizontal de un rectángulo."""
    _validar_positivos(base, altura)

    return base * altura**3 / 12


def momento_inercia_perfil_i(
    ancho_ala,
    espesor_ala,
    altura_alma,
    espesor_alma,
):
    """Calcula la inercia centroidal respecto al eje horizontal de un perfil I.

    La altura del alma es la distancia libre entre las alas. A la inercia
    propia de cada ala se le suma el término de ejes paralelos A * d**2,
    donde d es la distancia del centroide del ala al eje neutro.
    """
    _validar_positivos(ancho_ala, espesor_ala, altura_alma, espesor_alma)

    inercia_alma = espesor_alma * altura_alma**3 / 12
    inercia_propia_ala = ancho_ala * espesor_ala**3 / 12
    area_ala = ancho_ala * espesor_ala
    distancia_ala = (altura_alma + espesor_ala) / 2

    return inercia_alma + 2 * (inercia_propia_ala + area_ala * distancia_ala**2)


def radio_giro(inercia, area):
    """Calcula el radio de giro como sqrt(I / A)."""
    _validar_positivos(inercia, area)

    return math.sqrt(inercia / area)
