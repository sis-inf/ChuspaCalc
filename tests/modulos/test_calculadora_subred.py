import pytest

from escuadra.modulos.sistemas.calculadora_subred import (
    ErrorCIDR,
    calcular_subred,
)


def test_calcular_subred_direccion_ipv4_prefijo_24():
    resultado = calcular_subred("192.168.1.10", "24")

    assert resultado == {
        "red": "192.168.1.0",
        "broadcast": "192.168.1.255",
        "mascara": "255.255.255.0",
        "primer_host": "192.168.1.1",
        "ultimo_host": "192.168.1.254",
        "total_hosts": 254,
    }


def test_calcular_subred_prefijo_30_tiene_dos_hosts():
    resultado = calcular_subred("192.168.1.10", "30")

    assert resultado["total_hosts"] == 2
    assert resultado["primer_host"] == "192.168.1.9"
    assert resultado["ultimo_host"] == "192.168.1.10"


def test_calcular_subred_prefijo_31_no_tiene_hosts_asignables():
    resultado = calcular_subred("192.168.1.10", "31")

    assert resultado["primer_host"] == "N/A"
    assert resultado["ultimo_host"] == "N/A"
    assert resultado["total_hosts"] == 0


def test_calcular_subred_prefijo_32_no_tiene_hosts_asignables():
    resultado = calcular_subred("192.168.1.10", "32")

    assert resultado["primer_host"] == "N/A"
    assert resultado["ultimo_host"] == "N/A"
    assert resultado["total_hosts"] == 0


def test_prefijo_no_numerico_lanza_error_cidr():
    with pytest.raises(ErrorCIDR):
        calcular_subred("192.168.1.10", "abc")


def test_prefijo_menor_que_cero_lanza_error_cidr():
    with pytest.raises(ErrorCIDR):
        calcular_subred("192.168.1.10", "-1")


def test_prefijo_mayor_que_32_lanza_error_cidr():
    with pytest.raises(ErrorCIDR):
        calcular_subred("192.168.1.10", "33")


def test_ip_invalida_lanza_error_cidr():
    with pytest.raises(ErrorCIDR):
        calcular_subred("300.1.1.1", "24")


def test_prefijo_ipv4_cero_lanza_error_cidr():
    with pytest.raises(ErrorCIDR, match="entre 1 y 32"):
        calcular_subred("192.168.1.10", "0")


def test_calcular_subred_ipv6_prefijo_64():
    resultado = calcular_subred("2001:db8::1", "64")

    assert resultado == {
        "version": 6,
        "red": "2001:db8::",
        "prefijo": 64,
        "primera_direccion": "2001:db8::",
        "ultima_direccion": "2001:db8::ffff:ffff:ffff:ffff",
        "total_direcciones": 2**64,
    }


def test_calcular_subred_ipv6_no_tiene_broadcast():
    resultado = calcular_subred("2001:db8::1", "64")

    assert "broadcast" not in resultado


def test_calcular_subred_ipv6_prefijo_128_es_una_direccion():
    resultado = calcular_subred("2001:db8::1", "128")

    assert resultado["red"] == "2001:db8::1"
    assert resultado["primera_direccion"] == "2001:db8::1"
    assert resultado["ultima_direccion"] == "2001:db8::1"
    assert resultado["total_direcciones"] == 1


def test_calcular_subred_ipv6_prefijo_0_abarca_todo():
    resultado = calcular_subred("2001:db8::1", "0")

    assert resultado["red"] == "::"
    assert resultado["ultima_direccion"] == "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff"
    assert resultado["total_direcciones"] == 2**128


def test_calcular_subred_ipv6_prefijo_48():
    resultado = calcular_subred("2001:db8:abcd:12::1", "48")

    assert resultado["red"] == "2001:db8:abcd::"
    assert resultado["ultima_direccion"] == "2001:db8:abcd:ffff:ffff:ffff:ffff:ffff"
    assert resultado["total_direcciones"] == 2**80


def test_prefijo_ipv6_mayor_que_128_lanza_error_cidr():
    with pytest.raises(ErrorCIDR, match="entre 0 y 128"):
        calcular_subred("2001:db8::1", "129")


def test_prefijo_ipv6_negativo_lanza_error_cidr():
    with pytest.raises(ErrorCIDR, match="entre 0 y 128"):
        calcular_subred("2001:db8::1", "-1")


def test_prefijo_ipv6_no_numerico_lanza_error_cidr():
    with pytest.raises(ErrorCIDR, match="número entero"):
        calcular_subred("2001:db8::1", "abc")


def test_ipv6_invalida_lanza_error_cidr():
    with pytest.raises(ErrorCIDR, match="IPv6"):
        calcular_subred("2001:db8::zz", "64")


def test_ipv6_con_doble_compresion_lanza_error_cidr():
    with pytest.raises(ErrorCIDR, match="IPv6"):
        calcular_subred("2001::db8::1", "64")
