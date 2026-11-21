"""Conversión de energía entre distintas unidades de medida."""

import math

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def convertir_energia(
    valor: int | float,
    unidad_origen: str,
    unidad_destino: str,
) -> float:
    """Convierte una cantidad de energía entre unidades.

    Utiliza julios (J) como unidad base.

    Args:
        valor: Cantidad de energía, mayor o igual a cero.
        unidad_origen: Unidad de la cantidad inicial.
        unidad_destino: Unidad a la que se desea convertir.

    Returns:
        Cantidad de energía convertida como float.

    Raises:
        ErrorValidacion: Si el valor o alguna unidad no es válida,
            o si el resultado no es finito.
    """
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise ErrorValidacion("El valor debe ser un número entero o decimal.")

    try:
        valor_finito = math.isfinite(valor)
    except OverflowError as exc:
        raise ErrorValidacion(
            "El valor de entrada está fuera del rango permitido."
        ) from exc

    if not valor_finito:
        raise ErrorValidacion(f"El valor de entrada debe ser finito: {valor}")

    if valor < 0:
        raise ErrorValidacion(
            f"La energía no puede ser negativa (valor recibido: {valor})"
        )

    factores: dict[str, float] = {
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

    if not isinstance(unidad_origen, str) or unidad_origen not in factores:
        raise ErrorValidacion(f"Unidad de origen desconocida: {unidad_origen}")

    if not isinstance(unidad_destino, str) or unidad_destino not in factores:
        raise ErrorValidacion(f"Unidad de destino desconocida: {unidad_destino}")

    try:
        valor_joules = valor * factores[unidad_origen]
        resultado = valor_joules / factores[unidad_destino]
    except OverflowError as exc:
        raise ErrorValidacion(
            "El resultado de la conversión está fuera del rango permitido."
        ) from exc

    if not math.isfinite(resultado):
        raise ErrorValidacion("El resultado de la conversión no es un número finito.")

    return resultado
