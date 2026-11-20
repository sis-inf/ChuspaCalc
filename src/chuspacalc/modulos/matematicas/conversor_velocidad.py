import math

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def convertir_velocidad(
    valor: int | float,
    unidad_origen: str,
    unidad_destino: str,
) -> float:
    """Convierte una velocidad entre unidades utilizando m/s como base.

    Unidades disponibles: m/s, km/h, mph, nudos y ft/s.

    Args:
        valor: Velocidad de entrada, mayor o igual a cero.
        unidad_origen: Unidad del valor de entrada.
        unidad_destino: Unidad a la que se convierte.

    Returns:
        Velocidad convertida a la unidad de destino.

    Raises:
        ErrorValidacion: Si los parámetros o el resultado no son válidos.
    """
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise ErrorValidacion(f"El valor debe ser numérico (recibido: {valor!r})")

    try:
        if not math.isfinite(valor):
            raise ErrorValidacion(f"El valor de entrada debe ser finito: {valor}")
    except OverflowError as exc:
        raise ErrorValidacion(
            "El valor de entrada está fuera del rango numérico permitido"
        ) from exc

    if valor < 0:
        raise ErrorValidacion(
            f"La velocidad no puede ser negativa (valor recibido: {valor})"
        )

    factores: dict[str, float] = {
        "m/s": 1.0,
        "km/h": 1 / 3.6,
        "mph": 0.44704,
        "nudos": 0.514444,
        "ft/s": 0.3048,
    }

    for unidad, nombre in (
        (unidad_origen, "origen"),
        (unidad_destino, "destino"),
    ):
        if not isinstance(unidad, str) or unidad not in factores:
            raise ErrorValidacion(
                f"Unidad de {nombre} desconocida: {unidad!r}. "
                f"Unidades válidas: {list(factores.keys())}"
            )

    valor_ms = valor * factores[unidad_origen]

    if not math.isfinite(valor_ms):
        raise ErrorValidacion(
            "El resultado intermedio está fuera del rango numérico permitido"
        )

    resultado = valor_ms / factores[unidad_destino]

    if not math.isfinite(resultado):
        raise ErrorValidacion(
            "El resultado de la conversión está fuera del rango numérico permitido"
        )

    return resultado
