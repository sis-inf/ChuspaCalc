from ..matematicas.error_validacion import ErrorValidacion

BASES_SOPORTADAS: set[int] = {2, 8, 10, 16}

DIGITOS_POR_BASE: dict[int, set[str]] = {
    2: set("01"),
    8: set("01234567"),
    10: set("0123456789"),
    16: set("0123456789ABCDEF"),
}


def _validar_base(base: int, nombre: str) -> None:
    """Valida que la base sea un entero soportado."""
    if isinstance(base, bool) or not isinstance(base, int):
        raise ErrorValidacion(f"La base {nombre} debe ser un entero: {base!r}")

    if base not in BASES_SOPORTADAS:
        raise ErrorValidacion(f"Base {nombre} no soportada: {base}")


def _validar_digitos(numero: str, base: int) -> None:
    cuerpo = numero[1:] if numero[:1] in "+-" else numero
    for caracter in cuerpo:
        if caracter not in DIGITOS_POR_BASE[base]:
            raise ErrorValidacion(f"Carácter inválido '{caracter}' para base {base}")


def convertir(
    numero: str, base_origen: int, base_destino: int
) -> dict[str, str | int]:
    """
    Convierte números entre bases 2, 8, 10 y 16.

    Args:
        numero: Número a convertir, escrito en la base de origen.
        base_origen: Base en la que está escrito el número (2, 8, 10 o 16).
        base_destino: Base a la que se quiere convertir (2, 8, 10 o 16).

    Returns:
        Diccionario con el número original, las bases y el resultado.

    Raises:
        ErrorValidacion: Si el número no es texto, está vacío o tiene
            caracteres inválidos para su base, o si alguna base no es un
            entero soportado.
    """

    if not isinstance(numero, str):
        raise ErrorValidacion(
            f"El número debe ser una cadena de texto: {type(numero).__name__}"
        )

    if not numero or not numero.strip():
        raise ErrorValidacion("El número no puede estar vacío")

    _validar_base(base_origen, "origen")
    _validar_base(base_destino, "destino")

    numero = numero.strip().upper()

    _validar_digitos(numero, base_origen)

    try:
        valor_decimal = int(numero, base_origen)
    except ValueError as error:
        raise ErrorValidacion(
            f"Número inválido para base {base_origen}: {numero}"
        ) from error

    if base_destino == 2:
        resultado = bin(valor_decimal)[2:]
    elif base_destino == 8:
        resultado = oct(valor_decimal)[2:]
    elif base_destino == 10:
        resultado = str(valor_decimal)
    else:
        resultado = hex(valor_decimal)[2:].upper()

    return {
        "numero_original": numero,
        "base_origen": base_origen,
        "resultado": resultado,
        "base_destino": base_destino,
    }