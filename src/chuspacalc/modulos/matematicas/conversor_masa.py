import math

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def convertir_masa(valor, unidad_origen, unidad_destino):
    if not math.isfinite(valor):
        raise ValueError(f"El valor de entrada debe ser finito: {valor}")

    if valor < 0:
        raise ErrorValidacion(
            f"La masa no puede ser negativa (valor recibido: {valor})",
        )

    factores = {
        "kg": 1.0,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 0.453592,
        "oz": 0.0283495,
        "t": 1000.0,
        "slug": 14.5939,
    }

    if unidad_origen not in factores:
        raise ValueError(
            f"Unidad desconocida: {unidad_origen}. Unidades válidas: {list(factores.keys())}"
        )

    if unidad_destino not in factores:
        raise ValueError(
            f"Unidad desconocida: {unidad_destino}. Unidades válidas: {list(factores.keys())}"
        )

    valor_kg = valor * factores[unidad_origen]

    return valor_kg / factores[unidad_destino]
