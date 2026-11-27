"""Pruebas unitarias para chuspacalc.modulos.sistemas.herramienta_calculadora_subred."""

from chuspacalc.modulos.sistemas.herramienta_calculadora_subred import (
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


def test_salida_valida_tiene_seis_lineas_en_orden():
    resultado = herramienta_calculadora_subred("192.168.1.10", "24")
    etiquetas = [linea.split(":")[0] for linea in resultado.split("\n")]

    assert etiquetas == [
        "RED",
        "BROADCAST",
        "MÁSCARA",
        "PRIMER HOST",
        "ÚLTIMO HOST",
        "TOTAL HOSTS",
    ]


def test_prefijo_entero_equivale_a_texto():
    assert herramienta_calculadora_subred(
        "192.168.1.10", 24
    ) == herramienta_calculadora_subred("192.168.1.10", "24")


def test_prefijo_31_sin_hosts_asignables():
    resultado = herramienta_calculadora_subred("10.0.0.0", "31")

    assert "PRIMER HOST: N/A" in resultado
    assert "ÚLTIMO HOST: N/A" in resultado
    assert "TOTAL HOSTS: 0" in resultado


def test_error_conserva_mensaje_del_motor():
    resultado = herramienta_calculadora_subred("192.168.1.10", "33")

    assert resultado == "ERROR: El prefijo CIDR debe estar entre 1 y 32"


def test_entradas_invalidas_devuelven_error_sin_propagar():
    assert herramienta_calculadora_subred(None, "24").startswith("ERROR:")
    assert herramienta_calculadora_subred("192.168.1.10", None).startswith("ERROR:")
    assert herramienta_calculadora_subred("192.168.1.10", "abc").startswith("ERROR:")
    assert herramienta_calculadora_subred("192.168.1.10", "0").startswith("ERROR:")
