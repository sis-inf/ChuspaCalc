"""Pruebas de validación y tipado de ley_ohm.py (issue #1964)."""

import inspect
import math

import pytest

from chuspacalc.modulos.electrica.ley_ohm import calcular_ohm
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

# Para cada parámetro, un conjunto de argumentos válidos en los que ese
# parámetro es uno de los dos proporcionados.
BASES = {
    "voltaje": {"corriente": 2},
    "corriente": {"voltaje": 10},
    "resistencia": {"voltaje": 10},
}


def _argumentos(objetivo, valor):
    return {**BASES[objetivo], objetivo: valor}


def test_error_validacion_es_value_error():
    assert issubclass(ErrorValidacion, ValueError)


def test_valores_validos_siguen_funcionando():
    resultado = calcular_ohm(corriente=2, resistencia=5)

    assert resultado == {
        "voltaje": 10,
        "unidad_v": "V",
        "corriente": 2,
        "unidad_i": "A",
        "resistencia": 5,
        "unidad_r": "Ω",
    }
    assert calcular_ohm(voltaje=12, resistencia=3)["corriente"] == 4
    assert calcular_ohm(voltaje=10, corriente=2)["resistencia"] == 5


@pytest.mark.parametrize(
    "argumentos",
    [
        {},
        {"voltaje": 1},
        {"voltaje": 1, "corriente": 2, "resistencia": 3},
    ],
)
def test_exige_exactamente_dos_valores(argumentos):
    with pytest.raises(ErrorValidacion, match="exactamente dos parámetros"):
        calcular_ohm(**argumentos)


@pytest.mark.parametrize("objetivo", list(BASES))
@pytest.mark.parametrize("valor", ["5", True, False, [1], 2 + 1j])
def test_rechaza_valores_no_numericos(objetivo, valor):
    with pytest.raises(ErrorValidacion, match=f"{objetivo} debe ser un número real"):
        calcular_ohm(**_argumentos(objetivo, valor))


@pytest.mark.parametrize("objetivo", list(BASES))
@pytest.mark.parametrize("valor", [math.nan, math.inf, -math.inf, 10**400])
def test_rechaza_valores_no_finitos(objetivo, valor):
    with pytest.raises(ErrorValidacion, match=f"{objetivo} debe ser finito"):
        calcular_ohm(**_argumentos(objetivo, valor))


def test_rechaza_resistencia_cero():
    with pytest.raises(ErrorValidacion, match="resistencia no puede ser cero"):
        calcular_ohm(voltaje=10, resistencia=0)

    with pytest.raises(ErrorValidacion, match="resistencia no puede ser cero"):
        calcular_ohm(corriente=2, resistencia=0.0)


def test_rechaza_corriente_cero_al_calcular_resistencia():
    with pytest.raises(ErrorValidacion, match="corriente no puede ser cero"):
        calcular_ohm(voltaje=10, corriente=0)


def test_rechaza_resultado_desbordado_en_voltaje():
    with pytest.raises(ErrorValidacion, match="excede el rango numérico"):
        calcular_ohm(corriente=1e200, resistencia=1e200)

    with pytest.raises(ErrorValidacion, match="excede el rango numérico"):
        calcular_ohm(corriente=10**200, resistencia=10**200)


def test_rechaza_resultado_desbordado_en_corriente():
    with pytest.raises(ErrorValidacion, match="excede el rango numérico"):
        calcular_ohm(voltaje=1, resistencia=5e-324)


def test_rechaza_resultado_desbordado_en_resistencia():
    with pytest.raises(ErrorValidacion, match="excede el rango numérico"):
        calcular_ohm(voltaje=1e300, corriente=1e-300)


def test_errores_son_capturables_como_value_error():
    with pytest.raises(ValueError):
        calcular_ohm(voltaje=10, resistencia=0)


def test_anotaciones_de_tipo_completas():
    firma = inspect.signature(calcular_ohm)

    assert firma.return_annotation is not inspect.Signature.empty
    for nombre, parametro in firma.parameters.items():
        assert parametro.annotation is not inspect.Parameter.empty, nombre
