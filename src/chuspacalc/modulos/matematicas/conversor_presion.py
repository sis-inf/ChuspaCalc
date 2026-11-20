import math

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def convertir_presion(
    valor: int | float,
    unidad_origen: str,
    unidad_destino: str,
) -> float:
    """Convierte una presión entre unidades utilizando Pa como unidad base.

    Unidades disponibles: Pa, kPa, MPa, bar, mbar, atm, psi, mmHg y torr.

    Args:
        valor: Valor de presión mayor o igual a cero.
        unidad_origen: Unidad del valor de entrada.
        unidad_destino: Unidad a la que se convierte.

    Returns:
        Valor convertido a la unidad de destino.

    Raises:
        ErrorValidacion: Si el valor, las unidades o el resultado no son válidos.
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
            f"La presión no puede ser negativa (valor recibido: {valor})"
        )

    factores: dict[str, float] = {
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

    for unidad, nombre in (
        (unidad_origen, "origen"),
        (unidad_destino, "destino"),
    ):
        if not isinstance(unidad, str) or unidad not in factores:
            raise ErrorValidacion(
                f"Unidad de {nombre} desconocida: {unidad!r}. "
                f"Unidades válidas: {list(factores.keys())}"
            )

    try:
        valor_pa = valor * factores[unidad_origen]
        resultado = valor_pa / factores[unidad_destino]
    except (OverflowError, ZeroDivisionError) as exc:
        raise ErrorValidacion(
            "No se pudo realizar la conversión por desbordamiento numérico"
        ) from exc

    if not math.isfinite(resultado):
        raise ErrorValidacion(
            "El resultado de la conversión está fuera del rango numérico permitido"
        )

    return resultado
