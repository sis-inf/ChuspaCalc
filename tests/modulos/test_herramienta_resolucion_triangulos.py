from PySide6.QtWidgets import QWidget

from chuspacalc.core.carrera import Carrera
from chuspacalc.modulos.geometria.herramienta_resolucion_triangulos import (
    HerramientaResolucionTriangulos,
)


def test_metadatos_devuelve_nombre_y_carrera():
    metadatos = HerramientaResolucionTriangulos.metadatos()

    assert metadatos["nombre"] == "Resolución de triángulos"
    assert metadatos["carrera"] == Carrera.GEOMETRIA


def test_crear_widget_devuelve_qwidget(qtbot):
    herramienta = HerramientaResolucionTriangulos()

    widget = herramienta.crear_widget()
    qtbot.addWidget(widget)

    assert isinstance(widget, QWidget)


def test_resolver_tres_lados_muestra_angulos(qtbot):
    herramienta = HerramientaResolucionTriangulos()
    widget = herramienta.crear_widget()
    qtbot.addWidget(widget)

    herramienta._modo.setCurrentIndex(0)
    herramienta._valor1.setText("3")
    herramienta._valor2.setText("4")
    herramienta._valor3.setText("5")

    herramienta._resolver()

    assert "Ángulo C: 90.0°" in herramienta._resultado.text()


def test_resolver_un_lado_y_dos_angulos_muestra_lado_c(qtbot):
    herramienta = HerramientaResolucionTriangulos()
    widget = herramienta.crear_widget()
    qtbot.addWidget(widget)

    herramienta._modo.setCurrentIndex(1)
    herramienta._valor1.setText("10")
    herramienta._valor2.setText("30")
    herramienta._valor3.setText("60")

    herramienta._resolver()

    assert "Lado C: 20.0" in herramienta._resultado.text()


def test_valor_no_numerico_muestra_error(qtbot):
    herramienta = HerramientaResolucionTriangulos()
    widget = herramienta.crear_widget()
    qtbot.addWidget(widget)

    herramienta._valor1.setText("abc")
    herramienta._valor2.setText("4")
    herramienta._valor3.setText("5")

    herramienta._resolver()

    assert herramienta._resultado.text() != ""


def test_triangulo_invalido_muestra_error(qtbot):
    herramienta = HerramientaResolucionTriangulos()
    widget = herramienta.crear_widget()
    qtbot.addWidget(widget)

    herramienta._modo.setCurrentIndex(0)
    herramienta._valor1.setText("1")
    herramienta._valor2.setText("2")
    herramienta._valor3.setText("10")

    herramienta._resolver()

    assert herramienta._resultado.text() != ""
