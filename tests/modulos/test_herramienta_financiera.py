import pytest

from chuspacalc.modulos.matematicas.herramienta_financiera import (
    HerramientaFinanciera,
)


@pytest.fixture
def herramienta(qapp, qtbot):
    h = HerramientaFinanciera()
    widget = h.crear_widget()
    qtbot.addWidget(widget)
    h._widget_prueba = widget
    return h


def _calcular(h, monto, tasa, periodos):
    h._campos["monto"].setText(monto)
    h._campos["tasa"].setText(tasa)
    h._campos["periodos"].setText(periodos)
    h._calcular()


def test_calculo_valido_valor_futuro(herramienta):
    _calcular(herramienta, "1000", "0.05", "10")
    assert herramienta._resultado_output.text() == "1628.8946"
    assert herramienta._error_label.text() == ""


@pytest.mark.parametrize(
    ("monto", "tasa", "periodos", "mensaje"),
    [
        ("", "0.05", "10", "Completa el campo"),
        ("abc", "0.05", "10", "no es un número válido"),
        ("nan", "0.05", "10", "finitos"),
        ("inf", "0.05", "10", "finitos"),
        ("-5", "0.05", "10", "no puede ser negativo"),
        ("1000", "-0.1", "10", "no puede ser negativo"),
        ("1000", "0.05", "", "número de períodos"),
        ("1000", "0.05", "2.5", "número entero"),
        ("1000", "0.05", "0", "mayores que 0"),
        ("1000", "0.05", "-3", "mayores que 0"),
        ("1000", "0.05", "99999", "no pueden superar"),
    ],
)
def test_entradas_invalidas_muestran_error(herramienta, monto, tasa, periodos, mensaje):
    _calcular(herramienta, monto, tasa, periodos)
    assert mensaje in herramienta._error_label.text()
    assert herramienta._resultado_output.text() == ""


def test_limpiar_borra_campos_y_errores(herramienta):
    _calcular(herramienta, "abc", "0.05", "10")
    herramienta._limpiar()
    assert herramienta._error_label.text() == ""
    assert herramienta._campos["monto"].text() == ""
