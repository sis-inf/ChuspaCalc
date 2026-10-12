import logging
import sys


def configurar_logging(nivel="INFO"):
    # Usamos "escuadra" como el logger raíz según el requerimiento
    logger_raiz = logging.getLogger("escuadra")

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


def obtener_logger(nombre):
    # Wrapper para mantener la API consistente
    return logging.getLogger(nombre)
