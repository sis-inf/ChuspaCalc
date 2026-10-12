from escuadra.modulos.matematicas.error_validacion import ErrorValidacion

UNIDADES_A_METROS = {
    "m": 1,
    "cm": 0.01,
    "mm": 0.001,
    "km": 1000,
    "in": 0.0254,
    "ft": 0.3048,
}


def convertir(valor: float, de_unidad: str, a_unidad: str) -> dict:
    """
    Convierte unidades de longitud usando metros como base.

    Args:
        valor (float): Valor a convertir.
        de_unidad (str): Unidad origen.
        a_unidad (str): Unidad destino.

    Returns:
        dict: Resultado de la conversión.

    Raises:
        ErrorValidacion: Si el valor es negativo.
        ValueError: Si la unidad no existe.
    """

    if valor < 0:
        raise ErrorValidacion(
            f"La longitud no puede ser negativa (valor recibido: {valor})"
        )

    de_unidad = de_unidad.strip().lower()
    a_unidad = a_unidad.strip().lower()

    if de_unidad not in UNIDADES_A_METROS:
        raise ValueError(f"Unidad origen no reconocida: {de_unidad}")

    if a_unidad not in UNIDADES_A_METROS:
        raise ValueError(f"Unidad destino no reconocida: {a_unidad}")

    # Convertir a metros
    valor_en_metros = valor * UNIDADES_A_METROS[de_unidad]

    # Convertir desde metros a unidad destino
    valor_convertido = valor_en_metros / UNIDADES_A_METROS[a_unidad]

    return {
        "valor_original": valor,
        "unidad_original": de_unidad,
        "valor_convertido": valor_convertido,
        "unidad_destino": a_unidad,
    }
