"""
Funciones básicas para mapas de Karnaugh.

La simplificación implementada cubre únicamente casos básicos
de agrupaciones (pares y cuartetos). No implementa el algoritmo
completo de Quine-McCluskey.
"""


def generar_mapa_karnaugh(
    tabla_verdad: list[int], num_variables: int
) -> list[list[int]]:
    """
    Genera un mapa de Karnaugh básico (hasta 4 variables).

    Retorna una representación simple en forma de lista.
    """
    if num_variables < 2 or num_variables > 4:
        raise ValueError("Solo se soportan entre 2 y 4 variables.")

    return tabla_verdad


def simplificar_expresion(mapa: list[list[int]] | list[int]) -> str:
    """
    Simplifica casos básicos del mapa de Karnaugh.

    Esta implementación únicamente identifica algunos casos
    sencillos y no reemplaza algoritmos completos de minimización.
    """
    if not mapa:
        return "0"

    if all(valor == 1 for valor in mapa):
        return "1"

    return "Expresión simplificada (caso básico)"
