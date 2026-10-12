"""
Panel de estadísticas de uso de herramientas.

Genera un resumen del historial persistente mostrando
la cantidad de usos por herramienta y carrera.
"""

from collections import Counter


class PanelEstadisticasUso:
    """Genera estadísticas simples del historial de uso."""

    def __init__(self, historial):
        self.historial = historial

    def contar_por_herramienta(self):
        """Cuenta el uso agrupado por herramienta."""

        herramientas = [
            registro.get("herramienta")
            for registro in self.historial
            if registro.get("herramienta")
        ]

        return dict(Counter(herramientas))

    def contar_por_carrera(self):
        """Cuenta el uso agrupado por carrera."""

        carreras = [
            registro.get("carrera")
            for registro in self.historial
            if registro.get("carrera")
        ]

        return dict(Counter(carreras))

    def generar_resumen(self):
        """Devuelve las estadísticas generales."""

        return {
            "herramientas": self.contar_por_herramienta(),
            "carreras": self.contar_por_carrera(),
        }

    def generar_grafico_barras(self):
        """
        Genera datos para un gráfico de barras básico.

        La capa visual puede usar estos datos con QtCharts
        o matplotlib.
        """

        return list(self.contar_por_herramienta().items())
