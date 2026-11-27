from ..matematicas.error_validacion import ErrorValidacion


def caracter_a_ascii(char: str) -> dict[str, str | int]:
    """
    Convierte un carácter ASCII a sus representaciones.

    Args:
        char: Carácter a convertir (una sola letra, dígito o símbolo ASCII).

    Returns:
        Diccionario con las claves "caracter", "decimal", "hexadecimal",
        "octal" y "binario".

    Raises:
        ErrorValidacion: Si char no es texto, no es un solo carácter o está
            fuera del rango ASCII (0 a 127).
    """

    if not isinstance(char, str):
        raise ErrorValidacion("El carácter debe ser una cadena de texto")

    if len(char) != 1:
        raise ErrorValidacion("Debe ser un solo carácter")

    codigo = ord(char)

    if not 0 <= codigo <= 127:
        raise ErrorValidacion("Carácter fuera del rango ASCII")

    return {
        "caracter": char,
        "decimal": codigo,
        "hexadecimal": hex(codigo),
        "octal": oct(codigo),
        "binario": bin(codigo),
    }


def ascii_a_caracter(codigo: int) -> dict[str, str | int]:
    """
    Convierte un código ASCII a carácter y sus representaciones.

    Args:
        codigo: Código ASCII entero, entre 0 y 127.

    Returns:
        Diccionario con las claves "caracter", "decimal", "hexadecimal",
        "octal" y "binario".

    Raises:
        ErrorValidacion: Si codigo no es un entero o está fuera del rango
            ASCII (0 a 127).
    """
    if isinstance(codigo, bool) or not isinstance(codigo, int):
        raise ErrorValidacion("El código ASCII debe ser un número entero")

    if not 0 <= codigo <= 127:
        raise ErrorValidacion("Código ASCII fuera de rango")

    caracter = chr(codigo)

    return {
        "caracter": caracter,
        "decimal": codigo,
        "hexadecimal": hex(codigo),
        "octal": oct(codigo),
        "binario": bin(codigo),
    }


def listar_ascii_rango(inicio: int, fin: int) -> list[dict[str, str | int]]:
    """
    Retorna una lista de diccionarios para un rango ASCII.

    Args:
        inicio: Primer código ASCII del rango (entre 0 y 127).
        fin: Último código ASCII del rango, incluido (entre 0 y 127).

    Returns:
        Lista con un diccionario por cada código del rango, con el mismo
        formato que devuelve ascii_a_caracter.

    Raises:
        ErrorValidacion: Si inicio o fin no son enteros, si están fuera del
            rango ASCII (0 a 127) o si inicio es mayor que fin.
    """

    if isinstance(inicio, bool) or not isinstance(inicio, int):
        raise ErrorValidacion("El inicio del rango debe ser un número entero")

    if isinstance(fin, bool) or not isinstance(fin, int):
        raise ErrorValidacion("El fin del rango debe ser un número entero")

    if not (0 <= inicio <= 127 and 0 <= fin <= 127):
        raise ErrorValidacion("Rango ASCII inválido")

    if inicio > fin:
        raise ErrorValidacion("inicio no puede ser mayor que fin")

    return [ascii_a_caracter(codigo) for codigo in range(inicio, fin + 1)]
