import pytest

from escuadra.math.matrix import multiplicar, restar, sumar


def test_sumar_matrices():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    assert sumar(a, b) == [[6, 8], [10, 12]]


def test_restar_matrices():
    a = [[5, 6], [7, 8]]
    b = [[1, 2], [3, 4]]

    assert restar(a, b) == [[4, 4], [4, 4]]


def test_multiplicar_matrices():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    assert multiplicar(a, b) == [[19, 22], [43, 50]]


def test_sumar_dimensiones_invalidas():
    a = [[1, 2]]
    b = [[1, 2], [3, 4]]

    with pytest.raises(ValueError):
        sumar(a, b)


def test_restar_dimensiones_invalidas():
    a = [[1, 2]]
    b = [[1, 2], [3, 4]]

    with pytest.raises(ValueError):
        restar(a, b)


def test_multiplicar_dimensiones_invalidas():
    a = [[1, 2]]
    b = [[1, 2]]

    with pytest.raises(ValueError):
        multiplicar(a, b)


def test_multiplicar_por_identidad():
    identidad = [[1, 0], [0, 1]]
    matriz = [[2, 3], [4, 5]]

    assert multiplicar(matriz, identidad) == matriz
