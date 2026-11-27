"""Wrapper de herramienta para cálculo y verificación de paridad."""

from chuspacalc.modulos.sistemas.codigo_paridad import (
    calcular_bit_paridad,
    verificar_paridad,
)


def ejecutar_calculo_paridad(datos_binarios: str, tipo: str = "par") -> dict:
    """
    Ejecuta las funciones de paridad y devuelve los resultados.

    Args:
        datos_binarios: Cadena de bits original.
        tipo: Tipo de paridad ("par" o "impar").

    Returns:
        Diccionario con el bit generado y verificación.
    """
    bit = calcular_bit_paridad(datos_binarios, tipo)
    datos_completos = f"{datos_binarios}{bit}"

    return {
        "datos_originales": datos_binarios,
        "tipo_paridad": tipo,
        "bit_paridad": bit,
        "datos_con_paridad": datos_completos,
        "valido": verificar_paridad(datos_completos, tipo),
    }
