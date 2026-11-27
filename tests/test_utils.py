import logging
from pathlib import Path

import pytest
from PySide6.QtWidgets import QApplication

from chuspacalc.utils.converter import (
    celsius_to_fahrenheit,
    km_to_miles,
)
from chuspacalc.utils.helpers import (
    copiar_al_portapapeles,
    exportar_a_archivo,
    formatear_numero,
    leer_archivo,
    validar_numero,
)
from chuspacalc.utils.logging_config import configurar_logging, obtener_logger


def test_converter_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(80) == 176.0


def test_converter_km_to_miles():
    assert km_to_miles(4) == 2.485484


def test_formatear_numero_con_decimales():
    assert formatear_numero(1234.5678, 2) == "1,234.57"


def test_formatear_numero_sin_decimales():
    assert formatear_numero(1234.5678, 0) == "1,235"


def test_configurar_logging_crea_logger_funcional():
    configurar_logging("INFO")

    logger = obtener_logger("chuspacalc")

    assert logger is not None
    assert logger.level == logging.INFO


@pytest.mark.parametrize(
    "texto",
    ["nan", "NaN", "inf", "-inf", "+inf", "Infinity", "-infinity"],
)
def test_validar_numero_rechaza_no_finitos(texto: str) -> None:
    assert validar_numero(texto) is False


@pytest.mark.parametrize(
    "texto",
    ["nan", "inf", "-inf"],
)
def test_validar_numero_rechaza_no_finitos_con_flags(texto: str) -> None:
    assert validar_numero(texto, permitir_negativo=False) is False
    assert validar_numero(texto, permitir_decimal=False) is False


@pytest.mark.parametrize(
    "texto",
    ["0", "5", "-5", "3.5", "-3.5", "1e3"],
)
def test_validar_numero_acepta_finitos(texto: str) -> None:
    assert validar_numero(texto) is True


def test_validar_numero_respeta_permitir_negativo() -> None:
    assert validar_numero("-5", permitir_negativo=False) is False
    assert validar_numero("5", permitir_negativo=False) is True


def test_validar_numero_respeta_permitir_decimal() -> None:
    assert validar_numero("3.5", permitir_decimal=False) is False
    assert validar_numero("3", permitir_decimal=False) is True


def test_validar_numero_rechaza_texto_invalido() -> None:
    assert validar_numero("abc") is False
    assert validar_numero("") is False


def test_exportar_y_leer_archivo_conserva_unicode(tmp_path: Path) -> None:
    contenido = "áéíóú ñ Ω 你好 😀 °C"
    ruta = tmp_path / "subcarpeta" / "unicode.txt"

    exportar_a_archivo(contenido, ruta)

    assert ruta.read_bytes().decode("utf-8") == contenido
    assert leer_archivo(ruta) == contenido


def test_copiar_al_portapapeles_sin_qapplication(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class SinInstancia:
        @staticmethod
        def instance() -> None:
            return None

    monkeypatch.setattr("PySide6.QtWidgets.QApplication", SinInstancia)

    with pytest.raises(RuntimeError, match="No hay QApplication activa"):
        copiar_al_portapapeles("texto")


def test_copiar_al_portapapeles_con_qapplication(app_qt: QApplication) -> None:
    portapapeles = app_qt.clipboard()
    previo = portapapeles.text()

    try:
        copiar_al_portapapeles("texto de prueba áéí")
        assert portapapeles.text() == "texto de prueba áéí"
    finally:
        portapapeles.setText(previo)
