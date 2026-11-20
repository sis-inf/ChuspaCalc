import math

from ..matematicas.error_validacion import ErrorValidacion


def calcular_diagonal_rectangulo(
    base: int | float,
    altura: int | float,
) -> float:
    """
    Calcula la diagonal de un rectángulo mediante el teorema
    de Pitágoras.

    Args:
        base: Base del rectángulo.
        altura: Altura del rectángulo.

    Returns:
        Longitud de la diagonal.

    Raises:
        ErrorValidacion: Si las dimensiones no son numéricas,
            positivas o finitas, o si la diagonal calculada
            no es finita.
    """
    dimensiones: dict[str, int | float] = {
        "base": base,
        "altura": altura,
    }

    for nombre, valor in dimensiones.items():
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ErrorValidacion(f"La {nombre} debe ser numérica.")

        try:
            es_finito = math.isfinite(valor)
        except OverflowError as error:
            raise ErrorValidacion(
                f"La {nombre} debe ser positiva y finita."
            ) from error

        if not es_finito or valor <= 0:
            raise ErrorValidacion(
                f"La {nombre} debe ser positiva y finita."
            )

    diagonal = math.hypot(base, altura)

    if not math.isfinite(diagonal):
        raise ErrorValidacion(
            "La diagonal calculada debe ser finita."
        )

    return diagonal
