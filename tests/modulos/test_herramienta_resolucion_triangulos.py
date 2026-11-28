from typing import get_type_hints

import pytest
from PySide6.QtWidgets import QWidget

from chuspacalc.core.carrera import Carrera
from chuspacalc.modulos.geometria.herramienta_resolucion_triangulos import (
    HerramientaResolucionTriangulos,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def _crear_herramienta(qtbot):
    """Crea la herramienta y registra su widget para las pruebas."""
    herramienta = HerramientaResolucionTriangulos()
    widget = herramienta.crear_widget()
    qtbot.addWidget(widget)
    return herramienta


def test_metadatos_devuelve_nombre_y_carrera():
    metadatos = HerramientaResolucionTriangulos.metadatos()

    assert metadatos["nombre"] == "Resolución de triángulos"
    assert metadatos["carrera"] == Carrera.GEOMETRIA


def test_crear_widget_devuelve_qwidget(qtbot):
    herramienta = HerramientaResolucionTriangulos()

    widget = herramienta.crear_widget()
    qtbot.addWidget(widget)

    assert isinstance(widget, QWidget)


def test_crear_widget_tiene_anotacion_de_retorno():
    anotaciones = get_type_hints(HerramientaResolucionTriangulos.crear_widget)

    assert anotaciones["return"] is QWidget


def test_resolver_tres_lados_muestra_angulos(qtbot):
    herramienta = _crear_herramienta(qtbot)

    herramienta._modo.setCurrentIndex(0)
    herramienta._valor1.setText("3")
    herramienta._valor2.setText("4")
    herramienta._valor3.setText("5")

    herramienta._resolver()

    assert "Ángulo C: 90.0°" in herramienta._resultado.text()


def test_resolver_un_lado_y_dos_angulos_muestra_lado_c(qtbot):
    herramienta = _crear_herramienta(qtbot)

    herramienta._modo.setCurrentIndex(1)
    herramienta._valor1.setText("10")
    herramienta._valor2.setText("30")
    herramienta._valor3.setText("60")

    herramienta._resolver()

    assert "Lado C: 20.0" in herramienta._resultado.text()


def test_valor_no_numerico_muestra_error(qtbot):
    herramienta = _crear_herramienta(qtbot)

    herramienta._valor1.setText("abc")
    herramienta._valor2.setText("4")
    herramienta._valor3.setText("5")

    herramienta._resolver()

    assert "número válido" in herramienta._resultado.text()


def test_triangulo_invalido_muestra_error(qtbot):
    herramienta = _crear_herramienta(qtbot)

    herramienta._modo.setCurrentIndex(0)
    herramienta._valor1.setText("1")
    herramienta._valor2.setText("2")
    herramienta._valor3.setText("10")

    herramienta._resolver()

    assert "triángulo válido" in herramienta._resultado.text()


@pytest.mark.parametrize(
    "texto",
    ["", "   ", "abc", "nan", "inf", "-inf"],
)
def test_leer_valor_rechaza_entradas_invalidas(qtbot, texto):
    herramienta = _crear_herramienta(qtbot)
    herramienta._valor1.setText(texto)

    with pytest.raises(ErrorValidacion):
        herramienta._leer_valor(herramienta._valor1, "Valor 1")


@pytest.mark.parametrize(
    ("valores", "mensaje"),
    [
        (("", "4", "5"), "obligatorio"),
        (("3", "", "5"), "obligatorio"),
        (("3", "4", ""), "obligatorio"),
        (("nan", "4", "5"), "finito"),
        (("inf", "4", "5"), "finito"),
        (("-inf", "4", "5"), "finito"),
        (("0", "4", "5"), "mayores que cero"),
        (("-3", "4", "5"), "mayores que cero"),
    ],
)
def test_modo_tres_lados_rechaza_datos_invalidos(qtbot, valores, mensaje):
    herramienta = _crear_herramienta(qtbot)
    herramienta._modo.setCurrentIndex(0)

    herramienta._valor1.setText(valores[0])
    herramienta._valor2.setText(valores[1])
    herramienta._valor3.setText(valores[2])

    herramienta._resolver()

    assert mensaje in herramienta._resultado.text()


@pytest.mark.parametrize(
    ("valores", "mensaje"),
    [
        (("0", "30", "60"), "mayor que cero"),
        (("-5", "30", "60"), "mayor que cero"),
        (("10", "0", "60"), "mayor que 0°"),
        (("10", "-1", "60"), "mayor que 0°"),
        (("10", "180", "60"), "mayor que 0°"),
        (("10", "181", "60"), "mayor que 0°"),
        (("10", "nan", "60"), "finito"),
        (("10", "120", "60"), "menor que 180°"),
        (("10", "120", "80"), "menor que 180°"),
    ],
)
def test_modo_lado_angulos_rechaza_datos_invalidos(qtbot, valores, mensaje):
    herramienta = _crear_herramienta(qtbot)
    herramienta._modo.setCurrentIndex(1)

    herramienta._valor1.setText(valores[0])
    herramienta._valor2.setText(valores[1])
    herramienta._valor3.setText(valores[2])

    herramienta._resolver()

    assert mensaje in herramienta._resultado.text()
