"""Pruebas de validación de herramienta_tabla_ascii."""

from unittest.mock import MagicMock

import pytest

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.sistemas.herramienta_tabla_ascii import (
    HerramientaTablaAscii,
    leer_codigo_ascii,
)


@pytest.mark.parametrize("texto, esperado", [("0", 0), ("65", 65), (" 127 ", 127)])
def test_leer_codigo_valido(texto, esperado):
    assert leer_codigo_ascii(texto, "Código") == esperado


@pytest.mark.parametrize(
    "texto", ["", "   ", "abc", "6.5", "nan", "inf", "-1", "128", "9" * 5000, None, 65]
)
def test_leer_codigo_invalido(texto):
    with pytest.raises(ErrorValidacion, match="Código"):
        leer_codigo_ascii(texto, "Código")


def _herramienta(**textos: str) -> HerramientaTablaAscii:
    herramienta = HerramientaTablaAscii()
    for atributo in ("_error_label", "_resultado_codigo", "_tabla"):
        setattr(herramienta, atributo, MagicMock())
    for atributo, texto in textos.items():
        campo = MagicMock()
        campo.text.return_value = texto
        setattr(herramienta, atributo, campo)
    return herramienta


def test_convertir_codigo_muestra_error_descriptivo():
    herramienta = _herramienta(_input_codigo="abc")
    herramienta._convertir_codigo()
    herramienta._error_label.setText.assert_called_with(
        "El valor de 'Código' debe ser un número entero."
    )
    herramienta._resultado_codigo.setText.assert_called_with("")


@pytest.mark.parametrize(
    "inicio, fin, mensaje",
    [
        ("", "10", "Ingrese un valor en 'Desde'."),
        ("0", "200", "El valor de 'Hasta' debe estar entre 0 y 127."),
        ("10", "5", "inicio no puede ser mayor que fin"),
    ],
)
def test_listar_rango_muestra_error_descriptivo(inicio, fin, mensaje):
    herramienta = _herramienta(_input_inicio=inicio, _input_fin=fin)
    herramienta._listar_rango()
    herramienta._error_label.setText.assert_called_with(mensaje)
    herramienta._tabla.setRowCount.assert_called_once_with(0)
