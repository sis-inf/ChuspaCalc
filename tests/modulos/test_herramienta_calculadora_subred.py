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
