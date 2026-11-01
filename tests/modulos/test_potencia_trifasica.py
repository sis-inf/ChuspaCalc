import pytest

from escuadra.modulos.electrica.potencia_trifasica import calcular_potencia_trifasica


def test_potencia_aparente_y_activa_con_factor_de_potencia_ocho_decimas():
    resultado = calcular_potencia_trifasica(400, 10, 0.8)

    assert resultado["potencia_aparente"] == pytest.approx(6928.203230275509)
    assert resultado["potencia_activa"] == pytest.approx(5542.562584220407)


def test_potencia_reactiva_con_factor_de_potencia_ocho_decimas():
    resultado = calcular_potencia_trifasica(400, 10, 0.8)

    assert resultado["potencia_reactiva"] == pytest.approx(4156.921938165306)


def test_factor_de_potencia_unidad_da_potencia_reactiva_cero():
    resultado = calcular_potencia_trifasica(400, 10, 1)

    assert resultado["potencia_reactiva"] == pytest.approx(0.0, abs=1e-12)


def test_estrella_y_triangulo_dan_las_mismas_potencias_con_valores_de_linea():
    estrella = calcular_potencia_trifasica(400, 10, 0.8, conexion="estrella")
    triangulo = calcular_potencia_trifasica(400, 10, 0.8, conexion="triangulo")

    assert estrella == pytest.approx(triangulo)


@pytest.mark.parametrize("voltaje_linea", [0, -400])
def test_voltaje_no_positivo_lanza_value_error(voltaje_linea):
    with pytest.raises(ValueError, match="voltaje_linea debe ser mayor que 0"):
        calcular_potencia_trifasica(voltaje_linea, 10, 0.8)


@pytest.mark.parametrize("corriente_linea", [0, -10])
def test_corriente_no_positiva_lanza_value_error(corriente_linea):
    with pytest.raises(ValueError, match="corriente_linea debe ser mayor que 0"):
        calcular_potencia_trifasica(400, corriente_linea, 0.8)


@pytest.mark.parametrize("factor_potencia", [0, -0.5, 1.1])
def test_factor_de_potencia_fuera_del_intervalo_lanza_value_error(factor_potencia):
    with pytest.raises(ValueError, match="factor_potencia debe estar entre 0 y 1"):
        calcular_potencia_trifasica(400, 10, factor_potencia)


def test_conexion_desconocida_lanza_value_error():
    with pytest.raises(ValueError, match="conexion debe ser 'estrella' o 'triangulo'"):
        calcular_potencia_trifasica(400, 10, 0.8, conexion="desconocida")
