"""
Módulo para comparar resultados numéricos con tolerancia configurable.
"""

import math


def comparar_resultados(resultado1, resultado2, tolerancia=1e-6):
    """
    Compara dos resultados numéricos verificando si son equivalentes
    dentro de una tolerancia definida.

    Args:
        resultado1 (float): Primer resultado a comparar.
        resultado2 (float): Segundo resultado a comparar.
        tolerancia (float): Diferencia máxima permitida.

    Returns:
        dict: Resultado de la comparación con detalle.

    Raises:
        ValueError: Si la tolerancia es negativa.
    """

    if tolerancia < 0:
        raise ValueError("La tolerancia no puede ser negativa.")

    diferencia = abs(resultado1 - resultado2)

    equivalente = diferencia <= tolerancia

    return {
        "equivalente": equivalente,
        "resultado1": resultado1,
        "resultado2": resultado2,
        "diferencia": diferencia,
        "tolerancia": tolerancia,
    }


def comparar_diccionarios_resultados(
    a: dict,
    b: dict,
    tolerancia: float = 1e-4,
) -> dict:
    if not isinstance(a, dict) or not isinstance(b, dict):
        raise TypeError("Los resultados deben ser diccionarios.")
    if (
        isinstance(tolerancia, bool)
        or not isinstance(tolerancia, (int, float))
        or not math.isfinite(tolerancia)
        or tolerancia < 0
    ):
        raise ValueError("La tolerancia debe ser un numero finito no negativo.")

    diferencias_numericas = {}
    coincidentes = []
    for clave in a:
        if clave not in b:
            continue
        valor_a, valor_b = a[clave], b[clave]
        son_numericos = all(
            isinstance(valor, (int, float)) and not isinstance(valor, bool)
            for valor in (valor_a, valor_b)
        )
        if son_numericos:
            if not all(math.isfinite(valor) for valor in (valor_a, valor_b)):
                raise ValueError(f"La clave {clave!r} contiene un numero no finito.")
            diferencia = abs(valor_a - valor_b)
            porcentaje = None
            if valor_a != 0:
                porcentaje = diferencia / abs(valor_a) * 100
            elif diferencia == 0:
                porcentaje = 0.0
            diferencias_numericas[clave] = {
                "valor_a": valor_a,
                "valor_b": valor_b,
                "diferencia_absoluta": diferencia,
                "diferencia_porcentual": porcentaje,
            }
            if diferencia <= tolerancia:
                coincidentes.append(clave)
        elif type(valor_a) is type(valor_b) and valor_a == valor_b:
            coincidentes.append(clave)

    return {
        "diferencias_numericas": diferencias_numericas,
        "coincidentes": coincidentes,
        "claves_disjuntas": {
            "solo_a": [clave for clave in a if clave not in b],
            "solo_b": [clave for clave in b if clave not in a],
        },
    }
