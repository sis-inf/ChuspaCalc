"""Pruebas para el diálogo enriquecido Acerca de."""

from unittest.mock import MagicMock, patch

import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QWidget

from chuspacalc import __version__
from chuspacalc.ui import dialogo_acerca_de as modulo
from chuspacalc.ui.dialogo_acerca_de import mostrar_acerca_de


@pytest.fixture
def app():
    """Fixture para la aplicación Qt"""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


@pytest.fixture
def cuadro_mensaje():
    with patch("chuspacalc.ui.dialogo_acerca_de.QMessageBox") as clase:
        instancia = clase.return_value
        instancia.findChildren.return_value = []
        yield clase, instancia


class TestDialogoAcercaDe:
    """Pruebas para el diálogo Acerca de"""

    def test_mostrar_acerca_de_instancia(self, app, cuadro_mensaje):
        """Crea la instancia modal, configura el botón y la abre."""
        clase, dialogo = cuadro_mensaje

        mostrar_acerca_de()

        clase.assert_called_once_with(None)
        dialogo.setIcon.assert_called_once_with(clase.Icon.Information)
        dialogo.setStandardButtons.assert_called_once_with(clase.StandardButton.Close)
        dialogo.button.assert_called_once_with(clase.StandardButton.Close)
        dialogo.button.return_value.setText.assert_called_once_with("Cerrar")
        dialogo.exec.assert_called_once_with()

    def test_mostrar_acerca_de_con_parent(self, app, qtbot, cuadro_mensaje):
        """Verifica que mostrar_acerca_de funciona con un parent (widget real)"""
        parent = QWidget()
        qtbot.addWidget(parent)
        clase, dialogo = cuadro_mensaje

        mostrar_acerca_de(parent)

        clase.assert_called_once_with(parent)
        dialogo.exec.assert_called_once_with()

    def test_mostrar_acerca_de_usa_version(self, app, cuadro_mensaje):
        """Verifica que mostrar_acerca_de usa la versión del proyecto"""
        _, dialogo = cuadro_mensaje

        mostrar_acerca_de()

        texto = dialogo.setText.call_args.args[0]
        assert f"Versión: {__version__}" in texto

    def test_mostrar_acerca_de_contenido(self, app, cuadro_mensaje):
        """Verifica que el diálogo contiene la información esperada"""
        _, dialogo = cuadro_mensaje
        etiqueta = MagicMock(spec=QLabel)
        dialogo.findChildren.return_value = [etiqueta]

        mostrar_acerca_de()

        dialogo.setTextFormat.assert_called_once_with(Qt.TextFormat.RichText)
        texto = dialogo.setText.call_args.args[0]
        assert "ChuspaCalc" in texto
        assert "Versión:" in texto
        assert "Especialidades soportadas:" in texto
        assert "Licencia:</b> MIT" in texto
        assert "Créditos:" in texto
        assert "Universidad Técnica de Oruro" in texto
        assert "Documentación técnica" in texto
        dialogo.findChildren.assert_called_once_with(QLabel)
        etiqueta.setOpenExternalLinks.assert_called_once_with(False)
        etiqueta.linkActivated.connect.assert_called_once()

    def test_mostrar_acerca_de_titulo(self, app, cuadro_mensaje):
        """Verifica que el diálogo tiene el título correcto"""
        _, dialogo = cuadro_mensaje

        mostrar_acerca_de()

        dialogo.setWindowTitle.assert_called_once_with("Acerca de ChuspaCalc")


class TestAbrirEnlace:
    """Pruebas del slot que abre los enlaces del dialogo."""

    def test_enlace_valido_abre_navegador(self, app):
        """Un enlace https se envia al navegador del sistema."""
        with patch.object(modulo, "QDesktopServices") as escritorio:
            escritorio.openUrl.return_value = True

            modulo._abrir_enlace("https://example.com")

            escritorio.openUrl.assert_called_once()

    def test_esquema_invalido_muestra_error(self, app):
        """Un enlace que no es http ni https se rechaza con un mensaje."""
        with (
            patch.object(modulo, "QDesktopServices") as escritorio,
            patch.object(modulo, "mostrar_error_contextualizado") as error,
        ):
            modulo._abrir_enlace("file:///etc/passwd")

            escritorio.openUrl.assert_not_called()
            error.assert_called_once()

    def test_openurl_falla_muestra_advertencia(self, app):
        """Si el sistema no puede abrir el enlace, se avisa al usuario."""
        with (
            patch.object(modulo, "QDesktopServices") as escritorio,
            patch.object(modulo, "mostrar_advertencia") as aviso,
        ):
            escritorio.openUrl.return_value = False

            modulo._abrir_enlace("https://example.com")

            aviso.assert_called_once()
