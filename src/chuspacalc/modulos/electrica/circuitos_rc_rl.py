import math

from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
)


def _validar_resultado(valor: float, nombre: str) -> float:
    """Comprueba que un resultado calculado sea un número finito."""
    if not math.isfinite(valor):
        raise ErrorValidacion(
            f"El resultado de {nombre} debe ser un número real finito"
        )

    return valor


def calcular_constante_tiempo_rc(resistencia: float, capacitancia: float) -> float:
    """
    Calcula la constante de tiempo de un circuito RC.

    Args:
        resistencia: Resistencia en ohmios.
        capacitancia: Capacitancia en faradios.

    Returns:
        Constante de tiempo en segundos.

    Raises:
        ErrorValidacion: Si los parámetros no son válidos o el resultado
            no es finito.
    """

    resistencia = validar_numero(resistencia, "La resistencia")
    capacitancia = validar_numero(capacitancia, "La capacitancia")

    if resistencia <= 0:
        raise ErrorValidacion("La resistencia debe ser mayor que 0")
    if capacitancia <= 0:
        raise ErrorValidacion("La capacitancia debe ser mayor que 0")

    resultado = resistencia * capacitancia

    return _validar_resultado(resultado, "la constante de tiempo RC")


def calcular_constante_tiempo_rl(resistencia: float, inductancia: float) -> float:
    """
    Calcula la constante de tiempo de un circuito RL.

    Args:
        resistencia: Resistencia en ohmios.
        inductancia: Inductancia en henrios.

    Returns:
        Constante de tiempo en segundos.

    Raises:
        ErrorValidacion: Si los parámetros no son válidos o el resultado
            no es finito.
    """
    resistencia = validar_numero(resistencia, "La resistencia")
    inductancia = validar_numero(inductancia, "La inductancia")

    if resistencia <= 0:
        raise ErrorValidacion("La resistencia debe ser mayor que 0")
    if inductancia <= 0:
        raise ErrorValidacion("La inductancia debe ser mayor que 0")
    resultado = inductancia / resistencia
    return _validar_resultado(resultado, "la constante de tiempo RL")


def calcular_voltaje_carga_capacitor(
    voltaje_fuente: float, tiempo: float, constante_tiempo: float
) -> float:
    """
    Calcula el voltaje de carga de un capacitor en un circuito RC.

    Args:
        voltaje_fuente: Voltaje de la fuente.
        tiempo: Tiempo transcurrido en segundos.
        constante_tiempo: Constante de tiempo del circuito en segundos.

    Returns:
        Voltaje del capacitor.

    Raises:
        ErrorValidacion: Si los parámetros no son válidos o el resultado
            no es finito.
    """
    voltaje_fuente = validar_numero(voltaje_fuente, "El voltaje de la fuente")
    tiempo = validar_numero(tiempo, "El tiempo")
    constante_tiempo = validar_numero(
        constante_tiempo,
        "La constante de tiempo",
    )

    if constante_tiempo <= 0:
        raise ErrorValidacion("La constante de tiempo debe ser mayor que 0")
    if tiempo < 0:
        raise ErrorValidacion("El tiempo no puede ser negativo")
    try:
        resultado = voltaje_fuente * (1 - math.exp(-tiempo / constante_tiempo))
    except OverflowError as error:
        raise ErrorValidacion(
            "No se pudo calcular el voltaje con los valores proporcionados"
        ) from error

    return _validar_resultado(resultado, "el voltaje de carga del capacitor")


def analisis_transitorio(
    tipo: str, resistencia: float, componente: float, tension: float
) -> dict[str, float]:
    """
    Calcula la constante de tiempo y la energía almacenada de un circuito RC o RL.

    Para un circuito RC:
        componente = capacitancia en Faradios
        tau = R * C
        energia = 0.5 * C * V^2

    Para un circuito RL:
        componente = inductancia en Henrios
        tau = L / R
        energia = 0.5 * L * I^2, con I = V / R (corriente en estado estacionario)

    Args:
        tipo: Tipo de circuito, 'RC' o 'RL'.
        resistencia: Resistencia en ohmios.
        componente: Capacitancia en faradios o inductancia en henrios.
        tension: Voltaje aplicado o tensión de alimentación.

    Returns:
        Diccionario con la constante de tiempo, la energía almacenada
        y el tiempo estimado de estabilización.

    Raises:
        ErrorValidacion: Si el tipo de circuito o alguno de los parámetros
            no es válido, o si un resultado no es finito.
    """
    if not isinstance(tipo, str) or tipo not in ("RC", "RL"):
        raise ErrorValidacion("El tipo de circuito debe ser 'RC' o 'RL'")

    resistencia = validar_numero(resistencia, "La resistencia")
    componente = validar_numero(componente, "El componente")
    tension = validar_numero(tension, "La tensión")

    if resistencia <= 0:
        raise ErrorValidacion("La resistencia debe ser mayor que 0")

    if componente <= 0:
        nombre_componente = "La capacitancia" if tipo == "RC" else "La inductancia"
        raise ErrorValidacion(f"{nombre_componente} debe ser mayor que 0")

    try:
        if tipo == "RC":
            tau = calcular_constante_tiempo_rc(resistencia, componente)
            energia = 0.5 * componente * tension * tension
        else:
            tau = calcular_constante_tiempo_rl(resistencia, componente)
            corriente = tension / resistencia
            energia = 0.5 * componente * corriente * corriente
        tiempo_estable = 5 * tau
    except OverflowError as error:
        raise ErrorValidacion(
            "No se pudo calcular la constante de tiempo o la energía con los valores proporcionados"
        ) from error

    return {
        "tau": _validar_resultado(tau, "la constante de tiempo"),
        "energia_joules": _validar_resultado(energia, "la energia almacenada"),
        "tiempo_estable": _validar_resultado(
            tiempo_estable, "el tiempo de estabilizacion"
        ),
    }
