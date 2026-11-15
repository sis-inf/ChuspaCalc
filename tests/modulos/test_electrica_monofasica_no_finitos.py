"""
Tests unitarios que verifican que los cálculos eléctricos monofásicos rechazan
entradas no finitas (NaN, inf y -inf) y conservan los resultados válidos.
"""

import math

import pytest

from chuspacalc.modulos.electrica.caida_tension import calcular_caida
from chuspacalc.modulos.electrica.circuito_serie_paralelo import (
    capacitancia_paralelo,
    capacitancia_serie,
    resistencia_paralelo,
    resistencia_serie,
)
from chuspacalc.modulos.electrica.correccion_fp import calcular_capacitancia_correccion
from chuspacalc.modulos.electrica.divisor_tension import (
    calcular_r2_para_tension,
    calcular_tension_salida,
)
from chuspacalc.modulos.electrica.potencia import potencia_ir, potencia_vi, potencia_vr

NO_FINITOS = [math.nan, math.inf, -math.inf]

# (función, argumentos válidos con nombre, parámetro que se reemplaza)
CASOS_CON_NOMBRE = [
    (calcular_caida, {"longitud": 100, "corriente": 15, "seccion": 4}, "longitud"),
    (calcular_caida, {"longitud": 100, "corriente": 15, "seccion": 4}, "corriente"),
    (calcular_caida, {"longitud": 100, "corriente": 15, "seccion": 4}, "seccion"),
    (calcular_caida, {"longitud": 100, "corriente": 15, "seccion": 4}, "tension"),
    (
        calcular_caida,
        {"longitud": 100, "corriente": 15, "seccion": 4},
        "factor_potencia",
    ),
    (
        calcular_capacitancia_correccion,
        {"potencia_activa": 1000, "fp_actual": 0.8, "fp_deseado": 0.95, "voltaje": 220},
        "potencia_activa",
    ),
    (
        calcular_capacitancia_correccion,
        {"potencia_activa": 1000, "fp_actual": 0.8, "fp_deseado": 0.95, "voltaje": 220},
        "fp_actual",
    ),
    (
        calcular_capacitancia_correccion,
        {"potencia_activa": 1000, "fp_actual": 0.8, "fp_deseado": 0.95, "voltaje": 220},
        "fp_deseado",
    ),
    (
        calcular_capacitancia_correccion,
        {"potencia_activa": 1000, "fp_actual": 0.8, "fp_deseado": 0.95, "voltaje": 220},
        "voltaje",
    ),
    (
        calcular_capacitancia_correccion,
        {"potencia_activa": 1000, "fp_actual": 0.8, "fp_deseado": 0.95, "voltaje": 220},
        "frecuencia",
    ),
    (calcular_tension_salida, {"v_entrada": 10, "r1": 1, "r2": 1}, "v_entrada"),
    (calcular_tension_salida, {"v_entrada": 10, "r1": 1, "r2": 1}, "r1"),
    (calcular_tension_salida, {"v_entrada": 10, "r1": 1, "r2": 1}, "r2"),
    (calcular_r2_para_tension, {"v_entrada": 10, "v_salida": 5, "r1": 9}, "v_entrada"),
    (calcular_r2_para_tension, {"v_entrada": 10, "v_salida": 5, "r1": 9}, "v_salida"),
    (calcular_r2_para_tension, {"v_entrada": 10, "v_salida": 5, "r1": 9}, "r1"),
    (potencia_vi, {"voltaje": 2, "corriente": 3}, "voltaje"),
    (potencia_vi, {"voltaje": 2, "corriente": 3}, "corriente"),
    (potencia_ir, {"corriente": 2, "resistencia": 3}, "corriente"),
    (potencia_ir, {"corriente": 2, "resistencia": 3}, "resistencia"),
    (potencia_vr, {"voltaje": 4, "resistencia": 2}, "voltaje"),
    (potencia_vr, {"voltaje": 4, "resistencia": 2}, "resistencia"),
]


@pytest.mark.parametrize("no_finito", NO_FINITOS)
@pytest.mark.parametrize(
    ("funcion", "argumentos", "parametro"),
    CASOS_CON_NOMBRE,
    ids=[f"{f.__name__}-{p}" for f, _, p in CASOS_CON_NOMBRE],
)
def test_rechaza_parametro_no_finito_e_identifica_el_parametro(
    funcion, argumentos, parametro, no_finito
):
    with pytest.raises(ValueError, match=parametro) as excinfo:
        funcion(**{**argumentos, parametro: no_finito})
    assert "finito" in str(excinfo.value)


@pytest.mark.parametrize("no_finito", NO_FINITOS)
@pytest.mark.parametrize(
    ("funcion", "nombre"),
    [
        (resistencia_serie, "La resistencia 2"),
        (resistencia_paralelo, "La resistencia 2"),
        (capacitancia_serie, "La capacitancia 2"),
        (capacitancia_paralelo, "La capacitancia 2"),
    ],
)
def test_circuito_serie_paralelo_rechaza_valor_no_finito(funcion, nombre, no_finito):
    with pytest.raises(ValueError, match=f"^{nombre} debe ser finita"):
        funcion(1.0, no_finito, 3.0)


@pytest.mark.parametrize("no_finito", NO_FINITOS)
def test_resistencia_serie_rechaza_no_finito_en_lista(no_finito):
    with pytest.raises(ValueError, match="^La resistencia 1 debe ser finita"):
        resistencia_serie([no_finito, 2.0])


def test_calcular_caida_conserva_resultado_valido():
    resultado = calcular_caida(longitud=100, corriente=15, seccion=4)

    assert resultado["caida_v"] == pytest.approx(12.9)
    assert resultado["tension_v"] == 220.0


def test_circuito_serie_paralelo_conserva_resultados_validos():
    assert resistencia_serie(2, 3) == pytest.approx(5.0)
    assert resistencia_paralelo(2, 2) == pytest.approx(1.0)
    assert capacitancia_paralelo(1, 2) == pytest.approx(3.0)
    assert capacitancia_serie(2, 2) == pytest.approx(1.0)


def test_correccion_fp_conserva_resultado_valido():
    esperado = (1000 * (math.tan(math.acos(0.8)) - math.tan(math.acos(0.95)))) / (
        2 * math.pi * 60 * 220**2
    )

    resultado = calcular_capacitancia_correccion(1000, 0.8, 0.95, 220)

    assert resultado == pytest.approx(esperado)


def test_divisor_tension_conserva_resultados_validos():
    assert calcular_tension_salida(10, 1, 1)["v_salida"] == pytest.approx(5.0)
    assert calcular_r2_para_tension(10, 5, 100)["r2"] == pytest.approx(100.0)


def test_potencia_conserva_resultados_validos():
    assert potencia_vi(2, 3) == pytest.approx(6.0)
    assert potencia_ir(2, 3) == pytest.approx(12.0)
    assert potencia_vr(4, 2) == pytest.approx(8.0)
