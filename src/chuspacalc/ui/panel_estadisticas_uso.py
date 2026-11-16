"""
Panel de estadísticas de uso de herramientas.

Genera un resumen del historial persistente mostrando
la cantidad de usos por herramienta y carrera.
"""


from collections import Counter

from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

SIN_ESPECIALIDAD = "Sin especialidad"


class PanelEstadisticasUso(QWidget):
    """Genera estadísticas simples del historial de uso."""

    def __init__(self, historial, parent=None):
        super().__init__(parent)
        self.historial = historial
        self.metricas = {}

        self._tabla = QTableWidget(0, 5)
        self._tabla.setHorizontalHeaderLabels(
            ["Módulo", "Especialidad", "Exitosas", "Con error", "Total"]
        )
        self._tabla.horizontalHeader().setStretchLastSection(True)
        self._tabla.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        layout = QVBoxLayout(self)
        layout.addWidget(self._tabla)

    def actualizar_estadisticas(self, modulo: str, exito: bool) -> None:
        """
        Registra una ejecución del módulo y refresca la tabla del panel.

        Args:
            modulo: nombre del módulo ejecutado.
            exito: True si la ejecución se completó; False si terminó
                con error de validación.
        """

        metrica = self.metricas.setdefault(
            modulo,
            {"exitosas": 0, "fallidas": 0},
        )
        metrica["especialidad"] = self._obtener_especialidad(modulo)
        metrica["exitosas" if exito else "fallidas"] += 1

        self._refrescar_tabla()

    def _obtener_especialidad(self, modulo):
        """Busca en el historial la carrera asociada al módulo."""

        for registro in self.historial:
            if registro.get("herramienta") == modulo and registro.get("carrera"):
                return str(registro.get("carrera"))

        return SIN_ESPECIALIDAD

    def _refrescar_tabla(self):
        """Vuelve a cargar la tabla con las métricas actuales."""

        self._tabla.setRowCount(len(self.metricas))

        for fila, (modulo, metrica) in enumerate(self.metricas.items()):
            total = metrica["exitosas"] + metrica["fallidas"]
            valores = [
                modulo,
                metrica["especialidad"],
                metrica["exitosas"],
                metrica["fallidas"],
                total,
            ]

            for columna, valor in enumerate(valores):
                self._tabla.setItem(
                    fila,
                    columna,
                    QTableWidgetItem(str(valor)),
                )

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
            "carreras": self.contar_por_carrera()
        }

    def generar_grafico_barras(self):
        """
        Genera datos para un gráfico de barras básico.

        La capa visual puede usar estos datos con QtCharts
        o matplotlib.
        """

        return list(
            self.contar_por_herramienta().items()
        )
