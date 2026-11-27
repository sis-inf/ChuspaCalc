"""
Tests unitarios para las funciones de conversión de bases numéricas.
"""

import pytest

from chuspacalc.modulos.sistemas.herramienta_conversion_bases import (
    convertir_desde_decimal,
    parsear_valor,
)


def test_decimal_255_a_binario():
    # 255 en binario es 11111111
    resultado = convertir_desde_decimal(255)
    assert resultado["binario"] == "11111111"


def test_decimal_255_a_octal():
    # 255 en octal es 377
    resultado = convertir_desde_decimal(255)
    assert resultado["octal"] == "377"


def test_decimal_255_a_hexadecimal():
    # 255 en hexadecimal es FF
    resultado = convertir_desde_decimal(255)
    assert resultado["hexadecimal"] == "FF"


def test_decimal_0_todas_las_bases():
    # 0 en todas las bases es 0
    resultado = convertir_desde_decimal(0)
    assert resultado["binario"] == "0"
    assert resultado["octal"] == "0"
    assert resultado["hexadecimal"] == "0"


def test_decimal_negativo():
    # -10 debe mostrar signo en las otras bases
    resultado = convertir_desde_decimal(-10)
    assert resultado["binario"] == "-1010"
    assert resultado["octal"] == "-12"
    assert resultado["hexadecimal"] == "-A"


def test_binario_a_decimal():
    # 1010 en binario es 10 en decimal
    assert parsear_valor("1010", 2) == 10


def test_hexadecimal_a_decimal():
    # FF en hexadecimal es 255 en decimal
    assert parsear_valor("FF", 16) == 255


def test_octal_a_decimal():
    # 777 en octal es 511 en decimal
    assert parsear_valor("777", 8) == 511


def test_caracter_invalido_lanza_error():
    # Un caracter invalido para la base debe lanzar ValueError
    with pytest.raises(ValueError):
        parsear_valor("2", 2)
