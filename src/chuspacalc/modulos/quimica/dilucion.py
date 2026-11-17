"""
Calculadora de concentración final después de una dilución.

Fórmula:
    C1 * V1 = C2 * V2
    C2 = (C1 * V1) / V2
"""

import math


def calcular_concentracion_diluida(
    concentracion_inicial, volumen_inicial, volumen_final
):
    """
    Calcula la concentración final de una solución diluida.

    Args:
        concentracion_inicial: Concentración inicial.
        volumen_inicial: Volumen inicial.
        volumen_final: Volumen final.

    Returns:
        La concentración final calculada.

    Raises:
        TypeError: Si algún valor no es numérico.
        ValueError: Si los valores no son positivos, finitos
                    o el volumen final es menor que el inicial.
    """
    valores = (
        concentracion_inicial,
        volumen_inicial,
        volumen_final,
    )

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Todos los valores deben ser numéricos.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Todos los valores deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Los valores deben ser finitos.") from error

        if valor <= 0:
            raise ValueError("Todos los valores deben ser positivos.")

    if volumen_final < volumen_inicial:
        raise ValueError("El volumen final no puede ser menor que el volumen inicial.")

    try:
        concentracion_final = (
            float(concentracion_inicial) * float(volumen_inicial) / float(volumen_final)
        )
    except (OverflowError, ZeroDivisionError) as error:
        raise ValueError("No se pudo calcular un resultado válido.") from error

    if not math.isfinite(concentracion_final):
        raise ValueError("El resultado debe ser finito.")

    return concentracion_final
