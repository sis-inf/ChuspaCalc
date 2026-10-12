import math


def convertir_angulo(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    Convierte ángulos entre grados, radianes y gradianes.
    """

    unidad_origen = unidad_origen.lower()
    unidad_destino = unidad_destino.lower()

    unidades_validas = {
        "grados",
        "radianes",
        "gradianes",
    }

    if unidad_origen not in unidades_validas:
        raise ValueError("Unidad de origen inválida")

    if unidad_destino not in unidades_validas:
        raise ValueError("Unidad de destino inválida")

    if unidad_origen == unidad_destino:
        return valor

    # Convertir a grados primero
    if unidad_origen == "grados":
        grados = valor

    elif unidad_origen == "radianes":
        grados = math.degrees(valor)

    else:  # gradianes
        grados = valor * 0.9

    # Convertir desde grados al destino
    if unidad_destino == "grados":
        return grados

    if unidad_destino == "radianes":
        return math.radians(grados)

    return grados / 0.9


def grados_a_radianes(grados: float) -> float:
    """
    Convierte grados a radianes.
    """
    return math.radians(grados)


def radianes_a_grados(rad: float) -> float:
    """
    Convierte radianes a grados.
    """
    return math.degrees(rad)
