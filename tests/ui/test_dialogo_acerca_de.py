"""
Pruebas para el módulo dialogo_acerca_de.py
"""

import pytest
from unittest.mock import patch, MagicMock

from PySide6.QtWidgets import QApplication, QWidget

from escuadra.ui.dialogo_acerca_de import mostrar_acerca_de


@pytest.fixture
def app():
    """Fixture para la aplicación Qt"""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


class TestDialogoAcercaDe:
    """Pruebas para el diálogo Acerca de"""

    def test_mostrar_acerca_de_instancia(self, app, qtbot):
        """Verifica que mostrar_acerca_de se ejecuta sin error"""
        try:
            mostrar_acerca_de()
        except Exception as e:
            pytest.fail(f"mostrar_acerca_de lanzó excepción: {e}")

    def test_mostrar_acerca_de_con_parent(self, app, qtbot):
        """Verifica que mostrar_acerca_de funciona con un parent (widget real)"""
        parent = QWidget()
        qtbot.addWidget(parent)

        try:
            mostrar_acerca_de(parent)
        except Exception as e:
            pytest.fail(f"mostrar_acerca_de con parent lanzó excepción: {e}")

    def test_mostrar_acerca_de_usa_version(self, app, qtbot):
        """Verifica que mostrar_acerca_de usa la versión del proyecto"""
        with patch('escuadra.ui.dialogo_acerca_de.QMessageBox') as MockQMessageBox:
            mock_messagebox = MagicMock()
            MockQMessageBox.about = mock_messagebox

            mostrar_acerca_de()

            mock_messagebox.assert_called_once()
            args = mock_messagebox.call_args[0]
            assert "Versión:" in args[2]

    def test_mostrar_acerca_de_contenido(self, app, qtbot):
        """Verifica que el diálogo contiene la información esperada"""
        with patch('escuadra.ui.dialogo_acerca_de.QMessageBox') as MockQMessageBox:
            mock_messagebox = MagicMock()
            MockQMessageBox.about = mock_messagebox

            mostrar_acerca_de()

            mock_messagebox.assert_called_once()
            args = mock_messagebox.call_args[0]
            texto = args[2]

            assert "Escuadra" in texto
            assert "Versión:" in texto
            assert "Licencia:" in texto
            assert "MIT" in texto
            assert "Créditos:" in texto

    def test_mostrar_acerca_de_titulo(self, app, qtbot):
        """Verifica que el diálogo tiene el título correcto"""
        with patch('escuadra.ui.dialogo_acerca_de.QMessageBox') as MockQMessageBox:
            mock_messagebox = MagicMock()
            MockQMessageBox.about = mock_messagebox

            mostrar_acerca_de()

            mock_messagebox.assert_called_once()
            args = mock_messagebox.call_args[0]
            assert "Acerca de Escuadra" in args[1]
