"""
Tests unitarios para las funciones del módulo conversor_temperatura,
verificando conversiones entre Celsius, Fahrenheit y Kelvin, así
como el manejo de valores fuera del rango permitido.
"""

import pytest

from chuspacalc.modulos.matematicas.conversor_temperatura import (
    celsius_a_fahrenheit,
    celsius_a_kelvin,
    fahrenheit_a_celsius,
    kelvin_a_celsius,
)


def test_celsius_a_kelvin():
    assert celsius_a_kelvin(0) == 273.15


def test_kelvin_a_celsius():
    assert kelvin_a_celsius(273.15) == 0


def test_celsius_a_fahrenheit():
    assert celsius_a_fahrenheit(0) == 32


def test_fahrenheit_a_celsius():
    assert fahrenheit_a_celsius(32) == 0


def test_kelvin_negativo():
    with pytest.raises(ValueError):
        kelvin_a_celsius(-1)


def test_cero_absoluto_celsius():
    assert celsius_a_kelvin(-273.15) == 0


def test_celsius_bajo_cero_absoluto():
    with pytest.raises(ValueError):
        celsius_a_kelvin(-274)


def test_fahrenheit_bajo_cero_absoluto():
    with pytest.raises(ValueError):
        fahrenheit_a_celsius(-460)
