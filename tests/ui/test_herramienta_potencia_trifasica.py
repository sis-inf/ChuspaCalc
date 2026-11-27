import pytest

from chuspacalc.modulos.electrica.herramienta_potencia_trifasica import (
    HerramientaPotenciaTrifasica,
)


@pytest.fixture
def herramienta(app_qt):
    herramienta = HerramientaPotenciaTrifasica()
    widget = herramienta.crear_widget()

    # Se conserva una referencia al widget durante el test.
    herramienta._widget_raiz = widget

    yield herramienta

    widget.close()
    app_qt.processEvents()


def _llenar(
    herramienta,
    voltaje="400",
    corriente="10",
    factor_potencia="0.8",
):
    """Introduce valores en los campos de la herramienta."""
    herramienta._campos["voltaje"].setText(voltaje)
    herramienta._campos["corriente"].setText(corriente)
    herramienta._campos["factor_potencia"].setText(factor_potencia)


def test_calculo_valido_muestra_las_tres_potencias(herramienta):
    _llenar(herramienta)

    herramienta._calcular()

    assert herramienta._error_label.text() == ""

    assert float(herramienta._resultados["potencia_activa"].text()) == pytest.approx(
        5542.5626, abs=1e-4
    )

    assert float(herramienta._resultados["potencia_reactiva"].text()) == pytest.approx(
        4156.9219, abs=1e-4
    )

    assert float(herramienta._resultados["potencia_aparente"].text()) == pytest.approx(
        6928.2032, abs=1e-4
    )


@pytest.mark.parametrize(
    "clave",
    ["voltaje", "corriente", "factor_potencia"],
)
def test_campo_vacio_muestra_error(herramienta, clave):
    valores = {
        "voltaje": "400",
        "corriente": "10",
        "factor_potencia": "0.8",
    }
    valores[clave] = ""

    _llenar(
        herramienta,
        valores["voltaje"],
        valores["corriente"],
        valores["factor_potencia"],
    )

    herramienta._calcular()

    assert "obligatorio" in herramienta._error_label.text()

    assert all(campo.text() == "" for campo in herramienta._resultados.values())


@pytest.mark.parametrize(
    "clave",
    ["voltaje", "corriente", "factor_potencia"],
)
def test_texto_no_numerico_muestra_error(herramienta, clave):
    valores = {
        "voltaje": "400",
        "corriente": "10",
        "factor_potencia": "0.8",
    }
    valores[clave] = "abc"

    _llenar(
        herramienta,
        valores["voltaje"],
        valores["corriente"],
        valores["factor_potencia"],
    )

    herramienta._calcular()

    assert "no es un número válido" in herramienta._error_label.text()


@pytest.mark.parametrize(
    "clave,valor",
    [
        ("voltaje", "0"),
        ("voltaje", "-400"),
        ("voltaje", "nan"),
        ("voltaje", "inf"),
        ("voltaje", "-inf"),
        ("corriente", "0"),
        ("corriente", "-10"),
        ("corriente", "nan"),
        ("corriente", "inf"),
        ("corriente", "-inf"),
        ("factor_potencia", "nan"),
        ("factor_potencia", "inf"),
        ("factor_potencia", "-inf"),
    ],
)
def test_valores_no_validos_muestran_error(herramienta, clave, valor):
    valores = {
        "voltaje": "400",
        "corriente": "10",
        "factor_potencia": "0.8",
    }
    valores[clave] = valor

    _llenar(
        herramienta,
        valores["voltaje"],
        valores["corriente"],
        valores["factor_potencia"],
    )

    herramienta._calcular()

    assert herramienta._error_label.text().startswith("Error:")

    assert all(campo.text() == "" for campo in herramienta._resultados.values())


@pytest.mark.parametrize("factor_potencia", ["-0.1", "1.1"])
def test_factor_de_potencia_fuera_del_rango_muestra_error(
    herramienta,
    factor_potencia,
):
    _llenar(herramienta, factor_potencia=factor_potencia)

    herramienta._calcular()

    assert herramienta._error_label.text().startswith("Error:")
    assert "factor_potencia" in herramienta._error_label.text()


@pytest.mark.parametrize("factor_potencia", ["0", "1"])
def test_limites_validos_del_factor_de_potencia(herramienta, factor_potencia):
    _llenar(herramienta, factor_potencia=factor_potencia)

    herramienta._calcular()

    assert herramienta._error_label.text() == ""
    assert herramienta._resultados["potencia_activa"].text() != ""
    assert herramienta._resultados["potencia_reactiva"].text() != ""
    assert herramienta._resultados["potencia_aparente"].text() != ""


def test_resultado_no_finito_muestra_error(herramienta):
    _llenar(
        herramienta,
        voltaje="1e308",
        corriente="1e308",
        factor_potencia="0.8",
    )

    herramienta._calcular()

    assert herramienta._error_label.text().startswith("Error:")
    assert "finito" in herramienta._error_label.text()


def test_limpiar_restaura_campos_resultados_y_conexion(herramienta):
    _llenar(herramienta)
    herramienta._conexion_combo.setCurrentIndex(1)

    herramienta._calcular()
    herramienta._limpiar()

    assert herramienta._error_label.text() == ""

    assert all(campo.text() == "" for campo in herramienta._campos.values())

    assert all(campo.text() == "" for campo in herramienta._resultados.values())

    assert herramienta._conexion_combo.currentIndex() == 0
