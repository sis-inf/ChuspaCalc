import math

import pytest

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.matematicas.financiera import (
    calcular_cuota_prestamo,
    calcular_interes_compuesto,
    calcular_interes_simple,
    calcular_valor_futuro,
    calcular_valor_presente,
)

FUNCIONES = [
    calcular_valor_futuro,
    calcular_valor_presente,
    calcular_interes_compuesto,
    calcular_interes_simple,
    calcular_cuota_prestamo,
]


@pytest.mark.parametrize("funcion", FUNCIONES)
@pytest.mark.parametrize("invalido", ["100", None, True, [1], 1 + 2j])
def test_capital_tipo_invalido(funcion, invalido):
    with pytest.raises(ErrorValidacion, match="capital"):
        funcion(invalido, 0.05, 12)


@pytest.mark.parametrize("funcion", FUNCIONES)
@pytest.mark.parametrize("invalido", ["0.05", None, False])
def test_tasa_tipo_invalido(funcion, invalido):
    with pytest.raises(ErrorValidacion, match="tasa"):
        funcion(1000.0, invalido, 12)


@pytest.mark.parametrize("funcion", FUNCIONES)
@pytest.mark.parametrize("invalido", [math.nan, math.inf, -math.inf, 10**400])
def test_capital_no_finito(funcion, invalido):
    with pytest.raises(ErrorValidacion, match="capital"):
        funcion(invalido, 0.05, 12)


@pytest.mark.parametrize("funcion", FUNCIONES)
@pytest.mark.parametrize("invalido", [math.nan, math.inf, -math.inf])
def test_tasa_no_finita(funcion, invalido):
    with pytest.raises(ErrorValidacion, match="tasa"):
        funcion(1000.0, invalido, 12)


@pytest.mark.parametrize("funcion", FUNCIONES)
def test_valores_negativos(funcion):
    with pytest.raises(ErrorValidacion, match="capital"):
        funcion(-1.0, 0.05, 12)
    with pytest.raises(ErrorValidacion, match="tasa"):
        funcion(1000.0, -0.01, 12)


@pytest.mark.parametrize("funcion", FUNCIONES)
@pytest.mark.parametrize("invalido", [0, -3, 2.5, "12", None, True])
def test_periodos_invalidos(funcion, invalido):
    with pytest.raises(ErrorValidacion, match="periodos"):
        funcion(1000.0, 0.05, invalido)


@pytest.mark.parametrize(
    "funcion", [calcular_valor_futuro, calcular_valor_presente, calcular_interes_compuesto]
)
def test_desbordamiento_lanza_error_validacion(funcion):
    with pytest.raises(ErrorValidacion, match="rango"):
        funcion(1000.0, 1e10, 1000)


def test_cuota_con_tasa_diminuta_no_divide_por_cero():
    # 1 + 1e-20 == 1.0 en punto flotante: antes lanzaba ZeroDivisionError
    assert calcular_cuota_prestamo(1200.0, 1e-20, 12) == pytest.approx(100.0)


def test_cuota_con_tasa_cero():
    assert calcular_cuota_prestamo(1200.0, 0, 12) == pytest.approx(100.0)


def test_errores_siguen_siendo_value_error():
    with pytest.raises(ValueError):
        calcular_valor_futuro(-1.0, 0.05, 12)


def test_resultados_validos_no_cambian():
    assert calcular_valor_futuro(1000.0, 0.1, 2) == pytest.approx(1210.0)
    assert calcular_valor_presente(1210.0, 0.1, 2) == pytest.approx(1000.0)
    assert calcular_interes_compuesto(1000.0, 0.1, 2) == pytest.approx(210.0)
    assert calcular_interes_simple(1000.0, 0.1, 2) == pytest.approx(200.0)
    assert calcular_cuota_prestamo(1000.0, 0.1, 2) == pytest.approx(576.19, abs=0.01)