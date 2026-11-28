"""Pruebas de validación de tipos y dominio para karnaugh."""

import pytest

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.sistemas.karnaugh import (
    generar_mapa_karnaugh,
    simplificar_expresion,
)


def test_entrada_valida_conserva_resultado():
    assert generar_mapa_karnaugh([0, 1, 1, 0], 2) == [0, 1, 1, 0]
    assert simplificar_expresion([0, 1, 1, 0]) == "A'B + AB'"
    assert simplificar_expresion([[0, 1], [1, 0]]) == "A'B + AB'"


@pytest.mark.parametrize("variables", ["2", None, True, 2.0, [2]])
def test_num_variables_no_entero_lanza_error_validacion(variables):
    with pytest.raises(ErrorValidacion, match="num_variables debe ser un entero"):
        generar_mapa_karnaugh([0, 1, 1, 0], variables)


@pytest.mark.parametrize("tabla", [None, "0110", (0, 1, 1, 0), 5, {0: 1}])
def test_tabla_no_lista_lanza_error_validacion(tabla):
    with pytest.raises(ErrorValidacion, match="debe ser una lista"):
        generar_mapa_karnaugh(tabla, 2)


@pytest.mark.parametrize("mapa", [None, "0110", (0, 1, 1, 0), 5])
def test_mapa_no_lista_lanza_error_validacion(mapa):
    with pytest.raises(ErrorValidacion, match="El mapa debe ser una lista"):
        simplificar_expresion(mapa)


@pytest.mark.parametrize("valor", [float("nan"), float("inf"), -1, 2, "1", None])
def test_valores_no_booleanos_lanzan_error_validacion(valor):
    with pytest.raises(ErrorValidacion, match="Solo se admiten 0 y 1"):
        simplificar_expresion([0, 1, valor, 0])
    with pytest.raises(ErrorValidacion, match="Solo se admiten 0 y 1"):
        generar_mapa_karnaugh([0, 1, valor, 0], 2)


@pytest.mark.parametrize("variables", [1, 5, 0, -2])
def test_variables_fuera_de_rango_lanzan_error_validacion(variables):
    with pytest.raises(ErrorValidacion, match="entre 2 y 4 variables"):
        generar_mapa_karnaugh([0, 1], variables)


def test_longitud_y_forma_invalidas_lanzan_error_validacion():
    with pytest.raises(ErrorValidacion, match="debe tener 8 valores"):
        generar_mapa_karnaugh([0, 1, 1, 0], 3)
    with pytest.raises(ErrorValidacion, match="4, 8 o 16 valores"):
        simplificar_expresion([0, 1, 1])
    with pytest.raises(ErrorValidacion, match="2x2, 2x4 o 4x4"):
        simplificar_expresion([[0, 1, 0], [1, 0, 1], [0, 0, 0]])


def test_error_validacion_sigue_siendo_value_error():
    with pytest.raises(ValueError):
        simplificar_expresion([])
