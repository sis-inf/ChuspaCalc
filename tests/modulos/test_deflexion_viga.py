"""
Pruebas unitarias para deflexion_viga.py.
"""

import pytest
from escuadra.modulos.civil.deflexion_viga import calcular_deflexion_max

E = 200e9  # Pa (acero)
INERCIA = 8e-5  # m4


@pytest.mark.parametrize(
    "longitud, carga, inercia, tipo_carga, esperado_mm",
    [
        (4, 10000, INERCIA, "puntual_central", 0.8333),
        (4, 10000, INERCIA, "distribuida", 2.0833),
        (6, 5000, 1e-4, "distribuida", 4.2188),
    ],
)
def test_flecha_maxima_casos_conocidos(
    longitud, carga, inercia, tipo_carga, esperado_mm
):
    resultado = calcular_deflexion_max(longitud, carga, E, inercia, tipo_carga)
    assert resultado["deflexion_max"] == pytest.approx(esperado_mm, abs=1e-4)


def test_carga_puntual_es_el_tipo_por_defecto():
    por_defecto = calcular_deflexion_max(4, 10000, E, INERCIA)
    explicito = calcular_deflexion_max(4, 10000, E, INERCIA, "puntual_central")
    assert por_defecto == explicito


def test_posicion_del_maximo_es_el_centro():
    resultado = calcular_deflexion_max(4, 10000, E, INERCIA)
    assert resultado["posicion"] == pytest.approx(2.0)


@pytest.mark.parametrize(
    "longitud, carga, modulo, inercia",
    [
        (0, 10000, E, INERCIA),
        (-4, 10000, E, INERCIA),
        (4, 0, E, INERCIA),
        (4, 10000, 0, INERCIA),
        (4, 10000, -E, INERCIA),
        (4, 10000, E, 0),
    ],
)
def test_parametros_no_positivos_lanzan_error(longitud, carga, modulo, inercia):
    with pytest.raises(ValueError):
        calcular_deflexion_max(longitud, carga, modulo, inercia)


def test_tipo_de_carga_invalido_lanza_error():
    with pytest.raises(ValueError):
        calcular_deflexion_max(4, 10000, E, INERCIA, "triangular")
