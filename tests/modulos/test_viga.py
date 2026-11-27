"""
Tests unitarios para la función calcular_reacciones() del módulo
viga, verificando el cálculo de reacciones para cargas puntuales y
distribuidas, así como el manejo de entradas inválidas.
"""

import pytest

from chuspacalc.modulos.civil.viga import calcular_reacciones


def test_carga_distribuida_simetrica():
    resultado = calcular_reacciones(longitud=10, carga=100)
    assert resultado["Ra"] == 50
    assert resultado["Rb"] == 50


def test_carga_puntual_centro():
    resultado = calcular_reacciones(longitud=10, carga=200, posicion=5)
    assert resultado["Ra"] == 100
    assert resultado["Rb"] == 100


def test_carga_puntual_extremo_apoyo_a():
    # posicion=0 → carga sobre el apoyo A → Ra absorbe toda la carga
    resultado = calcular_reacciones(longitud=10, carga=300, posicion=0)
    assert resultado["Ra"] == 300
    assert resultado["Rb"] == 0


def test_carga_puntual_extremo_apoyo_b():
    # posicion=longitud → carga sobre el apoyo B → Rb absorbe toda la carga
    resultado = calcular_reacciones(longitud=10, carga=300, posicion=10)
    assert resultado["Ra"] == 0
    assert resultado["Rb"] == 300


def test_longitud_negativa():
    with pytest.raises(ValueError):
        calcular_reacciones(longitud=-10, carga=100)


def test_longitud_cero():
    with pytest.raises(ValueError):
        calcular_reacciones(longitud=0, carga=100)


def test_carga_negativa():
    with pytest.raises(ValueError):
        calcular_reacciones(longitud=10, carga=-100)


def test_posicion_fuera_de_rango():
    with pytest.raises(ValueError):
        calcular_reacciones(longitud=10, carga=100, posicion=15)


def test_resultado_contiene_unidad():
    resultado = calcular_reacciones(longitud=10, carga=100)
    assert resultado["unidad"] == "kN"
