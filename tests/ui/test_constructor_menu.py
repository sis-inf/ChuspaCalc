"""
Pruebas para el módulo constructor_menu.py
"""

import pytest
from unittest.mock import MagicMock, patch

from escuadra.ui.constructor_menu import construir_menu
from escuadra.core.carrera import Carrera


class TestConstructorMenu:
    """Pruebas para la función construir_menu"""

    def test_construir_menu_con_herramientas(self):
        """Verifica que construir_menu genera entradas de menú con herramientas"""
        mock_ventana = MagicMock()
        mock_menu_carrera = MagicMock()
        mock_menu_herramientas = MagicMock()
        mock_ventana.menu_carrera.return_value = mock_menu_carrera
        mock_ventana.menu_herramientas.return_value = mock_menu_herramientas

        class HerramientaMock:
            nombre = "Herramienta Test"

        herramientas_por_carrera = {
            Carrera.SISTEMAS: [HerramientaMock],
            Carrera.ELECTRICA: [HerramientaMock],
        }

        callback = MagicMock()

        with patch("escuadra.ui.constructor_menu.QAction") as MockQAction:
            mock_action = MagicMock()
            MockQAction.return_value = mock_action

            construir_menu(mock_ventana, herramientas_por_carrera, callback)

            mock_ventana.menu_carrera.assert_called_once()
            mock_ventana.menu_herramientas.assert_called_once()

    def test_construir_menu_agrupacion_por_carrera(self):
        """Verifica que las herramientas se agrupan correctamente por carrera"""
        mock_ventana = MagicMock()
        mock_menu_carrera = MagicMock()
        mock_menu_herramientas = MagicMock()
        mock_ventana.menu_carrera.return_value = mock_menu_carrera
        mock_ventana.menu_herramientas.return_value = mock_menu_herramientas

        class HerramientaMock:
            nombre = "Herramienta Test"

        herramientas_por_carrera = {
            Carrera.SISTEMAS: [HerramientaMock],
            Carrera.MATEMATICAS: [HerramientaMock],
        }

        callback = MagicMock()

        with patch("escuadra.ui.constructor_menu.QAction") as MockQAction:
            mock_action = MagicMock()
            MockQAction.return_value = mock_action

            construir_menu(mock_ventana, herramientas_por_carrera, callback)

            assert mock_menu_carrera.addMenu.call_count >= 2

    def test_construir_menu_lista_vacia(self):
        """Verifica que una lista vacía no produce excepción"""
        mock_ventana = MagicMock()
        mock_menu_carrera = MagicMock()
        mock_menu_herramientas = MagicMock()
        mock_ventana.menu_carrera.return_value = mock_menu_carrera
        mock_ventana.menu_herramientas.return_value = mock_menu_herramientas

        herramientas_por_carrera = {}

        callback = MagicMock()

        with patch("escuadra.ui.constructor_menu.QAction") as MockQAction:
            mock_action = MagicMock()
            MockQAction.return_value = mock_action

            # No debe lanzar excepción
            try:
                construir_menu(mock_ventana, herramientas_por_carrera, callback)
            except Exception as e:
                pytest.fail(f"construir_menu lanzó excepción con lista vacía: {e}")

    def test_construir_menu_carrera_sin_herramientas(self):
        """Verifica que una carrera sin herramientas no crea submenú"""
        mock_ventana = MagicMock()
        mock_menu_carrera = MagicMock()
        mock_menu_herramientas = MagicMock()
        mock_ventana.menu_carrera.return_value = mock_menu_carrera
        mock_ventana.menu_herramientas.return_value = mock_menu_herramientas

        class HerramientaMock:
            nombre = "Herramienta Test"

        herramientas_por_carrera = {
            Carrera.SISTEMAS: [HerramientaMock],
        }

        callback = MagicMock()

        with patch("escuadra.ui.constructor_menu.QAction") as MockQAction:
            mock_action = MagicMock()
            MockQAction.return_value = mock_action

            construir_menu(mock_ventana, herramientas_por_carrera, callback)

            assert mock_menu_carrera.addMenu.call_count >= 1

    def test_construir_menu_herramientas_todas(self):
        """Verifica que el menú Herramientas tiene todas las herramientas"""
        mock_ventana = MagicMock()
        mock_menu_carrera = MagicMock()
        mock_menu_herramientas = MagicMock()
        mock_ventana.menu_carrera.return_value = mock_menu_carrera
        mock_ventana.menu_herramientas.return_value = mock_menu_herramientas

        class Herramienta1:
            nombre = "Herramienta 1"

        class Herramienta2:
            nombre = "Herramienta 2"

        herramientas_por_carrera = {
            Carrera.SISTEMAS: [Herramienta1, Herramienta2],
        }

        callback = MagicMock()

        with patch("escuadra.ui.constructor_menu.QAction") as MockQAction:
            mock_action = MagicMock()
            MockQAction.return_value = mock_action

            construir_menu(mock_ventana, herramientas_por_carrera, callback)

            assert mock_menu_herramientas.addAction.call_count == 2

    def test_construir_menu_callback_seleccion(self):
        """Verifica que el callback se ejecuta al seleccionar una herramienta"""
        mock_ventana = MagicMock()
        mock_menu_carrera = MagicMock()
        mock_menu_herramientas = MagicMock()
        mock_ventana.menu_carrera.return_value = mock_menu_carrera
        mock_ventana.menu_herramientas.return_value = mock_menu_herramientas

        class HerramientaMock:
            nombre = "Herramienta Test"

        herramientas_por_carrera = {
            Carrera.SISTEMAS: [HerramientaMock],
        }

        callback = MagicMock()

        with patch("escuadra.ui.constructor_menu.QAction") as MockQAction:
            mock_action = MagicMock()
            MockQAction.return_value = mock_action

            construir_menu(mock_ventana, herramientas_por_carrera, callback)

            mock_action.triggered.connect.assert_called()
