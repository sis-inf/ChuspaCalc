"""
Funciones de matemática financiera básica.
"""

import math
from numbers import Real

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

_MSG_RANGO = "el resultado excede el rango representable"


def _validar_real_finito(nombre: str, valor: object) -> None:
    """Valida que valor sea un número real finito (no bool, NaN ni infinito)."""
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(f"{nombre} debe ser un numero real finito")

    try:
        es_finito = math.isfinite(valor)
    except OverflowError:  # enteros demasiado grandes para float
        es_finito = False

    if not es_finito:
        raise ErrorValidacion(f"{nombre} debe ser un numero real finito")


def _validar_parametros(capital: float, tasa: float, periodos: int) -> None:
    """Valida capital, tasa y periodos de las operaciones financieras.

    Raises:
        ErrorValidacion: Si capital o tasa no son reales finitos o son negativos,
            o si periodos no es un entero mayor que 0.
    """
    for nombre, valor in (("capital", capital), ("tasa", tasa)):
        _validar_real_finito(nombre, valor)

        if valor < 0:
            raise ErrorValidacion(f"{nombre} debe ser mayor o igual que 0")

    if isinstance(periodos, bool) or not isinstance(periodos, int):
        raise ErrorValidacion("periodos debe ser un entero positivo")

    if periodos <= 0:
        raise ErrorValidacion("periodos debe ser mayor que 0")


def _resultado_finito(valor: float) -> float:
    """Devuelve el resultado como float verificando que sea finito."""
    try:
        resultado = float(valor)
    except OverflowError as exc:
        raise ErrorValidacion(_MSG_RANGO) from exc

    if not math.isfinite(resultado):
        raise ErrorValidacion(_MSG_RANGO)
    return resultado


def _factor_capitalizacion(tasa: float, periodos: int) -> float:
    """Calcula (1 + tasa) ** periodos controlando el desbordamiento."""
    try:
        factor = (1.0 + float(tasa)) ** periodos
    except OverflowError as exc:
        raise ErrorValidacion(_MSG_RANGO) from exc

    return _resultado_finito(factor)


def calcular_valor_futuro(valor_presente: float, tasa: float, periodos: int) -> float:
    """
    Calcula el valor futuro usando interés compuesto.

    VF = VP * (1 + i) ** n

    Raises:
        ErrorValidacion: Si los parámetros son inválidos o el resultado
            excede el rango representable.
    """
    _validar_parametros(valor_presente, tasa, periodos)
    factor = _factor_capitalizacion(tasa, periodos)
    return _resultado_finito(valor_presente * factor)


def calcular_valor_presente(valor_futuro: float, tasa: float, periodos: int) -> float:
    """
    Calcula el valor presente.

    VP = VF / (1 + i) ** n

    Raises:
        ErrorValidacion: Si los parámetros son inválidos o el resultado
            excede el rango representable.
    """
    _validar_parametros(valor_futuro, tasa, periodos)
    factor = _factor_capitalizacion(tasa, periodos)
    return _resultado_finito(valor_futuro / factor)


def calcular_interes_compuesto(capital: float, tasa: float, periodos: int) -> float:
    """
    Calcula únicamente el interés ganado.

    I = VF - Capital

    Raises:
        ErrorValidacion: Si los parámetros son inválidos o el resultado
            excede el rango representable.
    """
    _validar_parametros(capital, tasa, periodos)
    valor_futuro = calcular_valor_futuro(capital, tasa, periodos)
    return _resultado_finito(valor_futuro - capital)


def calcular_interes_simple(capital: float, tasa: float, periodos: int) -> float:
    """
    Calcula el interés simple.

    I = Capital * i * n

    Raises:
        ErrorValidacion: Si capital < 0, tasa < 0, periodos <= 0, algún valor
            no es un real finito o el resultado excede el rango representable.
    """
    _validar_parametros(capital, tasa, periodos)
    return _resultado_finito(capital * tasa * periodos)


def calcular_cuota_prestamo(capital: float, tasa: float, periodos: int) -> float:
    """
    Calcula la cuota nivelada de un préstamo (sistema francés).

    C = Capital * (i * (1 + i) ** n) / ((1 + i) ** n - 1)

    Con tasa 0 la fórmula no está definida (división entre cero), por lo que
    la cuota es Capital / n. Lo mismo se aplica si la tasa es tan pequeña que
    (1 + i) ** n es indistinguible de 1 en punto flotante.

    Raises:
        ErrorValidacion: Si capital < 0, tasa < 0, periodos <= 0, algún valor
            no es un real finito o el resultado excede el rango representable.
    """
    _validar_parametros(capital, tasa, periodos)

    factor = _factor_capitalizacion(tasa, periodos)

    if tasa == 0 or factor == 1.0:
        return _resultado_finito(capital / periodos)

    return _resultado_finito(capital * (tasa * factor) / (factor - 1))