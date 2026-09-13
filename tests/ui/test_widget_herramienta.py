import sys
import types

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget

pyqt5 = types.ModuleType("PyQt5")
qtgui = types.ModuleType("PyQt5.QtGui")
qtwidgets = types.ModuleType("PyQt5.QtWidgets")

qtgui.QFont = QFont

qtwidgets.QFrame = QFrame
qtwidgets.QLabel = QLabel
qtwidgets.QVBoxLayout = QVBoxLayout
qtwidgets.QWidget = QWidget

sys.modules["PyQt5"] = pyqt5
sys.modules["PyQt5.QtGui"] = qtgui
sys.modules["PyQt5.QtWidgets"] = qtwidgets

from escuadra.ui.widget_herramienta import (
    WidgetHerramienta,
    ejecutar_con_progreso_ui,
)


def test_widget_herramienta_se_instancia(qtbot):
    widget = WidgetHerramienta(
        "Herramienta prueba",
        "Descripción de prueba",
    )

    qtbot.addWidget(widget)

    assert widget is not None


def test_widget_herramienta_area_contenido(qtbot):
    widget = WidgetHerramienta(
        "Herramienta prueba",
        "Descripción de prueba",
    )

    qtbot.addWidget(widget)

    contenido = widget.area_contenido()

    assert contenido is not None


def test_ejecutar_con_progreso_ui_devuelve_resultado():
    def suma(a, b):
        return a + b

    resultado = ejecutar_con_progreso_ui(suma, 2, 3)

    assert resultado == 5


def test_ejecutar_con_progreso_ui_maneja_error(monkeypatch):
    def funcion_error():
        raise ValueError("error de prueba")

    monkeypatch.setattr(
        "escuadra.ui.widget_herramienta.mostrar_error_contextualizado",
        lambda *args: None,
    )

    resultado = ejecutar_con_progreso_ui(funcion_error)

    assert resultado is None
