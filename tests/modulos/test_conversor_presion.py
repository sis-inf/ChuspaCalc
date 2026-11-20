"""Pruebas unitarias para conversor_presion.py."""

import math

import pytest

from chuspacalc.modulos.matematicas.conversor_presion import convertir_presion
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


@pytest.mark.parametrize(
    "valor, origen, destino, esperado",
    [
        (1.0, "atm", "Pa", 101325.0),
        (1.0, "bar", "psi", 14.5038),
        (1.0, "kPa", "Pa", 1000.0),
        (101325.0, "Pa", "atm", 1.0),
        (1.0, "bar", "kPa", 100.0),
        (1.0, "atm", "bar", 1.01325),
        (1.0, "MPa", "kPa", 1000.0),
        (1.0, "mbar", "Pa", 100.0),
        (1.0, "torr", "mmHg", 1.0),
    ],
)
def test_conversiones_cruzadas(valor, origen, destino, esperado):
    resultado = convertir_presion(valor, origen, destino)
    assert resultado == pytest.approx(esperado, rel=1e-4)


def test_psi_a_atm_dentro_del_margen():
    resultado = convertir_presion(14.696, "psi", "atm")
    assert resultado == pytest.approx(1.0, rel=0.001)


@pytest.mark.parametrize("destino", ["Pa", "kPa", "bar", "psi", "atm"])
def test_presion_cero_es_valida(destino):
    assert convertir_presion(0, "Pa", destino) == 0.0


@pytest.mark.parametrize("valor", [-1, -0.001, -101325])
def test_presion_negativa_lanza_error(valor):
    with pytest.raises(ErrorValidacion):
        convertir_presion(valor, "Pa", "kPa")


@pytest.mark.parametrize("valor", [True, False, "10", None, [], {}])
def test_valores_no_numericos_lanzan_error(valor):
    with pytest.raises(ErrorValidacion):
        convertir_presion(valor, "Pa", "kPa")


@pytest.mark.parametrize("valor", [math.nan, math.inf, -math.inf])
def test_valores_no_finitos_lanzan_error(valor):
    with pytest.raises(ErrorValidacion):
        convertir_presion(valor, "Pa", "kPa")


@pytest.mark.parametrize(
    "origen, destino",
    [
        ("XYZ", "Pa"),
        ("Pa", "XYZ"),
        (None, "Pa"),
        ("Pa", None),
        ([], "Pa"),
        ("Pa", []),
    ],
)
def test_unidades_invalidas_lanzan_error(origen, destino):
    with pytest.raises(ErrorValidacion):
        convertir_presion(1, origen, destino)


def test_desbordamiento_numerico_lanza_error():
    with pytest.raises(ErrorValidacion):
        convertir_presion(1.7e308, "MPa", "Pa")
