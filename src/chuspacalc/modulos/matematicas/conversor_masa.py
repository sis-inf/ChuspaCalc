"""Conversión de unidades de masa."""

import math

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def convertir_masa(
    valor: int | float,
    unidad_origen: str,
    unidad_destino: str,
) -> float:
    """Convierte una masa entre unidades utilizando kilogramos como base.

    Args:
        valor: Masa que se desea convertir. Debe ser finita y no negativa.
        unidad_origen: Unidad de la masa original.
        unidad_destino: Unidad a la que se desea convertir.

    Returns:
        Masa convertida como número decimal.

    Raises:
        ErrorValidacion: Si el valor o las unidades no son válidos,
            o si el resultado no es finito.
    """
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise ErrorValidacion("El valor de entrada debe ser numérico y no booleano.")

    try:
        valor_finito = math.isfinite(valor)
    except (OverflowError, TypeError):
        valor_finito = False

    if not valor_finito:
        raise ErrorValidacion(f"El valor de entrada debe ser finito: {valor}")

    if valor < 0:
        raise ErrorValidacion(
            f"La masa no puede ser negativa (valor recibido: {valor})"
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

    if not isinstance(unidad_origen, str) or unidad_origen not in factores:
        raise ErrorValidacion(
            f"Unidad de origen desconocida: {unidad_origen}. "
            f"Unidades válidas: {list(factores.keys())}"
        )

    if not isinstance(unidad_destino, str) or unidad_destino not in factores:
        raise ErrorValidacion(
            f"Unidad de destino desconocida: {unidad_destino}. "
            f"Unidades válidas: {list(factores.keys())}"
        )

    valor_kg = valor * factores[unidad_origen]

    if not math.isfinite(valor_kg):
        raise ErrorValidacion("El resultado intermedio de la conversión no es finito.")

    resultado = valor_kg / factores[unidad_destino]

    if not math.isfinite(resultado):
        raise ErrorValidacion("El resultado de la conversión no es finito.")

    return resultado
