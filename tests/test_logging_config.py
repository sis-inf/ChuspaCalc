import logging

from chuspacalc.utils.logging_config import configurar_logging, obtener_logger


def test_configurar_logging_debug():
    configurar_logging("DEBUG")

    logger = logging.getLogger("chuspacalc")

    assert logger.level == logging.DEBUG


def test_configurar_logging_nivel_invalido():
    configurar_logging("XYZ")

    logger = logging.getLogger("chuspacalc")

    assert logger.level == logging.INFO


def test_configurar_logging_no_duplica_handlers():
    logger = logging.getLogger("chuspacalc")

    antes = len(logger.handlers)

    configurar_logging("INFO")
    configurar_logging("INFO")

    assert len(logger.handlers) == antes


def test_configurar_logging_formato_handler():
    logger = logging.getLogger("chuspacalc")

    if not logger.handlers:
        configurar_logging("INFO")

    h = logger.handlers[0]
    fmt = h.formatter._fmt

    assert "%(asctime)s" in fmt
    assert "%(levelname)s" in fmt
    assert "%(name)s" in fmt


def test_obtener_logger_devuelve_mismo_logger():
    logger = obtener_logger("chuspacalc.prueba")

    assert logger is logging.getLogger("chuspacalc.prueba")
