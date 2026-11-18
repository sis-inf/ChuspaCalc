"""
Tests unitarios para las funciones del módulo diseno_vial, verificando
el cálculo de pendiente y de peralte de curva, así como el manejo de
valores no válidos.
"""

import pytest

from chuspacalc.modulos.civil.diseno_vial import (
    ErrorDisenoVial,
    calcular_pendiente,
    calcular_peralte_curva,
)


def test_calcular_pendiente_positiva():
    assert calcular_pendiente(100, 105, 100) == 5.0


def test_calcular_pendiente_negativa():
    assert calcular_pendiente(105, 100, 100) == -5.0


def test_calcular_pendiente_con_distancia_cero_lanza_error():
    with pytest.raises(ErrorDisenoVial):
        calcular_pendiente(0, 1, 0)


def test_calcular_peralte_curva_valor_aproximado():
    assert calcular_peralte_curva(60, 100) == pytest.approx(0.134, abs=1e-3)


def test_calcular_peralte_curva_con_radio_cero_lanza_error():
    with pytest.raises(ErrorDisenoVial):
        calcular_peralte_curva(60, 0)


def test_calcular_peralte_curva_con_velocidad_cero_lanza_error():
    with pytest.raises(ErrorDisenoVial):
        calcular_peralte_curva(0, 100)
