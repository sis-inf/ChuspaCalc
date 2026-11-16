"""
Modulo para el Calculo de reacciones en vigas simplemente apoyadas.
             Soporta carga distribuida uniforme y carga puntual.
"""


def calcular_reacciones(longitud: float, carga: float, posicion: float = None) -> dict:
    """
    Calcula las reacciones Ra y Rb de una viga simplemente apoyada.
    Si posicion es None, asume carga distribuida uniforme.
    """

    # Validaciones
    if longitud <= 0:
        raise ValueError(f"La longitud debe ser mayor que 0. Valor recibido: {longitud}")
    if carga <= 0:
        raise ValueError(f"La carga debe ser mayor que 0. Valor recibido: {carga}")
    if posicion is not None and not (0 <= posicion <= longitud):
        raise ValueError(
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

    return {
        "Ra": round(Ra, 4),
        "Rb": round(Rb, 4),
        "unidad": "kN"
    }
