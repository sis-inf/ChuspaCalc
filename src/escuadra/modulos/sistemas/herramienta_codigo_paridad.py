"""Wrapper de herramienta para cálculo y verificación de paridad."""

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.sistemas.codigo_paridad import (
    calcular_bit_paridad,
    verificar_paridad,
)


def ejecutar_calculo_paridad(datos_binarios: str, tipo: str = "par") -> dict[str, object]:
    """
    Ejecuta las funciones de paridad y devuelve los resultados.

    Args:
        datos_binarios: Cadena de bits original.
        tipo: Tipo de paridad ("par" o "impar").

    Returns:
        Diccionario con el bit generado y verificación.

    Raises:
        ErrorValidacion: Si los argumentos no son cadenas de texto, si la
            cadena no es binaria o está vacía, o si el tipo no es válido.
    """
    if not isinstance(datos_binarios, str):
        raise ErrorValidacion(
            "Los datos binarios deben ser una cadena de texto, "
            f"se recibió {type(datos_binarios).__name__}."
        )

    if not isinstance(tipo, str):
        raise ErrorValidacion(
            f"El tipo de paridad debe ser una cadena de texto, se recibió {type(tipo).__name__}."
        )

    try:
        bit = calcular_bit_paridad(datos_binarios, tipo)
        datos_completos = f"{datos_binarios}{bit}"
        valido = verificar_paridad(datos_completos, tipo)
    except ValueError as e:
        # ErrorValidacion hereda de ValueError: se conserva el mensaje original.
        raise ErrorValidacion(str(e)) from e

    return {
        "datos_originales": datos_binarios,
        "tipo_paridad": tipo,
        "bit_paridad": bit,
        "datos_con_paridad": datos_completos,
        "valido": valido,
    }
