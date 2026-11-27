import math

import pytest

from chuspacalc.modulos.matematicas.conversor_angulo import (
    convertir_angulo,
    grados_a_dms,
    grados_a_radianes,
    radianes_a_grados,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def test_convierte_grados_a_radianes():
    assert convertir_angulo(180, "grados", "radianes") == pytest.approx(math.pi)


def test_convierte_gradianes_a_grados():
    assert convertir_angulo(100, "gradianes", "grados") == pytest.approx(90.0)


def test_normaliza_espacios_y_mayusculas():
    assert convertir_angulo(90, " GRADOS ", "Gradianes") == pytest.approx(100.0)


def test_misma_unidad_devuelve_el_valor():
    assert convertir_angulo(45, "grados", "grados") == 45


@pytest.mark.parametrize("valor", [True, False, "1", None, [1]])
def test_rechaza_tipos_invalidos(valor):
    with pytest.raises(ErrorValidacion, match="número finito"):
        convertir_angulo(valor, "grados", "radianes")


@pytest.mark.parametrize("valor", [float("nan"), float("inf"), float("-inf")])
def test_rechaza_no_finitos(valor):
    with pytest.raises(ErrorValidacion, match="número finito"):
        convertir_angulo(valor, "grados", "radianes")


def test_rechaza_entero_demasiado_grande():
    with pytest.raises(ErrorValidacion, match="demasiado grande"):
        convertir_angulo(10**400, "grados", "radianes")


@pytest.mark.parametrize(
    ("origen", "destino", "mensaje"),
    [
        ("xx", "grados", "origen inválida"),
        ("grados", "xx", "destino inválida"),
        (1, "grados", "origen debe ser texto"),
        ("grados", None, "destino debe ser texto"),
    ],
)
def test_rechaza_unidades_invalidas(origen, destino, mensaje):
    with pytest.raises(ErrorValidacion, match=mensaje):
        convertir_angulo(1, origen, destino)


def test_rechaza_resultado_desbordado():
    with pytest.raises(ErrorValidacion, match="no es finito"):
        convertir_angulo(1e308, "radianes", "grados")


@pytest.mark.parametrize("valor", [True, "1", float("nan"), float("inf")])
def test_funciones_directas_rechazan_valores_invalidos(valor):
    for funcion in (grados_a_radianes, radianes_a_grados, grados_a_dms):
        with pytest.raises(ErrorValidacion):
            funcion(valor)


def test_grados_a_dms_valido():
    assert grados_a_dms(10.5) == (10, 30, pytest.approx(0.0))


def test_grados_a_dms_negativo():
    assert grados_a_dms(-10.5) == (-10, -30, pytest.approx(0.0))
