import math

import pytest

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.matematicas.herramienta_calculadora_cientifica import (
    HerramientaCalculadoraCientifica,
)
from chuspacalc.modulos.sistemas.herramienta_tablas_verdad import (
    HerramientaTablasVerdad,
)


@pytest.fixture
def calculadora():
    return HerramientaCalculadoraCientifica()


@pytest.fixture
def tablas():
    return HerramientaTablasVerdad()


@pytest.mark.parametrize(
    ("expresion", "esperado"),
    [
        ("2 + 3 * 4", 14.0),
        ("(2 + 3) * 4", 20.0),
        ("2^3", 8.0),
        ("7 // 2", 3.0),
        ("7 % 3", 1.0),
        ("-2 + +5", 3.0),
    ],
)
def test_calculadora_preserva_operaciones(expresion, esperado, calculadora):
    assert calculadora.evaluar_expresion(expresion) == pytest.approx(esperado)


def test_calculadora_preserva_funciones_y_constantes(calculadora):
    resultado = calculadora.evaluar_expresion(
        "sin(pi / 2) + cos(0) + log(100) + ln(e) + sqrt(9)"
    )
    assert resultado == pytest.approx(8.0)
    assert calculadora.evaluar_expresion("π") == pytest.approx(math.pi)
    assert calculadora.evaluar_expresion("sin(90)", "Grados") == pytest.approx(1.0)


def test_calculadora_preserva_division_por_cero(calculadora):
    with pytest.raises(ZeroDivisionError, match="División por cero"):
        calculadora.evaluar_expresion("1 / 0")


@pytest.mark.parametrize(
    "expresion",
    [
        "nombre_desconocido",
        "open('archivo')",
        "math.pi",
        "(1).__class__",
        "[1, 2, 3]",
        "{'a': 1}",
        "(lambda: 1)()",
        "[x for x in [1]]",
        "sin(x=0)",
        "sin(0, 1)",
    ],
)
def test_calculadora_rechaza_construcciones_python(expresion, calculadora):
    with pytest.raises((ValueError, SyntaxError)):
        calculadora.evaluar_expresion(expresion)


def test_calculadora_aplica_limites_de_recursos(calculadora):
    with pytest.raises(ValueError, match="longitud"):
        calculadora.evaluar_expresion("1+" * 300 + "1")
    with pytest.raises(ValueError, match="exponente"):
        calculadora.evaluar_expresion("2**1000")
    with pytest.raises(ValueError, match="límite"):
        calculadora.evaluar_expresion("1e100 * 10")
    with pytest.raises(ValueError, match="profundidad|compleja"):
        calculadora.evaluar_expresion("-" * 40 + "1")


@pytest.mark.parametrize(
    "expresion",
    [
        "A AND B",
        "A & B",
        "A * B",
        "A ∧ B",
    ],
)
def test_tablas_preserva_aliases_and(expresion, tablas):
    assert tablas.generar_tabla(expresion)[2] == [False, False, False, True]


@pytest.mark.parametrize("expresion", ["A OR B", "A | B", "A + B", "A ∨ B"])
def test_tablas_preserva_aliases_or(expresion, tablas):
    assert tablas.generar_tabla(expresion)[2] == [False, True, True, True]


@pytest.mark.parametrize("expresion", ["NOT A", "!A", "~A", "¬A"])
def test_tablas_preserva_aliases_not(expresion, tablas):
    assert tablas.generar_tabla(expresion)[2] == [True, False]


@pytest.mark.parametrize("expresion", ["A XOR B", "A ^ B"])
def test_tablas_preserva_xor(expresion, tablas):
    assert tablas.generar_tabla(expresion)[2] == [False, True, True, False]


def test_tablas_preserva_precedencia_parentesis_y_constantes(tablas):
    assert tablas.generar_tabla("A OR B AND C")[2] == [
        False,
        False,
        False,
        True,
        True,
        True,
        True,
        True,
    ]
    assert tablas.generar_tabla("(A OR B) AND C")[2] == [
        False,
        False,
        False,
        True,
        False,
        True,
        False,
        True,
    ]
    assert tablas.generar_tabla("A AND 1")[2] == [False, True]
    assert tablas.generar_tabla("A OR 0")[2] == [False, True]


@pytest.mark.parametrize(
    "expresion",
    [
        "A.__class__",
        "A[0]",
        "A == 1",
        "A / 1",
        "a OR b",
        "A OR 2",
    ],
)
def test_tablas_rechaza_construcciones_no_autorizadas(expresion, tablas):
    with pytest.raises(ErrorValidacion):
        tablas.generar_tabla(expresion)


def test_tablas_aplica_limites(tablas):
    with pytest.raises(ErrorValidacion, match="longitud"):
        tablas.generar_tabla("A OR " * 60 + "A")
    with pytest.raises(ErrorValidacion, match="4 variables"):
        tablas.generar_tabla("A OR B OR C OR D OR E")
    with pytest.raises(ErrorValidacion, match="profundidad|compleja"):
        tablas.generar_tabla("NOT " * 40 + "A")
