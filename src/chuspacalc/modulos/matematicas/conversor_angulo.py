import math


def _validar_numero_finito(valor: float) -> float:
    try:
        if not math.isfinite(valor):
            raise ValueError("El valor debe ser un número finito")
    except TypeError as error:
        raise ValueError("El valor debe ser un número finito") from error
    return valor


def convertir_angulo(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    Convierte ángulos entre grados, radianes y gradianes.
    """

    _validar_numero_finito(valor)

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
    _validar_numero_finito(grados)
    return math.radians(grados)


def radianes_a_grados(rad: float) -> float:
    """
    Convierte radianes a grados.
    """
    _validar_numero_finito(rad)
    return math.degrees(rad)


def grados_a_dms(grados: float) -> tuple[int, int, float]:
    """
    Convierte grados decimales a grados, minutos y segundos.
    """
    _validar_numero_finito(grados)
    signo = -1 if grados < 0 else 1
    valor_absoluto = abs(grados)
    grados_enteros = int(valor_absoluto)
    resto = (valor_absoluto - grados_enteros) * 60
    minutos = int(resto)
    segundos = (resto - minutos) * 60
    return (
        signo * grados_enteros,
        signo * minutos,
        signo * segundos,
    )
