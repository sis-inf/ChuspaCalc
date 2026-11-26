import math
from numbers import Real

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

UNIDADES_VALIDAS: frozenset[str] = frozenset({"grados", "radianes", "gradianes"})


def _validar_numero_finito(valor: float) -> float:
    """Valida que el valor sea un número real finito (sin booleanos)."""
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(f"El valor debe ser un número finito: {valor!r}")

    try:
        es_finito = math.isfinite(valor)
    except OverflowError as error:
        raise ErrorValidacion(
            "El valor debe ser un número finito: es demasiado grande"
        ) from error

    if not es_finito:
        raise ErrorValidacion(f"El valor debe ser un número finito: {valor}")

    return valor


def _validar_resultado(resultado: float) -> float:
    """Valida que el resultado de la conversión sea finito."""
    if not math.isfinite(resultado):
        raise ErrorValidacion(
            f"El resultado de la conversión no es finito: {resultado}"
        )
    return resultado


def _validar_unidad(unidad: str, nombre: str) -> str:
    """Valida que la unidad sea texto y esté entre las unidades permitidas."""
    if not isinstance(unidad, str):
        raise ErrorValidacion(f"La unidad de {nombre} debe ser texto: {unidad!r}")

    unidad_normalizada = unidad.strip().lower()
    if unidad_normalizada not in UNIDADES_VALIDAS:
        raise ErrorValidacion(f"Unidad de {nombre} inválida: {unidad}")

    return unidad_normalizada


def convertir_angulo(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    Convierte ángulos entre grados, radianes y gradianes.

    Args:
        valor (float): Valor a convertir.
        unidad_origen (str): Unidad origen (grados, radianes o gradianes).
        unidad_destino (str): Unidad destino (grados, radianes o gradianes).

    Returns:
        float: Valor convertido a la unidad destino.

    Raises:
        ErrorValidacion: Si el valor no es un número finito, si alguna unidad
            no es texto o no es válida, o si el resultado no es finito.
    """
    _validar_numero_finito(valor)

    unidad_origen = _validar_unidad(unidad_origen, "origen")
    unidad_destino = _validar_unidad(unidad_destino, "destino")

    if unidad_origen == unidad_destino:
        return valor

    # Convertir a grados primero
    if unidad_origen == "grados":
        grados = valor

    elif unidad_origen == "radianes":
        grados = math.degrees(valor)

    else:  # gradianes
        grados = valor * 0.9

    _validar_resultado(grados)

    # Convertir desde grados al destino
    if unidad_destino == "grados":
        return grados

    if unidad_destino == "radianes":
        return _validar_resultado(math.radians(grados))

    return _validar_resultado(grados / 0.9)


def grados_a_radianes(grados: float) -> float:
    """
    Convierte grados a radianes.

    Raises:
        ErrorValidacion: Si el valor no es un número finito.
    """
    _validar_numero_finito(grados)
    return math.radians(grados)


def radianes_a_grados(rad: float) -> float:
    """
    Convierte radianes a grados.

    Raises:
        ErrorValidacion: Si el valor no es un número finito o el resultado
            no es finito.
    """
    _validar_numero_finito(rad)
    return _validar_resultado(math.degrees(rad))


def grados_a_dms(grados: float) -> tuple[int, int, float]:
    """
    Convierte grados decimales a grados, minutos y segundos.

    Raises:
        ErrorValidacion: Si el valor no es un número finito.
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
