"""
Tests unitarios que verifican que los conversores de unidades rechazan
valores no finitos (NaN, inf y -inf) y conservan las conversiones válidas.
"""

import math

import pytest

from chuspacalc.modulos.matematicas.conversor_energia import convertir_energia
from chuspacalc.modulos.matematicas.conversor_longitud import convertir
from chuspacalc.modulos.matematicas.conversor_longitud_extendido import (
    convertir_longitud,
)
from chuspacalc.modulos.matematicas.conversor_masa import convertir_masa
from chuspacalc.modulos.matematicas.conversor_presion import convertir_presion
from chuspacalc.modulos.matematicas.conversor_temperatura import (
    celsius_a_fahrenheit,
    celsius_a_kelvin,
    fahrenheit_a_celsius,
    kelvin_a_celsius,
)
from chuspacalc.modulos.matematicas.conversor_velocidad import convertir_velocidad

CONVERSORES = [
    pytest.param(lambda v: convertir(v, "m", "km"), id="longitud"),
    pytest.param(lambda v: convertir_longitud(v, "m", "ua"), id="longitud_extendido"),
    pytest.param(lambda v: convertir_masa(v, "kg", "g"), id="masa"),
    pytest.param(lambda v: convertir_presion(v, "bar", "kPa"), id="presion"),
    pytest.param(celsius_a_fahrenheit, id="celsius_a_fahrenheit"),
    pytest.param(fahrenheit_a_celsius, id="fahrenheit_a_celsius"),
    pytest.param(celsius_a_kelvin, id="celsius_a_kelvin"),
    pytest.param(kelvin_a_celsius, id="kelvin_a_celsius"),
    pytest.param(lambda v: convertir_velocidad(v, "km/h", "m/s"), id="velocidad"),
    pytest.param(lambda v: convertir_energia(v, "kWh", "J"), id="energia"),
]


@pytest.mark.parametrize("no_finito", [math.nan, math.inf, -math.inf])
@pytest.mark.parametrize("conversor", CONVERSORES)
def test_conversor_rechaza_valor_no_finito(conversor, no_finito):
    with pytest.raises(ValueError, match="debe ser finito"):
        conversor(no_finito)


@pytest.mark.parametrize(
    "conversor, valor, esperado",
    [
        pytest.param(
            lambda v: convertir(v, "km", "m")["valor_convertido"],
            1,
            1000,
            id="longitud",
        ),
        pytest.param(
            lambda v: convertir_longitud(v, "mn", "m"),
            1,
            1852.0,
            id="longitud_extendido",
        ),
        pytest.param(lambda v: convertir_masa(v, "kg", "g"), 1, 1000, id="masa"),
        pytest.param(
            lambda v: convertir_presion(v, "bar", "kPa"),
            1,
            100,
            id="presion",
        ),
        pytest.param(celsius_a_fahrenheit, 100, 212, id="celsius_a_fahrenheit"),
        pytest.param(fahrenheit_a_celsius, 32, 0, id="fahrenheit_a_celsius"),
        pytest.param(celsius_a_kelvin, 0, 273.15, id="celsius_a_kelvin"),
        pytest.param(kelvin_a_celsius, 273.15, 0, id="kelvin_a_celsius"),
        pytest.param(
            lambda v: convertir_velocidad(v, "km/h", "m/s"),
            36,
            10,
            id="velocidad",
        ),
        pytest.param(
            lambda v: convertir_energia(v, "kWh", "J"),
            1,
            3600000,
            id="energia",
        ),
    ],
)
def test_conversor_mantiene_conversion_valida(conversor, valor, esperado):
    assert conversor(valor) == pytest.approx(esperado)
