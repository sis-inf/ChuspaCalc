"""
Tests unitarios para la función convertir() del módulo
conversor_bases, verificando conversiones entre bases soportadas
y el manejo de entradas inválidas.
"""

import pytest

from chuspacalc.modulos.sistemas.conversor_bases import convertir


def test_decimal_a_binario():
    assert convertir("10", 10, 2)["resultado"] == "1010"


def test_binario_a_decimal():
    assert convertir("1010", 2, 10)["resultado"] == "10"


def test_hexadecimal_a_decimal():
    assert convertir("F", 16, 10)["resultado"] == "15"


def test_octal_a_decimal():
    assert convertir("17", 8, 10)["resultado"] == "15"


def test_decimal_a_hexadecimal():
    assert convertir("10", 10, 16)["resultado"] == "A"


def test_octal_a_binario():
    assert convertir("12", 8, 2)["resultado"] == "1010"


def test_base_origen_no_soportada():
    with pytest.raises(ValueError):
        convertir("10", 5, 10)


def test_base_destino_no_soportada():
    with pytest.raises(ValueError):
        convertir("10", 10, 5)


def test_digito_invalido_para_base():
    with pytest.raises(ValueError):
        convertir("102", 2, 10)


def test_numero_vacio():
    with pytest.raises(ValueError):
        convertir("", 10, 2)


def test_resultado_contiene_metadatos():
    resultado = convertir("10", 10, 2)

    assert resultado["numero_original"] == "10"
    assert resultado["base_origen"] == 10
    assert resultado["base_destino"] == 2
