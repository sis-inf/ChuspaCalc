import pytest

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.matematicas.progresion_aritmetica import (
    calcular_termino_aritmetico as calc,
)


def test_caso_base():
    assert calc(2, 3, 4) == 11


@pytest.mark.parametrize("posicion", [0, -1, True, False])
def test_posicion_invalida(posicion):
    with pytest.raises(ErrorValidacion):
        calc(2, 3, posicion)


@pytest.mark.parametrize("malo", [float("inf"), float("-inf"), float("nan")])
def test_operandos_no_finitos(malo):
    with pytest.raises(ErrorValidacion):
        calc(malo, 3, 4)
    with pytest.raises(ErrorValidacion):
        calc(2, malo, 4)


def test_resultado_no_finito():
    with pytest.raises(ErrorValidacion):
        calc(1e308, 1e308, 10)


def test_resultado_entero_gigante():
    with pytest.raises(ErrorValidacion):
        calc(10**200, 10**200, 10**200)
