"""
Pruebas para el panel de estadísticas de uso de herramientas:
- panel_estadisticas_uso.py
"""

from chuspacalc.ui.panel_estadisticas_uso import PanelEstadisticasUso


class TestPanelEstadisticasUso:
    """Pruebas para el panel de estadísticas de uso"""

    def test_contar_por_herramienta(self):
        """Verifica la cuenta de usos agrupada por herramienta"""
        panel = PanelEstadisticasUso(
            [
                {"herramienta": "Ley de Ohm"},
                {"herramienta": "Ley de Ohm"},
                {"herramienta": "Viga"},
            ]
        )

        assert panel.contar_por_herramienta() == {"Ley de Ohm": 2, "Viga": 1}

    def test_contar_por_carrera(self):
        """Verifica la agrupación por carrera e ignora registros sin ella"""
        panel = PanelEstadisticasUso(
            [
                {"herramienta": "Ley de Ohm", "carrera": "Electricidad"},
                {"herramienta": "Viga", "carrera": "Civil"},
                {"herramienta": "Ley de Ohm"},
            ]
        )

        assert panel.contar_por_carrera() == {"Electricidad": 1, "Civil": 1}

    def test_contar_por_herramienta_sin_herramienta(self):
        """Verifica que los registros sin herramienta no se cuentan"""
        panel = PanelEstadisticasUso(
            [
                {"carrera": "Electricidad"},
                {"herramienta": None},
            ]
        )

        assert panel.contar_por_herramienta() == {}

    def test_generar_resumen(self):
        """Verifica que el resumen tiene las claves herramientas y carreras"""
        panel = PanelEstadisticasUso(
            [
                {"herramienta": "Ley de Ohm", "carrera": "Electricidad"},
            ]
        )

        resumen = panel.generar_resumen()

        assert set(resumen) == {"herramientas", "carreras"}
        assert resumen["herramientas"] == {"Ley de Ohm": 1}
        assert resumen["carreras"] == {"Electricidad": 1}

    def test_generar_grafico_barras(self):
        """Verifica que el gráfico devuelve las herramientas y sus cantidades"""
        panel = PanelEstadisticasUso(
            [
                {"herramienta": "Ley de Ohm"},
                {"herramienta": "Ley de Ohm"},
                {"herramienta": "Viga"},
            ]
        )

        grafico = panel.generar_grafico_barras()

        assert ("Ley de Ohm", 2) in grafico
        assert ("Viga", 1) in grafico

    def test_estadisticas_historial_vacio(self):
        """Verifica que con historial vacío todos los métodos devuelven estructuras vacías"""
        panel = PanelEstadisticasUso([])

        assert panel.contar_por_herramienta() == {}
        assert panel.contar_por_carrera() == {}
        assert panel.generar_resumen() == {"herramientas": {}, "carreras": {}}
        assert panel.generar_grafico_barras() == []
