
"""
Calculadora de reactancia capacitiva.

Calcula la oposición de un condensador al paso de corriente alterna.

Fórmula:
    Xc = 1 / (2 * pi * f * C)

Donde:
    f: Frecuencia en hercios (Hz).
    C: Capacitancia en faradios (F).
    Xc: Reactancia capacitiva en ohmios.
"""

import math


def calcular_reactancia_capacitiva(frecuencia, capacitancia):
    """
    Calcula la reactancia capacitiva de un condensador.

    Args:
        frecuencia: Frecuencia de la señal en hercios.
        capacitancia: Capacitancia del condensador en faradios.

    Returns:
        Reactancia capacitiva en ohmios.

    Raises:
        TypeError: Si los argumentos no son numéricos.
        ValueError: Si los valores no son positivos, finitos
            o si el resultado no es finito.
    """
    valores = (frecuencia, capacitancia)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("La frecuencia y la capacitancia deben ser números.")

        try:
            if not math.isfinite(valor):
                raise ValueError("Los valores deben ser finitos.")
        except OverflowError as error:
            raise ValueError("Los valores deben ser finitos.") from error

        if valor <= 0:
            raise ValueError("La frecuencia y la capacitancia deben ser mayores que cero.")

    try:
        denominador = 2 * math.pi * frecuencia * capacitancia

        if not math.isfinite(denominador) or denominador <= 0:
            raise ValueError("No se puede calcular un resultado finito.")

        reactancia = 1 / denominador

    except (OverflowError, ZeroDivisionError) as error:
        raise ValueError("No se pudo calcular la reactancia capacitiva.") from error

    if not math.isfinite(reactancia) or reactancia <= 0:
        raise ValueError("La reactancia debe ser un número positivo y finito.")

    return reactancia
