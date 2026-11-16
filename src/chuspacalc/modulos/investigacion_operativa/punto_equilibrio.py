
import math
from numbers import Real


def calcular_punto_equilibrio(costos_fijos, precio_unitario, costo_variable):
    """
    Calcula el punto de equilibrio de una actividad económica.

    Args:
        costos_fijos: Costos fijos totales.
        precio_unitario: Precio de venta de cada unidad.
        costo_variable: Costo variable por unidad.

    Returns:
        float: Cantidad de unidades necesarias para alcanzar
        el punto de equilibrio.

    Raises:
        TypeError: Si algún argumento no es numérico.
        ValueError: Si los valores no son finitos, los costos fijos
                    son negativos o el margen de contribución
                    es cero o negativo.
    """
    valores = (costos_fijos, precio_unitario, costo_variable)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, Real):
            raise TypeError("Todos los argumentos deben ser numéricos.")

        if not math.isfinite(valor):
            raise ValueError("Todos los argumentos deben ser finitos.")

    if costos_fijos < 0:
        raise ValueError("Los costos fijos no pueden ser negativos.")

    margen_contribucion = precio_unitario - costo_variable

    if margen_contribucion <= 0:
        raise ValueError(
            "El precio unitario debe ser mayor que el costo variable."
        )

    punto_equilibrio = costos_fijos / margen_contribucion

    return punto_equilibrio
