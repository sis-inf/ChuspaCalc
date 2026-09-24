"""
Tests unitarios para módulos avanzados de civil:
- area_seccion.py
- deflexion_viga.py
- momento_flector.py
"""

import pytest

from escuadra.modulos.civil.area_seccion import (
    area_rectangular,
    area_circular,
    area_circular_hueca,
    area_perfil_i,
    area_perfil_t,
)

from escuadra.modulos.civil.deflexion_viga import (
    calcular_deflexion_max,
)

from escuadra.modulos.civil.momento_flector import (
    calcular_momento_max,
)


# ------------------------
# Área de secciones
# ------------------------


def test_area_seccion_rectangular():
    # Área = base * altura
    assert area_rectangular(10, 5) == 50


def test_area_seccion_circular():
    # Área = pi * r²
    assert area_circular(2) == pytest.approx(
        4 * 3.141592653589793
    )


def test_area_seccion_circular_hueca():
    # Área = pi * (R² - r²)
    esperado = 3.141592653589793 * (5**2 - 3**2)

    assert area_circular_hueca(5, 3) == pytest.approx(
        esperado
    )


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

    esperado = (
        (1000 * 4**3)
        / (48 * 200000000000 * 0.0001)
    ) * 1000

    assert resultado["deflexion_max"] == pytest.approx(
        esperado
    )

    assert resultado["posicion"] == 2


def test_deflexion_viga_distribuida():
    resultado = calcular_deflexion_max(
        longitud=5,
        carga=500,
        modulo_elasticidad=200000000000,
        inercia=0.0002,
        tipo_carga="distribuida",
    )

    esperado = (
        (5 * 500 * 5**4)
        / (384 * 200000000000 * 0.0002)
    ) * 1000

    assert resultado["deflexion_max"] == pytest.approx(
        esperado
    )


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

    assert resultado["momento_max"] == pytest.approx(
        esperado
    )
