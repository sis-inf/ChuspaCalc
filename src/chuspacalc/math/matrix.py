"""
Operaciones básicas de matrices usando listas de listas.
"""

import math
from collections.abc import Sequence

Matriz = Sequence[Sequence[float]]


def sumar(a: Matriz, b: Matriz) -> list[list[float]]:
    """
    Suma dos matrices de iguales dimensiones.

    Args:
        a: Primera matriz.
        b: Segunda matriz.

    Returns:
        Nueva matriz con la suma elemento a elemento.

    Raises:
        ValueError: Si alguna matriz es inválida o las dimensiones son incompatibles.

    Examples:
        >>> sumar([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[6, 8], [10, 12]]
    """
    _validar_dimensiones(a, b)
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def restar(a: Matriz, b: Matriz) -> list[list[float]]:
    """
    Resta dos matrices de iguales dimensiones.

    Args:
        a: Primera matriz.
        b: Segunda matriz.

    Returns:
        Nueva matriz con la resta elemento a elemento.

    Raises:
        ValueError: Si alguna matriz es inválida o las dimensiones son incompatibles.

    Examples:
        >>> restar([[5, 6], [7, 8]], [[1, 2], [3, 4]])
        [[4, 4], [4, 4]]
    """
    _validar_dimensiones(a, b)
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def multiplicar(a: Matriz, b: Matriz) -> list[list[float]]:
    """
    Multiplica dos matrices (producto matricial).

    Args:
        a: Primera matriz de dimensiones m x n.
        b: Segunda matriz de dimensiones n x p.

    Returns:
        Nueva matriz de dimensiones m x p.

    Raises:
        ValueError: Si alguna matriz es inválida o las dimensiones son incompatibles.

    Examples:
        >>> multiplicar([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
    """
    _validar_matriz(a)
    _validar_matriz(b)
    filas_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    if cols_a != len(b):
        raise ValueError(
            f"Dimensiones incompatibles para multiplicación: "
            f"{filas_a}x{cols_a} y {len(b)}x{cols_b}"
        )

    return [
        [sum(a[i][k] * b[k][j] for k in range(cols_a)) for j in range(cols_b)]
        for i in range(filas_a)
    ]


def _es_numero_finito(valor: object) -> bool:
    """Acepta enteros y flotantes finitos, excluyendo valores booleanos."""
    if isinstance(valor, int):
        return not isinstance(valor, bool)
    return isinstance(valor, float) and math.isfinite(valor)


def _validar_matriz(m: Matriz) -> None:
    """Exige una matriz rectangular no vacía con valores numéricos finitos."""
    if not isinstance(m, Sequence) or isinstance(m, (str, bytes, bytearray)):
        raise ValueError("La matriz debe ser una secuencia de filas.")
    if not m:
        raise ValueError("La matriz no puede estar vacía.")
    if any(
        not isinstance(fila, Sequence) or isinstance(fila, (str, bytes, bytearray))
        for fila in m
    ):
        raise ValueError("Cada fila de la matriz debe ser una secuencia.")
    columnas = len(m[0])
    if not columnas:
        raise ValueError("La matriz no puede estar vacía.")
    if any(len(fila) != columnas for fila in m):
        raise ValueError("Todas las filas deben tener la misma longitud.")
    if any(not _es_numero_finito(elemento) for fila in m for elemento in fila):
        raise ValueError("Todos los elementos de la matriz deben ser números finitos.")


def _validar_dimensiones(a: Matriz, b: Matriz) -> None:
    """Valida que dos matrices tengan las mismas dimensiones."""
    _validar_matriz(a)
    _validar_matriz(b)
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError(
            f"Dimensiones incompatibles: {len(a)}x{len(a[0])} y {len(b)}x{len(b[0])}"
        )


def transponer(a: Matriz) -> list[list[float]]:
    """
    Calcula la transpuesta de una matriz.

    Args:
        a: Matriz de dimensiones m x n.

    Returns:
        Nueva matriz de dimensiones n x m con filas y columnas intercambiadas.

    Raises:
        ValueError: Si la matriz está vacía, no es rectangular o tiene valores inválidos.

    Examples:
        >>> transponer([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
    """
    _validar_matriz(a)
    return [list(columna) for columna in zip(*a)]


def multiplicar_escalar(a: Matriz, escalar: float) -> list[list[float]]:
    """
    Multiplica cada elemento de una matriz por un escalar.

    Args:
        a: Matriz de entrada.
        escalar: Valor por el que se multiplica cada elemento.

    Returns:
        Nueva matriz con cada elemento multiplicado por ``escalar``.

    Raises:
        ValueError: Si la matriz es inválida o el escalar no es un número finito.

    Examples:
        >>> multiplicar_escalar([[1.0, -2.0], [3.0, 4.0]], 2.5)
        [[2.5, -5.0], [7.5, 10.0]]
    """
    _validar_matriz(a)
    if not _es_numero_finito(escalar):
        raise ValueError("El escalar debe ser un número finito.")
    return [[elemento * escalar for elemento in fila] for fila in a]
