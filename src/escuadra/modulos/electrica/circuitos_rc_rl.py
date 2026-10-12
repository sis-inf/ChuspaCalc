import math


def calcular_constante_tiempo_rc(resistencia: float, capacitancia: float) -> float:
    if resistencia <= 0:
        raise ValueError("La resistencia debe ser mayor que 0")
    if capacitancia <= 0:
        raise ValueError("La capacitancia debe ser mayor que 0")
    return resistencia * capacitancia


def calcular_constante_tiempo_rl(resistencia: float, inductancia: float) -> float:
    if resistencia <= 0:
        raise ValueError("La resistencia debe ser mayor que 0")
    if inductancia <= 0:
        raise ValueError("La inductancia debe ser mayor que 0")
    return inductancia / resistencia


def calcular_voltaje_carga_capacitor(
    voltaje_fuente: float, tiempo: float, constante_tiempo: float
) -> float:
    if constante_tiempo <= 0:
        raise ValueError("La constante de tiempo debe ser mayor que 0")
    if tiempo < 0:
        raise ValueError("El tiempo no puede ser negativo")

    return voltaje_fuente * (1 - math.exp(-tiempo / constante_tiempo))
