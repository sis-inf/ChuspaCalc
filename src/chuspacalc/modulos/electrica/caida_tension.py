"""
Modulo para el calculo de caida de tension en conductores electricos.

Formula aplicada:
    DV = 2 * p * L * I / S

Donde:
    p = resistividad del material (Ohm*mm2/m)
    L = longitud del conductor (m)
    I = corriente (A)
    S = seccion transversal del conductor (mm2)
"""

from __future__ import annotations

import math
from numbers import Real

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

# Resistividades en Ohm*mm2/m a 20 C
RESISTIVIDADES: dict[str, float] = {
    "cobre": 0.0172,
    "aluminio": 0.0282,
}

TENSION_REFERENCIA_V: float = 220.0
PORCENTAJE_ADMISIBLE: float = 3.0


def _validar_numero(valor: object, nombre: str) -> float:
    """Verifica que el valor sea un número real y lo devuelve como float.

    Args:
        valor: Dato a validar.
        nombre: Nombre del parametro, usado en el mensaje de error.

    Returns:
        El valor convertido a ``float``.

    Raises:
        ErrorValidacion: Si el tipo no es numerico (incluye ``bool``) o si
            el valor es demasiado grande para convertirse a ``float``.
    """
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(
            f"El parametro '{nombre}' debe ser un numero real. "
            f"Se recibio: {type(valor).__name__}."
        )
    try:
        return float(valor)
    except OverflowError:
        raise ErrorValidacion(
            f"El parametro '{nombre}' es demasiado grande para procesarse."
        ) from None


def calcular_caida(
    longitud: float,
    corriente: float,
    seccion: float,
    material: str = "cobre",
    tension: float = TENSION_REFERENCIA_V,
    factor_potencia: float = 1.0,
) -> dict[str, float | bool]:
    """Calcula la caida de tension en un conductor electrico.

    Aplica la formula DV = 2 * p * L * I / S para circuitos
    monofasicos de ida y vuelta.

    Args:
        longitud:  Longitud del conductor en metros (m). Debe ser > 0.
        corriente: Corriente que circula en amperios (A). Debe ser > 0.
        seccion:   Seccion transversal del conductor en mm2. Debe ser > 0.
        material:  Material del conductor. Valores aceptados: ``'cobre'``
                   (por defecto) y ``'aluminio'``.
        tension:   Tension nominal de referencia en voltios (V). Debe ser > 0.
                   Por defecto 220.0.
        factor_potencia: Factor de potencia (cos phi) de la carga. Debe estar
                   en el intervalo [0.0, 1.0]. Por defecto 1.0, que equivale
                   a la formula sin factor de potencia.
    Returns:
        Diccionario con los siguientes campos:

        * ``caida_v``    - Caida de tension en voltios (float).
        * ``porcentaje`` - Caida expresada como porcentaje respecto a
                           ``tension`` (float).
        * ``admisible``  - ``True`` si el porcentaje es <= 3 % (bool).
        * ``tension_v``  - Tension de referencia utilizada, en voltios (float).

    Raises:
        ErrorValidacion: Si ``material`` no es texto o no esta entre los
            reconocidos.
        ErrorValidacion: Si algun parametro numerico no es un numero real,
            no es finito o no es positivo.
        ErrorValidacion: Si ``factor_potencia`` no pertenece al intervalo
            [0.0, 1.0].

    Examples:
        >>> calcular_caida(longitud=100, corriente=15, seccion=4)
        {'caida_v': 12.9, 'porcentaje': 5.8636, 'admisible': False, 'tension_v': 220.0}
    """
    # Validar material
    if not isinstance(material, str):
        raise ErrorValidacion(
            f"El parametro 'material' debe ser texto. "
            f"Se recibio: {type(material).__name__}."
        )
    material_lower = material.lower()
    if material_lower not in RESISTIVIDADES:
        materiales_validos = ", ".join(f"'{m}'" for m in RESISTIVIDADES)
        raise ErrorValidacion(
            f"Material '{material}' no reconocido. Valores aceptados: {materiales_validos}."
        )

    # Validar tipos numericos
    longitud = _validar_numero(longitud, "longitud")
    corriente = _validar_numero(corriente, "corriente")
    seccion = _validar_numero(seccion, "seccion")
    tension = _validar_numero(tension, "tension")
    factor_potencia = _validar_numero(factor_potencia, "factor_potencia")

    # Validar parametros positivos
    parametros = {
        "longitud": longitud,
        "corriente": corriente,
        "seccion": seccion,
        "tension": tension,
    }
    for nombre, valor in {**parametros, "factor_potencia": factor_potencia}.items():
        if not math.isfinite(valor):
            mensaje = f"El parametro '{nombre}' debe ser finito. Se recibio: {valor}."
            raise ErrorValidacion(mensaje)
    for nombre, valor in parametros.items():
        if valor <= 0:
            mensaje = f"El parametro '{nombre}' debe ser positivo. Se recibio: {valor}."
            raise ErrorValidacion(mensaje)
    if not 0.0 <= factor_potencia <= 1.0:
        raise ErrorValidacion(
            "El factor de potencia debe pertenecer al intervalo [0.0, 1.0]. "
            f"Se recibio: {factor_potencia}."
        )

    resistividad = RESISTIVIDADES[material_lower]
    caida_v = 2 * resistividad * longitud * corriente * factor_potencia / seccion
    porcentaje = (caida_v / tension) * 100
    admisible = porcentaje <= PORCENTAJE_ADMISIBLE

    return {
        "caida_v": round(caida_v, 4),
        "porcentaje": round(porcentaje, 4),
        "admisible": admisible,
        "tension_v": tension,
    }
