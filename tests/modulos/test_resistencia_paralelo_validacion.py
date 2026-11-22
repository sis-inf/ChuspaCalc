"""Pruebas de validación y tipado de resistencia_paralelo.py (issue #1971)."""

import inspect
import math

import pytest

from chuspacalc.modulos.electricidad.resistencia_paralelo import (
    calcular_resistencia_paralelo,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def test_error_validacion_es_value_error():
    assert issubclass(ErrorValidacion, ValueError)


def test_valores_validos_siguen_funcionando():
    assert calcular_resistencia_paralelo([10, 10]) == pytest.approx(5.0)
    assert calcular_resistencia_paralelo([10, 20, 30]) == pytest.approx(60 / 11)
    assert calcular_resistencia_paralelo([4.5]) == pytest.approx(4.5)


@pytest.mark.parametrize("entrada", [(10, 20), "10", 5, None, {10, 20}])
def test_rechaza_entrada_que_no_es_lista(entrada):
    with pytest.raises(ErrorValidacion, match="en una lista"):
        calcular_resistencia_paralelo(entrada)


def test_rechaza_lista_vacia():
    with pytest.raises(ErrorValidacion, match="no puede estar vacía"):
        calcular_resistencia_paralelo([])


@pytest.mark.parametrize("valor", ["10", None, True, False, [1], 2 + 1j])
def test_rechaza_elementos_no_numericos(valor):
    with pytest.raises(ErrorValidacion, match="deben ser números"):
        calcular_resistencia_paralelo([10, valor])


@pytest.mark.parametrize("valor", [math.nan, math.inf, -math.inf, 10**400])
def test_rechaza_valores_no_finitos(valor):
    with pytest.raises(ErrorValidacion, match="valores finitos"):
        calcular_resistencia_paralelo([10, valor])


@pytest.mark.parametrize("valor", [0, 0.0, -1, -0.5])
def test_rechaza_cero_y_negativos(valor):
    with pytest.raises(ErrorValidacion, match="mayores que cero"):
        calcular_resistencia_paralelo([10, valor])


def test_rechaza_resistencias_diminutas_que_desbordan_la_conductancia():
    with pytest.raises(ErrorValidacion, match="No se pudo calcular"):
        calcular_resistencia_paralelo([5e-324])


def test_errores_son_capturables_como_value_error():
    with pytest.raises(ValueError):
        calcular_resistencia_paralelo([10, 0])


def test_anotaciones_de_tipo_completas():
    firma = inspect.signature(calcular_resistencia_paralelo)
    assert firma.return_annotation is not inspect.Signature.empty
    for nombre, parametro in firma.parameters.items():
        assert parametro.annotation is not inspect.Parameter.empty, nombre
