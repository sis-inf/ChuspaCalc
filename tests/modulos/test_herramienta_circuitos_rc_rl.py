"""
Tests unitarios para las funciones de cálculo de circuitos RC y RL.
"""

import pytest

from chuspacalc.modulos.electrica.herramienta_circuitos_rc_rl import (
    herramienta_calcular_constante_tiempo_rc,
    herramienta_calcular_constante_tiempo_rl,
    herramienta_calcular_voltaje_carga_capacitor,
)


def test_herramienta_calcular_constante_tiempo_rc_devuelve_constante():
    resultado = herramienta_calcular_constante_tiempo_rc(1000, 1e-6)

    assert resultado == pytest.approx(0.001)


def test_herramienta_calcular_constante_tiempo_rl_devuelve_constante():
    resultado = herramienta_calcular_constante_tiempo_rl(10, 0.5)

    assert resultado == pytest.approx(0.05)


def test_herramienta_calcular_voltaje_carga_capacitor_devuelve_cero_a_tiempo_cero():
    resultado = herramienta_calcular_voltaje_carga_capacitor(10, 0, 1)

    assert resultado == pytest.approx(0.0)


def test_herramienta_calcular_voltaje_carga_capacitor_devuelve_casi_carga():
    resultado = herramienta_calcular_voltaje_carga_capacitor(10, 5, 1)

    assert resultado / 10 == pytest.approx(0.993, abs=0.005)


def test_herramienta_calcular_constante_tiempo_rc_resistencia_invalida():
    with pytest.raises(ValueError):
        herramienta_calcular_constante_tiempo_rc(0, 1e-6)


def test_herramienta_calcular_constante_tiempo_rc_capacitancia_invalida():
    with pytest.raises(ValueError):
        herramienta_calcular_constante_tiempo_rc(1000, 0)


def test_herramienta_calcular_constante_tiempo_rl_resistencia_invalida():
    with pytest.raises(ValueError):
        herramienta_calcular_constante_tiempo_rl(0, 0.5)


def test_herramienta_calcular_constante_tiempo_rl_inductancia_invalida():
    with pytest.raises(ValueError):
        herramienta_calcular_constante_tiempo_rl(10, 0)


def test_herramienta_calcular_voltaje_carga_capacitor_constante_tiempo_invalida():
    with pytest.raises(ValueError):
        herramienta_calcular_voltaje_carga_capacitor(10, 0, 0)
