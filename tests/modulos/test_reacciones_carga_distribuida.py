"""Pruebas de validación para reacciones_carga_distribuida."""

import pytest

from chuspacalc.modulos.civil.reacciones_carga_distribuida import (
    calcular_reacciones_carga_distribuida as calcular,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def test_entrada_valida_reparte_por_igual():
    assert calcular(10, 4) == (20.0, 20.0)
    assert calcular(2.5, 2) == (2.5, 2.5)


@pytest.mark.parametrize("invalido", ["10", None, True, [1]])
def test_carga_no_numerica_lanza_error_validacion(invalido):
    with pytest.raises(ErrorValidacion, match="La carga distribuida debe ser numérica"):
        calcular(invalido, 4)


@pytest.mark.parametrize("invalido", ["4", None, True, [1]])
def test_longitud_no_numerica_lanza_error_validacion(invalido):
    with pytest.raises(ErrorValidacion, match="La longitud debe ser numérica"):
        calcular(10, invalido)


@pytest.mark.parametrize("no_finito", [float("nan"), float("inf"), float("-inf")])
def test_no_finitos_lanzan_error_validacion(no_finito):
    with pytest.raises(ErrorValidacion, match="La carga distribuida debe ser finita"):
        calcular(no_finito, 4)
    with pytest.raises(ErrorValidacion, match="La longitud debe ser finita"):
        calcular(10, no_finito)


@pytest.mark.parametrize("valor", [0, -1])
def test_no_positivos_lanzan_error_validacion(valor):
    with pytest.raises(
        ErrorValidacion, match="La carga distribuida debe ser mayor que cero"
    ):
        calcular(valor, 4)
    with pytest.raises(ErrorValidacion, match="La longitud debe ser mayor que cero"):
        calcular(10, valor)


def test_entero_gigante_lanza_error_validacion():
    with pytest.raises(ErrorValidacion, match="demasiado grande"):
        calcular(10**400, 4)


def test_resultado_desbordado_lanza_error_validacion():
    with pytest.raises(ErrorValidacion, match="se desborda"):
        calcular(1e308, 10)


def test_error_validacion_sigue_siendo_value_error():
    with pytest.raises(ValueError):
        calcular(0, 4)
