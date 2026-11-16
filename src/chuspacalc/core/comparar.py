"""
Módulo para comparar resultados numéricos con tolerancia configurable.
"""

import math
from typing import Any


def comparar_resultados(
    resultado1: float,
    resultado2: float,
    tolerancia: float = 1e-6,
) -> dict[str, Any]:
    """
    Compara dos resultados numéricos verificando si son equivalentes
    dentro de una tolerancia definida.

    Args:
        resultado1 (float): Primer resultado a comparar.
        resultado2 (float): Segundo resultado a comparar.
        tolerancia (float): Diferencia máxima permitida.

    Returns:
        dict[str, Any]: Resultado de la comparación con las claves
            ``equivalente``, ``resultado1``, ``resultado2``,
            ``diferencia`` y ``tolerancia``.

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
    a: dict[str, Any],
    b: dict[str, Any],
    tolerancia: float = 1e-4,
) -> dict[str, Any]:
    """
    Compara dos diccionarios de resultados clave por clave.

    Para las claves presentes en ambos diccionarios: si los dos valores
    son numéricos (``int`` o ``float``, sin contar ``bool``), calcula la
    diferencia absoluta y porcentual y los considera coincidentes cuando
    la diferencia no supera la tolerancia. Si no son numéricos, los
    considera coincidentes cuando tienen el mismo tipo y el mismo valor.

    Args:
        a (dict[str, Any]): Primer diccionario de resultados.
        b (dict[str, Any]): Segundo diccionario de resultados.
        tolerancia (float): Diferencia absoluta máxima permitida para
            considerar coincidentes dos valores numéricos.

    Returns:
        dict[str, Any]: Diccionario con tres claves:

            - ``diferencias_numericas``: detalle por clave numérica
              (``valor_a``, ``valor_b``, ``diferencia_absoluta`` y
              ``diferencia_porcentual``, que es ``None`` si no se puede
              calcular).
            - ``coincidentes``: lista de claves cuyos valores coinciden.
            - ``claves_disjuntas``: claves presentes solo en ``a``
              (``solo_a``) o solo en ``b`` (``solo_b``).

    Raises:
        TypeError: Si ``a`` o ``b`` no son diccionarios.
        ValueError: Si la tolerancia no es un número finito no negativo,
            o si algún valor numérico comparado no es finito.
    """
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
