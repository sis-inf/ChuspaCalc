import math
from typing import TypedDict


class ResultadoMomento(TypedDict):
    momento_max: float
    posicion: float
    unidad: str


def _validar_finito(nombre: str, valor: float) -> None:
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise ValueError(f"'{nombre}' debe ser un número finito")
    if not math.isfinite(valor):
        raise ValueError(f"'{nombre}' debe ser un número finito")
    if valor <= 0:
        raise ValueError(f"'{nombre}' debe ser mayor que cero")


def calcular_momento_max(
    longitud: float,
    carga: float,
    tipo_carga: str = "puntual_central",
) -> ResultadoMomento:
    """
    Calcula el momento flector máximo de una viga simplemente apoyada.

    Fórmula:
        Carga puntual central: Mmax = carga * longitud / 4.
        Carga distribuida: Mmax = carga * longitud**2 / 8.

    Args:
        longitud: Longitud de la viga (m).
        carga: Carga puntual (kN) o carga distribuida (kN/m).
        tipo_carga: ``puntual_central`` o ``distribuida``.

    Returns:
        Momento máximo, posición y unidad.

    Raises:
        ValueError: Si los valores no son positivos y finitos o el tipo
            de carga no está soportado.
    """
    _validar_finito("longitud", longitud)
    _validar_finito("carga", carga)

    if tipo_carga == "puntual_central":
        momento = carga * longitud / 4
    elif tipo_carga == "distribuida":
        momento = carga * longitud**2 / 8
    else:
        raise ValueError("El tipo de carga debe ser 'puntual_central' o 'distribuida'")

    return {
        "momento_max": float(momento),
        "posicion": float(longitud / 2),
        "unidad": "kN·m",
    }


def calcular_momento_maximo(carga: float, longitud: float) -> float:
    """Calcula el caso escalar compatible de carga puntual central."""
    return calcular_momento_max(longitud, carga)["momento_max"]
