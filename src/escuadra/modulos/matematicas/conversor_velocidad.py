def convertir_velocidad(
    valor,
    unidad_origen,
    unidad_destino,
):
    if valor < 0:
        raise ValueError("La velocidad no puede ser negativa")

    factores = {
        "m/s": 1.0,
        "km/h": 1 / 3.6,
        "mph": 0.44704,
        "nudos": 0.514444,
        "ft/s": 0.3048,
    }

    if unidad_origen not in factores:
        raise ValueError(
            f"Unidad desconocida: {unidad_origen}. "
            f"Unidades válidas: {list(factores.keys())}"
        )

    if unidad_destino not in factores:
        raise ValueError(
            f"Unidad desconocida: {unidad_destino}. "
            f"Unidades válidas: {list(factores.keys())}"
        )

    valor_ms = valor * factores[unidad_origen]

    return valor_ms / factores[unidad_destino]
