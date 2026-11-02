import pytest

from escuadra.modulos.sistemas.karnaugh import (
    generar_mapa_karnaugh,
    simplificar_expresion,
)


def test_generar_mapa_karnaugh_devuelve_la_misma_tabla():
    tabla = [0, 1, 1, 0]

    resultado = generar_mapa_karnaugh(tabla, 2)

    assert resultado == tabla


def test_generar_mapa_karnaugh_rechaza_una_variable():
    with pytest.raises(ValueError):
        generar_mapa_karnaugh([0, 1], 1)


def test_generar_mapa_karnaugh_rechaza_cinco_variables():
    with pytest.raises(ValueError):
        generar_mapa_karnaugh([0, 1], 5)


def test_simplificar_expresion_lista_vacia_devuelve_cero():
    assert simplificar_expresion([]) == "0"


def test_simplificar_expresion_todos_unos_devuelve_uno():
    assert simplificar_expresion([1, 1, 1, 1]) == "1"


def test_simplificar_expresion_mapa_mixto_devuelve_mensaje_basico():
    mapa = [[0, 1], [1, 0]]

    assert (
        simplificar_expresion(mapa)
        == "Expresión simplificada (caso básico)"
    )
