from PySide6.QtWidgets import QWidget

from escuadra.core.carrera import Carrera
from escuadra.modulos.civil.herramienta_combinacion_cargas import (
    HerramientaCombinacionCargas,
)


def test_metadatos_devuelve_nombre_y_carrera():
    metadatos = HerramientaCombinacionCargas.metadatos()

    assert metadatos["nombre"] == "Combinación de cargas"
    assert metadatos["carrera"] == Carrera.CIVIL


def test_crear_widget_devuelve_qwidget(qtbot):
    herramienta = HerramientaCombinacionCargas()

    widget = herramienta.crear_widget()
    qtbot.addWidget(widget)

    assert isinstance(widget, QWidget)


def test_calcular_con_carga_muerta_10_y_viva_5(qtbot):
    herramienta = HerramientaCombinacionCargas()
    widget = herramienta.crear_widget()
    qtbot.addWidget(widget)

    herramienta._carga_muerta.setValue(10)
    herramienta._carga_viva.setValue(5)

    herramienta._calcular()

    assert herramienta._resultado.text() == (
        "Carga última de diseño: 20.00 kN"
    )


def test_calcular_con_ambas_cargas_en_cero(qtbot):
    herramienta = HerramientaCombinacionCargas()
    widget = herramienta.crear_widget()
    qtbot.addWidget(widget)

    herramienta._carga_muerta.setValue(0)
    herramienta._carga_viva.setValue(0)

    herramienta._calcular()

    assert herramienta._resultado.text() == (
        "Carga última de diseño: 0.00 kN"
    )
