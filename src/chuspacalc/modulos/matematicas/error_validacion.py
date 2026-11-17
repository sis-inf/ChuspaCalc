"""
Excepción personalizada para errores de validación de rangos físicos.
"""


class ErrorValidacion(ValueError):
    """Excepción para errores de validación de rangos físicos.

    Se usa cuando un valor de entrada no está dentro del rango
    físicamente permitido (ej. temperatura bajo cero absoluto,
    masa o longitud negativas).
    """
