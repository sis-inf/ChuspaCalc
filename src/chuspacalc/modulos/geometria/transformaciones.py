"""
Funciones de transformaciones geométricas 2D.
"""

import math

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

Punto = tuple[float, float]


def _validar_numero(valor: object, nombre: str) -> float:
    """Valida que ``valor`` sea un número real finito y lo devuelve como float."""
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise ErrorValidacion(
            f"'{nombre}' debe ser un numero (int o float), se recibio {type(valor).__name__}."
        )
    try:
        numero = float(valor)
    except OverflowError:
        raise ErrorValidacion(f"'{nombre}' es demasiado grande para operar.") from None
    if not math.isfinite(numero):
        raise ErrorValidacion(f"'{nombre}' debe ser un numero finito (sin NaN ni infinitos).")
    return numero


def _validar_punto(punto: object, nombre: str) -> Punto:
    """Valida que ``punto`` sea una pareja (x, y) de números finitos."""
    if not isinstance(punto, (tuple, list)) or len(punto) != 2:
        raise ErrorValidacion(f"'{nombre}' debe ser una pareja (x, y) de numeros.")
    return (
        _validar_numero(punto[0], f"{nombre}[0]"),
        _validar_numero(punto[1], f"{nombre}[1]"),
    )


def _verificar_resultado(resultado: Punto) -> Punto:
    """Evita devolver NaN o infinitos producidos por desbordamiento."""
    if not all(math.isfinite(c) for c in resultado):
        raise ErrorValidacion("El resultado esta fuera del rango numerico representable.")
    return resultado


def rotar_punto(
    punto: Punto,
    angulo: float,
    centro: Punto = (0.0, 0.0),
) -> Punto:
    """
    Rota un punto alrededor de un centro.
    El ángulo está en grados.

    Raises:
        ErrorValidacion: Si algún parámetro no es numérico, no es finito
            o el resultado se desborda.
    """
    x, y = _validar_punto(punto, "punto")
    cx, cy = _validar_punto(centro, "centro")
    grados = _validar_numero(angulo, "angulo")

    x -= cx
    y -= cy

    rad = math.radians(grados)

    xr = x * math.cos(rad) - y * math.sin(rad)
    yr = x * math.sin(rad) + y * math.cos(rad)

    return _verificar_resultado((xr + cx, yr + cy))


def trasladar_punto(
    punto: Punto,
    dx: float,
    dy: float,
) -> Punto:
    """
    Traslada un punto.

    Raises:
        ErrorValidacion: Si algún parámetro no es numérico, no es finito
            o el resultado se desborda.
    """
    x, y = _validar_punto(punto, "punto")
    desplazamiento_x = _validar_numero(dx, "dx")
    desplazamiento_y = _validar_numero(dy, "dy")

    return _verificar_resultado((x + desplazamiento_x, y + desplazamiento_y))


def escalar_punto(
    punto: Punto,
    factor: float,
    centro: Punto = (0.0, 0.0),
) -> Punto:
    """
    Escala un punto respecto a un centro.

    Raises:
        ErrorValidacion: Si algún parámetro no es numérico, no es finito
            o el resultado se desborda.
    """
    x, y = _validar_punto(punto, "punto")
    cx, cy = _validar_punto(centro, "centro")
    escala = _validar_numero(factor, "factor")

    return _verificar_resultado(
        (
            cx + (x - cx) * escala,
            cy + (y - cy) * escala,
        )
    )


def reflejar_punto(
    punto: Punto,
    eje: str = "x",
) -> Punto:
    """
    Refleja un punto respecto a un eje de coordenadas o al origen.

    Args:
        punto: Coordenadas (x, y) del punto a reflejar.
        eje: Eje de reflexión: 'x', 'y' u 'origen' (no distingue
            mayúsculas de minúsculas). Por defecto 'x'.

    Returns:
        Coordenadas (x, y) del punto reflejado.

    Raises:
        ErrorValidacion: Si ``punto`` no es válido o ``eje`` no es
            'x', 'y' ni 'origen'.

    Examples:
        >>> reflejar_punto((2.0, 3.0), 'x')
        (2.0, -3.0)
        >>> reflejar_punto((2.0, 3.0), 'y')
        (-2.0, 3.0)
        >>> reflejar_punto((2.0, 3.0), 'origen')
        (-2.0, -3.0)
    """
    x, y = _validar_punto(punto, "punto")

    if not isinstance(eje, str):
        raise ErrorValidacion(
            f"'eje' debe ser texto ('x', 'y' u 'origen'), se recibio {type(eje).__name__}."
        )
    eje_normalizado = eje.lower()

    if eje_normalizado == "x":
        return (x, -y)
    if eje_normalizado == "y":
        return (-x, y)
    if eje_normalizado == "origen":
        return (-x, -y)

    raise ErrorValidacion(f"Eje '{eje}' no valido. Solo se admiten 'x', 'y' y 'origen'.")
