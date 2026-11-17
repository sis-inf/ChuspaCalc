
"""
Calculadora de frecuencia relativa.
"""


def calcular_frecuencia_relativa(datos, valor):
    """
    Calcula la frecuencia relativa de un valor en un conjunto de datos.

    Args:
        datos: Lista de observaciones.
        valor: Valor cuya frecuencia relativa se desea calcular.

    Returns:
        Proporcion de apariciones del valor respecto al total.
    """
    if not isinstance(datos, (list, tuple)):
        raise TypeError("Los datos deben ser una lista o tupla.")

    if not datos:
        raise ValueError("El conjunto de datos no puede estar vacio.")

    frecuencia_absoluta = sum(1 for elemento in datos if elemento == valor)
    frecuencia_relativa = frecuencia_absoluta / len(datos)

    return frecuencia_relativa
