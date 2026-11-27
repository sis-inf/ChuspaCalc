"""
Wrapper de herramienta para calculadora de subredes IP/CIDR
"""

from chuspacalc.modulos.sistemas.calculadora_subred import ErrorCIDR, calcular_subred


def herramienta_calculadora_subred(ip: str, prefijo_cidr: str | int) -> str:
    """
    Herramienta CLI/texto que ejecuta cálculo de subred.

    Delega la validación y el cálculo en calcular_subred y solo da formato
    a la salida.

    Args:
        ip: Dirección IPv4 en notación decimal con puntos.
        prefijo_cidr: Prefijo CIDR entre 1 y 32 (entero o texto numérico).

    Returns:
        Texto de seis líneas (RED, BROADCAST, MÁSCARA, PRIMER HOST,
        ÚLTIMO HOST y TOTAL HOSTS) o, si calcular_subred lanza ErrorCIDR,
        una sola línea con el formato "ERROR: <mensaje>".
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
