"""
Tests unitarios para las funciones de cálculo del divisor de tensión.
"""

import pytest

from chuspacalc.modulos.electrica.divisor_tension import (
    calcular_r2_para_tension,
    calcular_tension_salida,
)
from chuspacalc.modulos.electrica.herramienta_divisor_tension import (
    calcular_r1,
    calcular_r2,
    calcular_vout,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def test_calcular_vout():
    # Vout = Vin * R2 / (R1 + R2) → 12 * 2000 / (1000 + 2000) = 8
    assert calcular_vout(12, 1000, 2000) == pytest.approx(8.0)


def test_calcular_r2():
    # R2 = (Vout * R1) / (Vin - Vout) → (5 * 1000) / (12 - 5) ≈ 714.29
    assert calcular_r2(12, 5, 1000) == pytest.approx(714.29, rel=1e-3)


def test_calcular_r1():
    # R1 = R2 * (Vin - Vout) / Vout → 1000 * (9 - 3) / 3 = 2000
    assert calcular_r1(9, 3, 1000) == pytest.approx(2000.0)


def test_calcular_vout_vin_cero():
    # Si Vin = 0, Vout debe ser 0
    assert calcular_vout(0, 1000, 2000) == 0


def test_calcular_vout_resistencias_cero():
    # R1 = 0 y R2 = 0 debe lanzar error
    with pytest.raises(ValueError):
        calcular_vout(12, 0, 0)


def test_calcular_r2_vout_igual_vin():
    # Vout = Vin divide por cero en la formula
    with pytest.raises(ValueError):
        calcular_r2(12, 12, 1000)


def test_calcular_r1_vout_cero():
    # Vout = 0 divide por cero en la formula
    with pytest.raises(ValueError):
        calcular_r1(12, 0, 1000)


@pytest.mark.parametrize(
    "funcion, base",
    [
        (calcular_tension_salida, {"v_entrada": 12, "r1": 1000, "r2": 2000}),
        (calcular_r2_para_tension, {"v_entrada": 12, "v_salida": 5, "r1": 1000}),
    ],
)
@pytest.mark.parametrize("indice", [0, 1, 2])
@pytest.mark.parametrize(
    "invalido",
    [
        None,
        True,
        False,
        "12",
        1j,
        float("nan"),
        float("inf"),
        -float("inf"),
        10**400,
        0,
        -1,
    ],
)
def test_divisor_rechaza_entradas_invalidas_con_error_validacion(
    funcion, base, indice, invalido
):
    parametros = dict(base)
    nombre = list(parametros)[indice]
    parametros[nombre] = invalido
    with pytest.raises(ErrorValidacion, match=nombre):
        funcion(**parametros)


def test_divisor_conserva_formula_y_contrato():
    assert calcular_tension_salida(12, 1000, 2000) == {
        "v_entrada": 12,
        "r1": 1000,
        "r2": 2000,
        "v_salida": 8,
        "unidad": "V",
    }
    res = calcular_r2_para_tension(12, 5, 1000)
    assert res["r2"] == pytest.approx(5000 / 7)
    assert res["unidad"] == "ohm"


@pytest.mark.parametrize("salida", [12, 13])
def test_divisor_rechaza_salida_sin_diferencia_de_potencial(salida):
    with pytest.raises(ErrorValidacion, match="menor"):
        calcular_r2_para_tension(12, salida, 1000)


def test_divisor_evade_desbordamiento_intermedio_con_resultado_representable():
    assert calcular_tension_salida(1e308, 1e308, 1e308)["v_salida"] == pytest.approx(
        5e307
    )
    assert calcular_tension_salida(1e308, 1e308, 1e-308)["v_salida"] == pytest.approx(
        1e-308, abs=0
    )
    assert calcular_r2_para_tension(1e308, 5e307, 1e308)["r2"] == pytest.approx(1e308)


def test_divisor_rechaza_resultados_fuera_de_rango():
    with pytest.raises(ErrorValidacion):
        calcular_r2_para_tension(1, 0.9999999999999999, 1e308)
    with pytest.raises(ErrorValidacion):
        calcular_tension_salida(5e-324, 1e308, 5e-324)
