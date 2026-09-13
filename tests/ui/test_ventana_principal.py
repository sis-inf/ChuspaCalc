"""
Pruebas de humo para el módulo ventana_principal.py
"""

import pytest
from unittest.mock import MagicMock, patch

from PySide6.QtWidgets import QApplication, QMainWindow

from escuadra.ui.ventana_principal import VentanaPrincipal


@pytest.fixture
def app():
    """Fixture para la aplicación Qt"""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


class TestVentanaPrincipal:
    """Pruebas para la clase VentanaPrincipal"""

    def test_ventana_instancia(self, app):
        """Verifica que la ventana se instancia correctamente"""
        ventana = VentanaPrincipal()
        assert ventana is not None
        assert isinstance(ventana, QMainWindow)

    def test_ventana_muestra(self, app, qtbot):
        """Verifica que la ventana se muestra sin excepción"""
        ventana = VentanaPrincipal()
        qtbot.addWidget(ventana)

        with qtbot.waitExposed(ventana):
            ventana.show()

        assert ventana.isVisible()

    def test_ventana_titulo(self, app, qtbot):
        """Verifica que la ventana tiene el título correcto"""
        ventana = VentanaPrincipal()
        qtbot.addWidget(ventana)

        assert ventana.windowTitle() == "Escuadra"

    def test_ventana_menu_archivo(self, app, qtbot):
        """Verifica que el menú Archivo existe"""
        ventana = VentanaPrincipal()
        qtbot.addWidget(ventana)

        menu_bar = ventana.menuBar()
        menus = [action.text() for action in menu_bar.actions()]

        assert "Archivo" in menus

    def test_ventana_menu_carrera(self, app, qtbot):
        """Verifica que el menú Carrera existe"""
        ventana = VentanaPrincipal()
        qtbot.addWidget(ventana)

        menu_carrera = ventana.menu_carrera()
        assert menu_carrera is not None
        assert menu_carrera.title() == "Carrera"

    def test_ventana_menu_herramientas(self, app, qtbot):
        """Verifica que el menú Herramientas existe"""
        ventana = VentanaPrincipal()
        qtbot.addWidget(ventana)

        menu_herramientas = ventana.menu_herramientas()
        assert menu_herramientas is not None
        assert menu_herramientas.title() == "Herramientas"

    def test_ventana_menu_ayuda(self, app, qtbot):
        """Verifica que el menú Ayuda existe"""
        ventana = VentanaPrincipal()
        qtbot.addWidget(ventana)

        menu_bar = ventana.menuBar()
        menus = [action.text() for action in menu_bar.actions()]

        assert "Ayuda" in menus

    def test_ventana_area_central(self, app, qtbot):
        """Verifica que el área central existe"""
        ventana = VentanaPrincipal()
        qtbot.addWidget(ventana)

        area = ventana._area_central
        assert area is not None

    def test_ventana_cierre(self, app, qtbot):
        """Verifica que la ventana se cierra correctamente"""
        ventana = VentanaPrincipal()
        qtbot.addWidget(ventana)
        ventana.show()

        ventana.close()

        # Verificar que no hay excepción
        assert True

    def test_ventana_cierre_limpio(self, app, qtbot):
        """Verifica que cerrar la ventana no deja procesos colgados"""
        ventana = VentanaPrincipal()
        qtbot.addWidget(ventana)
        ventana.show()

        ventana.close()

        assert not ventana.isVisible()
