"""
Modulo para el Calculo de reacciones en vigas simplemente apoyadas.
             Soporta carga distribuida uniforme y carga puntual.
"""

import math

from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
)


def calcular_reacciones(
    longitud: float, carga: float, posicion: float | None = None
) -> dict[str, float | str]:
    """
    Calcula las reacciones Ra y Rb de una viga simplemente apoyada.
    Si posicion es None, asume carga distribuida uniforme.
    Si posicion tiene un valor, asume carga puntual aplicada
    en dicha posicion medida desde el apoyo A.

    Args:
        longitud: Longitud de la viga en metros. Debe ser mayor que cero.
        carga: Carga aplicada en kN. Debe ser mayor que cero.
        posicion: Posicion de la carga puntual en metros.
            Debe encontrarse dentro del intervalo [0, longitud].
            Si es None, se considera carga distribuida uniforme.

    Returns:
        Diccionario con las reacciones Ra y Rb en kN.

    Raises:
        ErrorValidacion: Si algun parametro tiene un tipo incorrecto,
            no es finito o incumple las restricciones del dominio.
    """

    # Validaciones
    longitud = validar_numero(longitud, "longitud")
    carga = validar_numero(carga, "carga")
    if posicion is not None:
        posicion = validar_numero(posicion, "posicion")
    if longitud <= 0:
        raise ErrorValidacion(
            f"La longitud debe ser mayor que 0. Valor recibido: {longitud}"
        )
    if carga <= 0:
        raise ErrorValidacion(f"La carga debe ser mayor que 0. Valor recibido: {carga}")
    if posicion is not None and not (0 <= posicion <= longitud):
        raise ErrorValidacion(
            f"La posición debe estar en el intervalo [0, {longitud}]. "
            f"Valor recibido: {posicion}"
        )

    # Cálculo de reacciones
    if posicion is None:
        # Carga distribuida uniforme
        Ra = carga / 2
        Rb = carga / 2
    else:
        # Carga puntual en la posición indicada (distancia desde apoyo A)
        Rb = carga * posicion / longitud
        Ra = carga - Rb
    # Verificacion de resultados numericos
    if not math.isfinite(Ra) or not math.isfinite(Rb):
        raise ErrorValidacion(
            "El resultado del calculo de reacciones "
            "esta fuera del rango numerico permitido."
        )
    return {"Ra": round(Ra, 4), "Rb": round(Rb, 4), "unidad": "kN"}
