"""
Pruebas para el módulo progress.py (indicador de progreso)
"""

from unittest.mock import patch, MagicMock

from escuadra.ui.progress import mostrar_progreso, ProgressIndicator


class TestMostrarProgreso:
    """Pruebas para la función mostrar_progreso"""

    def test_mostrar_progreso_0_porciento(self):
        """Verifica que muestra 0% cuando current=0"""
        with patch('builtins.print') as mock_print:
            mostrar_progreso(0, 100)
            mock_print.assert_called_with("\r[------------------------------] 0%", end="", flush=True)

    def test_mostrar_progreso_50_porciento(self):
        """Verifica que muestra 50% cuando current=50"""
        with patch('builtins.print') as mock_print:
            mostrar_progreso(50, 100)
            mock_print.assert_called_with("\r[===============---------------] 50%", end="", flush=True)

    def test_mostrar_progreso_100_porciento(self):
        """Verifica que muestra 100% cuando current=100"""
        with patch('builtins.print') as mock_print:
            mostrar_progreso(100, 100)
            # Primera llamada: la barra con 100%
            mock_print.assert_any_call("\r[==============================] 100%", end="", flush=True)
            # Segunda llamada: salto de línea
            mock_print.assert_called_with()

    def test_mostrar_progreso_25_porciento(self):
        """Verifica que muestra 25% cuando current=25"""
        with patch('builtins.print') as mock_print:
            mostrar_progreso(25, 100)
            expected = f"\r[{'=' * 7}{'-' * 23}] 25%"
            mock_print.assert_called_with(expected, end="", flush=True)

    def test_mostrar_progreso_75_porciento(self):
        """Verifica que muestra 75% cuando current=75"""
        with patch('builtins.print') as mock_print:
            mostrar_progreso(75, 100)
            expected = f"\r[{'=' * 22}{'-' * 8}] 75%"
            mock_print.assert_called_with(expected, end="", flush=True)

    def test_mostrar_progreso_total_cero(self):
        """Verifica que no hace nada cuando total=0"""
        with patch('builtins.print') as mock_print:
            mostrar_progreso(50, 0)
            mock_print.assert_not_called()

    def test_mostrar_progreso_width_personalizado(self):
        """Verifica que usa el ancho personalizado"""
        with patch('builtins.print') as mock_print:
            mostrar_progreso(50, 100, width=20)
            expected = "\r[==========----------] 50%"
            mock_print.assert_called_with(expected, end="", flush=True)


class TestProgressIndicator:
    """Pruebas para la clase ProgressIndicator"""

    def test_progress_indicator_init(self):
        """Verifica que se inicializa correctamente"""
        indicator = ProgressIndicator("Cargando...")
        assert indicator.mensaje == "Cargando..."
        assert indicator._activo is False
        assert indicator.thread is None

    def test_progress_indicator_init_default(self):
        """Verifica que usa el mensaje por defecto"""
        indicator = ProgressIndicator()
        assert indicator.mensaje == "Procesando..."

    def test_progress_indicator_start(self):
        """Verifica que start inicia el indicador"""
        indicator = ProgressIndicator("Test")
        
        with patch('builtins.print') as mock_print:
            with patch('threading.Thread') as mock_thread:
                mock_thread_instance = MagicMock()
                mock_thread.return_value = mock_thread_instance
                
                indicator.start()
                
                mock_print.assert_any_call("\nTest")
                mock_thread.assert_called_once()
                mock_thread_instance.start.assert_called_once()
                assert indicator._activo is True

    def test_progress_indicator_stop(self):
        """Verifica que stop detiene el indicador"""
        indicator = ProgressIndicator("Test")
        indicator._activo = True
        indicator.thread = MagicMock()
        
        with patch('builtins.print') as mock_print:
            indicator.stop()
            
            assert indicator._activo is False
            indicator.thread.join.assert_called_once()
            mock_print.assert_called_with("\n✔ terminado")

    def test_progress_indicator_stop_sin_thread(self):
        """Verifica que stop maneja el caso sin thread"""
        indicator = ProgressIndicator("Test")
        indicator._activo = True
        
        with patch('builtins.print') as mock_print:
            indicator.stop()
            
            assert indicator._activo is False
            mock_print.assert_called_with("\n✔ terminado")
