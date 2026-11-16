"""
Funciones de transformaciones geométricas 2D.
"""

import math


def rotar_punto(
    punto: tuple[float, float],
    angulo: float,
    centro: tuple[float, float] = (0.0, 0.0),
) -> tuple[float, float]:
    """
    Rota un punto alrededor de un centro.
    El ángulo está en grados.
    """
    x, y = punto
    cx, cy = centro

    x -= cx
    y -= cy

    rad = math.radians(angulo)

    xr = x * math.cos(rad) - y * math.sin(rad)
    yr = x * math.sin(rad) + y * math.cos(rad)

    return (xr + cx, yr + cy)


def trasladar_punto(
    punto: tuple[float, float],
    dx: float,
    dy: float,
) -> tuple[float, float]:
    """
    Traslada un punto.
    """
    return (punto[0] + dx, punto[1] + dy)


def escalar_punto(
    punto: tuple[float, float],
    factor: float,
    centro: tuple[float, float] = (0.0, 0.0),
) -> tuple[float, float]:
    """
    Escala un punto respecto a un centro.
    """
    cx, cy = centro

    return (
        cx + (punto[0] - cx) * factor,
        cy + (punto[1] - cy) * factor,
    )


def reflejar_punto(
    punto: tuple[float, float],
    eje: str = "x",
) -> tuple[float, float]:
    """
    Refleja un punto respecto a un eje de coordenadas o al origen.

    Args:
        punto: Coordenadas (x, y) del punto a reflejar.
        eje: Eje de reflexión: 'x', 'y' u 'origen' (no distingue
            mayúsculas de minúsculas). Por defecto 'x'.

    Returns:
        Coordenadas (x, y) del punto reflejado.

    Raises:
        ValueError: Si ``eje`` no es 'x', 'y' ni 'origen'.

    Examples:
        >>> reflejar_punto((2.0, 3.0), 'x')
        (2.0, -3.0)
        >>> reflejar_punto((2.0, 3.0), 'y')
        (-2.0, 3.0)
        >>> reflejar_punto((2.0, 3.0), 'origen')
        (-2.0, -3.0)
    """
    x, y = punto
    eje_normalizado = eje.lower() if isinstance(eje, str) else eje

    if eje_normalizado == "x":
        return (x, -y)
    if eje_normalizado == "y":
        return (-x, y)
    if eje_normalizado == "origen":
        return (-x, -y)

    raise ValueError(
        f"Eje '{eje}' no valido. Solo se admiten 'x', 'y' y 'origen'."
    )
