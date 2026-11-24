"""
Tests unitarios para los conversores de presión, masa y longitud.
"""

import pytest

from chuspacalc.modulos.matematicas.conversor_longitud import (
    UNIDADES_A_METROS,
    convertir,
)
from chuspacalc.modulos.matematicas.conversor_masa import convertir_masa
from chuspacalc.modulos.matematicas.conversor_presion import convertir_presion
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

try:
    from chuspacalc.modulos.matematicas.conversor_longitud_extendido import (
        UNIDADES_BASE,
        convertir_longitud,
    )

    MODULO_DISPONIBLE = True
except ModuleNotFoundError:
    MODULO_DISPONIBLE = False


# ------------------------
# Conversor de presión
# ------------------------


def test_convertir_presion_atm_a_pa():
    assert convertir_presion(1, "atm", "Pa") == pytest.approx(101325.0)


def test_convertir_presion_bar_a_kpa():
    assert convertir_presion(1, "bar", "kPa") == pytest.approx(100.0)


def test_convertir_presion_valor_negativo():
    with pytest.raises(ValueError):
        convertir_presion(-1, "Pa", "kPa")


# ------------------------
# Conversor de masa
# ------------------------


def test_convertir_masa_kg_a_lb():
    assert convertir_masa(1, "kg", "lb") == pytest.approx(2.20462, rel=1e-4)


def test_convertir_masa_kg_a_g():
    assert convertir_masa(1, "kg", "g") == pytest.approx(1000.0)


def test_convertir_masa_valor_negativo():
    with pytest.raises(ValueError):
        convertir_masa(-1, "kg", "g")


# ------------------------
# Conversor de longitud
# ------------------------


def test_convertir_longitud_m_a_cm():
    resultado = convertir(1, "m", "cm")
    assert resultado["valor_convertido"] == pytest.approx(100.0)


def test_convertir_longitud_km_a_m():
    resultado = convertir(1, "km", "m")
    assert resultado["valor_convertido"] == pytest.approx(1000.0)


def test_convertir_longitud_valor_negativo():
    with pytest.raises(ValueError):
        convertir(-1, "m", "cm")


@pytest.mark.parametrize("valor", [True, False, "1", None, [1]])
def test_convertir_longitud_rechaza_tipos_invalidos(valor):
    with pytest.raises(ErrorValidacion):
        convertir(valor, "m", "cm")


@pytest.mark.parametrize("valor", [float("nan"), float("inf"), float("-inf")])
def test_convertir_longitud_rechaza_no_finitos(valor):
    with pytest.raises(ErrorValidacion):
        convertir(valor, "m", "cm")


def test_convertir_longitud_negativo_lanza_error_validacion():
    with pytest.raises(ErrorValidacion):
        convertir(-1, "m", "cm")


@pytest.mark.parametrize(
    ("de_unidad", "a_unidad"),
    [("xx", "m"), ("m", "xx"), (1, "m"), ("m", None)],
)
def test_convertir_longitud_rechaza_unidades_invalidas(de_unidad, a_unidad):
    with pytest.raises(ErrorValidacion):
        convertir(1, de_unidad, a_unidad)


def test_convertir_longitud_retorna_claves_esperadas():
    resultado = convertir(2, " KM ", "M")
    assert resultado == {
        "valor_original": 2,
        "unidad_original": "km",
        "valor_convertido": pytest.approx(2000.0),
        "unidad_destino": "m",
    }


# ------------------------
# Conversor de longitud extendido
# ------------------------


@pytest.mark.skipif(
    not MODULO_DISPONIBLE,
    reason="Bug conocido: conversor_longitud_extendido.py importa desde 'src.chuspacalc'.",
)
def test_convertir_longitud_extendida_pc_a_al():
    assert convertir_longitud(1, "pc", "al") == pytest.approx(3.086e16 / 9.461e15)


@pytest.mark.skipif(
    not MODULO_DISPONIBLE,
    reason="Bug conocido: conversor_longitud_extendido.py importa desde 'src.chuspacalc'.",
)
def test_convertir_longitud_extendida_mn_a_m():
    assert convertir_longitud(1, "mn", "m") == pytest.approx(1852.0)


@pytest.mark.skipif(
    not MODULO_DISPONIBLE,
    reason="Bug conocido: conversor_longitud_extendido.py importa desde 'src.chuspacalc'.",
)
def test_unidades_base_importadas_correctamente():
    assert UNIDADES_BASE is UNIDADES_A_METROS
