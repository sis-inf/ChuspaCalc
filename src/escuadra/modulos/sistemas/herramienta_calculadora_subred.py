"""
Wrapper de herramienta para calculadora de subredes IP/CIDR
"""

from .calculadora_subred import ErrorCIDR, calcular_subred


def herramienta_calculadora_subred(ip: str, prefijo_cidr: str) -> str:
    """
    Herramienta CLI/texto que ejecuta cálculo de subred IPv4 o IPv6.
    """

    try:
        resultado = calcular_subred(ip, prefijo_cidr)

        if resultado.get("version") == 6:
            return (
                f"RED: {resultado['red']}\n"
                f"PREFIJO: /{resultado['prefijo']}\n"
                f"PRIMERA DIRECCIÓN: {resultado['primera_direccion']}\n"
                f"ÚLTIMA DIRECCIÓN: {resultado['ultima_direccion']}\n"
                f"TOTAL DIRECCIONES: {resultado['total_direcciones']}"
            )

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
