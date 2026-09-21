"""
Tests unitarios para las funciones de cálculo de la Ley de Ohm.
"""

import pytest

from escuadra.modulos.electrica.ley_ohm import calcular_ohm
from escuadra.modulos.electrica.herramienta_ley_ohm import calcular_potencia


def test_calcular_voltaje():
    # V = I * R → 2 * 5 = 10
    resultado = calcular_ohm(corriente=2, resistencia=5)

    assert resultado["voltaje"] == 10


def test_calcular_corriente():
    # I = V / R → 12 / 3 = 4
    resultado = calcular_ohm(voltaje=12, resistencia=3)

    assert resultado["corriente"] == 4


def test_calcular_resistencia():
    # R = V / I → 10 / 2 = 5
    resultado = calcular_ohm(voltaje=10, corriente=2)

    assert resultado["resistencia"] == 5


def test_calcular_potencia():
    # P = V * I → 10 * 2 = 20
    assert calcular_potencia(10, 2) == 20


def test_calcular_corriente_division_por_cero():
    # La resistencia no puede ser cero
    with pytest.raises(ValueError):
        calcular_ohm(voltaje=10, resistencia=0)


def test_calcular_resistencia_division_por_cero():
    # La corriente no puede ser cero
    with pytest.raises(ValueError):
        calcular_ohm(voltaje=10, corriente=0)


def test_funciones_aceptan_floats():
    # Las funciones deben aceptar valores decimales

    resultado1 = calcular_ohm(
        corriente=2.5,
        resistencia=4.0
    )

    assert resultado1["voltaje"] == pytest.approx(10.0)


    resultado2 = calcular_ohm(
        voltaje=7.5,
        resistencia=2.5
    )

    assert resultado2["corriente"] == pytest.approx(3.0)


    resultado3 = calcular_ohm(
        voltaje=9.0,
        corriente=3.0
    )

    assert resultado3["resistencia"] == pytest.approx(3.0)
