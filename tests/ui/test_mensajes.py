from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMessageBox

from chuspacalc.ui.mensajes import confirmar


def test_confirmar_retorna_true_al_presionar_si(qtbot):
    def hacer_click():
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, QMessageBox):
                for boton in widget.buttons():
                    if boton.text() == "Sí":
                        qtbot.mouseClick(
                            boton,
                            Qt.MouseButton.LeftButton,
                        )
                        return

    QTimer.singleShot(100, hacer_click)

    resultado = confirmar(
        None,
        "Continuar?",
        "¿Desea continuar?",
    )

    assert resultado is True


def test_confirmar_retorna_false_al_presionar_no(qtbot):
    def hacer_click():
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, QMessageBox):
                for boton in widget.buttons():
                    if boton.text() == "No":
                        qtbot.mouseClick(
                            boton,
                            Qt.MouseButton.LeftButton,
                        )
                        return

    QTimer.singleShot(100, hacer_click)

    resultado = confirmar(
        None,
        "Continuar?",
        "¿Desea continuar?",
    )

    assert resultado is False
