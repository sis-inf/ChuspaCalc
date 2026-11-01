"""
Modulo para el dialogo 'Acerca de' de la aplicación ChuspaCalc.

Expone la función `mostrar_acerca_de` que muestra un dialogo modal
con informacion del proyecto: nombre, versión, licencia y créditos.
"""

from __future__ import annotations

from PySide6.QtWidgets import QMessageBox, QWidget


def mostrar_acerca_de(parent: QWidget | None = None) -> None:
    """Muestra el dialogo 'Acerca de ChuspaCalc'.

    Presenta informacion general del proyecto: nombre, version,
    descripción, licencia y créditos institucionales. El dialogo
    se cierra con el botón 'Cerrar' o con la tecla Esc.

    Args:
        parent: Ventana padre sobre la que se centra el dialogo.
                Si es ``None``, el dialogo se muestra sin padre.
    """
    try:
        from chuspacalc import __version__ as version
    except (ImportError, AttributeError):
        version = "0.1.0"

    texto = (
        "<b>ChuspaCalc</b><br>"
        f"Versión: {version}<br><br>"
        "Suite de herramientas de cálculo para distintas carreras "
        "de ingeniería.<br><br>"
        "<b>Licencia:</b> MIT<br><br>"
        "<b>Créditos:</b><br>"
        "Desarrollado por la Carrera de Ingeniería de Sistemas e "
        "Informática,<br>"
        "Facultad Nacional de Ingeniería,<br>"
        "Universidad Técnica de Oruro."
    )

    QMessageBox.about(parent, "Acerca de ChuspaCalc", texto)
