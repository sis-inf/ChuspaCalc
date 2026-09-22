import ipaddress


class ErrorCIDR(Exception):
    pass


def calcular_subred(ip: str, prefijo_cidr: str) -> dict:
    """
    Calcula información de subred a partir de una IP y un prefijo CIDR.

    Retorna:
        dict con:
        - red
        - broadcast
        - mascara
        - primer_host
        - ultimo_host
        - total_hosts
    """

    # ===== VALIDACIÓN =====
    try:
        prefijo = int(prefijo_cidr)
    except ValueError:
        raise ErrorCIDR("El prefijo CIDR debe ser un número entero")

    if prefijo < 0 or prefijo > 32:
        raise ErrorCIDR("El prefijo CIDR debe estar entre 0 y 32")

    try:
        red = ipaddress.ip_network(f"{ip}/{prefijo}", strict=False)
    except ValueError:
        raise ErrorCIDR("IP inválida o formato incorrecto")

    # ===== CÁLCULOS =====
    network_address = red.network_address
    broadcast_address = red.broadcast_address
    netmask = red.netmask

    hosts = list(red.hosts())

    if len(hosts) > 0:
        primer_host = hosts[0]
        ultimo_host = hosts[-1]
        total_hosts = len(hosts)
    else:
        primer_host = None
        ultimo_host = None
        total_hosts = 0

    return {
        "red": str(network_address),
        "broadcast": str(broadcast_address),
        "mascara": str(netmask),
        "primer_host": str(primer_host) if primer_host else "N/A",
        "ultimo_host": str(ultimo_host) if ultimo_host else "N/A",
        "total_hosts": total_hosts,
    }
