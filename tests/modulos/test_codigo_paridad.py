"""
Tests unitarios para las funciones de código de paridad.
"""

import pytest

from escuadra.modulos.sistemas.codigo_paridad import (
    calcular_bit_paridad,
    verificar_paridad,
)


def test_calcular_bit_paridad_par():
    # "101" tiene dos unos (cantidad par), el bit de paridad par es 0
    assert calcular_bit_paridad("101", "par") == 0


def test_calcular_bit_paridad_impar():
    # "101" tiene dos unos (cantidad par), el bit de paridad impar es 1
    assert calcular_bit_paridad("101", "impar") == 1


def test_verificar_paridad_par_correcta():
    # "1010" tiene dos unos (cantidad par), cumple la paridad par
    assert verificar_paridad("1010", "par") is True


def test_verificar_paridad_par_incorrecta():
    # "1011" tiene tres unos (cantidad impar), no cumple la paridad par
    assert verificar_paridad("1011", "par") is False


def test_calcular_bit_paridad_tipo_invalido_lanza_error():
    with pytest.raises(ValueError):
        calcular_bit_paridad("101", "mixto")


def test_verificar_paridad_tipo_invalido_lanza_error():
    with pytest.raises(ValueError):
        verificar_paridad("1010", "mixto")
