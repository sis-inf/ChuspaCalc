import math


def convertir_energia(valor, unidad_origen, unidad_destino):
    if not math.isfinite(valor):
        raise ValueError(f"El valor de entrada debe ser finito: {valor}")

    if valor < 0:
        raise ValueError("El valor debe ser mayor o igual a 0")

    factores = {
        "J": 1.0,
        "kJ": 1000.0,
        "MJ": 1000000.0,
        "Wh": 3600.0,
        "kWh": 3600000.0,
        "cal": 4.184,
        "kcal": 4184.0,
        "BTU": 1055.06,
        "eV": 1.602176634e-19,
    }

    if unidad_origen not in factores:
        raise ValueError(
            f"Unidad desconocida: {unidad_origen}. Unidades válidas: {list(factores.keys())}"
        )

    if unidad_destino not in factores:
        raise ValueError(
            f"Unidad desconocida: {unidad_destino}. Unidades válidas: {list(factores.keys())}"
        )

    valor_joules = valor * factores[unidad_origen]

    return valor_joules / factores[unidad_destino]
