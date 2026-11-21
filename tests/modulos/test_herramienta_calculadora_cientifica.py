import pytest

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.matematicas.herramienta_calculadora_cientifica import (
    HerramientaCalculadoraCientifica,
)


@pytest.fixture
def calculadora() -> HerramientaCalculadoraCientifica:
    return HerramientaCalculadoraCientifica()


@pytest.mark.parametrize("valor", [None, 123, 4.5, ["1+1"], True])
def test_rechaza_expresion_no_texto(calculadora, valor):
    with pytest.raises(ErrorValidacion, match="cadena de texto"):
        calculadora.evaluar_expresion(valor)


@pytest.mark.parametrize("valor", ["", "   ", "\t"])
def test_rechaza_expresion_vacia(calculadora, valor):
    with pytest.raises(ErrorValidacion, match="vacía"):
        calculadora.evaluar_expresion(valor)


@pytest.mark.parametrize("modo", ["Gradianes", "radianes", "", "GRADOS"])
def test_rechaza_modo_angular_invalido(calculadora, modo):
    with pytest.raises(ErrorValidacion, match="modo angular"):
        calculadora.evaluar_expresion("sin(1)", modo)


@pytest.mark.parametrize(
    ("expresion", "funcion"),
    [
        ("sqrt(-1)", "sqrt"),
        ("log(0)", "log"),
        ("log(-3)", "log"),
        ("ln(0)", "ln"),
        ("ln(-5)", "ln"),
    ],
)
def test_dominio_de_funciones_lanza_error_validacion(calculadora, expresion, funcion):
    with pytest.raises(ErrorValidacion, match=f"dominio de {funcion}"):
        calculadora.evaluar_expresion(expresion)


def test_division_por_cero_se_conserva(calculadora):
    with pytest.raises(ZeroDivisionError, match="División por cero"):
        calculadora.evaluar_expresion("1 / 0")


def test_resultado_fuera_de_limite_lanza_error_validacion(calculadora):
    with pytest.raises(ErrorValidacion, match="límite"):
        calculadora.evaluar_expresion("1e100 * 10")


def test_errores_siguen_siendo_value_error(calculadora):
    with pytest.raises(ValueError):
        calculadora.evaluar_expresion("sqrt(-4)")


def test_casos_validos_no_se_afectan(calculadora):
    assert calculadora.evaluar_expresion("sqrt(9)") == pytest.approx(3.0)
    assert calculadora.evaluar_expresion("sin(90)", "Grados") == pytest.approx(1.0)
