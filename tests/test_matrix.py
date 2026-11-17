import pytest

from chuspacalc.math.matrix import multiplicar, restar, sumar


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


def test_sumar_y_restar_rectangulares():
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[6, 5, 4], [3, 2, 1]]

    assert sumar(a, b) == [[7, 7, 7], [7, 7, 7]]
    assert restar(a, b) == [[-5, -3, -1], [1, 3, 5]]


def test_multiplicar_rectangulares():
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10], [11, 12]]

    assert multiplicar(a, b) == [[58, 64], [139, 154]]


@pytest.mark.parametrize("operacion", [sumar, restar, multiplicar])
@pytest.mark.parametrize(
    "a, b",
    [
        ([], [[1]]),
        ([[1]], []),
        ([[]], [[]]),
    ],
)
def test_matriz_vacia_lanza_error(operacion, a, b):
    with pytest.raises(ValueError):
        operacion(a, b)


@pytest.mark.parametrize("operacion", [sumar, restar])
@pytest.mark.parametrize(
    "a, b",
    [
        ([[1, 2], [3]], [[1, 2], [3, 4]]),
        ([[1, 2], [3, 4]], [[1, 2], [3]]),
    ],
)
def test_sumar_restar_filas_irregulares_lanza_error(operacion, a, b):
    with pytest.raises(ValueError):
        operacion(a, b)


@pytest.mark.parametrize(
    "a, b",
    [
        ([[1, 2], [3]], [[1], [2]]),
        ([[1, 2]], [[1, 2], [3]]),
    ],
)
def test_multiplicar_filas_irregulares_lanza_error(a, b):
    with pytest.raises(ValueError):
        multiplicar(a, b)
