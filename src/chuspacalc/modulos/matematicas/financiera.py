"""
Funciones de matemática financiera básica.
"""


import math
from numbers import Real


def calcular_valor_futuro(valor_presente: float, tasa: float, periodos: int) -> float:
    """
    Calcula el valor futuro usando interés compuesto.

    VF = VP * (1 + i) ** n
    """
    _validar_parametros(valor_presente, tasa, periodos)
    return valor_presente * (1 + tasa) ** periodos


def calcular_valor_presente(valor_futuro: float, tasa: float, periodos: int) -> float:
    """
    Calcula el valor presente.

    VP = VF / (1 + i) ** n
    """
    _validar_parametros(valor_futuro, tasa, periodos)
    return valor_futuro / (1 + tasa) ** periodos


def calcular_interes_compuesto(capital: float, tasa: float, periodos: int) -> float:
    """
    Calcula únicamente el interés ganado.

    I = VF - Capital
    """
    _validar_parametros(capital, tasa, periodos)
    valor_futuro = calcular_valor_futuro(capital, tasa, periodos)
    return valor_futuro - capital


def _validar_parametros(capital: float, tasa: float, periodos: int) -> None:
    """Valida capital, tasa y periodos de las operaciones financieras."""
    for nombre, valor in (("capital", capital), ("tasa", tasa)):
        if isinstance(valor, bool) or not isinstance(valor, Real):
            raise ValueError(f"{nombre} debe ser un numero real finito")

        if not isinstance(valor, int) and not math.isfinite(valor):
            raise ValueError(f"{nombre} debe ser un numero real finito")

        if valor < 0:
            raise ValueError(f"{nombre} debe ser mayor o igual que 0")

    if isinstance(periodos, bool) or not isinstance(periodos, int):
        raise ValueError("periodos debe ser un entero positivo")

    if periodos <= 0:
        raise ValueError("periodos debe ser mayor que 0")


def calcular_interes_simple(capital: float, tasa: float, periodos: int) -> float:
    """
    Calcula el interés simple.

    I = Capital * i * n

    Raises:
        ValueError: Si capital < 0, tasa < 0 o periodos <= 0.
    """
    _validar_parametros(capital, tasa, periodos)
    return capital * tasa * periodos


def calcular_cuota_prestamo(capital: float, tasa: float, periodos: int) -> float:
    """
    Calcula la cuota nivelada de un préstamo (sistema francés).

    C = Capital * (i * (1 + i) ** n) / ((1 + i) ** n - 1)

    Con tasa 0 la fórmula no está definida (división entre cero), por lo que
    la cuota es Capital / n.

    Raises:
        ValueError: Si capital < 0, tasa < 0 o periodos <= 0.
    """
    _validar_parametros(capital, tasa, periodos)

    if tasa == 0:
        return capital / periodos

    factor = (1 + tasa) ** periodos
    return capital * (tasa * factor) / (factor - 1)
