"""
Pruebas para el módulo historial.py
"""

from escuadra.core.historial import Historial


class TestHistorial:
    """Pruebas para la clase Historial"""

    def test_historial_initialization(self):
        """Verifica que el historial se inicializa correctamente"""
        historial = Historial()
        assert historial is not None
        assert historial.obtener_historial() == []

    def test_historial_agregar_calculo(self):
        """Verifica que se puede agregar un cálculo al historial"""
        historial = Historial()

        historial.agregar_calculo(
            herramienta="suma", parametros={"a": 1, "b": 2}, resultado={"valor": 3}
        )

        historial_data = historial.obtener_historial()
        assert len(historial_data) == 1
        assert historial_data[0]["herramienta"] == "suma"
        assert historial_data[0]["parametros"] == {"a": 1, "b": 2}
        assert historial_data[0]["resultado"] == {"valor": 3}
        assert "timestamp" in historial_data[0]

    def test_historial_limite_capacidad(self):
        """Verifica que el historial respeta el límite de 20 entradas"""
        historial = Historial()

        for i in range(25):
            historial.agregar_calculo(
                herramienta=f"test_{i}", parametros={"n": i}, resultado={"valor": i * 2}
            )

        historial_data = historial.obtener_historial()

        assert len(historial_data) == 20

        assert historial_data[0]["herramienta"] == "test_24"
        assert historial_data[0]["resultado"] == {"valor": 48}

    def test_historial_obtener_historial_reciente_primero(self):
        """Verifica que obtener_historial devuelve el más reciente primero"""
        historial = Historial()

        historial.agregar_calculo("tool1", {}, {"r": 1})
        historial.agregar_calculo("tool2", {}, {"r": 2})
        historial.agregar_calculo("tool3", {}, {"r": 3})

        historial_data = historial.obtener_historial()

        assert historial_data[0]["herramienta"] == "tool3"
        assert historial_data[1]["herramienta"] == "tool2"
        assert historial_data[2]["herramienta"] == "tool1"

    def test_historial_obtener_ultimo(self):
        """Verifica que obtener_ultimo retorna el último registro"""
        historial = Historial()

        historial.agregar_calculo("tool1", {}, {"r": 1})
        historial.agregar_calculo("tool2", {}, {"r": 2})
        historial.agregar_calculo("tool3", {}, {"r": 3})

        ultimo = historial.obtener_ultimo()

        assert ultimo["herramienta"] == "tool3"
        assert ultimo["resultado"] == {"r": 3}

    def test_historial_obtener_ultimo_vacio(self):
        """Verifica que obtener_ultimo retorna None si el historial está vacío"""
        historial = Historial()

        ultimo = historial.obtener_ultimo()

        assert ultimo is None

    def test_historial_limpiar(self):
        """Verifica que limpiar vacía el historial"""
        historial = Historial()

        historial.agregar_calculo("tool1", {}, {"r": 1})
        historial.agregar_calculo("tool2", {}, {"r": 2})

        assert len(historial.obtener_historial()) == 2

        historial.limpiar()

        assert historial.obtener_historial() == []
        assert historial.obtener_ultimo() is None
