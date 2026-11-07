"""
Modulo para el dialogo 'Acerca de' de la aplicación ChuspaCalc.

Expone la función `mostrar_acerca_de` que muestra un dialogo modal
con informacion del proyecto: nombre, versión, especialidades,
licencia, créditos y documentación.
"""

from __future__ import annotations

from chuspacalc import __version__
from chuspacalc.core.carrera import Carrera
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QMessageBox, QWidget

DOCUMENTACION_URL = (
    "https://github.com/sis-inf/ChuspaCalc/blob/main/docs/indice-general.md"
)


def mostrar_acerca_de(parent: QWidget | None = None) -> None:
    """Muestra el dialogo 'Acerca de ChuspaCalc'.

    Presenta informacion general del proyecto: nombre, version,
    especialidades soportadas, licencia, créditos institucionales
    y enlace a la documentación técnica. El dialogo se cierra con
    el botón 'Cerrar' o con la tecla Esc.

    Args:
        parent: Ventana padre sobre la que se centra el dialogo.
                Si es ``None``, el dialogo se muestra sin padre.
    """
    especialidades = "".join(f"<li>{carrera.etiqueta}</li>" for carrera in Carrera)
    texto = (
        "<b>ChuspaCalc</b><br>"
        f"Versión: {__version__}<br><br>"
        "Suite de herramientas de cálculo para distintas carreras "
        "de ingeniería.<br><br>"
        "<b>Especialidades soportadas:</b>"
        f"<ul>{especialidades}</ul>"
        "<b>Licencia:</b> MIT<br><br>"
        "<b>Créditos:</b><br>"
        "Desarrollado por la Carrera de Ingeniería de Sistemas e "
        "Informática,<br>"
        "Facultad Nacional de Ingeniería,<br>"
        "Universidad Técnica de Oruro.<br><br>"
        f'<a href="{DOCUMENTACION_URL}">Documentación técnica</a>'
    )

    dialogo = QMessageBox(parent)
    dialogo.setIcon(QMessageBox.Icon.Information)
    dialogo.setWindowTitle("Acerca de ChuspaCalc")
    dialogo.setTextFormat(Qt.TextFormat.RichText)
    dialogo.setText(texto)
    dialogo.setStandardButtons(QMessageBox.StandardButton.Close)
    dialogo.button(QMessageBox.StandardButton.Close).setText("Cerrar")

    for etiqueta in dialogo.findChildren(QLabel):
        etiqueta.setOpenExternalLinks(True)

    dialogo.exec()
