import pytest

from escuadra.modulos.geometria.figuras_compuestas import (
    calcular_area_compuesta,
    calcular_volumen_compuesto,
)


def test_calcular_area_compuesta_suma_y_resta():
    figuras = [
        {
            "tipo": "rectangulo",
            "parametros": {"base": 10, "altura": 5},
            "operacion": "sumar",
        },
        {
            "tipo": "rectangulo",
            "parametros": {"base": 2, "altura": 5},
            "operacion": "restar",
        },
    ]

    assert calcular_area_compuesta(figuras) == 40


def test_operacion_ausente_equivale_a_sumar():
    figuras = [
        {
            "tipo": "rectangulo",
            "parametros": {"base": 10, "altura": 5},
        }
    ]

    assert calcular_area_compuesta(figuras) == 50


def test_tipo_area_no_soportado_lanza_value_error():
    figuras = [
        {
            "tipo": "pentagono",
            "parametros": {},
        }
    ]

    with pytest.raises(ValueError, match="Figura de área no soportada"):
        calcular_area_compuesta(figuras)


def test_operacion_no_valida_lanza_value_error():
    figuras = [
        {
            "tipo": "rectangulo",
            "parametros": {"base": 10, "altura": 5},
            "operacion": "multiplicar",
        }
    ]

    with pytest.raises(ValueError, match="Operación no válida"):
        calcular_area_compuesta(figuras)


def test_calcular_volumen_compuesto_suma_y_resta():
    figuras = [
        {
            "tipo": "cubo",
            "parametros": {"lado": 2},
            "operacion": "sumar",
        },
        {
            "tipo": "cubo",
            "parametros": {"lado": 1},
            "operacion": "restar",
        },
    ]

    assert calcular_volumen_compuesto(figuras) == 7


def test_lista_vacia_devuelve_cero():
    assert calcular_area_compuesta([]) == 0
    assert calcular_volumen_compuesto([]) == 0
