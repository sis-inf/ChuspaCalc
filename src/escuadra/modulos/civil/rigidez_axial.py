
import math


def calcular_rigidez_axial(elasticidad, area, longitud):
    """
    Calcula la rigidez axial de un elemento estructural.

    Args:
        elasticidad: Módulo de elasticidad en Pa.
        area: Área transversal en m².
        longitud: Longitud del elemento en m.

    Returns:
        float: Rigidez axial en N/m.

    Raises:
        ValueError: Si los parámetros no son numéricos,
                    positivos o finitos.
    """

    parametros = {
        "elasticidad": elasticidad,
        "area": area,
        "longitud": longitud
    }

    for nombre, valor in parametros.items():
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError(f"{nombre} debe ser un valor numérico.")

        if not math.isfinite(valor) or valor <= 0:
            raise ValueError(f"{nombre} debe ser positivo y finito.")

    rigidez = (elasticidad * area) / longitud

    if not math.isfinite(rigidez):
        raise ValueError("El resultado debe ser finito.")

    return rigidez
