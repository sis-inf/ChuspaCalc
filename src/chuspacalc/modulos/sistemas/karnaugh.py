"""
Funciones para mapas de Karnaugh de 2 a 4 variables.

La tabla de verdad es una lista de 0 y 1 en orden de mintérminos: la
posición i corresponde a la combinación binaria de i, con A como bit más
significativo (variables A, B, C y D).

``simplificar_expresion`` devuelve una suma de productos mínima: los
términos se separan con " + ", cada término concatena sus literales y la
negación se indica con apóstrofo (A' = no A). Ejemplo: "A'B + AC". Las
funciones constantes devuelven "0" o "1".
"""

from itertools import combinations

VARIABLES = "ABCD"
VARIABLES_POR_LONGITUD = {4: 2, 8: 3, 16: 4}
ORDEN_GRAY = {2: [0, 1], 4: [0, 1, 3, 2]}

# Un implicante es (valor, máscara): los bits de la máscara son variables
# eliminadas y en el valor quedan en 0.
Implicante = tuple[int, int]


def generar_mapa_karnaugh(
    tabla_verdad: list[int],
    num_variables: int,
) -> list[list[int]]:
    """
    Valida la tabla de verdad de un mapa de Karnaugh (2 a 4 variables).

    Retorna la misma tabla de verdad, lista para ``simplificar_expresion``.

    Raises:
        ValueError: Si la cantidad de variables no está entre 2 y 4, si la
            tabla no tiene 2**num_variables valores o si algún valor no es
            0 o 1.
    """
    if num_variables < 2 or num_variables > 4:
        raise ValueError("Solo se soportan entre 2 y 4 variables.")

    if len(tabla_verdad) != 2**num_variables:
        raise ValueError(
            f"Para {num_variables} variables la tabla debe tener "
            f"{2**num_variables} valores; tiene {len(tabla_verdad)}."
        )

    _validar_valores(tabla_verdad)

    return tabla_verdad


def simplificar_expresion(mapa: list[list[int]] | list[int]) -> str:
    """
    Simplifica la función booleana a una suma de productos mínima.

    Args:
        mapa: Tabla de verdad plana de 4, 8 o 16 valores, o un mapa de
            Karnaugh de 2x2, 2x4 o 4x4. En el mapa, las filas corresponden
            a las primeras variables y las columnas a las últimas, ambas en
            orden Gray (00, 01, 11, 10).

    Returns:
        La expresión mínima en suma de productos (ver docstring del módulo).

    Raises:
        ValueError: Si la tabla no tiene 4, 8 o 16 valores, si el mapa no
            tiene una forma válida o si algún valor no es 0 o 1.
    """
    if mapa and all(isinstance(fila, list) for fila in mapa):
        tabla = _tabla_desde_mapa(mapa)  # type: ignore[arg-type]
    else:
        tabla = list(mapa)  # type: ignore[arg-type]

    num_variables = _num_variables(tabla)
    _validar_valores(tabla)

    minterminos = [i for i, valor in enumerate(tabla) if valor == 1]
    if not minterminos:
        return "0"
    if len(minterminos) == len(tabla):
        return "1"

    primos = _implicantes_primos(minterminos)
    cobertura = _cobertura_minima(primos, minterminos, num_variables)

    return " + ".join(sorted(_termino(p, num_variables) for p in cobertura))


def _validar_valores(tabla: list[int]) -> None:
    for posicion, valor in enumerate(tabla):
        if type(valor) not in (int, bool) or valor not in (0, 1):
            raise ValueError(f"Solo se admiten 0 y 1: posición {posicion} = {valor!r}.")


def _num_variables(tabla: list[int]) -> int:
    if len(tabla) not in VARIABLES_POR_LONGITUD:
        raise ValueError(
            "La tabla de verdad debe tener 4, 8 o 16 valores (2 a 4 variables); "
            f"tiene {len(tabla)}."
        )
    return VARIABLES_POR_LONGITUD[len(tabla)]


def _tabla_desde_mapa(mapa: list[list[int]]) -> list[int]:
    filas = len(mapa)
    columnas = len(mapa[0])
    forma_valida = (filas, columnas) in {(2, 2), (2, 4), (4, 4)}
    if not forma_valida or any(len(fila) != columnas for fila in mapa):
        raise ValueError("El mapa de Karnaugh debe ser de 2x2, 2x4 o 4x4.")

    bits_columnas = columnas.bit_length() - 1
    tabla = [0] * (filas * columnas)
    for i, fila in enumerate(mapa):
        for j, valor in enumerate(fila):
            indice = ORDEN_GRAY[filas][i] << bits_columnas | ORDEN_GRAY[columnas][j]
            tabla[indice] = valor
    return tabla


def _implicantes_primos(minterminos: list[int]) -> set[Implicante]:
    """Quine-McCluskey: combina implicantes que difieren en un solo bit."""
    actuales = {(m, 0) for m in minterminos}
    primos: set[Implicante] = set()
    while actuales:
        siguientes: set[Implicante] = set()
        combinados: set[Implicante] = set()
        for a, b in combinations(sorted(actuales), 2):
            diferencia = a[0] ^ b[0]
            if a[1] == b[1] and diferencia & (diferencia - 1) == 0:
                siguientes.add((a[0] & ~diferencia, a[1] | diferencia))
                combinados.update((a, b))
        primos |= actuales - combinados
        actuales = siguientes
    return primos


def _cubre(implicante: Implicante, mintermino: int) -> bool:
    valor, mascara = implicante
    return (mintermino & ~mascara) == valor


def _literales(implicante: Implicante, num_variables: int) -> int:
    return num_variables - bin(implicante[1]).count("1")


def _cobertura_minima(
    primos: set[Implicante],
    minterminos: list[int],
    num_variables: int,
) -> list[Implicante]:
    """Elige la menor cantidad de primos que cubre todo (y menos literales)."""
    esenciales = set()
    for m in minterminos:
        cubren = [p for p in primos if _cubre(p, m)]
        if len(cubren) == 1:
            esenciales.add(cubren[0])

    pendientes = [m for m in minterminos if not any(_cubre(p, m) for p in esenciales)]
    candidatos = sorted(primos - esenciales)

    for cantidad in range(len(candidatos) + 1):
        coberturas = [
            grupo
            for grupo in combinations(candidatos, cantidad)
            if all(any(_cubre(p, m) for p in grupo) for m in pendientes)
        ]
        if coberturas:
            mejor = min(
                coberturas,
                key=lambda grupo: sum(_literales(p, num_variables) for p in grupo),
            )
            return sorted(esenciales) + list(mejor)

    return sorted(primos)


def _termino(implicante: Implicante, num_variables: int) -> str:
    valor, mascara = implicante
    literales = []
    for i in range(num_variables):
        bit = 1 << (num_variables - 1 - i)
        if not mascara & bit:
            literales.append(VARIABLES[i] if valor & bit else VARIABLES[i] + "'")
    return "".join(literales)
