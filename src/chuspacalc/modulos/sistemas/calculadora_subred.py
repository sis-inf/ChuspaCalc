import ipaddress

from ..matematicas.error_validacion import ErrorValidacion


class ErrorCIDR(ErrorValidacion):
    pass


def calcular_subred(ip: str, prefijo_cidr: str | int) -> dict[str, str | int]:
    """
    Calcula información de subred a partir de una IP y un prefijo CIDR.

    Args:
        ip: Dirección IPv4 en notación decimal con puntos.
        prefijo_cidr: Prefijo CIDR entre 1 y 32 (entero o texto numérico).

    Retorna:
        dict con:
        - red
        - broadcast
        - mascara
        - primer_host
        - ultimo_host
        - total_hosts

    Raises:
        ErrorCIDR: Si los tipos, el prefijo o la IP no son válidos.
    """

    # ===== VALIDACIÓN =====
    if not isinstance(ip, str):
        raise ErrorCIDR("La dirección IP debe ser una cadena de texto")

    if isinstance(prefijo_cidr, bool) or not isinstance(prefijo_cidr, (str, int)):
        raise ErrorCIDR("El prefijo CIDR debe ser un número entero")

    try:
        prefijo = int(prefijo_cidr)
    except ValueError:
        raise ErrorCIDR("El prefijo CIDR debe ser un número entero")

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
