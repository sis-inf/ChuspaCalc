"""Pruebas unitarias para escuadra.modulos.sistemas.herramienta_calculadora_subred."""

from escuadra.modulos.sistemas.herramienta_calculadora_subred import (
    herramienta_calculadora_subred,
)


def test_red_y_broadcast():
    resultado = herramienta_calculadora_subred("192.168.1.10", "24")

    assert "RED: 192.168.1.0" in resultado
    assert "BROADCAST: 192.168.1.255" in resultado


def test_mascara_hosts_y_total():
    resultado = herramienta_calculadora_subred("192.168.1.10", "24")

    assert "MÁSCARA" in resultado
    assert "PRIMER HOST" in resultado
    assert "ÚLTIMO HOST" in resultado
    assert "TOTAL HOSTS: 254" in resultado


def test_prefijo_33_devuelve_error():
    resultado = herramienta_calculadora_subred("192.168.1.10", "33")

    assert resultado.startswith("ERROR:")


def test_ip_invalida_devuelve_error():
    resultado = herramienta_calculadora_subred("999.999.999.999", "24")

    assert resultado.startswith("ERROR:")


def test_ipv6_muestra_red_rango_y_total():
    resultado = herramienta_calculadora_subred("2001:db8::1", "64")

    assert "RED: 2001:db8::" in resultado
    assert "PREFIJO: /64" in resultado
    assert "PRIMERA DIRECCIÓN: 2001:db8::" in resultado
    assert "ÚLTIMA DIRECCIÓN: 2001:db8::ffff:ffff:ffff:ffff" in resultado
    assert f"TOTAL DIRECCIONES: {2**64}" in resultado


def test_ipv6_no_muestra_broadcast():
    resultado = herramienta_calculadora_subred("2001:db8::1", "64")

    assert "BROADCAST" not in resultado


def test_ipv6_prefijo_129_devuelve_error():
    resultado = herramienta_calculadora_subred("2001:db8::1", "129")

    assert resultado == "ERROR: El prefijo CIDR de IPv6 debe estar entre 0 y 128"


def test_ipv6_invalida_devuelve_error():
    resultado = herramienta_calculadora_subred("2001:db8::zz", "64")

    assert resultado.startswith("ERROR:")
    assert "IPv6" in resultado
