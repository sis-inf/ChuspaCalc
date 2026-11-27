import math

from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
    validar_rango,
)


def calcular_punto_equilibrio(
    costos_fijos: float, precio_unitario: float, costo_variable: float
) -> float:
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
        ErrorValidacion: Si algún argumento no es numérico o no es finito,
            si los costos fijos son negativos, si el margen de
            contribución es cero o negativo, o si el resultado no es
            finito.
    """
    fijos = validar_rango(costos_fijos, "costos_fijos", minimo=0)
    precio = validar_numero(precio_unitario, "precio_unitario")
    variable = validar_numero(costo_variable, "costo_variable")

    margen_contribucion = precio - variable

    if not math.isfinite(margen_contribucion):
        raise ErrorValidacion("El margen de contribución no es finito.")

    if margen_contribucion <= 0:
        raise ErrorValidacion(
            "El precio unitario debe ser mayor que el costo variable."
        )

    punto_equilibrio = fijos / margen_contribucion

    if not math.isfinite(punto_equilibrio):
        raise ErrorValidacion("El punto de equilibrio calculado no es finito.")

    return punto_equilibrio
