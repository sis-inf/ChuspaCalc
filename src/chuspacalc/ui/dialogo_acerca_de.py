"""
Modulo para el dialogo 'Acerca de' de la aplicación ChuspaCalc.

Expone la función `mostrar_acerca_de` que muestra un dialogo modal
con informacion del proyecto: nombre, versión, especialidades,
licencia, créditos y documentación.
"""

from __future__ import annotations

from functools import partial

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QLabel, QMessageBox, QWidget

from chuspacalc import __version__
from chuspacalc.core.carrera import Carrera
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.ui.mensajes import mostrar_advertencia, mostrar_error_contextualizado

DOCUMENTACION_URL = (
    "https://github.com/sis-inf/ChuspaCalc/blob/main/docs/indice-general.md"
)

# Esquemas permitidos para los enlaces del dialogo. Evita abrir rutas
# locales o protocolos inesperados.
ESQUEMAS_PERMITIDOS = ("http://", "https://")


def _construir_texto() -> str:
    """Arma el contenido HTML que se muestra en el dialogo."""
    especialidades = "".join(f"<li>{carrera.etiqueta}</li>" for carrera in Carrera)
    return (
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


def _abrir_enlace(enlace: str, parent: QWidget | None = None) -> None:
    """Slot que abre en el navegador un enlace pulsado en el dialogo.

    Se conecta a la señal ``linkActivated`` de cada etiqueta. Si el enlace
    no es valido o el sistema no logra abrirlo, muestra un mensaje claro
    en lugar de fallar en silencio.

    Args:
        enlace: Direccion del enlace pulsado por el usuario.
        parent: Ventana padre para los mensajes de error.
    """
    try:
        # Validacion: solo se aceptan enlaces web.
        if not enlace.startswith(ESQUEMAS_PERMITIDOS):
            raise ErrorValidacion(f"El enlace no es valido: {enlace}")

        # openUrl devuelve False si el sistema no pudo abrir el navegador.
        if not QDesktopServices.openUrl(QUrl(enlace)):
            mostrar_advertencia(
                parent,
                "No se pudo abrir el enlace",
                f"No fue posible abrir el enlace en el navegador:\n{enlace}",
            )
    except Exception as error:
        # Captura segura: cualquier fallo (incluido ErrorValidacion) se
        # informa en la interfaz en vez de cerrar la aplicacion.
        mostrar_error_contextualizado(parent, error)


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
    # Si falla la construccion del texto, se informa el error y se sale.
    try:
        texto = _construir_texto()
    except Exception as error:
        mostrar_error_contextualizado(parent, error)
        return

    dialogo = QMessageBox(parent)
    dialogo.setIcon(QMessageBox.Icon.Information)
    dialogo.setWindowTitle("Acerca de ChuspaCalc")
    dialogo.setTextFormat(Qt.TextFormat.RichText)
    dialogo.setText(texto)
    dialogo.setStandardButtons(QMessageBox.StandardButton.Close)
    dialogo.button(QMessageBox.StandardButton.Close).setText("Cerrar")

    # Conexion de señales: se desactiva la apertura automatica de enlaces y
    # cada clic se redirige al slot _abrir_enlace, que controla los errores.
    for etiqueta in dialogo.findChildren(QLabel):
        etiqueta.setOpenExternalLinks(False)
        etiqueta.linkActivated.connect(partial(_abrir_enlace, parent=parent))

    dialogo.exec()
