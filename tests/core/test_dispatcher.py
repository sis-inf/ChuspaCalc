"""
Pruebas para el módulo dispatcher.py
"""

from unittest.mock import MagicMock, patch

from escuadra.core.dispatcher import dispatch


class TestDispatcher:
    """Pruebas para las funciones del dispatcher"""

    def test_dispatch_subcomando_valido(self):
        """Verifica que dispatch ejecuta un subcomando válido"""
        mock_herramienta = MagicMock()
        mock_instancia = MagicMock()
        mock_instancia.ejecutar.return_value = 0
        mock_herramienta.return_value = mock_instancia

        with patch('escuadra.core.registry.buscar_por_nombre', return_value=mock_herramienta):
            resultado = dispatch('test_tool')
            assert resultado == 0
            mock_instancia.ejecutar.assert_called_once()

    def test_dispatch_subcomando_desconocido(self):
        """Verifica que dispatch maneja subcomandos desconocidos"""
        with patch('escuadra.core.registry.buscar_por_nombre', return_value=None):
            resultado = dispatch('comando_inexistente')
            assert resultado == 1

    def test_dispatch_error_importacion(self):
        """Verifica que dispatch maneja errores de importación"""
        mock_herramienta = MagicMock()
        mock_herramienta.side_effect = ImportError("Módulo no encontrado")

        with patch('escuadra.core.registry.buscar_por_nombre', return_value=mock_herramienta):
            resultado = dispatch('tool_fallo')
            assert resultado == 1
