import pytest

from chuspacalc.modulos.civil.diseno_vial import (
    ErrorDisenoVial,
    calcular_pendiente,
    calcular_peralte_curva,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

INVALIDOS = [float("nan"), float("inf"), float("-inf"), True, "5", None]


def test_error_diseno_vial_es_error_validacion():
    assert issubclass(ErrorDisenoVial, ErrorValidacion)


@pytest.mark.parametrize("valor", INVALIDOS)
def test_pendiente_rechaza_valores_invalidos(valor):
    with pytest.raises(ErrorValidacion):
        calcular_pendiente(valor, 105, 100)
    with pytest.raises(ErrorValidacion):
        calcular_pendiente(100, valor, 100)
    with pytest.raises(ErrorValidacion):
        calcular_pendiente(100, 105, valor)


@pytest.mark.parametrize("valor", INVALIDOS)
def test_peralte_rechaza_valores_invalidos(valor):
    with pytest.raises(ErrorValidacion):
        calcular_peralte_curva(valor, 100)
    with pytest.raises(ErrorValidacion):
        calcular_peralte_curva(60, valor)
    with pytest.raises(ErrorValidacion):
        calcular_peralte_curva(60, 100, valor)


def test_pendiente_con_resultado_no_finito_lanza_error():
    with pytest.raises(ErrorValidacion):
        calcular_pendiente(-1e308, 1e308, 1e-300)
