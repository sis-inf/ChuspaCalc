
import math


def calcular_diagonal_rectangulo(base, altura):
    """
    Calcula la diagonal de un rectángulo mediante el teorema
    de Pitágoras.

    Args:
        base: Base del rectángulo.
        altura: Altura del rectángulo.

    Returns:
        float: Longitud de la diagonal.

    Raises:
        ValueError: Si las dimensiones no son numéricas,
                    positivas o finitas.
    """

    dimensiones = {
        "base": base,
        "altura": altura
    }

    for nombre, valor in dimensiones.items():
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError(f"La {nombre} debe ser numérica.")

        if not math.isfinite(valor) or valor <= 0:
            raise ValueError(f"La {nombre} debe ser positiva y finita.")

    diagonal = math.hypot(base, altura)

    if not math.isfinite(diagonal):
        raise ValueError("La diagonal calculada debe ser finita.")

    return diagonal
