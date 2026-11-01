"""
Tests unitarios para la lógica de generación de tablas de verdad.
"""

import pytest

from chuspacalc.modulos.sistemas.herramienta_tablas_verdad import HerramientaTablasVerdad


@pytest.fixture
def herramienta():
    return HerramientaTablasVerdad()


def test_and_produce_4_filas(herramienta):
    # A & B tiene 4 combinaciones
    variables, filas, resultados = herramienta.generar_tabla("A & B")
    assert len(filas) == 4


def test_and_resultados_correctos(herramienta):
    # A & B: 0,0,0,1
    _, _, resultados = herramienta.generar_tabla("A & B")
    assert [int(r) for r in resultados] == [0, 0, 0, 1]


def test_or_resultados_correctos(herramienta):
    # A | B: 0,1,1,1
    _, _, resultados = herramienta.generar_tabla("A | B")
    assert [int(r) for r in resultados] == [0, 1, 1, 1]


def test_not_produce_2_filas(herramienta):
    # ~A tiene 2 combinaciones
    _, filas, _ = herramienta.generar_tabla("~A")
    assert len(filas) == 2


def test_not_resultados_correctos(herramienta):
    # ~A: 1,0
    _, _, resultados = herramienta.generar_tabla("~A")
    assert [int(r) for r in resultados] == [1, 0]


def test_xor_resultados_correctos(herramienta):
    # A ^ B: 0,1,1,0
    _, _, resultados = herramienta.generar_tabla("A ^ B")
    assert [int(r) for r in resultados] == [0, 1, 1, 0]


def test_tres_variables_produce_8_filas(herramienta):
    # A & B & C tiene 8 combinaciones con un único 1
    _, filas, resultados = herramienta.generar_tabla("A & B & C")
    assert len(filas) == 8
    assert sum(int(r) for r in resultados) == 1


def test_cinco_variables_lanza_error(herramienta):
    # Más de 4 variables debe lanzar error
    with pytest.raises(ValueError):
        herramienta.generar_tabla("A & B & C & D & E")


def test_expresion_invalida_lanza_error(herramienta):
    # Caracteres no permitidos deben lanzar error
    with pytest.raises(ValueError):
        herramienta.generar_tabla("a + b")
