def caracter_a_ascii(char: str) -> dict:
    """
    Convierte un carácter ASCII a sus representaciones.
    """

    if len(char) != 1:
        raise ValueError("Debe ser un solo carácter")

    codigo = ord(char)

    if not 0 <= codigo <= 127:
        raise ValueError("Carácter fuera del rango ASCII")

    return {
        "caracter": char,
        "decimal": codigo,
        "hexadecimal": hex(codigo),
        "octal": oct(codigo),
        "binario": bin(codigo),
    }


def ascii_a_caracter(codigo: int) -> dict:
    """
    Convierte un código ASCII a carácter y sus representaciones.
    """

    if not 0 <= codigo <= 127:
        raise ValueError("Código ASCII fuera de rango")

    caracter = chr(codigo)

    return {
        "caracter": caracter,
        "decimal": codigo,
        "hexadecimal": hex(codigo),
        "octal": oct(codigo),
        "binario": bin(codigo),
    }


def listar_ascii_rango(inicio: int, fin: int) -> list:
    """
    Retorna una lista de diccionarios para un rango ASCII.
    """

    if not (0 <= inicio <= 127 and 0 <= fin <= 127):
        raise ValueError("Rango ASCII inválido")

    if inicio > fin:
        raise ValueError("inicio no puede ser mayor que fin")

    return [ascii_a_caracter(codigo) for codigo in range(inicio, fin + 1)]
