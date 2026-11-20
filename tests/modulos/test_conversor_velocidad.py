"""Pruebas unitarias para conversor_velocidad.py."""

import math

import pytest

from chuspacalc.modulos.matematicas.conversor_velocidad import (
    convertir_velocidad,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


@pytest.mark.parametrize(
    "valor, origen, destino, esperado",
    [
        (100, "km/h", "m/s", 27.7777777778),
        (10, "m/s", "km/h", 36.0),
        (1, "mph", "m/s", 0.44704),
        (1, "nudos", "m/s", 0.514444),
        (1, "ft/s", "m/s", 0.3048),
        (1, "m/s", "m/s", 1.0),
    ],
)
def test_conversiones_validas(valor, origen, destino, esperado):
    assert convertir_velocidad(valor, origen, destino) == pytest.approx(esperado)


@pytest.mark.parametrize("destino", ["m/s", "km/h", "mph", "nudos", "ft/s"])
def test_velocidad_cero_es_valida(destino):
    assert convertir_velocidad(0, "m/s", destino) == 0.0


@pytest.mark.parametrize("valor", [-1, -0.001, -100])
def test_velocidad_negativa_lanza_error(valor):
    with pytest.raises(ErrorValidacion):
        convertir_velocidad(valor, "m/s", "km/h")


@pytest.mark.parametrize("valor", [True, False, "10", None, [], {}])
def test_valores_no_numericos_lanzan_error(valor):
    with pytest.raises(ErrorValidacion):
        convertir_velocidad(valor, "m/s", "km/h")


@pytest.mark.parametrize("valor", [math.nan, math.inf, -math.inf])
def test_valores_no_finitos_lanzan_error(valor):
    with pytest.raises(ErrorValidacion, match="debe ser finito"):
        convertir_velocidad(valor, "m/s", "km/h")


@pytest.mark.parametrize(
    "origen, destino",
    [
        ("XYZ", "m/s"),
        ("m/s", "XYZ"),
        (None, "m/s"),
        ("m/s", None),
        ([], "m/s"),
        ("m/s", []),
    ],
)
def test_unidades_invalidas_lanzan_error(origen, destino):
    with pytest.raises(ErrorValidacion):
        convertir_velocidad(1, origen, destino)


def test_desbordamiento_numerico_lanza_error():
    with pytest.raises(ErrorValidacion):
        convertir_velocidad(1.7e308, "m/s", "km/h")
