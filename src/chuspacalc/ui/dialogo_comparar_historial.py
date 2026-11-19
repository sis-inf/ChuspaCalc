"""Diálogo para comparar dos entradas del historial lado a lado."""

from __future__ import annotations

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

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.ui.mensajes import mostrar_error_contextualizado


class DialogoCompararHistorial(QDialog):
    """Muestra dos entradas del historial una junto a la otra."""

    def __init__(
        self,
        entrada1: Mapping[str, Any],
        entrada2: Mapping[str, Any],
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        # Validación: si las entradas no son válidas, se informa el error
        # en la interfaz y se usan mapeos vacíos para no romper el diálogo.
        try:
            self._validar_entradas(entrada1, entrada2)
        except ErrorValidacion as error:
            mostrar_error_contextualizado(parent, error)
            entrada1, entrada2 = {}, {}

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

        self.boton_cerrar = QPushButton("Cerrar")
        layout.addWidget(self.boton_cerrar)
        self._conectar_senales()

    @staticmethod
    def _validar_entradas(entrada1: Mapping[str, Any], entrada2: Mapping[str, Any]) -> None:
        """Comprueba que ambas entradas sean mapeos antes de mostrarlas.

        Raises:
            ErrorValidacion: Si alguna de las entradas no es un mapeo.
        """
        for numero, entrada in ((1, entrada1), (2, entrada2)):
            if not isinstance(entrada, Mapping):
                raise ErrorValidacion(f"La entrada {numero} del historial no es válida.")

    def _conectar_senales(self) -> None:
        """Conecta las señales de la interfaz con sus slots.

        Se concentran aquí todas las conexiones para que sea fácil
        ver qué evento dispara cada acción del diálogo.
        """
        self.boton_cerrar.clicked.connect(self._on_cerrar)

    def _on_cerrar(self) -> None:
        """Slot del botón 'Cerrar': cierra el diálogo aceptándolo.

        Si algo falla al cerrar, se informa el error en la interfaz
        en lugar de dejar que la excepción termine la aplicación.
        """
        try:
            self.accept()
        except Exception as error:
            # Captura segura: se muestra un mensaje claro al usuario.
            mostrar_error_contextualizado(self, error)

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
