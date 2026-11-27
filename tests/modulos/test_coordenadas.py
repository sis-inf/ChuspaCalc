import math

import pytest

from chuspacalc.modulos.geometria.coordenadas import (
    cartesiana_a_cilindrica,
    cartesiana_a_esferica,
    cartesiana_a_polar,
    polar_a_cartesiana,
)


def test_cartesiana_a_polar():
    resultado = cartesiana_a_polar(3, 4)

    assert resultado["r"] == 5.00
    assert resultado["theta_grados"] == 53.13


def test_cartesiana_a_polar_origen():
    resultado = cartesiana_a_polar(0, 0)

    assert resultado["r"] == 0.00
    assert resultado["theta_grados"] == 0.00


def test_polar_a_cartesiana():
    resultado = polar_a_cartesiana(5, 53.13)

    assert resultado["x"] == 3.00
    assert resultado["y"] == 4.00


def test_cartesiana_a_cilindrica():
    resultado = cartesiana_a_cilindrica(3, 4, 7)

    assert resultado == {
        "r": 5.00,
        "theta_grados": 53.13,
        "z": 7,
    }


def test_cartesiana_a_esferica():
    resultado = cartesiana_a_esferica(0, 0, 5)

    assert set(resultado) == {
        "rho",
        "theta_grados",
        "phi_grados",
        "theta_radianes",
        "phi_radianes",
        "elevacion_grados",
        "elevacion_radianes",
    }
    assert resultado["rho"] == pytest.approx(5.0)
    assert resultado["theta_grados"] == pytest.approx(0.0)
    assert resultado["phi_grados"] == pytest.approx(0.0)
    assert resultado["theta_radianes"] == pytest.approx(0.0)
    assert resultado["phi_radianes"] == pytest.approx(0.0)
    assert resultado["elevacion_grados"] == pytest.approx(90.0)
    assert resultado["elevacion_radianes"] == pytest.approx(math.pi / 2)
