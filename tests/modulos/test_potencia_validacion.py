"""Pruebas de validación y tipado de potencia.py (issue #1965)."""

import inspect
import math

import pytest

from chuspacalc.modulos.electrica.potencia import (
    potencia_ir,
    potencia_vi,
    potencia_vr,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

PARAMETROS = {
    potencia_vi: ("voltaje", "corriente"),
    potencia_ir: ("corriente", "resistencia"),
    potencia_vr: ("voltaje", "resistencia"),
}

CASOS = [
    (funcion, nombres, objetivo)
    for funcion, nombres in PARAMETROS.items()
    for objetivo in nombres
]


def _argumentos(nombres, objetivo, valor):
    return {nombre: (valor if nombre == objetivo else 2) for nombre in nombres}


def _id(caso):
    return caso.__name__ if callable(caso) else None


def test_error_validacion_es_value_error():
    assert issubclass(ErrorValidacion, ValueError)


@pytest.mark.parametrize("funcion, nombres, objetivo", CASOS, ids=lambda c: _id(c))
@pytest.mark.parametrize("valor", ["5", None, True, False, [1], 2 + 1j])
def test_rechaza_valores_no_numericos(funcion, nombres, objetivo, valor):
    with pytest.raises(ErrorValidacion, match=f"{objetivo} debe ser un número real"):
        funcion(**_argumentos(nombres, objetivo, valor))


@pytest.mark.parametrize("funcion, nombres, objetivo", CASOS, ids=lambda c: _id(c))
@pytest.mark.parametrize("valor", [math.nan, math.inf, -math.inf, 10**400])
def test_rechaza_valores_no_finitos(funcion, nombres, objetivo, valor):
    with pytest.raises(ErrorValidacion, match=f"{objetivo} debe ser finito"):
        funcion(**_argumentos(nombres, objetivo, valor))


@pytest.mark.parametrize("funcion, nombres, objetivo", CASOS, ids=lambda c: _id(c))
@pytest.mark.parametrize("valor", [0, 0.0, -1, -0.5])
def test_rechaza_cero_y_negativos(funcion, nombres, objetivo, valor):
    with pytest.raises(ErrorValidacion, match=f"{objetivo} debe ser mayor que 0"):
        funcion(**_argumentos(nombres, objetivo, valor))


def test_vi_rechaza_resultado_desbordado():
    with pytest.raises(ErrorValidacion, match="excede el rango numérico"):
        potencia_vi(1e200, 1e200)
    with pytest.raises(ErrorValidacion, match="excede el rango numérico"):
        potencia_vi(10**200, 10**200)


def test_ir_rechaza_resultado_desbordado():
    with pytest.raises(ErrorValidacion, match="excede el rango numérico"):
        potencia_ir(1e200, 1)
    with pytest.raises(ErrorValidacion, match="excede el rango numérico"):
        potencia_ir(1e154, 1e154)


def test_vr_rechaza_resultado_desbordado():
    with pytest.raises(ErrorValidacion, match="excede el rango numérico"):
        potencia_vr(1e200, 1)
    with pytest.raises(ErrorValidacion, match="excede el rango numérico"):
        potencia_vr(1, 5e-324)


def test_errores_son_capturables_como_value_error():
    with pytest.raises(ValueError):
        potencia_vi(0, 2)


def test_valores_validos_siguen_funcionando():
    assert potencia_vi(10, 2) == 20.0
    assert potencia_ir(2, 5) == 20.0
    assert potencia_vr(10, 5) == 20.0
    assert isinstance(potencia_vi(10, 2), float)


@pytest.mark.parametrize("funcion", list(PARAMETROS), ids=lambda f: f.__name__)
def test_anotaciones_de_tipo_completas(funcion):
    firma = inspect.signature(funcion)
    assert firma.return_annotation is not inspect.Signature.empty
    for nombre, parametro in firma.parameters.items():
        assert parametro.annotation is not inspect.Parameter.empty, nombre
