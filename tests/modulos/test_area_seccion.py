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
    momento_inercia_perfil_i,
    momento_inercia_rectangular,
    radio_giro,
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


def test_inercia_rectangular_es_b_h3_sobre_12():
    resultado = momento_inercia_rectangular(0.3, 0.5)

    assert resultado == pytest.approx(0.3 * 0.5**3 / 12, abs=1e-5)
    assert resultado == pytest.approx(0.003125, abs=1e-5)


def test_inercia_perfil_i_aplica_ejes_paralelos():
    # Alas 200 x 20 mm, alma libre de 300 x 10 mm.
    resultado = momento_inercia_perfil_i(200, 20, 300, 10)

    inercia_alma = 10 * 300**3 / 12
    inercia_ala = 200 * 20**3 / 12 + 200 * 20 * 160**2
    assert resultado == pytest.approx(inercia_alma + 2 * inercia_ala, abs=1e-5)
    assert resultado == pytest.approx(227_566_666.666667, abs=1e-5)


def test_inercia_perfil_i_coincide_con_rectangulo_menos_huecos():
    resultado = momento_inercia_perfil_i(200, 20, 300, 10)

    altura_total = 300 + 2 * 20
    esperado = (200 * altura_total**3 - (200 - 10) * 300**3) / 12
    assert resultado == pytest.approx(esperado, abs=1e-5)


def test_radio_giro_es_raiz_de_inercia_sobre_area():
    inercia = momento_inercia_rectangular(0.3, 0.5)
    area = area_rectangular(0.3, 0.5)

    resultado = radio_giro(inercia, area)

    assert resultado == pytest.approx(math.sqrt(inercia / area), abs=1e-5)
    assert resultado == pytest.approx(0.5 / math.sqrt(12), abs=1e-5)


def test_radio_giro_de_perfil_i():
    inercia = momento_inercia_perfil_i(200, 20, 300, 10)
    area = area_perfil_i(200, 20, 300, 10)

    assert radio_giro(inercia, area) == pytest.approx(143.832815, abs=1e-5)


@pytest.mark.parametrize(
    "base, altura",
    [(0, 0.5), (0.3, 0), (-0.3, 0.5), (0.3, math.nan), (math.inf, 0.5)],
)
def test_inercia_rectangular_rechaza_dimensiones_invalidas(base, altura):
    with pytest.raises(ValueError):
        momento_inercia_rectangular(base, altura)


@pytest.mark.parametrize(
    "dimensiones",
    [
        (0, 20, 300, 10),
        (200, -20, 300, 10),
        (200, 20, 0, 10),
        (200, 20, 300, -10),
        (200, 20, math.nan, 10),
    ],
)
def test_inercia_perfil_i_rechaza_dimensiones_invalidas(dimensiones):
    with pytest.raises(ValueError):
        momento_inercia_perfil_i(*dimensiones)


@pytest.mark.parametrize(
    "inercia, area",
    [(0, 1), (1, 0), (-1, 1), (1, -1), (math.nan, 1), (1, math.inf)],
)
def test_radio_giro_rechaza_valores_invalidos(inercia, area):
    with pytest.raises(ValueError):
        radio_giro(inercia, area)
