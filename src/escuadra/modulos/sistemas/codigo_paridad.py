"""Herramientas educativas para cálculo y verificación de bits de paridad."""


def validar_cadena_binaria(cadena: str) -> None:
    """Valida que la entrada sea una cadena binaria no vacía."""
    if not isinstance(cadena, str):
        raise ValueError("La entrada debe ser una cadena de texto binaria.")

    if not cadena:
        raise ValueError("La cadena de entrada no puede estar vacía.")

    if not all(char in "01" for char in cadena):
        raise ValueError("La cadena debe contener exclusivamente caracteres binarios ('0' y '1').")


def calcular_bit_paridad(datos_binarios: str, tipo: str = "par") -> int:
    """
    Calcula el bit de paridad para una cadena binaria.

    Args:
        datos_binarios: Cadena compuesta por 0 y 1.
        tipo: Tipo de paridad ("par" o "impar").

    Returns:
        Bit de paridad calculado (0 o 1).
    """
    validar_cadena_binaria(datos_binarios)

    unos = datos_binarios.count("1")

    if tipo == "par":
        return 0 if unos % 2 == 0 else 1

    if tipo == "impar":
        return 1 if unos % 2 == 0 else 0

    raise ValueError("El tipo debe ser 'par' o 'impar'")


def verificar_paridad(datos_con_paridad: str, tipo: str = "par") -> bool:
    """
    Verifica si una cadena binaria cumple con la paridad indicada.

    Args:
        datos_con_paridad: Datos incluyendo el bit de paridad.
        tipo: Tipo de paridad ("par" o "impar").

    Returns:
        True si la paridad es correcta, False en caso contrario.
    """
    validar_cadena_binaria(datos_con_paridad)

    cantidad_unos = datos_con_paridad.count("1")

    if tipo == "par":
        return cantidad_unos % 2 == 0

    if tipo == "impar":
        return cantidad_unos % 2 != 0

    raise ValueError("El tipo debe ser 'par' o 'impar'")
    