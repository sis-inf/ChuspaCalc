"""
Wrapper de herramienta para calculadora de subredes IP/CIDR
"""

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.sistemas.calculadora_subred import ErrorCIDR, calcular_subred


def herramienta_calculadora_subred(ip: str, prefijo_cidr: str) -> str:
    """
    Herramienta CLI/texto que ejecuta cálculo de subred.

    Lanza ErrorValidacion si ip o prefijo_cidr no son cadenas de texto.
    Los errores de formato de la IP o del prefijo se devuelven como texto
    ("ERROR: ...") para no cambiar el comportamiento actual.
    """
    if not isinstance(ip, str):
        raise ErrorValidacion(
            f"La dirección IP debe ser una cadena de texto, se recibió {type(ip).__name__}."
        )

    if not isinstance(prefijo_cidr, str):
        raise ErrorValidacion(
            "El prefijo CIDR debe ser una cadena de texto, "
            f"se recibió {type(prefijo_cidr).__name__}."
        )

    try:
        resultado = calcular_subred(ip, prefijo_cidr)

        return (
            f"RED: {resultado['red']}\n"
            f"BROADCAST: {resultado['broadcast']}\n"
            f"MÁSCARA: {resultado['mascara']}\n"
            f"PRIMER HOST: {resultado['primer_host']}\n"
            f"ÚLTIMO HOST: {resultado['ultimo_host']}\n"
            f"TOTAL HOSTS: {resultado['total_hosts']}"
        )

    except ErrorCIDR as e:
        return f"ERROR: {str(e)}"