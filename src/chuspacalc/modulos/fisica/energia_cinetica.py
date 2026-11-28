import math

from ..matematicas.error_validacion import ErrorValidacion, validar_numero


def calcular_energia_cinetica(masa: int | float, velocidad: int | float) -> float:
    """
    Calcula la energia cinetica de un cuerpo.

    Args:
        masa: Masa del cuerpo en kilogramos. Debe ser un numero finito positivo.
        velocidad: Velocidad del cuerpo en metros por segundo. Debe ser un
            numero finito.

    Returns:
        Energia cinetica en joules.

    Raises:
        ErrorValidacion: Si la masa o la velocidad no son numericas, no son
            finitas o estan fuera del rango representable; si la masa no es
            positiva; o si el resultado no es finito.
    """
    masa_kg = validar_numero(masa, "masa")
    velocidad_ms = validar_numero(velocidad, "velocidad")

    if masa_kg <= 0:
        raise ErrorValidacion("La masa debe ser un numero positivo.")

    try:
        energia = (masa_kg * velocidad_ms**2) / 2
    except OverflowError as exc:
        raise ErrorValidacion("El resultado esta fuera del rango permitido.") from exc

    if not math.isfinite(energia):
        raise ErrorValidacion("El resultado debe ser finito.")

    return energia
