import pytest

from escuadra.modulos.electrica.correccion_fp import calcular_capacitancia_correccion


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
