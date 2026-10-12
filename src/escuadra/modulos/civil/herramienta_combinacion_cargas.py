"""
Herramienta para calcular combinaciones de cargas en ingeniería civil.
"""

from PySide6.QtWidgets import (
    QDoubleSpinBox,
    QFormLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta
from escuadra.modulos.civil.combinacion_cargas import combinar_cargas_lrfd


class HerramientaCombinacionCargas(Herramienta):
    nombre = "Combinación de cargas"
    carrera = Carrera.CIVIL
    descripcion = "Calcula una combinación simplificada de cargas vivas y muertas."

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout()

        self._carga_muerta = QDoubleSpinBox()
        self._carga_muerta.setRange(0, 100000)
        self._carga_muerta.setSuffix(" kN")

        self._carga_viva = QDoubleSpinBox()
        self._carga_viva.setRange(0, 100000)
        self._carga_viva.setSuffix(" kN")

        formulario = QFormLayout()
        formulario.addRow("Carga muerta:", self._carga_muerta)
        formulario.addRow("Carga viva:", self._carga_viva)

        boton = QPushButton("Calcular")
        boton.clicked.connect(self._calcular)

        self._resultado = QLabel("")

        layout.addLayout(formulario)
        layout.addWidget(boton)
        layout.addWidget(self._resultado)

        widget.setLayout(layout)
        return widget

    def _calcular(self) -> None:
        resultado = combinar_cargas_lrfd(
            self._carga_muerta.value(),
            self._carga_viva.value(),
        )

        self._resultado.setText(f"Carga última de diseño: {resultado:.2f} kN")
