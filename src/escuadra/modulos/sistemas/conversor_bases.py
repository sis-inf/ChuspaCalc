BASES_SOPORTADAS = {2, 8, 10, 16}


def convertir(numero: str, base_origen: int, base_destino: int) -> dict:
    """
    Convierte números entre bases 2, 8, 10 y 16.
    """

    if not numero or not numero.strip():
        raise ValueError("El número no puede estar vacío")

    if base_origen not in BASES_SOPORTADAS:
        raise ValueError(f"Base origen no soportada: {base_origen}")

    if base_destino not in BASES_SOPORTADAS:
        raise ValueError(f"Base destino no soportada: {base_destino}")

    numero = numero.strip().upper()

    try:
        valor_decimal = int(numero, base_origen)
    except ValueError as error:
        raise ValueError(
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
