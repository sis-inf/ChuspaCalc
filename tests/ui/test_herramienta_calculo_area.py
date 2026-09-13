import escuadra.core.carrera as carrera
import escuadra.modulos.geometria.calculo_area as calculo_area

from PySide6.QtCore import Qt


# Dependencias pendientes del módulo de geometría.
# Se agregan temporalmente para permitir probar el widget hasta que
# sean implementadas correctamente en el módulo correspondiente.
if not hasattr(carrera.Carrera, "GEOMETRIA"):
    carrera.Carrera.GEOMETRIA = "GEOMETRIA"


if not hasattr(calculo_area, "area_trapecio"):

    def area_trapecio(base_mayor, base_menor, altura):
        return ((base_mayor + base_menor) * altura) / 2

    calculo_area.area_trapecio = area_trapecio


from escuadra.modulos.geometria.herramienta_calculo_area import (
    HerramientaCalculoArea,
)


def test_widget_se_instancia(qtbot):
    herramienta = HerramientaCalculoArea()
    widget = herramienta.crear_widget()

    qtbot.addWidget(widget)

    assert widget is not None


def test_calculo_area_triangulo(qtbot):
    herramienta = HerramientaCalculoArea()
    widget = herramienta.crear_widget()

    qtbot.addWidget(widget)

    herramienta.figura_combo.setCurrentText("Triángulo")

    herramienta._inputs[0].setText("10")
    herramienta._inputs[1].setText("5")

    qtbot.mouseClick(
        herramienta.btn_calcular,
        Qt.MouseButton.LeftButton,
    )

    assert herramienta.error_label.text() == ""
    assert herramienta.resultado_output.text() == "25.000000"
