import logging

from escuadra.utils.converter import (
    celsius_to_fahrenheit,
    km_to_miles,
)
from escuadra.utils.helpers import formatear_numero
from escuadra.utils.logging_config import configurar_logging, obtener_logger


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

    logger = obtener_logger("escuadra")

    assert logger is not None
    assert logger.level == logging.INFO
