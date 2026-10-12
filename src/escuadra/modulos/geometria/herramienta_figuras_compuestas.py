"""
Herramienta de Figuras Compuestas para Escuadra.
"""

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QTextEdit,
)
from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta
from .figuras_compuestas import calcular_area_compuesta, calcular_volumen_compuesto


class HerramientaFigurasCompuestas(Herramienta):
    nombre = "Figuras Compuestas"
    carrera = Carrera.GEOMETRIA
    descripcion = "Calcula el área y volumen total de una figura compuesta."

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        root = QVBoxLayout()
        root.setSpacing(10)

        ayuda = QLabel(
            "Esta herramienta usa calcular_area_compuesta y calcular_volumen_compuesto. Ingresa JSON de figuras o usa valores de prueba."
        )
        ayuda.setWordWrap(True)
        root.addWidget(ayuda)

        self._entrada = QTextEdit()
        self._entrada.setPlaceholderText(
            'Ej: [{"tipo": "rectangulo", "base": 5, "altura": 3}] - Deja vacío para demo'
        )
        root.addWidget(self._entrada)

        botones = QHBoxLayout()
        btn_calc = QPushButton("Calcular Área")
        btn_calc.clicked.connect(lambda: self._calcular("area"))
        btn_vol = QPushButton("Calcular Volumen")
        btn_vol.clicked.connect(lambda: self._calcular("volumen"))
        botones.addWidget(btn_calc)
        botones.addWidget(btn_vol)
        root.addLayout(botones)

        self._resultado = QLineEdit()
        self._resultado.setReadOnly(True)
        self._resultado.setPlaceholderText("—")
        root.addWidget(self._resultado)

        self._error = QLabel("")
        self._error.setStyleSheet("color: red;")
        root.addWidget(self._error)

        root.addStretch()
        widget.setLayout(root)
        return widget

    def _calcular(self, tipo):
        self._error.setText("")
        try:
            # Si no hay entrada, usar demo vacío que llame a la lógica
            # Aquí solo demostramos que la Herramienta existe y es descubrible
            import json

            texto = self._entrada.toPlainText().strip()
            if not texto:
                self._resultado.setText(
                    "Herramienta registrada correctamente. Ingresa figuras para calcular."
                )
                return

            figuras = json.loads(texto)
            if tipo == "area":
                res = calcular_area_compuesta(figuras)
                self._resultado.setText(f"ÁREA: {res}")
            else:
                res = calcular_volumen_compuesto(figuras)
                self._resultado.setText(f"VOLUMEN: {res}")
        except Exception as e:
            self._error.setText(f"Error: {e}")

    def ejecutar(self, figuras):
        # Método requerido por algunos tests
        return calcular_area_compuesta(figuras)


def calcular_volumen(figuras):
    """
    Calcula el volumen total de una figura compuesta.
    """
    return calcular_volumen_compuesto(figuras)
