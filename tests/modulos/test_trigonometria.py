"""
Tests unitarios para el módulo trigonometria, verificando las funciones
trigonométricas directas e inversas en grados y el manejo de valores
fuera de dominio.
"""

import pytest

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.matematicas.trigonometria import (
    arcocoseno,
    arcoseno,
    arcotangente,
    coseno,
    seno,
    tangente,
)


def test_seno_de_30_grados_es_medio():
    # sen(30°) = 0.5 (con tolerancia por los decimales)
    assert seno(30) == pytest.approx(0.5)


def test_coseno_de_60_grados_es_medio():
    # cos(60°) = 0.5 (con tolerancia por los decimales)
    assert coseno(60) == pytest.approx(0.5)


def test_tangente_de_45_grados_es_uno():
    # tan(45°) = 1 (con tolerancia por los decimales)
    assert tangente(45) == pytest.approx(1.0)


def test_tangente_de_90_grados_lanza_value_error():
    # La tangente no está definida en 90°
    with pytest.raises(ValueError, match="Tangente indefinida para este ángulo"):
        tangente(90)


def test_tangente_de_270_grados_lanza_value_error():
    # 270° equivale a 90° (mod 180), donde la tangente no está definida
    with pytest.raises(ValueError, match="Tangente indefinida para este ángulo"):
        tangente(270)


def test_arcoseno_de_1_es_90_grados():
    # asen(1) = 90° (el resultado se devuelve en grados)
    assert arcoseno(1) == pytest.approx(90.0)


def test_arcocoseno_de_0_es_90_grados():
    # acos(0) = 90° (el resultado se devuelve en grados)
    assert arcocoseno(0) == pytest.approx(90.0)


def test_arcoseno_de_2_lanza_value_error():
    # El arcoseno solo está definido en el rango [-1, 1]
    with pytest.raises(ValueError):
        arcoseno(2)


def test_arcocoseno_de_menos_2_lanza_value_error():
    # El arcocoseno solo está definido en el rango [-1, 1]
    with pytest.raises(ValueError):
        arcocoseno(-2)


def test_arcotangente_de_1_es_45_grados():
    # atan(1) = 45° (el resultado se devuelve en grados)
    assert arcotangente(1) == pytest.approx(45.0)


@pytest.mark.parametrize(
    "funcion", [seno, coseno, tangente, arcoseno, arcocoseno, arcotangente]
)
@pytest.mark.parametrize("valor", [True, False])
def test_rechaza_booleanos(funcion, valor):
    with pytest.raises(ErrorValidacion):
        funcion(valor)
