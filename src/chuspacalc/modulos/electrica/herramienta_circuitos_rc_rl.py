from chuspacalc.modulos.electrica.circuitos_rc_rl import (
    calcular_constante_tiempo_rc,
    calcular_constante_tiempo_rl,
    calcular_voltaje_carga_capacitor,
)
from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
)


def _validar_positivo(valor: float, nombre: str) -> float:
    """Valida que un parámetro sea numérico, finito y positivo."""
    numero = validar_numero(valor, nombre)

    if numero <= 0:
        raise ErrorValidacion(f"{nombre} debe ser mayor que 0.")

    return numero


def herramienta_calcular_constante_tiempo_rc(
    resistencia: float, capacitancia: float
) -> float:
    """Calcula la constante de tiempo de un circuito RC.

    Args:
        resistencia: Resistencia eléctrica en ohmios.
        capacitancia: Capacitancia en faradios.

    Returns:
        Constante de tiempo en segundos.

    Raises:
        ErrorValidacion: Si los parámetros son inválidos o el resultado
            no es finito.
    """
    resistencia = _validar_positivo(resistencia, "La resistencia")
    capacitancia = _validar_positivo(capacitancia, "La capacitancia")

    return calcular_constante_tiempo_rc(resistencia, capacitancia)


def herramienta_calcular_constante_tiempo_rl(
    resistencia: float, inductancia: float
) -> float:
    """Calcula la constante de tiempo de un circuito RL.

    Args:
        resistencia: Resistencia eléctrica en ohmios.
        inductancia: Inductancia en henrios.

    Returns:
        Constante de tiempo en segundos.

    Raises:
        ErrorValidacion: Si los parámetros son inválidos o el resultado
            no es finito.
    """
    resistencia = _validar_positivo(resistencia, "La resistencia")
    inductancia = _validar_positivo(inductancia, "La inductancia")

    return calcular_constante_tiempo_rl(resistencia, inductancia)


def herramienta_calcular_voltaje_carga_capacitor(
    voltaje_fuente: float, tiempo: float, constante_tiempo: float
) -> float:
    """Calcula el voltaje de carga de un capacitor en un circuito RC.

    Args:
        voltaje_fuente: Voltaje de la fuente.
        tiempo: Tiempo transcurrido en segundos.
        constante_tiempo: Constante de tiempo del circuito en segundos.

    Returns:
        Voltaje del capacitor.

    Raises:
        ErrorValidacion: Si los parámetros son inválidos o el resultado
            no es finito.
    """
    voltaje_fuente = validar_numero(voltaje_fuente, "El voltaje de la fuente")
    tiempo = validar_numero(tiempo, "El tiempo")
    constante_tiempo = _validar_positivo(constante_tiempo, "La constante de tiempo")

    if tiempo < 0:
        raise ErrorValidacion("El tiempo no puede ser negativo.")

    return calcular_voltaje_carga_capacitor(voltaje_fuente, tiempo, constante_tiempo)
