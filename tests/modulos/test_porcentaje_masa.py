import math

import pytest

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.quimica.porcentaje_masa import calcular_porcentaje_masa


def test_porcentaje_masa_conserva_formula_publica():
    assert calcular_porcentaje_masa(25, 100) == pytest.approx(25.0)
    assert calcular_porcentaje_masa(1.5, 4.0) == pytest.approx(37.5)


@pytest.mark.parametrize("valor", [True, "1", None, complex(1, 0)])
def test_porcentaje_masa_rechaza_tipos_no_admitidos(valor):
    with pytest.raises(ErrorValidacion, match="valores numéricos"):
        calcular_porcentaje_masa(valor, 100)


@pytest.mark.parametrize("valor", [0, -1, math.nan, math.inf, -math.inf])
def test_porcentaje_masa_rechaza_masas_no_positivas_o_no_finitas(valor):
    with pytest.raises(ErrorValidacion):
        calcular_porcentaje_masa(1, valor)


def test_porcentaje_masa_rechaza_soluto_mayor_que_total():
    with pytest.raises(ErrorValidacion, match="no puede superar"):
        calcular_porcentaje_masa(101, 100)


def test_error_validacion_mantiene_compatibilidad_con_value_error():
    with pytest.raises(ValueError):
        calcular_porcentaje_masa(0, 100)
