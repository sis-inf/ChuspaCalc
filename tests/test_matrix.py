import pytest

from chuspacalc.math.matrix import (
    multiplicar,
    multiplicar_escalar,
    restar,
    sumar,
    transponer,
)

MENSAJE_NO_SECUENCIA = r"^La matriz debe ser una secuencia de filas\.$"
MENSAJE_FILA_NO_SECUENCIA = r"^Cada fila de la matriz debe ser una secuencia\.$"
MENSAJE_VACIA = r"^La matriz no puede estar vacía\.$"
MENSAJE_IRREGULAR = r"^Todas las filas deben tener la misma longitud\.$"
MENSAJE_ELEMENTO = r"^Todos los elementos de la matriz deben ser números finitos\.$"
MENSAJE_ESCALAR = r"^El escalar debe ser un número finito\.$"

VALIDA = [[1, 2], [3, 4]]
BINARIAS = [sumar, restar, multiplicar]
UNARIAS = [
    pytest.param(transponer, id="transponer"),
    pytest.param(lambda a: multiplicar_escalar(a, 2), id="multiplicar_escalar"),
]

MATRICES_NO_SECUENCIA = [5, None, "12", b"12", {1, 2}]
IDS_NO_SECUENCIA = ["entero", "none", "texto", "bytes", "conjunto"]
FILAS_NO_SECUENCIA = [
    [1, 2],
    [[1, 2], 3],
    [[1, 2], "ab"],
    [[1, 2], None],
]
IDS_FILAS = ["lista_plana", "fila_entero", "fila_texto", "fila_none"]
ELEMENTOS_INVALIDOS = [True, False, float("nan"), float("inf"), float("-inf")]
IDS_ELEMENTOS = ["true", "false", "nan", "inf", "menos_inf"]
ESCALARES_INVALIDOS = [
    True,
    False,
    float("nan"),
    float("inf"),
    float("-inf"),
    "2",
    None,
]
IDS_ESCALARES = ["true", "false", "nan", "inf", "menos_inf", "texto", "none"]


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


@pytest.mark.parametrize("operacion", BINARIAS)
@pytest.mark.parametrize("invalida", MATRICES_NO_SECUENCIA, ids=IDS_NO_SECUENCIA)
def test_binarias_matriz_no_secuencia_lanza_error(operacion, invalida):
    with pytest.raises(ValueError, match=MENSAJE_NO_SECUENCIA):
        operacion(invalida, VALIDA)
    with pytest.raises(ValueError, match=MENSAJE_NO_SECUENCIA):
        operacion(VALIDA, invalida)


@pytest.mark.parametrize("operacion", UNARIAS)
@pytest.mark.parametrize("invalida", MATRICES_NO_SECUENCIA, ids=IDS_NO_SECUENCIA)
def test_unarias_matriz_no_secuencia_lanza_error(operacion, invalida):
    with pytest.raises(ValueError, match=MENSAJE_NO_SECUENCIA):
        operacion(invalida)


@pytest.mark.parametrize("operacion", BINARIAS)
@pytest.mark.parametrize("invalida", FILAS_NO_SECUENCIA, ids=IDS_FILAS)
def test_binarias_fila_no_secuencia_lanza_error(operacion, invalida):
    with pytest.raises(ValueError, match=MENSAJE_FILA_NO_SECUENCIA):
        operacion(invalida, VALIDA)
    with pytest.raises(ValueError, match=MENSAJE_FILA_NO_SECUENCIA):
        operacion(VALIDA, invalida)


@pytest.mark.parametrize("operacion", UNARIAS)
@pytest.mark.parametrize("invalida", FILAS_NO_SECUENCIA, ids=IDS_FILAS)
def test_unarias_fila_no_secuencia_lanza_error(operacion, invalida):
    with pytest.raises(ValueError, match=MENSAJE_FILA_NO_SECUENCIA):
        operacion(invalida)


