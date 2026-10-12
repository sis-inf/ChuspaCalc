import math


def calcular_potencia_trifasica(
    voltaje_linea: float,
    corriente_linea: float,
    factor_potencia: float,
    conexion: str = "estrella",
) -> dict[str, float]:
    """
    Calcula la potencia trifásica activa, reactiva y aparente.

    Fórmulas:
        P = √3 · V_linea · I_linea · cos(φ)
        Q = √3 · V_linea · I_linea · sin(φ)
        S = √3 · V_linea · I_linea

    Unidades:
        - V_linea: voltaje de línea en Volts (V)
        - I_linea: corriente de línea en Amperes (A)
        - cos(φ): factor de potencia (adimensional, entre 0 y 1)
        - P: potencia activa en Watts (W)
        - Q: potencia reactiva en Volt-Amperes reactivos (VAR)
        - S: potencia aparente en Volt-Amperes (VA)

    Args:
        voltaje_linea: Voltaje de línea en Volts
        corriente_linea: Corriente de línea en Amperes
        factor_potencia: Factor de potencia (cos φ), entre 0 y 1
        conexion: Tipo de conexión, 'estrella' o 'triangulo' (default: 'estrella')

    Returns:
        Diccionario con las potencias calculadas:
        {
            'potencia_activa': P en Watts,
            'potencia_reactiva': Q en VAR,
            'potencia_aparente': S en VA
        }

    Raises:
        ValueError: Si los parámetros no son válidos
    """
    if voltaje_linea <= 0:
        raise ValueError("voltaje_linea debe ser mayor que 0")

    if corriente_linea <= 0:
        raise ValueError("corriente_linea debe ser mayor que 0")

    if factor_potencia <= 0 or factor_potencia > 1:
        raise ValueError("factor_potencia debe estar entre 0 y 1")

    if conexion not in ("estrella", "triangulo"):
        raise ValueError("conexion debe ser 'estrella' o 'triangulo'")

    # Calcular el ángulo de fase φ a partir del factor de potencia
    angulo_fase = math.acos(factor_potencia)

    # Calcular potencias trifásicas
    # La fórmula es la misma para estrella y triángulo usando valores de línea
    raiz_3 = math.sqrt(3)
    potencia_aparente = raiz_3 * voltaje_linea * corriente_linea
    potencia_activa = potencia_aparente * factor_potencia
    potencia_reactiva = potencia_aparente * math.sin(angulo_fase)

    return {
        "potencia_activa": float(potencia_activa),
        "potencia_reactiva": float(potencia_reactiva),
        "potencia_aparente": float(potencia_aparente),
    }
