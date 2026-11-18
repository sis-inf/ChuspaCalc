"""
Tests unitarios para las funciones de cálculo del divisor de tensión.
"""

import pytest

from chuspacalc.modulos.electrica.herramienta_divisor_tension import (
    calcular_r1,
    calcular_r2,
    calcular_vout,
)


def test_calcular_vout():
    # Vout = Vin * R2 / (R1 + R2) → 12 * 2000 / (1000 + 2000) = 8
    assert calcular_vout(12, 1000, 2000) == pytest.approx(8.0)


def test_calcular_r2():
    # R2 = (Vout * R1) / (Vin - Vout) → (5 * 1000) / (12 - 5) ≈ 714.29
    assert calcular_r2(12, 5, 1000) == pytest.approx(714.29, rel=1e-3)


def test_calcular_r1():
    # R1 = R2 * (Vin - Vout) / Vout → 1000 * (9 - 3) / 3 = 2000
    assert calcular_r1(9, 3, 1000) == pytest.approx(2000.0)


def test_calcular_vout_vin_cero():
    # Si Vin = 0, Vout debe ser 0
    assert calcular_vout(0, 1000, 2000) == 0


def test_calcular_vout_resistencias_cero():
    # R1 = 0 y R2 = 0 debe lanzar error
    with pytest.raises(ValueError):
        calcular_vout(12, 0, 0)


def test_calcular_r2_vout_igual_vin():
    # Vout = Vin divide por cero en la formula
    with pytest.raises(ValueError):
        calcular_r2(12, 12, 1000)


def test_calcular_r1_vout_cero():
    # Vout = 0 divide por cero en la formula
    with pytest.raises(ValueError):
        calcular_r1(12, 0, 1000)
