"""
Tests unitarios para las funciones del módulo transformaciones,
verificando la rotación, traslación y escalado de puntos en 2D, con y
sin centro de transformación.
"""

import pytest

from chuspacalc.modulos.geometria.transformaciones import (
    escalar_punto,
    rotar_punto,
    trasladar_punto,
)


def test_rotar_punto_90_grados_respecto_al_origen():
    assert rotar_punto((1, 0), 90) == pytest.approx((0, 1))


def test_rotar_punto_180_grados_respecto_a_un_centro():
    assert rotar_punto((2, 1), 180, centro=(1, 1)) == pytest.approx((0, 1))


def test_trasladar_punto():
    assert trasladar_punto((1, 2), 3, -1) == (4, 1)


def test_escalar_punto_respecto_al_origen():
    assert escalar_punto((2, 2), 2) == (4, 4)


def test_escalar_punto_respecto_a_un_centro():
    assert escalar_punto((3, 3), 2, centro=(1, 1)) == (5, 5)