@pytest.mark.parametrize("operacion", BINARIAS)
@pytest.mark.parametrize("elemento", ELEMENTOS_INVALIDOS, ids=IDS_ELEMENTOS)
def test_binarias_elemento_invalido_lanza_error(operacion, elemento):
    invalida = [[1, elemento], [3, 4]]

    with pytest.raises(ValueError, match=MENSAJE_ELEMENTO):
        operacion(invalida, VALIDA)
    with pytest.raises(ValueError, match=MENSAJE_ELEMENTO):
        operacion(VALIDA, invalida)


@pytest.mark.parametrize("operacion", UNARIAS)
@pytest.mark.parametrize("elemento", ELEMENTOS_INVALIDOS, ids=IDS_ELEMENTOS)
def test_unarias_elemento_invalido_lanza_error(operacion, elemento):
    with pytest.raises(ValueError, match=MENSAJE_ELEMENTO):
        operacion([[1, elemento], [3, 4]])


@pytest.mark.parametrize("escalar", ESCALARES_INVALIDOS, ids=IDS_ESCALARES)
def test_multiplicar_escalar_invalido_lanza_error(escalar):
    with pytest.raises(ValueError, match=MENSAJE_ESCALAR):
        multiplicar_escalar(VALIDA, escalar)


@pytest.mark.parametrize("operacion", UNARIAS)
@pytest.mark.parametrize(
    "matriz, mensaje",
    [
        ([], MENSAJE_VACIA),
        ([[]], MENSAJE_VACIA),
        ([[1, 2], [3]], MENSAJE_IRREGULAR),
        ([[1], [2, 3]], MENSAJE_IRREGULAR),
    ],
    ids=["sin_filas", "sin_columnas", "fila_corta", "fila_larga"],
)
def test_unarias_vacia_o_irregular_lanza_error(operacion, matriz, mensaje):
    with pytest.raises(ValueError, match=mensaje):
        operacion(matriz)


@pytest.mark.parametrize(
    "matriz, esperado",
    [
        ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
        ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
        ([[1, 2, 3]], [[1], [2], [3]]),
        ([[1], [2], [3]], [[1, 2, 3]]),
        ([[1.5, -2.0]], [[1.5], [-2.0]]),
    ],
    ids=[
        "rectangular",
        "cuadrada",
        "fila_a_columna",
        "columna_a_fila",
        "flotantes",
    ],
)
def test_transponer_matrices_validas(matriz, esperado):
    assert transponer(matriz) == esperado


def test_transponer_dos_veces_devuelve_la_original():
    matriz = [[1, 2, 3], [4, 5, 6]]

    assert transponer(transponer(matriz)) == matriz


def test_transponer_acepta_tuplas():
    assert transponer(((1, 2), (3, 4))) == [[1, 3], [2, 4]]


def test_transponer_no_modifica_la_entrada():
    matriz = [[1, 2, 3], [4, 5, 6]]

    transponer(matriz)

    assert matriz == [[1, 2, 3], [4, 5, 6]]


@pytest.mark.parametrize(
    "matriz, escalar, esperado",
    [
        ([[1.0, -2.0], [3.0, 4.0]], 2.5, [[2.5, -5.0], [7.5, 10.0]]),
        ([[1, 2], [3, 4]], 3, [[3, 6], [9, 12]]),
        ([[1, 2], [3, 4]], 0, [[0, 0], [0, 0]]),
        ([[1, -2]], -1, [[-1, 2]]),
        ([[1, 2, 3], [4, 5, 6]], 2, [[2, 4, 6], [8, 10, 12]]),
    ],
    ids=["flotantes", "enteros", "cero", "negativo", "rectangular"],
)
def test_multiplicar_escalar_valido(matriz, escalar, esperado):
    assert multiplicar_escalar(matriz, escalar) == esperado


def test_multiplicar_escalar_no_modifica_la_entrada():
    matriz = [[1, 2], [3, 4]]

    multiplicar_escalar(matriz, 2)

    assert matriz == [[1, 2], [3, 4]]
