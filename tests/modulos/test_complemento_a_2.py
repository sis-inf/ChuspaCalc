"""
Tests unitarios para las funciones de complemento a 2.
"""

import pytest

from chuspacalc.modulos.sistemas.complemento_a_2 import (
    complemento_a_decimal,
    decimal_a_complemento,
)


def test_positivo_8_bits():
    # 5 en 8 bits es 00000101
    assert decimal_a_complemento(5, 8) == "00000101"


def test_negativo_8_bits():
    # -5 en complemento a 2 con 8 bits es 11111011
    assert decimal_a_complemento(-5, 8) == "11111011"


def test_maximo_8_bits():
    # 127 es el máximo positivo en 8 bits
    assert decimal_a_complemento(127, 8) == "01111111"


def test_minimo_8_bits():
    # -128 es el mínimo negativo en 8 bits
    assert decimal_a_complemento(-128, 8) == "10000000"


def test_overflow_positivo_lanza_error():
    # 128 supera el rango de 8 bits
    with pytest.raises(ValueError):
        decimal_a_complemento(128, 8)


def test_overflow_negativo_lanza_error():
    # -129 supera el rango de 8 bits
    with pytest.raises(ValueError):
        decimal_a_complemento(-129, 8)


def test_binario_negativo_a_decimal():
    # 11111011 en complemento a 2 con 8 bits es -5
    assert complemento_a_decimal("11111011", 8) == -5


def test_binario_positivo_a_decimal():
    # 01111111 en complemento a 2 con 8 bits es 127
    assert complemento_a_decimal("01111111", 8) == 127


def test_longitud_incorrecta_lanza_error():
    # "100" tiene 3 bits pero se espera 8
    with pytest.raises(ValueError):
        complemento_a_decimal("100", 8)


def test_caracter_invalido_lanza_error():
    # "1234" contiene caracteres no binarios
    with pytest.raises(ValueError):
        complemento_a_decimal("1234", 8)


def test_4_bits():
    # Prueba con ancho de 4 bits
    assert decimal_a_complemento(7, 4) == "0111"
    assert decimal_a_complemento(-8, 4) == "1000"


def test_16_bits():
    # Prueba con ancho de 16 bits
    assert decimal_a_complemento(1000, 16) == "0000001111101000"
    assert complemento_a_decimal("0000001111101000", 16) == 1000
