def calcular_ohm(
    voltaje=None,
    corriente=None,
    resistencia=None,
) -> dict:
    valores = [voltaje, corriente, resistencia]

    if valores.count(None) != 1:
        raise ValueError("Debe proporcionar exactamente dos parámetros")

    if resistencia == 0:
        raise ValueError("La resistencia no puede ser cero")

    if voltaje is None:
        voltaje = corriente * resistencia

    elif corriente is None:
        corriente = voltaje / resistencia

    else:
        if corriente == 0:
            raise ValueError("La corriente no puede ser cero")

        resistencia = voltaje / corriente

    return {
        "voltaje": voltaje,
        "unidad_v": "V",
        "corriente": corriente,
        "unidad_i": "A",
        "resistencia": resistencia,
        "unidad_r": "Ω",
    }
