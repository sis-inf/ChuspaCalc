"""Cálculo de resistencia equivalente en serie y paralelo."""

import math


def _validar_finitos(valores, nombre):
    """Rechaza NaN e infinitos indicando la posición del valor inválido."""
    for posicion, valor in enumerate(valores, start=1):
        if not math.isfinite(valor):
            mensaje = f"{nombre} {posicion} debe ser finita, se recibió: {valor}"
            raise ValueError(mensaje)


def _normalizar_resistencias(resistencias):
    """Acepta ``f(r1, r2, ...)`` o ``f([r1, r2, ...])`` y valida los valores."""
    if len(resistencias) == 1 and isinstance(resistencias[0], (list, tuple)):
        resistencias = tuple(resistencias[0])

    if len(resistencias) < 2:
        raise ValueError("Se requieren al menos 2 resistencias")

    _validar_finitos(resistencias, "La resistencia")

    if any(r <= 0 for r in resistencias):
        raise ValueError("Todas las resistencias deben ser mayores que 0")

    return resistencias


def resistencia_serie(*resistencias):
    """
    Calcula la resistencia equivalente en serie.

    Fórmula:
        R_eq = R1 + R2 + ... + Rn
    """
    resistencias = _normalizar_resistencias(resistencias)
    return float(sum(resistencias))


def resistencia_paralelo(*resistencias):
    """
    Calcula la resistencia equivalente en paralelo.

    Fórmula:
        1 / R_eq = 1/R1 + 1/R2 + ... + 1/Rn
    """
    resistencias = _normalizar_resistencias(resistencias)
    suma_inversas = sum(1 / r for r in resistencias)

    return float(1 / suma_inversas)


def capacitancia_paralelo(*capacitancias):
    """
    Calcula la capacitancia equivalente en paralelo.

    Fórmula:
        C_eq = C1 + C2 + ... + Cn
    """
    if len(capacitancias) < 2:
        raise ValueError("Se requieren al menos 2 capacitancias")

    _validar_finitos(capacitancias, "La capacitancia")

    if any(c <= 0 for c in capacitancias):
        raise ValueError("Todas las capacitancias deben ser mayores que 0")

    return float(sum(capacitancias))


def capacitancia_serie(*capacitancias):
    """
    Calcula la capacitancia equivalente en serie.

    Fórmula:
        1 / C_eq = 1/C1 + 1/C2 + ... + 1/Cn
    """
    if len(capacitancias) < 2:
        raise ValueError("Se requieren al menos 2 capacitancias")

    _validar_finitos(capacitancias, "La capacitancia")

    if any(c <= 0 for c in capacitancias):
        raise ValueError("Todas las capacitancias deben ser mayores que 0")

    return float(1.0 / sum(1.0 / c for c in capacitancias))
