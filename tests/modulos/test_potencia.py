"""
Pruebas unitarias para el módulo de cálculo de potencia eléctrica.
"""

import pytest

from chuspacalc.modulos.electrica.potencia import (
    potencia_ir,
    potencia_vi,
    potencia_vr,
)


def test_potencia_vi_calcula_resultado_correcto():
    assert potencia_vi(10, 2) == 20.0


def test_potencia_ir_calcula_resultado_correcto():
    assert potencia_ir(2, 5) == 20.0


def test_potencia_vr_calcula_resultado_correcto():
    assert potencia_vr(10, 5) == 20.0


def test_potencia_vi_rechaza_voltaje_cero_o_negativo():
    with pytest.raises(ValueError):
        potencia_vi(0, 2)

    with pytest.raises(ValueError):
        potencia_vi(-10, 2)


def test_potencia_vi_rechaza_corriente_cero_o_negativa():
    with pytest.raises(ValueError):
        potencia_vi(10, 0)

    with pytest.raises(ValueError):
        potencia_vi(10, -2)


def test_potencia_ir_rechaza_corriente_cero_o_negativa():
    with pytest.raises(ValueError):
        potencia_ir(0, 5)

    with pytest.raises(ValueError):
        potencia_ir(-2, 5)


def test_potencia_ir_rechaza_resistencia_cero_o_negativa():
    with pytest.raises(ValueError):
        potencia_ir(2, 0)

    with pytest.raises(ValueError):
        potencia_ir(2, -5)


def test_potencia_vr_rechaza_voltaje_cero_o_negativo():
    with pytest.raises(ValueError):
        potencia_vr(0, 5)

    with pytest.raises(ValueError):
        potencia_vr(-10, 5)


def test_potencia_vr_rechaza_resistencia_cero_o_negativa():
    with pytest.raises(ValueError):
        potencia_vr(10, 0)

    with pytest.raises(ValueError):
        potencia_vr(10, -5)


def test_potencia_vi_devuelve_float():
    assert isinstance(potencia_vi(10, 2), float)


def test_potencia_ir_devuelve_float():
    assert isinstance(potencia_ir(2, 5), float)


def test_potencia_vr_devuelve_float():
    assert isinstance(potencia_vr(10, 5), float)
