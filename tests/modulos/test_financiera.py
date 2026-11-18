import pytest

from chuspacalc.modulos.matematicas.financiera import (
    calcular_interes_compuesto,
    calcular_valor_futuro,
    calcular_valor_presente,
)


def test_calcular_valor_futuro():
    resultado = calcular_valor_futuro(1000, 0.1, 2)

    assert resultado == pytest.approx(1210.0)


def test_calcular_valor_presente():
    resultado = calcular_valor_presente(1210, 0.1, 2)

    assert resultado == pytest.approx(1000.0)


def test_calcular_interes_compuesto():
    resultado = calcular_interes_compuesto(1000, 0.1, 2)

    assert resultado == pytest.approx(210.0)


def test_valor_futuro_con_periodos_cero():
    with pytest.raises(ValueError):
        calcular_valor_futuro(1000, 0.1, 0)


def test_interes_compuesto_con_tasa_cero():
    resultado = calcular_interes_compuesto(1000, 0, 2)

    assert resultado == pytest.approx(0.0)


@pytest.mark.parametrize(
    "funcion",
    [
        calcular_valor_futuro,
        calcular_valor_presente,
        calcular_interes_compuesto,
    ],
)
@pytest.mark.parametrize(
    "capital,tasa,periodos",
    [
        (-1000, 0.1, 2),
        (1000, -0.1, 2),
        (1000, float("nan"), 2),
        (1000, float("inf"), 2),
        (1000, float("-inf"), 2),
        (float("nan"), 0.1, 2),
        (float("inf"), 0.1, 2),
        (float("-inf"), 0.1, 2),
        (1000, 0.1, 0),
        (1000, 0.1, -1),
    ],
)
def test_funciones_financieras_rechazan_parametros_invalidos(
    funcion, capital, tasa, periodos
):
    with pytest.raises(ValueError):
        funcion(capital, tasa, periodos)


@pytest.mark.parametrize(
    "funcion",
    [
        calcular_valor_futuro,
        calcular_valor_presente,
        calcular_interes_compuesto,
    ],
)
def test_funciones_financieras_aceptan_capital_y_tasa_cero(funcion):
    assert funcion(0, 0, 2) == pytest.approx(0.0)
