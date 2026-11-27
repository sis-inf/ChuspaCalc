import re

import pytest

from chuspacalc.modulos.sistemas.karnaugh import (
    generar_mapa_karnaugh,
    simplificar_expresion,
)


def _tabla(num_variables, minterminos):
    return [1 if i in minterminos else 0 for i in range(2**num_variables)]


def _evaluar(expresion, n, indice):
    """Evalúa una suma de productos como "A'B + AC" para una combinación."""
    if expresion in ("0", "1"):
        return int(expresion)
    bits = {"ABCD"[i]: (indice >> (n - 1 - i)) & 1 for i in range(n)}
    for termino in expresion.split(" + "):
        literales = re.findall(r"([A-D])('?)", termino)
        if all(bits[var] == (0 if negada else 1) for var, negada in literales):
            return 1
    return 0


def _tabla_de(expresion, num_variables):
    return [_evaluar(expresion, num_variables, i) for i in range(2**num_variables)]


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


def test_generar_mapa_karnaugh_rechaza_longitud_incorrecta():
    with pytest.raises(ValueError, match="debe tener 8 valores"):
        generar_mapa_karnaugh([0, 1, 1, 0], 3)


def test_generar_mapa_karnaugh_rechaza_valores_no_booleanos():
    with pytest.raises(ValueError, match="Solo se admiten 0 y 1"):
        generar_mapa_karnaugh([0, 1, 2, 0], 2)


def test_simplificar_expresion_lista_vacia_es_invalida():
    with pytest.raises(ValueError, match="4, 8 o 16 valores"):
        simplificar_expresion([])


def test_simplificar_expresion_todos_unos_devuelve_uno():
    assert simplificar_expresion([1, 1, 1, 1]) == "1"


@pytest.mark.parametrize("num_variables", [2, 3, 4])
def test_constantes(num_variables):
    assert simplificar_expresion([0] * 2**num_variables) == "0"
    assert simplificar_expresion([1] * 2**num_variables) == "1"


@pytest.mark.parametrize(
    "num_variables, minterminos, esperado",
    [
        (2, {1, 2}, "A'B + AB'"),
        (2, {2, 3}, "A"),
        (2, {0, 1, 3}, "A' + B"),
        (3, {0, 2, 5, 7}, "A'C' + AC"),
        (4, {0, 2, 5, 7, 8, 10, 13, 15}, "B'D' + BD"),
        (4, {0, 1, 2, 5, 6, 7, 8, 9, 10, 14}, "A'BD + B'C' + CD'"),
    ],
)
def test_simplifica_casos_simples(num_variables, minterminos, esperado):
    tabla = _tabla(num_variables, minterminos)

    assert simplificar_expresion(tabla) == esperado


@pytest.mark.parametrize(
    "num_variables, minterminos, esperado",
    [
        (3, {0, 2}, "A'C'"),
        (3, {0, 2, 4, 6}, "C'"),
        (4, {0, 2, 8, 10}, "B'D'"),
    ],
)
def test_agrupa_cruzando_los_bordes(num_variables, minterminos, esperado):
    tabla = _tabla(num_variables, minterminos)

    assert simplificar_expresion(tabla) == esperado


@pytest.mark.parametrize(
    "mapa, esperado",
    [
        ([[0, 1], [1, 0]], "A'B + AB'"),
        ([[1, 0, 0, 1], [1, 0, 0, 1]], "C'"),
        ([[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]], "B'D'"),
    ],
)
def test_acepta_mapa_en_orden_gray(mapa, esperado):
    assert simplificar_expresion(mapa) == esperado


@pytest.mark.parametrize("num_variables", [2, 3])
def test_todas_las_funciones_son_exactas_y_sin_terminos_redundantes(num_variables):
    total = 2**num_variables
    for codigo in range(2**total):
        tabla = [(codigo >> i) & 1 for i in range(total)]

        expresion = simplificar_expresion(tabla)

        assert _tabla_de(expresion, num_variables) == tabla
        terminos = expresion.split(" + ")
        if len(terminos) > 1:
            for k in range(len(terminos)):
                resto = " + ".join(terminos[:k] + terminos[k + 1 :])
                assert _tabla_de(resto, num_variables) != tabla


@pytest.mark.parametrize(
    "entrada, mensaje",
    [
        ([0, 1, 1], "4, 8 o 16 valores"),
        ([0] * 32, "4, 8 o 16 valores"),
        ([0, 1, 2, 0], "Solo se admiten 0 y 1"),
        (["1", 0, 0, 0], "Solo se admiten 0 y 1"),
        ([0.5, 0, 0, 0], "Solo se admiten 0 y 1"),
        ([None, 0, 0, 0], "Solo se admiten 0 y 1"),
        ([[0, 1, 0], [1, 0, 1], [0, 0, 0]], "2x2, 2x4 o 4x4"),
        ([[0, 1], [1]], "2x2, 2x4 o 4x4"),
    ],
)
def test_rechaza_entradas_invalidas(entrada, mensaje):
    with pytest.raises(ValueError, match=mensaje):
        simplificar_expresion(entrada)
