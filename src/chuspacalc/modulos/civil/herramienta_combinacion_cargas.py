"""
Herramienta para calcular combinaciones de cargas en ingeniería civil.
"""

import math

from PySide6.QtWidgets import (
    QDoubleSpinBox,
    QFormLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta
from chuspacalc.modulos.civil.combinacion_cargas import combinar_cargas_lrfd
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def _validar_carga(nombre: str, valor: float) -> float:
    """
    Comprueba que una carga sea un número finito y no negativo.

    Raises:
        ErrorValidacion: Si el valor no es numérico, no es finito o es negativo.
    """
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise ErrorValidacion(f"{nombre} debe ser un número.")
    if not math.isfinite(valor):
        raise ErrorValidacion(f"{nombre} debe ser un número finito.")
    if valor < 0:
        raise ErrorValidacion(f"{nombre} no puede ser negativa.")
    return valor


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
        try:
            carga_muerta = _validar_carga("La carga muerta", self._carga_muerta.value())
            carga_viva = _validar_carga("La carga viva", self._carga_viva.value())
            resultado = combinar_cargas_lrfd(carga_muerta, carga_viva)
        except ValueError as error:
            self._resultado.setText(f"Error: {error}")
            return

        self._resultado.setText(f"Carga última de diseño: {resultado:.2f} kN")
