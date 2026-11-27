import math
from numbers import Real

from ..matematicas.error_validacion import ErrorValidacion


def _validar_dimension(valor: object, nombre: str) -> None:
    """Verifica que una dimension sea real y finita."""
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(f"{nombre} debe ser un numero real finito")

    try:
        es_finito = math.isfinite(valor)
    except OverflowError as error:
        raise ErrorValidacion(f"{nombre} excede el rango numerico permitido") from error

    if not es_finito:
        raise ErrorValidacion(f"{nombre} debe ser un numero real finito")


def volumen_cubo(lado: int | float) -> float:
    """Volumen de un cubo: lado³"""
    _validar_dimension(lado, "lado")

    if lado <= 0:
        raise ErrorValidacion("La dimensión debe ser mayor que 0")

    try:
        resultado = float(lado**3)
    except OverflowError as error:
        raise ErrorValidacion("El volumen excede el rango numérico") from error

    if not math.isfinite(resultado):
        raise ErrorValidacion("El volumen calculado debe ser finito")

    return resultado


def volumen_esfera(radio: int | float) -> float:
    """Volumen de una esfera: (4/3)πr³"""
    _validar_dimension(radio, "radio")

    if radio <= 0:
        raise ErrorValidacion("La dimensión debe ser mayor que 0")

    try:
        resultado = float((4 / 3) * math.pi * radio**3)
    except OverflowError as error:
        raise ErrorValidacion("El volumen excede el rango numérico") from error

    if not math.isfinite(resultado):
        raise ErrorValidacion("El volumen calculado debe ser finito")

    return resultado


def volumen_cilindro(radio: int | float, altura: int | float) -> float:
    """Volumen de un cilindro: πr²h"""
    _validar_dimension(radio, "radio")
    _validar_dimension(altura, "altura")

    if radio <= 0 or altura <= 0:
        raise ErrorValidacion("Las dimensiones deben ser mayores que 0")

    try:
        resultado = float(math.pi * radio**2 * altura)
    except OverflowError as error:
        raise ErrorValidacion("El volumen excede el rango numérico") from error

    if not math.isfinite(resultado):
        raise ErrorValidacion("El volumen calculado debe ser finito")

    return resultado


def volumen_cono(radio: int | float, altura: int | float) -> float:
    """Volumen de un cono: (1/3)πr²h"""
    _validar_dimension(radio, "radio")
    _validar_dimension(altura, "altura")

    if radio <= 0 or altura <= 0:
        raise ErrorValidacion("Las dimensiones deben ser mayores que 0")

    try:
        resultado = float((1 / 3) * math.pi * radio**2 * altura)
    except OverflowError as error:
        raise ErrorValidacion("El volumen excede el rango numérico") from error

    if not math.isfinite(resultado):
        raise ErrorValidacion("El volumen calculado debe ser finito")

    return resultado


def volumen_paralelepipedo(
    largo: int | float,
    ancho: int | float,
    alto: int | float,
) -> float:
    """Volumen de un paralelepípedo: largo × ancho × alto"""
    _validar_dimension(largo, "largo")
    _validar_dimension(ancho, "ancho")
    _validar_dimension(alto, "alto")

    if largo <= 0 or ancho <= 0 or alto <= 0:
        raise ErrorValidacion("Las dimensiones deben ser mayores que 0")

    try:
        resultado = float(largo * ancho * alto)
    except OverflowError as error:
        raise ErrorValidacion("El volumen excede el rango numérico") from error

    if not math.isfinite(resultado):
        raise ErrorValidacion("El volumen calculado debe ser finito")

    return resultado
