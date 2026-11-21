"""
Configuración y obtención de loggers para la aplicación ChuspaCalc.
"""

import logging
import sys


def configurar_logging(nivel: str = "INFO") -> None:
    """
    Configura el logger principal de ChuspaCalc.

    Establece el nivel de logging y agrega un handler de consola
    con un formato estándar si todavía no existe uno.

    Args:
        nivel: Nombre del nivel de logging. Por defecto es "INFO".
            Si el nivel no existe, se utiliza logging.INFO.

    Returns:
        None
    """
    # Usamos "chuspacalc" como el logger raíz según el requerimiento
    logger_raiz = logging.getLogger("chuspacalc")

    # Convertir el nivel de string a constante de logging
    numeric_level = getattr(logging, nivel.upper(), logging.INFO)
    logger_raiz.setLevel(numeric_level)

    # Idempotencia: evitar duplicar handlers
    if not logger_raiz.handlers:
        handler = logging.StreamHandler(sys.stderr)

        # Formato: [YYYY-MM-DD HH:MM:SS] [NIVEL] [nombre_logger] mensaje
        formato = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        handler.setFormatter(formato)
        logger_raiz.addHandler(handler)


def obtener_logger(nombre: str) -> logging.Logger:
    """
    Obtiene un logger identificado por su nombre.

    Args:
        nombre: Nombre que identifica al logger.

    Returns:
        El logger solicitado.
    """
    # Wrapper para mantener la API consistente
    return logging.getLogger(nombre)
