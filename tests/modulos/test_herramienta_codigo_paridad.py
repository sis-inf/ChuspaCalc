"""Pruebas unitarias para herramienta_codigo_paridad."""

import pytest

from escuadra.modulos.sistemas.herramienta_codigo_paridad import (
    ejecutar_calculo_paridad,
)


def test_paridad_par_con_1011_devuelve_bit_1_y_datos_validos():
    resultado = ejecutar_calculo_paridad("1011")
    assert resultado["bit_paridad"] == 1
    assert resultado["datos_con_paridad"] == "10111"
    assert resultado["valido"] is True


def test_paridad_impar_con_1010_devuelve_bit_1_y_datos_con_paridad():
    resultado = ejecutar_calculo_paridad("1010", tipo="impar")
    assert resultado["bit_paridad"] == 1
    assert resultado["datos_con_paridad"] == "10101"


def test_resultado_contiene_todas_las_claves_esperadas():
    resultado = ejecutar_calculo_paridad("1011")
    claves_esperadas = {
        "datos_originales",
        "tipo_paridad",
        "bit_paridad",
        "datos_con_paridad",
        "valido",
    }
    assert claves_esperadas.issubset(resultado.keys())


def test_cadena_no_binaria_lanza_value_error():
    with pytest.raises(ValueError):
        ejecutar_calculo_paridad("10a1")
