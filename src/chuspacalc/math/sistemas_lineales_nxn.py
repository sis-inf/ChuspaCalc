"""
Módulo para resolver sistemas de ecuaciones lineales NxN.
Utiliza eliminación gaussiana con pivoteo parcial.
"""

import math


def resolver_sistema(A: list[list[float]], b: list[float]) -> list[float] | None:
    """
    Resuelve el sistema A·x = b usando eliminación gaussiana con pivoteo parcial.

    Args:
        A: Matriz de coeficientes n×n.
        b: Vector de términos independientes de tamaño n.

    Returns:
        Lista con la solución x, o None si el sistema es singular.

    Raises:
        ValueError: Si A está vacía, si A no es cuadrada, si b no tiene
            el mismo tamaño que A o si algún valor de A o b no es finito.
    """
    if not A:
        raise ValueError("La matriz A no puede estar vacía.")

    n = len(A)

    for fila in A:
        if len(fila) != n:
            # fmt: off
            raise ValueError(
                f"La matriz A debe ser cuadrada: se esperaban filas de tamaño {n}."
            )
            # fmt: on

    if len(b) != n:
        raise ValueError(f"El vector de términos independientes debe tener tamaño {n}.")

    for i, fila in enumerate(A):
        for j, valor in enumerate(fila):
            if not math.isfinite(valor):
                raise ValueError(f"El valor de A[{i}][{j}] debe ser finito: {valor}.")

    for i, valor in enumerate(b):
        if not math.isfinite(valor):
            raise ValueError(f"El valor de b[{i}] debe ser finito: {valor}.")

    # Crear copia aumentada [A|b] para no modificar los originales
    M = [A[i][:] + [b[i]] for i in range(n)]

    # Eliminación hacia adelante con pivoteo parcial
    for col in range(n):
        # Buscar la fila con el mayor valor absoluto en esta columna (pivote)
        fila_pivote = max(range(col, n), key=lambda f: abs(M[f][col]))

        # Intercambiar la fila actual con la del pivote
        M[col], M[fila_pivote] = M[fila_pivote], M[col]

        pivote = M[col][col]

        # Si el pivote es cercano a cero, el sistema es singular
        if abs(pivote) < 1e-10:
            return None

        # Eliminar los coeficientes debajo del pivote
        for fila in range(col + 1, n):
            factor = M[fila][col] / pivote
            for j in range(col, n + 1):
                M[fila][j] -= factor * M[col][j]

    # Sustitución hacia atrás
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = M[i][n]
        for j in range(i + 1, n):
            x[i] -= M[i][j] * x[j]
        x[i] /= M[i][i]

    return x
