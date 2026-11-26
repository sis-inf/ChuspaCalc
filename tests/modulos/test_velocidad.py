"""
Tests unitarios para la validación de parámetros en conversor_velocidad:
tipos inválidos, valores no finitos, velocidades negativas y unidades.
"""

import math

import pytest

from chuspacalc.modulos.matematicas.conversor_velocidad import convertir_velocidad
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def test_conversion_valida():
    assert convertir_velocidad(36, "km/h", "m/s") == pytest.approx(10)


@pytest.mark.parametrize("valor", ["10", None, [1], True])
def test_valor_tipo_invalido(valor):
    with pytest.raises(ErrorValidacion):
        convertir_velocidad(valor, "km/h", "m/s")


@pytest.mark.parametrize("valor", [math.nan, math.inf, -math.inf])
def test_valor_no_finito(valor):
    with pytest.raises(ErrorValidacion, match="debe ser finito"):
        convertir_velocidad(valor, "km/h", "m/s")


def test_velocidad_negativa():
    with pytest.raises(ErrorValidacion):
        convertir_velocidad(-1, "km/h", "m/s")


@pytest.mark.parametrize("unidad", [None, 5, ["km/h"]])
def test_unidad_tipo_invalido(unidad):
    with pytest.raises(ErrorValidacion):
        convertir_velocidad(1, unidad, "m/s")
    with pytest.raises(ErrorValidacion):
        convertir_velocidad(1, "m/s", unidad)


def test_unidad_desconocida():
    with pytest.raises(ErrorValidacion):
        convertir_velocidad(1, "furlongs/h", "m/s")
    with pytest.raises(ErrorValidacion):
        convertir_velocidad(1, "m/s", "furlongs/h")
