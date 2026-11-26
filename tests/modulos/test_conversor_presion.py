"""
Pruebas unitarias para conversor_presion.py.
"""

import pytest
from escuadra.modulos.matematicas.conversor_presion import convertir_presion


@pytest.mark.parametrize(
    "valor, origen, destino, esperado",
    [
        (1.0, "atm", "Pa", 101325.0),
        (1.0, "bar", "psi", 14.5038),
        (1.0, "kPa", "Pa", 1000.0),
        (101325.0, "Pa", "atm", 1.0),
        (1.0, "bar", "kPa", 100.0),
        (1.0, "atm", "bar", 1.01325),
    ],
)
def test_conversiones_cruzadas(valor, origen, destino, esperado):
    resultado = convertir_presion(valor, origen, destino)
    assert resultado == pytest.approx(esperado, rel=1e-4)


def test_psi_a_atm_dentro_del_margen():
    resultado = convertir_presion(14.696, "psi", "atm")
    assert resultado == pytest.approx(1.0, rel=0.001)


@pytest.mark.parametrize("destino", ["Pa", "kPa", "bar", "psi", "atm"])
def test_vacio_absoluto_es_cero(destino):
    assert convertir_presion(0, "Pa", destino) == 0.0


@pytest.mark.parametrize("valor", [-1, -0.001, -101325])
def test_presion_negativa_lanza_error(valor):
    with pytest.raises(ValueError):
        convertir_presion(valor, "Pa", "kPa")
