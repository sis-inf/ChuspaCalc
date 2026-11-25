import math

import pytest

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.matematicas.numeros_complejos import (
    ErrorDivisionPorCero,
    conjugado,
    dividir,
    modulo,
    multiplicar,
    polar_a_rectangular,
    rectangular_a_polar,
    restar,
    sumar,
)

BINARIAS = [sumar, restar, multiplicar, dividir]
UNARIAS = [modulo, conjugado, rectangular_a_polar]

TIPOS_INVALIDOS = ["1+2j", None, True, [1], (1, 2)]
NO_FINITOS = [
    math.nan,
    math.inf,
    -math.inf,
    complex(math.nan, 0),
    complex(0, math.inf),
    10**400,
]


@pytest.mark.parametrize("funcion", BINARIAS)
@pytest.mark.parametrize("invalido", TIPOS_INVALIDOS + NO_FINITOS)
def test_binarias_rechazan_operandos_invalidos(funcion, invalido):
    with pytest.raises(ErrorValidacion):
        funcion(invalido, 1 + 1j)
    with pytest.raises(ErrorValidacion):
        funcion(1 + 1j, invalido)


@pytest.mark.parametrize("funcion", UNARIAS)
@pytest.mark.parametrize("invalido", TIPOS_INVALIDOS + NO_FINITOS)
def test_unarias_rechazan_valores_invalidos(funcion, invalido):
    with pytest.raises(ErrorValidacion):
        funcion(invalido)


@pytest.mark.parametrize("divisor", [0, 0.0, 0j])
def test_dividir_entre_cero(divisor):
    with pytest.raises(ErrorValidacion, match="cero"):
        dividir(1 + 1j, divisor)


def test_dividir_entre_cero_sigue_siendo_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        dividir(1 + 0j, 0j)
    assert issubclass(ErrorDivisionPorCero, ValueError)


def test_desbordamiento_en_operaciones():
    grande = complex(1e308, 1e308)
    with pytest.raises(ErrorValidacion, match="rango"):
        sumar(grande, grande)
    with pytest.raises(ErrorValidacion, match="rango"):
        multiplicar(grande, grande)


def test_modulo_grande_pero_representable():
    # |1e308+1e308j| ~ 1.41e308 cabe en un float: no debe fallar
    assert modulo(complex(1e308, 1e308)) == pytest.approx(1.4142135623730951e308)


@pytest.mark.parametrize("invalido", ["2", None, True, math.nan, math.inf, 10**400])
def test_polar_a_rectangular_modulo_invalido(invalido):
    with pytest.raises(ErrorValidacion, match="módulo"):
        polar_a_rectangular(invalido, 0)


@pytest.mark.parametrize("invalido", ["0", None, True, math.nan, math.inf, 10**400])
def test_polar_a_rectangular_angulo_invalido(invalido):
    with pytest.raises(ErrorValidacion, match="ángulo"):
        polar_a_rectangular(1, invalido)


def test_polar_a_rectangular_modulo_negativo():
    with pytest.raises(ErrorValidacion):
        polar_a_rectangular(-1, 0)


def test_resultados_validos_no_cambian():
    assert sumar(1 + 2j, 3 + 4j) == 4 + 6j
    assert restar(3 + 4j, 1 + 2j) == 2 + 2j
    assert multiplicar(1 + 2j, 3 + 4j) == -5 + 10j
    assert dividir(4 + 2j, 2) == 2 + 1j
    assert modulo(3 + 4j) == 5.0
    assert conjugado(3 + 4j) == 3 - 4j
    assert rectangular_a_polar(1j) == pytest.approx((1.0, math.pi / 2))
    assert polar_a_rectangular(2, 0) == 2 + 0j
