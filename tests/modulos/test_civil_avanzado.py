"""
Tests unitarios para módulos avanzados de civil:
- area_seccion.py
- deflexion_viga.py
- momento_flector.py
"""

import pytest

from chuspacalc.modulos.civil.area_seccion import (
    area_circular,
    area_circular_hueca,
    area_perfil_i,
    area_perfil_t,
    area_rectangular,
)
from chuspacalc.modulos.civil.deflexion_viga import (
    calcular_deflexion_max,
)
from chuspacalc.modulos.civil.momento_flector import (
    calcular_momento_max,
    calcular_momento_maximo,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

# ------------------------
# Área de secciones
# ------------------------


def test_area_seccion_rectangular():
    # Área = base * altura
    assert area_rectangular(10, 5) == 50


def test_area_seccion_circular():
    # Área = pi * r²
    assert area_circular(2) == pytest.approx(4 * 3.141592653589793)


def test_area_seccion_circular_hueca():
    # Área = pi * (R² - r²)
    esperado = 3.141592653589793 * (5**2 - 3**2)

    assert area_circular_hueca(5, 3) == pytest.approx(esperado)


def test_area_perfil_i():
    resultado = area_perfil_i(
        ancho_ala=10,
        espesor_ala=2,
        altura_alma=20,
        espesor_alma=1,
    )

    esperado = 2 * 10 * 2 + 20 * 1

    assert resultado == esperado


def test_area_perfil_t():
    resultado = area_perfil_t(
        ancho_ala=10,
        espesor_ala=2,
        altura_alma=20,
        espesor_alma=1,
    )

    esperado = 10 * 2 + 20 * 1

    assert resultado == esperado


# ------------------------
# Deflexión de viga
# ------------------------


def test_deflexion_viga_puntual_central():
    resultado = calcular_deflexion_max(
        longitud=4,
        carga=1000,
        modulo_elasticidad=200000000000,
        inercia=0.0001,
        tipo_carga="puntual_central",
    )

    esperado = ((1000 * 4**3) / (48 * 200000000000 * 0.0001)) * 1000

    assert resultado["deflexion_max"] == pytest.approx(esperado)

    assert resultado["posicion"] == 2


def test_deflexion_viga_distribuida():
    resultado = calcular_deflexion_max(
        longitud=5,
        carga=500,
        modulo_elasticidad=200000000000,
        inercia=0.0002,
        tipo_carga="distribuida",
    )

    esperado = ((5 * 500 * 5**4) / (384 * 200000000000 * 0.0002)) * 1000

    assert resultado["deflexion_max"] == pytest.approx(esperado)


# ------------------------
# Momento flector
# ------------------------


def test_momento_flector_caso_documentado():
    resultado = calcular_momento_max(
        4,
        10,
        "puntual_central",
    )

    assert resultado["momento_max"] == pytest.approx(10.0)


def test_momento_flector_carga_distribuida():
    resultado = calcular_momento_max(
        4,
        10,
        "distribuida",
    )

    esperado = 10 * (4**2) / 8

    assert resultado["momento_max"] == pytest.approx(esperado)


@pytest.mark.parametrize("no_finito", [float("nan"), float("inf"), float("-inf")])
@pytest.mark.parametrize("parametro", ["longitud", "carga"])
def test_momento_flector_parametro_no_finito_lanza_error(parametro, no_finito):
    valores = {"longitud": 4, "carga": 10}
    valores[parametro] = no_finito
    with pytest.raises(ValueError, match=f"'{parametro}' debe ser un número finito"):
        calcular_momento_max(**valores)


@pytest.mark.parametrize("valor", [0, -1, float("nan"), float("inf"), True, "4"])
@pytest.mark.parametrize("parametro", ["longitud", "carga"])
def test_momento_flector_ambos_contratos_lanzan_error_validacion(parametro, valor):
    valores = {"longitud": 4, "carga": 10}
    valores[parametro] = valor

    with pytest.raises(ErrorValidacion):
        calcular_momento_max(**valores)

    with pytest.raises(ErrorValidacion):
        calcular_momento_maximo(carga=valores["carga"], longitud=valores["longitud"])


def test_momento_flector_tipo_de_carga_desconocido_lanza_error_validacion():
    with pytest.raises(ErrorValidacion, match="El tipo de carga debe ser"):
        calcular_momento_max(4, 10, "triangular")


def test_momento_flector_contrato_escalar_conserva_orden_de_parametros():
    assert calcular_momento_maximo(10, 4) == pytest.approx(10.0)
