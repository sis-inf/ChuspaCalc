"""
Tests unitarios para la función de conversión de unidades eléctricas.
"""

import pytest

from chuspacalc.modulos.electrica.herramienta_conversion_electrica import (
    convertir_unidad,
)


def test_convertir_kw_a_w():
    # 1 kW = 1000 W
    assert convertir_unidad(1, "kW", "W", "Potencia") == pytest.approx(1000.0)


def test_convertir_hp_a_w():
    # 1 HP = 745.7 W
    assert convertir_unidad(1, "HP", "W", "Potencia") == pytest.approx(745.7, rel=1e-3)


def test_convertir_w_a_kw():
    # 1000 W = 1 kW
    assert convertir_unidad(1000, "W", "kW", "Potencia") == pytest.approx(1.0)


def test_convertir_mw_a_kw():
    # 1 MW = 1000 kW
    assert convertir_unidad(1, "MW", "kW", "Potencia") == pytest.approx(1000.0)


def test_convertir_kwh_a_j():
    # 1 kWh = 3_600_000 J
    assert convertir_unidad(1, "kWh", "J", "Energía") == pytest.approx(3_600_000.0)


def test_convertir_kj_a_j():
    # 1 kJ = 1000 J
    assert convertir_unidad(1, "kJ", "J", "Energía") == pytest.approx(1000.0)


def test_unidad_no_soportada():
    # Una unidad no reconocida debe lanzar error
    with pytest.raises(ValueError):
        convertir_unidad(1, "BTU", "W", "Potencia")
