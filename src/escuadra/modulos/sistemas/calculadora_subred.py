import ipaddress


class ErrorCIDR(ValueError):
    pass


def _calcular_subred_ipv6(ip: str, prefijo: int) -> dict:
    """
    Calcula la red IPv6 a partir de una IP y un prefijo entre 0 y 128.

    IPv6 no tiene dirección broadcast: todas las direcciones del rango
    (de primera_direccion a ultima_direccion) son utilizables.
    """
    if prefijo < 0 or prefijo > 128:
        raise ErrorCIDR("El prefijo CIDR de IPv6 debe estar entre 0 y 128")

    try:
        red = ipaddress.IPv6Network(f"{ip}/{prefijo}", strict=False)
    except ValueError:
        raise ErrorCIDR(f"La dirección IPv6 '{ip}' no es válida")

    return {
        "version": 6,
        "red": str(red.network_address),
        "prefijo": red.prefixlen,
        "primera_direccion": str(red.network_address),
        "ultima_direccion": str(red[-1]),
        "total_direcciones": red.num_addresses,
    }


def calcular_subred(ip: str, prefijo_cidr: str) -> dict:
    """
    Calcula información de subred a partir de una IP (IPv4 o IPv6) y un prefijo CIDR.

    Retorna para IPv4 (prefijo entre 1 y 32):
        dict con:
        - red
        - broadcast
        - mascara
        - primer_host
        - ultimo_host
        - total_hosts

    Retorna para IPv6 (prefijo entre 0 y 128), sin broadcast:
        dict con:
        - version (6)
        - red
        - prefijo
        - primera_direccion
        - ultima_direccion
        - total_direcciones
    """

    # ===== VALIDACIÓN =====
    try:
        prefijo = int(prefijo_cidr)
    except ValueError:
        raise ErrorCIDR("El prefijo CIDR debe ser un número entero")

    if ":" in ip:
        return _calcular_subred_ipv6(ip, prefijo)

    if prefijo < 1 or prefijo > 32:
        raise ErrorCIDR("El prefijo CIDR debe estar entre 1 y 32")

    octetos = ip.split(".")
    if len(octetos) != 4:
        raise ErrorCIDR("La dirección IP debe tener cuatro octetos")

    for octeto in octetos:
        try:
            valor = int(octeto)
        except ValueError:
            raise ErrorCIDR("Cada octeto de la IP debe ser un número entero")

        if valor < 0 or valor > 255:
            raise ErrorCIDR("Cada octeto de la IP debe estar entre 0 y 255")

    try:
        red = ipaddress.ip_network(f"{ip}/{prefijo}", strict=False)
    except ValueError:
        raise ErrorCIDR("IP inválida o formato incorrecto")

    # ===== CÁLCULOS =====
    network_address = red.network_address
    broadcast_address = red.broadcast_address
    netmask = red.netmask

    # Para prefijos 31 y 32 no hay hosts asignables según los criterios del issue
    if red.prefixlen >= 31:
        primer_host = "N/A"
        ultimo_host = "N/A"
        total_hosts = 0
    else:
        # Sumamos/restamos enteros sobre las direcciones de red y broadcast
        primer_host = str(network_address + 1)
        ultimo_host = str(broadcast_address - 1)
        total_hosts = red.num_addresses - 2

    return {
        "red": str(network_address),
        "broadcast": str(broadcast_address),
        "mascara": str(netmask),
        "primer_host": primer_host,
        "ultimo_host": ultimo_host,
        "total_hosts": total_hosts,
    }
