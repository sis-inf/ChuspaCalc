"""
Módulo para resolver sistemas de ecuaciones lineales NxN.
Utiliza eliminación gaussiana con pivoteo parcial.
"""


def resolver_sistema(A: list[list[float]], b: list[float]) -> list[float] | None:
    """
    Resuelve el sistema A·x = b usando eliminación gaussiana con pivoteo parcial.

    Args:
        A: Matriz de coeficientes n×n.
        b: Vector de términos independientes de tamaño n.

    Returns:
        Lista con la solución x, o None si el sistema es singular.
    """
    n = len(A)

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
