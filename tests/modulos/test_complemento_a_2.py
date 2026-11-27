"""
Tests unitarios para las funciones de complemento a 2.
"""

import pytest

from chuspacalc.modulos.sistemas.complemento_a_2 import (
    complemento_a_decimal,
    decimal_a_complemento,
)
from chuspacalc.modulos.sistemas.herramienta_complemento_a_2 import (
    HerramientaComplementoA2,
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


@pytest.mark.parametrize("bits", [4, 8, 16, 32])
def test_limites_por_ancho_de_bits_se_aceptan(bits):
    minimo = -(2 ** (bits - 1))
    maximo = 2 ** (bits - 1) - 1
    binario_minimo = "1" + "0" * (bits - 1)
    binario_maximo = "0" + "1" * (bits - 1)

    assert decimal_a_complemento(minimo, bits) == binario_minimo
    assert decimal_a_complemento(maximo, bits) == binario_maximo
    assert complemento_a_decimal(binario_minimo, bits) == minimo
    assert complemento_a_decimal(binario_maximo, bits) == maximo


@pytest.mark.parametrize("bits", [4, 8, 16, 32])
def test_limites_por_ancho_de_bits_fuera_de_rango_se_rechazan(bits):
    minimo = -(2 ** (bits - 1))
    maximo = 2 ** (bits - 1) - 1

    with pytest.raises(ValueError):
        decimal_a_complemento(minimo - 1, bits)

    with pytest.raises(ValueError):
        decimal_a_complemento(maximo + 1, bits)


def test_binario_invalido_en_widget_muestra_error_sin_cerrar(qtbot):
    herramienta = HerramientaComplementoA2()
    widget = herramienta.crear_widget()
    qtbot.addWidget(widget)
    widget.show()

    herramienta.binario_input.setText("102")
    herramienta._convertir_binario()

    assert herramienta.error_label.text() != ""
    assert herramienta.decimal_output.text() == ""
    assert widget.isVisible()
