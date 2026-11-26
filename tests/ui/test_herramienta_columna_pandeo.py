import pytest

from chuspacalc.modulos.civil.herramienta_columna_pandeo import (
    HerramientaColumnaPandeo,
)


@pytest.fixture
def herramienta(qtbot):
    herramienta = HerramientaColumnaPandeo()
    widget = herramienta.crear_widget()
    qtbot.addWidget(widget)
    # Se conserva una referencia al widget para que Qt no lo destruya
    # mientras dura el test.
    herramienta._widget_raiz = widget
    return herramienta


def _llenar(herramienta, modulo, inercia, longitud):
    herramienta._campos["modulo_elasticidad"].setText(modulo)
    herramienta._campos["momento_inercia"].setText(inercia)
    herramienta._campos["longitud"].setText(longitud)


def test_calculo_valido_muestra_carga_critica(herramienta):
    _llenar(herramienta, "200e9", "8.33e-6", "3.0")

    herramienta._calcular()

    assert herramienta._error_label.text() == ""
    assert herramienta._carga_critica_output.text() != ""


@pytest.mark.parametrize("valor", ["0", "-1", "nan", "inf", "-inf"])
def test_valor_no_positivo_o_no_finito_muestra_error(herramienta, valor):
    _llenar(herramienta, "200e9", "8.33e-6", valor)

    herramienta._calcular()

    assert herramienta._error_label.text().startswith("Error:")
    assert herramienta._carga_critica_output.text() == ""


def test_texto_no_numerico_muestra_error(herramienta):
    _llenar(herramienta, "abc", "8.33e-6", "3.0")

    herramienta._calcular()

    assert "no es un número válido" in herramienta._error_label.text()


def test_campo_vacio_muestra_error(herramienta):
    _llenar(herramienta, "", "8.33e-6", "3.0")

    herramienta._calcular()

    assert "es obligatorio" in herramienta._error_label.text()
