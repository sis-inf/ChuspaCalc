"""
Operaciones básicas de matrices usando listas de listas.
"""


def sumar(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """
    Suma dos matrices de iguales dimensiones.

    Args:
        a: Primera matriz.
        b: Segunda matriz.

    Returns:
        Nueva matriz con la suma elemento a elemento.

    Raises:
        ValueError: Si las dimensiones no son compatibles.

    Examples:
        >>> sumar([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[6, 8], [10, 12]]
    """
    _validar_dimensiones(a, b)
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def restar(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """
    Resta dos matrices de iguales dimensiones.

    Args:
        a: Primera matriz.
        b: Segunda matriz.

    Returns:
        Nueva matriz con la resta elemento a elemento.

    Raises:
        ValueError: Si las dimensiones no son compatibles.

    Examples:
        >>> restar([[5, 6], [7, 8]], [[1, 2], [3, 4]])
        [[4, 4], [4, 4]]
    """
    _validar_dimensiones(a, b)
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def multiplicar(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """
    Multiplica dos matrices (producto matricial).

    Args:
        a: Primera matriz de dimensiones m x n.
        b: Segunda matriz de dimensiones n x p.

    Returns:
        Nueva matriz de dimensiones m x p.

    Raises:
        ValueError: Si las dimensiones no son compatibles para multiplicación.

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


def _validar_matriz(m: list[list[float]]) -> None:
    """Valida que la matriz no esté vacía y que sus filas tengan igual longitud."""
    if not m or not m[0]:
        raise ValueError("La matriz no puede estar vacía.")
    if any(len(fila) != len(m[0]) for fila in m):
        raise ValueError("Todas las filas deben tener la misma longitud.")


def _validar_dimensiones(a: list[list[float]], b: list[list[float]]) -> None:
    """Valida que dos matrices tengan las mismas dimensiones."""
    _validar_matriz(a)
    _validar_matriz(b)
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError(
            f"Dimensiones incompatibles: {len(a)}x{len(a[0])} y {len(b)}x{len(b[0])}"
        )


def transponer(a: list[list[float]]) -> list[list[float]]:
    """
    Calcula la transpuesta de una matriz.

    Args:
        a: Matriz de dimensiones m x n.

    Returns:
        Nueva matriz de dimensiones n x m con filas y columnas intercambiadas.

    Raises:
        ValueError: Si la matriz está vacía o sus filas no tienen todas
            la misma longitud.

    Examples:
        >>> transponer([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
    """
    if not a:
        raise ValueError("No se puede transponer una matriz vacía.")

    columnas = len(a[0])
    if any(len(fila) != columnas for fila in a):
        raise ValueError("Todas las filas deben tener la misma longitud.")

    return [[a[i][j] for i in range(len(a))] for j in range(columnas)]


def multiplicar_escalar(a: list[list[float]], escalar: float) -> list[list[float]]:
    """
    Multiplica cada elemento de una matriz por un escalar.

    Args:
        a: Matriz de entrada.
        escalar: Valor por el que se multiplica cada elemento.

    Returns:
        Nueva matriz con cada elemento multiplicado por ``escalar``.

    Examples:
        >>> multiplicar_escalar([[1.0, -2.0], [3.0, 4.0]], 2.5)
        [[2.5, -5.0], [7.5, 10.0]]
    """
    return [[elemento * escalar for elemento in fila] for fila in a]
