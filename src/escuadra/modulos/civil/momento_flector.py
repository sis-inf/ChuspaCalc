from typing import Any, Dict


def calcular_momento_max(
    longitud: float, carga: float, tipo_carga: str = "puntual_central"
) -> Dict[str, Any]:
    """
    Calcula el momento flector máximo en un elemento civil.

    Fórmulas:
        - Para carga puntual central: M_max = PL/4
        - Para carga distribuida: M_max = wL²/8

    Args:
        longitud (float): La longitud del elemento.
        carga (float): La carga aplicada al elemento.
        tipo_carga (str): El tipo de carga ('puntual_central' o 'distribuida').

    Returns:
        Dict[str, Any]: Un diccionario con los siguientes campos:
            - momento_max: El momento flector máximo.
            - posicion: La posición del momento máximo en metros desde el apoyo izquierdo.
            - unidad: La unidad del momento flector ('kN·m').

    Raises:
        ValueError: Si longitud <= 0, carga <= 0 o tipo_carga no es válido.
    """
    if longitud <= 0:
        raise ValueError(
            f"El parámetro 'longitud' debe ser mayor que cero. "
            f"Se recibió: {longitud}."
        )

    if carga <= 0:
        raise ValueError(
            f"El parámetro 'carga' debe ser mayor que cero. " f"Se recibió: {carga}."
        )

    if tipo_carga == "puntual_central":
        momento = carga * longitud / 4
    elif tipo_carga == "distribuida":
        momento = carga * (longitud**2) / 8
    else:
        raise ValueError(
            f"Tipo de carga '{tipo_carga}' no soportado. "
            "Tipos válidos: 'puntual_central' y 'distribuida'."
        )

    return {
        "momento_max": float(momento),
        "posicion": float(longitud / 2),
        "unidad": "kN·m",
    }
