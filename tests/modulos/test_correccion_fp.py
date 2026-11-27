import math
from decimal import Decimal, localcontext

import pytest

from chuspacalc.modulos.electrica.correccion_fp import calcular_capacitancia_correccion
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def test_correccion_de_070_a_095_da_capacitancia_positiva_esperada():
    resultado = calcular_capacitancia_correccion(10000, 0.7, 0.95, 220)

    assert resultado > 0
    assert resultado == pytest.approx(0.0003789904244170176, rel=1e-9)


def test_frecuencia_de_50_hz_requiere_mas_capacitancia_que_60_hz():
    capacitancia_50 = calcular_capacitancia_correccion(10000, 0.7, 0.95, 220, 50)
    capacitancia_60 = calcular_capacitancia_correccion(10000, 0.7, 0.95, 220, 60)

    assert capacitancia_50 > capacitancia_60
    assert capacitancia_50 / capacitancia_60 == pytest.approx(1.2)


def test_factor_de_potencia_deseado_unidad_es_valido():
    resultado = calcular_capacitancia_correccion(10000, 0.7, 1, 220)

    assert resultado == pytest.approx(0.0005591271325952287, rel=1e-9)


@pytest.mark.parametrize("fp_actual", [0, -0.1, 1.1])
def test_factor_actual_fuera_del_intervalo_lanza_value_error(fp_actual):
    with pytest.raises(ValueError, match="fp_actual debe estar entre 0 y 1"):
        calcular_capacitancia_correccion(10000, fp_actual, 0.95, 220)


@pytest.mark.parametrize("fp_deseado", [0, -0.1, 1.1])
def test_factor_deseado_fuera_del_intervalo_lanza_value_error(fp_deseado):
    with pytest.raises(ValueError, match="fp_deseado debe estar entre 0 y 1"):
        calcular_capacitancia_correccion(10000, 0.7, fp_deseado, 220)


@pytest.mark.parametrize("fp_actual, fp_deseado", [(0.7, 0.7), (0.8, 0.7)])
def test_factor_deseado_sin_mejora_lanza_value_error(fp_actual, fp_deseado):
    mensaje = "El factor de potencia deseado debe ser mayor al actual"
    with pytest.raises(ValueError, match=mensaje):
        calcular_capacitancia_correccion(10000, fp_actual, fp_deseado, 220)


@pytest.mark.parametrize("potencia_activa", [0, -10000])
def test_potencia_no_positiva_lanza_value_error(potencia_activa):
    with pytest.raises(ValueError, match="La potencia debe ser positiva"):
        calcular_capacitancia_correccion(potencia_activa, 0.7, 0.95, 220)


@pytest.mark.parametrize("voltaje", [0, -220])
def test_voltaje_no_positivo_lanza_value_error(voltaje):
    with pytest.raises(ValueError, match="El voltaje debe ser positivo"):
        calcular_capacitancia_correccion(10000, 0.7, 0.95, voltaje)


@pytest.mark.parametrize("frecuencia", [0, -60])
def test_frecuencia_no_positiva_lanza_value_error(frecuencia):
    with pytest.raises(ValueError, match="La frecuencia debe ser positiva"):
        calcular_capacitancia_correccion(10000, 0.7, 0.95, 220, frecuencia)


@pytest.mark.parametrize("indice", range(5))
@pytest.mark.parametrize(
    "invalido",
    [None, True, False, "0.7", 1j, float("nan"), float("inf"), -float("inf"), 10**400],
)
def test_correccion_rechaza_tipos_y_valores_no_finitos(indice, invalido):
    parametros = [10000, 0.7, 0.95, 220, 60]
    parametros[indice] = invalido
    with pytest.raises(ErrorValidacion):
        calcular_capacitancia_correccion(*parametros)


@pytest.mark.parametrize(
    "parametros",
    [
        (0, 0.7, 0.95, 220, 60),
        (10000, 0, 0.95, 220, 60),
        (10000, 0.7, 1.1, 220, 60),
        (10000, 0.7, 0.7, 220, 60),
        (10000, 0.7, 0.6, 220, 60),
        (10000, 0.7, 0.95, 0, 60),
        (10000, 0.7, 0.95, 220, 0),
        (1e308, 0.7, 0.95, 1e-200, 60),
        (1e-308, 0.7, 0.95, 1e308, 60),
    ],
)
def test_correccion_propaga_error_validacion_en_dominios_y_resultados_invalidos(
    parametros,
):
    with pytest.raises(ErrorValidacion):
        calcular_capacitancia_correccion(*parametros)


def test_correccion_recupera_resultado_finito_con_denominador_intermedio_desbordado():
    esperado = (math.tan(math.acos(0.7)) - math.tan(math.acos(0.95))) / (
        2 * math.pi * 60
    )
    assert calcular_capacitancia_correccion(
        1e308, 0.7, 0.95, 1e154, 60
    ) == pytest.approx(esperado)


def _capacitancia_referencia_decimal(parametros):
    with localcontext() as contexto:
        contexto.prec = 800
        potencia, actual, deseado, voltaje, frecuencia = (
            Decimal.from_float(float(valor)) for valor in parametros
        )
        uno = Decimal(1)
        diferencia = (uno - actual * actual).sqrt() / actual - (
            uno - deseado * deseado
        ).sqrt() / deseado
        return float(
            potencia
            * diferencia
            / (2 * Decimal.from_float(math.pi) * frecuencia * voltaje * voltaje)
        )


@pytest.mark.parametrize(
    "parametros",
    [
        (1, 1e-20, 2e-20, 220, 60),
        (1e-300, 1e-320, 2e-320, 220, 60),
        (1e-308, 0.7, 0.700001, 1e-100, 60),
        (1e-320, 0.7, 0.95, 1e-100, 60),
        (1e-300, 0.7, 0.95, 220, 1e-320),
        (1e-300, 0.7, 0.95, 1e-200, 60),
        (1, 0.7, math.nextafter(0.7, 1), 220, 60),
        (1, math.nextafter(1, 0), 1, 220, 60),
        (1e308, 0.7, 0.95, 1e154, 60),
        (1e-300, float.fromhex("0x0.0000000000001p-1022"), 1, 220, 60),
    ],
    ids=[
        "factores_muy_pequenos_del_revisor",
        "tangente_fuera_de_rango_con_capacitancia_finita",
        "potencia_reactiva_subnormal_no_nula",
        "potencia_subnormal",
        "denominador_subnormal_no_nulo",
        "cuadrado_del_voltaje_subdesbordado",
        "factores_adyacentes",
        "factor_actual_adyacente_a_uno",
        "denominador_intermedio_desbordado",
        "factor_actual_minimo_representable",
    ],
)
def test_correccion_conserva_precision_sin_perdidas_intermedias(parametros):
    esperado = _capacitancia_referencia_decimal(parametros)
    resultado = calcular_capacitancia_correccion(*parametros)

    assert math.isfinite(esperado) and esperado > 0
    assert math.isfinite(resultado) and resultado > 0
    assert resultado == pytest.approx(esperado, rel=1e-14, abs=0)
