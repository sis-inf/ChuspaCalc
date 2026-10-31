"""
Herramienta para resolver triángulos mediante ley de senos y cosenos.
"""

from ChuspaCalc.core.carrera import Carrera
from ChuspaCalc.core.herramienta import Herramienta
from ChuspaCalc.modulos.geometria.resolucion_triangulos import (
    resolver_triangulo_lado_angulo,
    resolver_triangulo_lados,
)
from PySide6.QtWidgets import (
    QComboBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class HerramientaResolucionTriangulos(Herramienta):
    nombre = "Resolución de triángulos"
    carrera = Carrera.GEOMETRIA
    descripcion = "Calcula triángulos usando ley de senos y cosenos."

    def crear_widget(self) -> QWidget:
        self._widget = QWidget()

        layout = QVBoxLayout()

        self._modo = QComboBox()
        self._modo.addItems(
            [
                "Tres lados (ley de cosenos)",
                "Un lado y dos ángulos (ley de senos)",
            ]
        )

        self._valor1 = QLineEdit()
        self._valor2 = QLineEdit()
        self._valor3 = QLineEdit()

        self._valor1.setPlaceholderText("Valor 1")
        self._valor2.setPlaceholderText("Valor 2")
        self._valor3.setPlaceholderText("Valor 3")

        boton = QPushButton("Resolver")
        boton.clicked.connect(self._resolver)

        self._resultado = QLabel("")

        layout.addWidget(self._modo)
        layout.addWidget(self._valor1)
        layout.addWidget(self._valor2)
        layout.addWidget(self._valor3)
        layout.addWidget(boton)
        layout.addWidget(self._resultado)

        self._widget.setLayout(layout)

        return self._widget

    def _resolver(self):
        try:
            v1 = float(self._valor1.text())
            v2 = float(self._valor2.text())
            v3 = float(self._valor3.text())

            if self._modo.currentIndex() == 0:
                a, b, c = resolver_triangulo_lados(v1, v2, v3)

                texto = (
                    f"Ángulo A: {round(a, 2)}°\n"
                    f"Ángulo B: {round(b, 2)}°\n"
                    f"Ángulo C: {round(c, 2)}°"
                )

            else:
                b, c, angulo_c = resolver_triangulo_lado_angulo(
                    v1,
                    v2,
                    v3,
                )

                texto = (
                    f"Lado B: {round(b, 2)}\n"
                    f"Lado C: {round(c, 2)}\n"
                    f"Ángulo C: {round(angulo_c, 2)}°"
                )

            self._resultado.setText(texto)

        except ValueError as error:
            self._resultado.setText(str(error))
