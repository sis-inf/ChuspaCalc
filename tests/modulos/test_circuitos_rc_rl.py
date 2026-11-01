import pytest

from escuadra.modulos.electrica.circuitos_rc_rl import (
    calcular_constante_tiempo_rc,
    calcular_constante_tiempo_rl,
    calcular_voltaje_carga_capacitor,
)


@pytest.mark.parametrize(
    "resistencia, capacitancia, esperado",
    [(1000.0, 0.001, 1.0), (4700.0, 0.000001, 0.0047)],
)
def test_constante_tiempo_rc_con_valores_positivos(resistencia, capacitancia, esperado):
    resultado = calcular_constante_tiempo_rc(resistencia, capacitancia)
    assert resultado == pytest.approx(esperado)


@pytest.mark.parametrize(
    "resistencia, capacitancia, mensaje",
    [
        (0.0, 0.001, "La resistencia debe ser mayor que 0"),
        (-1000.0, 0.001, "La resistencia debe ser mayor que 0"),
        (1000.0, 0.0, "La capacitancia debe ser mayor que 0"),
        (1000.0, -0.001, "La capacitancia debe ser mayor que 0"),
    ],
)
def test_constante_rc_rechaza_cero_y_negativos(resistencia, capacitancia, mensaje):
    with pytest.raises(ValueError, match=mensaje):
        calcular_constante_tiempo_rc(resistencia, capacitancia)


@pytest.mark.parametrize(
    "resistencia, inductancia, esperado",
    [(100.0, 0.5, 0.005), (10.0, 2.0, 0.2)],
)
def test_constante_tiempo_rl_con_valores_positivos(resistencia, inductancia, esperado):
    resultado = calcular_constante_tiempo_rl(resistencia, inductancia)
    assert resultado == pytest.approx(esperado)


@pytest.mark.parametrize(
    "resistencia, inductancia, mensaje",
    [
        (0.0, 0.5, "La resistencia debe ser mayor que 0"),
        (-100.0, 0.5, "La resistencia debe ser mayor que 0"),
        (100.0, 0.0, "La inductancia debe ser mayor que 0"),
        (100.0, -0.5, "La inductancia debe ser mayor que 0"),
    ],
)
def test_constante_rl_rechaza_cero_y_negativos(resistencia, inductancia, mensaje):
    with pytest.raises(ValueError, match=mensaje):
        calcular_constante_tiempo_rl(resistencia, inductancia)


@pytest.mark.parametrize(
    "tiempo, esperado",
    [(0.0, 0.0), (2.0, 3.1606027941427883), (4.0, 4.3233235838169365)],
)
def test_voltaje_carga_capacitor_al_inicio_y_durante_la_carga(tiempo, esperado):
    assert calcular_voltaje_carga_capacitor(5.0, tiempo, 2.0) == pytest.approx(esperado)


@pytest.mark.parametrize(
    "tiempo, constante_tiempo, mensaje",
    [
        (0.0, 0.0, "La constante de tiempo debe ser mayor que 0"),
        (0.0, -2.0, "La constante de tiempo debe ser mayor que 0"),
        (-1.0, 2.0, "El tiempo no puede ser negativo"),
    ],
)
def test_carga_rechaza_parametros_invalidos(tiempo, constante_tiempo, mensaje):
    with pytest.raises(ValueError, match=mensaje):
        calcular_voltaje_carga_capacitor(5.0, tiempo, constante_tiempo)
