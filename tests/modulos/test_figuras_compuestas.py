import pytest

from chuspacalc.modulos.geometria.figuras_compuestas import (
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


VALIDA = {"tipo": "cubo", "parametros": {"lado": 2}}
CALCULOS = [calcular_area_compuesta, calcular_volumen_compuesto]


@pytest.mark.parametrize("calcular", CALCULOS)
@pytest.mark.parametrize(
    ("figura", "mensaje"),
    [
        (["cubo", {"lado": 2}], r"Figura 1: el descriptor debe ser un mapeo"),
        (None, r"Figura 1: el descriptor debe ser un mapeo"),
        ({"parametros": {"lado": 2}}, r"Figura 1: falta la clave 'tipo'"),
        ({"tipo": "cubo"}, r"Figura 1: falta la clave 'parametros'"),
        ({"tipo": ["cubo"], "parametros": {}}, r"Figura 1: 'tipo' debe ser un texto"),
        (
            {"tipo": "cubo", "parametros": [2]},
            r"Figura 1: 'parametros' debe ser un mapeo",
        ),
    ],
)
def test_estructura_invalida_lanza_value_error(calcular, figura, mensaje):
    primera = {"tipo": "rectangulo", "parametros": {"base": 1, "altura": 1}}
    if calcular is calcular_volumen_compuesto:
        primera = VALIDA

    with pytest.raises(ValueError, match=mensaje):
        calcular([primera, figura])
