import math
from numbers import Real


def _validar_finito(valor: Real, nombre: str) -> None:
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ValueError(f"{nombre} debe ser un numero real finito")

    if isinstance(valor, int):
        return

    if not math.isfinite(valor):
        raise ValueError(f"{nombre} debe ser un numero real finito")


def calcular_constante_tiempo_rc(resistencia: float, capacitancia: float) -> float:
    _validar_finito(resistencia, "La resistencia")
    _validar_finito(capacitancia, "La capacitancia")

    if resistencia <= 0:
        raise ValueError("La resistencia debe ser mayor que 0")
    if capacitancia <= 0:
        raise ValueError("La capacitancia debe ser mayor que 0")

    return resistencia * capacitancia


def calcular_constante_tiempo_rl(resistencia: float, inductancia: float) -> float:
    _validar_finito(resistencia, "La resistencia")
    _validar_finito(inductancia, "La inductancia")

    if resistencia <= 0:
        raise ValueError("La resistencia debe ser mayor que 0")
    if inductancia <= 0:
        raise ValueError("La inductancia debe ser mayor que 0")

    return inductancia / resistencia


def calcular_voltaje_carga_capacitor(
    voltaje_fuente: float,
    tiempo: float,
    constante_tiempo: float
) -> float:
    _validar_finito(voltaje_fuente, "El voltaje")
    _validar_finito(tiempo, "El tiempo")
    _validar_finito(constante_tiempo, "La constante de tiempo")

    if constante_tiempo <= 0:
        raise ValueError("La constante de tiempo debe ser mayor que 0")
    if tiempo < 0:
        raise ValueError("El tiempo no puede ser negativo")

    return voltaje_fuente * (1 - math.exp(-tiempo / constante_tiempo))


def analisis_transitorio(
    tipo: str,
    resistencia: float,
    componente: float,
    tension: float
) -> dict:
    """
    Calcula la constante de tiempo y la energía almacenada de un circuito RC o RL.

    Para un circuito RC (componente = capacitancia en F):
        tau = R * C
        energia = 0.5 * C * V^2

    Para un circuito RL (componente = inductancia en H):
        tau = L / R
        energia = 0.5 * L * I^2, con I = V / R (corriente en estado estacionario)

    Returns:
        Diccionario con ``tau`` (s), ``energia_joules`` (J) y
        ``tiempo_estable`` (5 * tau, en s).

    Raises:
        ValueError: Si ``tipo`` no es 'RC' ni 'RL', o si ``resistencia`` o
            ``componente`` no son mayores que 0.
    """
    if tipo not in ("RC", "RL"):
        raise ValueError("El tipo de circuito debe ser 'RC' o 'RL'")

    _validar_finito(tension, "La tension")

    if tipo == "RC":
        tau = calcular_constante_tiempo_rc(resistencia, componente)
        energia = 0.5 * componente * tension ** 2
    else:
        tau = calcular_constante_tiempo_rl(resistencia, componente)
        corriente = tension / resistencia
        energia = 0.5 * componente * corriente ** 2

    return {
        "tau": tau,
        "energia_joules": energia,
        "tiempo_estable": 5 * tau,
    }
