"""
Herramientas para cálculo de divisor de tensión resistivo.
"""


def calcular_tension_salida(v_entrada, r1, r2):
    """
    Calcula la tensión de salida de un divisor resistivo.

    Fórmula:
        Vout = Vin * R2 / (R1 + R2)
    """

    if v_entrada <= 0:
        raise ValueError("v_entrada debe ser positiva")

    if r1 <= 0 or r2 <= 0:
        raise ValueError("Las resistencias deben ser positivas")

    v_salida = v_entrada * r2 / (r1 + r2)

    return {
        "v_entrada": v_entrada,
        "r1": r1,
        "r2": r2,
        "v_salida": v_salida,
        "unidad": "V",
    }


def calcular_r2_para_tension(v_entrada, v_salida, r1):
    """
    Calcula el valor de R2 necesario para obtener
    una tensión de salida deseada.
    """

    if v_entrada <= 0:
        raise ValueError("v_entrada debe ser positiva")

    if r1 <= 0:
        raise ValueError("r1 debe ser positiva")

    if v_salida <= 0 or v_salida >= v_entrada:
        raise ValueError("v_salida debe ser positiva y menor que v_entrada")

    r2 = (v_salida * r1) / (v_entrada - v_salida)

    return {
        "v_entrada": v_entrada,
        "v_salida": v_salida,
        "r1": r1,
        "r2": r2,
        "unidad": "ohm",
    }
