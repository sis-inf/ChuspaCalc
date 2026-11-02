import pytest

from escuadra.modulos.electrica.herramienta_correccion_fp import (
    herramienta_correccion_fp,
)
from escuadra.modulos.electrica.correccion_fp import (
    calcular_capacitancia_correccion,
)


def test_herramienta_devuelve_el_mismo_resultado():
    resultado = herramienta_correccion_fp(10000, 0.7, 0.95, 220)

    esperado = calcular_capacitancia_correccion(
        10000, 0.7, 0.95, 220
    )

    assert resultado == esperado


def test_herramienta_usa_frecuencia_por_defecto_de_60():
    resultado = herramienta_correccion_fp(10000, 0.7, 0.95, 220)

    esperado = herramienta_correccion_fp(
        10000, 0.7, 0.95, 220, frecuencia=60
    )

    assert resultado == esperado


def test_herramienta_propaga_value_error_si_fp_deseado_es_menor():
    with pytest.raises(ValueError):
        herramienta_correccion_fp(10000, 0.95, 0.7, 220)
