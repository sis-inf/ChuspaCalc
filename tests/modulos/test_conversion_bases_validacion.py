"""Pruebas de validación de herramienta_conversion_bases."""

import pytest

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.sistemas.herramienta_conversion_bases import (
    convertir_desde_decimal,
    parsear_valor,
)


@pytest.mark.parametrize(
    "texto, base, esperado",
    [(" -101 ", 2, -5), ("+17", 8, 15), ("-42", 10, -42), ("ff", 16, 255)],
)
def test_valores_validos(texto, base, esperado):
    assert parsear_valor(texto, base) == esperado


@pytest.mark.parametrize(
    "texto, base",
    [
        ("", 10),
        ("-", 2),
        ("--101", 2),
        ("0b101", 2),
        ("0xFF", 16),
        ("1_000", 10),
        ("nan", 10),
        ("inf", 10),
        ("1.5", 10),
        ("9" * 5000, 10),
        (None, 10),
    ],
)
def test_textos_invalidos(texto, base):
    with pytest.raises(ErrorValidacion):
        parsear_valor(texto, base)


@pytest.mark.parametrize("base", [0, 1, 3, 36, True, 2.0, "2", None])
def test_base_no_soportada(base):
    with pytest.raises(ErrorValidacion, match="Base no soportada"):
        parsear_valor("1", base)


@pytest.mark.parametrize("valor", [True, 1.5, float("nan"), float("inf"), "10", None])
def test_convertir_desde_decimal_rechaza(valor):
    with pytest.raises(ErrorValidacion):
        convertir_desde_decimal(valor)


def test_convertir_desde_decimal_rechaza_entero_enorme():
    with pytest.raises(ErrorValidacion, match="demasiado grande"):
        convertir_desde_decimal(10**5000)
