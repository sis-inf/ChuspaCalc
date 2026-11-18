"""Diálogo para comparar dos entradas del historial lado a lado."""

from collections.abc import Mapping
from html import escape
from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)


class DialogoCompararHistorial(QDialog):
    """Muestra dos entradas del historial una junto a la otra."""

    def __init__(
        self,
        entrada1: Mapping[str, Any],
        entrada2: Mapping[str, Any],
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.entrada1 = entrada1
        self.entrada2 = entrada2

        self.setWindowTitle("Comparación de historial")
        self.setMinimumSize(800, 400)
        self._setup_ui()

    def _setup_ui(self) -> None:
        """Construye los paneles de comparación y el botón de cierre."""
        layout = QVBoxLayout(self)

        titulo = QLabel("Comparación de entradas del historial")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titulo)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        contenido = QWidget()
        paneles = QHBoxLayout(contenido)
        paneles.addWidget(self._crear_panel(self.entrada1, "Entrada 1"))
        paneles.addWidget(self._crear_panel(self.entrada2, "Entrada 2"))
        scroll.setWidget(contenido)
        layout.addWidget(scroll)

        boton_cerrar = QPushButton("Cerrar")
        boton_cerrar.clicked.connect(self.accept)
        layout.addWidget(boton_cerrar)

    def _crear_panel(self, entrada: Mapping[str, Any], titulo: str) -> QWidget:
        """Crea un panel con los campos de una entrada."""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        encabezado = QLabel(titulo)
        encabezado.setStyleSheet("font-weight: bold;")
        layout.addWidget(encabezado)

        informacion = QLabel(self._formatear_entrada(entrada))
        informacion.setWordWrap(True)
        informacion.setTextFormat(Qt.TextFormat.RichText)
        layout.addWidget(informacion)
        return panel

    @staticmethod
    def _formatear_entrada(entrada: Mapping[str, Any]) -> str:
        """Devuelve los campos de la entrada en formato HTML seguro."""
        if not entrada:
            return "No hay datos disponibles."

        lineas = [
            f"<b>{escape(str(clave))}</b>: {escape(str(valor))}"
            for clave, valor in entrada.items()
            if clave != "id"
        ]
        return "<br>".join(lineas) or "No hay datos disponibles."
