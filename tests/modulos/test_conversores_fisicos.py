"""
Tests unitarios para los conversores físicos de energía, velocidad y ángulo.
"""

import math

import pytest

from escuadra.modulos.matematicas.conversor_angulo import convertir_angulo
from escuadra.modulos.matematicas.conversor_energia import convertir_energia
from escuadra.modulos.matematicas.conversor_velocidad import convertir_velocidad


# ------------------------
# Conversor de energía
# ------------------------


def test_convertir_energia_kwh_a_j():
    # 1 kWh = 3_600_000 J
    assert convertir_energia(1, "kWh", "J") == pytest.approx(3_600_000.0)


def test_convertir_energia_kj_a_j():
    # 1 kJ = 1000 J
    assert convertir_energia(1, "kJ", "J") == pytest.approx(1000.0)


def test_convertir_energia_mj_a_kwh():
    # 1 MJ = 0.277777... kWh
    assert convertir_energia(1, "MJ", "kWh") == pytest.approx(
        1 / 3.6
    )


# ------------------------
# Conversor de velocidad
# ------------------------


def test_convertir_velocidad_kmh_a_ms():
    # 100 km/h = 27.777... m/s
    assert convertir_velocidad(100, "km/h", "m/s") == pytest.approx(
        27.7777,
        rel=1e-4,
    )


def test_convertir_velocidad_ms_a_kmh():
    # 10 m/s = 36 km/h
    assert convertir_velocidad(10, "m/s", "km/h") == pytest.approx(
        36.0
    )


def test_convertir_velocidad_mph_a_ms():
    # 1 mph = 0.44704 m/s
    assert convertir_velocidad(1, "mph", "m/s") == pytest.approx(
        0.44704
    )


# ------------------------
# Conversor de ángulo
# ------------------------


def test_convertir_angulo_180_grados_a_radianes():
    # 180 grados = pi radianes
    assert convertir_angulo(180, "grados", "radianes") == pytest.approx(
        math.pi
    )


def test_convertir_angulo_pi_radianes_a_grados():
    # pi radianes = 180 grados
    assert convertir_angulo(math.pi, "radianes", "grados") == pytest.approx(
        180.0
    )


def test_convertir_angulo_100_gradianes_a_grados():
    # 100 gradianes = 90 grados
    assert convertir_angulo(100, "gradianes", "grados") == pytest.approx(
        90.0
    )
