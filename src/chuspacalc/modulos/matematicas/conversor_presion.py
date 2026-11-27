import math


def convertir_presion(valor, unidad_origen, unidad_destino):
    """Convierte un valor de presión entre unidades, usando Pa como base.

    Unidades disponibles: Pa, kPa, MPa, bar, mbar, atm, psi, mmHg y torr.

    Args:
        valor (float): Valor a convertir (mayor o igual a 0).
        unidad_origen (str): Unidad del valor de entrada.
        unidad_destino (str): Unidad a la que se convierte.

    Returns:
        float: Valor convertido a la unidad de destino.

    Raises:
        ValueError: Si el valor no es finito, es negativo o alguna unidad es
            desconocida.
    """
    if not math.isfinite(valor):
        raise ValueError(f"El valor de entrada debe ser finito: {valor}")

    if valor < 0:
        raise ValueError("El valor debe ser mayor o igual a 0")

    factores = {
        "Pa": 1.0,
        "kPa": 1000.0,
        "MPa": 1000000.0,
        "bar": 100000.0,
        "mbar": 100.0,
        "atm": 101325.0,
        "psi": 6894.76,
        "mmHg": 133.322,
        "torr": 133.322,
    }

    if unidad_origen not in factores:
        raise ValueError(
            f"Unidad desconocida: {unidad_origen}. Unidades válidas: {list(factores.keys())}"
        )

    if unidad_destino not in factores:
        raise ValueError(
            f"Unidad desconocida: {unidad_destino}. Unidades válidas: {list(factores.keys())}"
        )

    valor_pa = valor * factores[unidad_origen]

    return valor_pa / factores[unidad_destino]
