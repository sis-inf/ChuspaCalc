import math

import pytest

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.matematicas.numeros_primos import es_numero_primo


def test_dos_es_primo():
    assert es_numero_primo(2) is True


@pytest.mark.parametrize("primo", [3, 5, 7, 11, 13, 97, 7919])
def test_primos_conocidos(primo):
    assert es_numero_primo(primo) is True


@pytest.mark.parametrize("no_primo", [4, 6, 9, 15, 100, 7917])
def test_compuestos_no_son_primos(no_primo):
    assert es_numero_primo(no_primo) is False


@pytest.mark.parametrize("valor", [0, 1, -1, -2, -7, -100])
def test_cero_uno_y_negativos_no_son_primos(valor):
    assert es_numero_primo(valor) is False


@pytest.mark.parametrize(
    "invalido",
    [
        True,
        False,
        2.0,
        2.5,
        math.nan,
        math.inf,
        -math.inf,
        "7",
        "abc",
        None,
        [2],
        2 + 0j,
    ],
)
def test_tipos_invalidos_lanzan_error_validacion(invalido):
    with pytest.raises(ErrorValidacion):
        es_numero_primo(invalido)


def test_error_validacion_sigue_siendo_value_error():
    with pytest.raises(ValueError):
        es_numero_primo("7")
