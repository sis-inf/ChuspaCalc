import pytest

from escuadra.modulos.sistemas.calculadora_subred import (
    calcular_subred,
    ErrorCIDR,
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
