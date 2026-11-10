"""
Pruebas unitarias para area_seccion.py.
"""

import math

import pytest

from escuadra.modulos.civil.area_seccion import (
    area_circular,
    area_circular_hueca,
    area_perfil_i,
    area_perfil_t,
    area_rectangular,
)


def test_area_rectangular_formula_base_por_altura():
    assert area_rectangular(0.3, 0.5) == pytest.approx(0.15, abs=1e-5)


def test_area_circular_formula_pi_r2():
    assert area_circular(0.1) == pytest.approx(math.pi * 0.1**2, abs=1e-5)


def test_area_circular_hueca_es_diferencia_de_circulos():
    esperado = math.pi * (0.2**2 - 0.1**2)
    assert area_circular_hueca(0.2, 0.1) == pytest.approx(esperado, abs=1e-5)


def test_area_perfil_i_simetrico():
    # 2 alas de 0.2 x 0.02 y un alma de 0.4 x 0.01
    assert area_perfil_i(0.2, 0.02, 0.4, 0.01) == pytest.approx(0.012, abs=1e-5)


def test_area_perfil_t():
    # 1 ala de 0.2 x 0.02 y un alma de 0.4 x 0.01
    assert area_perfil_t(0.2, 0.02, 0.4, 0.01) == pytest.approx(0.008, abs=1e-5)


@pytest.mark.parametrize("base, altura", [(0, 1), (1, 0), (-1, 1), (1, -1)])
def test_area_rectangular_dimensiones_invalidas(base, altura):
    with pytest.raises(ValueError):
        area_rectangular(base, altura)


@pytest.mark.parametrize("radio", [0, -0.1])
def test_area_circular_radio_invalido(radio):
    with pytest.raises(ValueError):
        area_circular(radio)


@pytest.mark.parametrize("radio_ext, radio_int", [(0, 0.1), (0.2, 0), (0.2, -0.1)])
def test_area_circular_hueca_radios_no_positivos(radio_ext, radio_int):
    with pytest.raises(ValueError):
        area_circular_hueca(radio_ext, radio_int)


def test_area_circular_hueca_radio_interior_mayor_o_igual():
    with pytest.raises(ValueError):
        area_circular_hueca(0.1, 0.1)
    with pytest.raises(ValueError):
        area_circular_hueca(0.1, 0.2)


@pytest.mark.parametrize("funcion", [area_perfil_i, area_perfil_t])
@pytest.mark.parametrize(
    "dimensiones",
    [(0, 0.02, 0.4, 0.01), (0.2, -0.02, 0.4, 0.01), (0.2, 0.02, 0, 0.01)],
)
def test_perfiles_dimensiones_invalidas(funcion, dimensiones):
    with pytest.raises(ValueError):
        funcion(*dimensiones)
