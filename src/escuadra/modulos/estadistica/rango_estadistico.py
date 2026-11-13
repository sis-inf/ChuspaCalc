
import math


def calcular_rango(datos):
    """
    Calcula el rango estadístico de una lista de datos numéricos.

    Args:
        datos: Lista de números reales.

    Returns:
        Diferencia entre el valor máximo y el mínimo.

    Raises:
        TypeError: Si los datos no son una lista o contienen
                   elementos que no son números reales.
        ValueError: Si la lista está vacía o contiene valores
                    no finitos.
    """
    if not isinstance(datos, list):
        raise TypeError("Los datos deben proporcionarse en una lista.")

    if not datos:
        raise ValueError("La lista de datos no puede estar vacía.")

    for valor in datos:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Todos los elementos deben ser números reales.")

        if not math.isfinite(valor):
            raise ValueError("Todos los valores deben ser finitos.")

    valor_maximo = max(datos)
    valor_minimo = min(datos)

    return valor_maximo - valor_minimo
