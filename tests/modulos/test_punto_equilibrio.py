import pytest

from chuspacalc.modulos.investigacion_operativa.punto_equilibrio import (
    calcular_punto_equilibrio,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def test_calcula_punto_equilibrio_valido():
    assert calcular_punto_equilibrio(1000, 50, 30) == pytest.approx(50.0)


def test_costos_fijos_cero_da_cero():
    assert calcular_punto_equilibrio(0, 50, 30) == pytest.approx(0.0)


def test_acepta_decimales():
    assert calcular_punto_equilibrio(100.5, 10.5, 5.5) == pytest.approx(20.1)


@pytest.mark.parametrize("valor", [True, False, "1", None, [1]])
def test_rechaza_tipos_invalidos(valor):
    with pytest.raises(ErrorValidacion):
        calcular_punto_equilibrio(valor, 50, 30)
    with pytest.raises(ErrorValidacion):
        calcular_punto_equilibrio(1000, valor, 30)
    with pytest.raises(ErrorValidacion):
        calcular_punto_equilibrio(1000, 50, valor)


@pytest.mark.parametrize("valor", [float("nan"), float("inf"), float("-inf")])
def test_rechaza_no_finitos(valor):
    with pytest.raises(ErrorValidacion):
        calcular_punto_equilibrio(valor, 50, 30)
    with pytest.raises(ErrorValidacion):
        calcular_punto_equilibrio(1000, valor, 30)
    with pytest.raises(ErrorValidacion):
        calcular_punto_equilibrio(1000, 50, valor)


def test_rechaza_entero_demasiado_grande():
    with pytest.raises(ErrorValidacion):
        calcular_punto_equilibrio(10**400, 50, 30)


def test_rechaza_costos_fijos_negativos():
    with pytest.raises(ErrorValidacion, match="costos_fijos"):
        calcular_punto_equilibrio(-1, 50, 30)


@pytest.mark.parametrize("precio, variable", [(30, 30), (20, 30)])
def test_rechaza_margen_cero_o_negativo(precio, variable):
    with pytest.raises(ErrorValidacion, match="mayor que el costo variable"):
        calcular_punto_equilibrio(1000, precio, variable)


def test_rechaza_margen_desbordado():
    with pytest.raises(ErrorValidacion, match="margen"):
        calcular_punto_equilibrio(1000, 1.7e308, -1.7e308)


def test_rechaza_resultado_desbordado():
    with pytest.raises(ErrorValidacion, match="no es finito"):
        calcular_punto_equilibrio(1.7e308, 1, 0.9999999999999999)
