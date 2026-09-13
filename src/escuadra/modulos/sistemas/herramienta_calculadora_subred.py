"""
Wrapper de herramienta para calculadora de subredes IP/CIDR
"""

from escuadra.modulos.sistemas.calculadora_subred import calcular_subred, ErrorCIDR


def herramienta_calculadora_subred(ip: str, prefijo_cidr: str) -> str:
    """
    Herramienta CLI/texto que ejecuta cálculo de subred.
    """

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
