"""Pruebas de validacion de tipos y dominio para caida_tension."""

import pytest

from chuspacalc.modulos.electrica.caida_tension import calcular_caida
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

VALIDOS = {"longitud": 100, "corriente": 15, "seccion": 4}


def test_entrada_valida_conserva_resultado():
    resultado = calcular_caida(**VALIDOS)
    assert resultado == {
        "caida_v": 12.9,
        "porcentaje": 5.8636,
        "admisible": False,
        "tension_v": 220.0,
    }


@pytest.mark.parametrize("invalido", ["10", None, True, [1]])
@pytest.mark.parametrize("parametro", ["longitud", "corriente", "seccion"])
def test_tipo_no_numerico_lanza_error_validacion(parametro, invalido):
    valores = {**VALIDOS, parametro: invalido}
    with pytest.raises(ErrorValidacion, match=f"'{parametro}' debe ser un numero real"):
        calcular_caida(**valores)


@pytest.mark.parametrize("invalido", ["220", None, True])
def test_tension_y_factor_potencia_no_numericos(invalido):
    with pytest.raises(ErrorValidacion, match="'tension' debe ser un numero real"):
        calcular_caida(**VALIDOS, tension=invalido)
    with pytest.raises(
        ErrorValidacion, match="'factor_potencia' debe ser un numero real"
    ):
        calcular_caida(**VALIDOS, factor_potencia=invalido)


@pytest.mark.parametrize("material", [None, 5, True])
def test_material_no_texto_lanza_error_validacion(material):
    with pytest.raises(ErrorValidacion, match="'material' debe ser texto"):
        calcular_caida(**VALIDOS, material=material)


def test_entero_gigante_lanza_error_validacion():
    with pytest.raises(ErrorValidacion, match="demasiado grande"):
        calcular_caida(10**400, 15, 4)


def test_errores_de_dominio_son_error_validacion():
    with pytest.raises(ErrorValidacion):
        calcular_caida(0, 15, 4)
    with pytest.raises(ErrorValidacion):
        calcular_caida(100, 15, 4, factor_potencia=1.5)
    with pytest.raises(ErrorValidacion):
        calcular_caida(100, 15, 4, material="oro")
    with pytest.raises(ErrorValidacion):
        calcular_caida(float("nan"), 15, 4)
