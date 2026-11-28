"""
Herramienta para resolver triángulos mediante ley de senos y cosenos.
"""

import math

from PySide6.QtWidgets import (
    QComboBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta
from chuspacalc.modulos.geometria.resolucion_triangulos import (
    resolver_triangulo_lado_angulo,
    resolver_triangulo_lados,
)
from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
)


class HerramientaResolucionTriangulos(Herramienta):
    nombre: str = "Resolución de triángulos"
    carrera: Carrera = Carrera.GEOMETRIA
    descripcion: str = "Calcula triángulos usando ley de senos y cosenos."

    def crear_widget(self) -> QWidget:
        """Construye y devuelve la interfaz para resolver triángulos."""
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

    def _leer_valor(self, campo: QLineEdit, nombre: str) -> float:
        """
        Lee y valida un campo numérico de la interfaz.

        Args:
            campo: Campo de texto que contiene el valor.
            nombre: Nombre descriptivo del parámetro.

        Returns:
            El valor convertido a float y validado.

        Raises:
            ErrorValidacion: Si el campo está vacío, contiene texto no
                numérico, o el valor no es finito.
        """
        texto = campo.text().strip()

        if not texto:
            raise ErrorValidacion(f"El campo {nombre} es obligatorio.")

        try:
            valor = float(texto)
        except (ValueError, OverflowError) as error:
            raise ErrorValidacion(
                f"El campo {nombre} debe contener un número válido."
            ) from error

        return validar_numero(valor, nombre)

    def _resolver(self) -> None:
        """
        Valida las entradas, resuelve el triángulo y muestra el resultado.

        En el primer modo se reciben tres lados positivos. En el segundo,
        se recibe un lado positivo y dos ángulos interiores válidos.

        Los errores de validación se muestran en la etiqueta de resultado.
        """
        self._resultado.clear()

        try:
            v1 = self._leer_valor(self._valor1, "Valor 1")
            v2 = self._leer_valor(self._valor2, "Valor 2")
            v3 = self._leer_valor(self._valor3, "Valor 3")

            if self._modo.currentIndex() == 0:
                if v1 <= 0 or v2 <= 0 or v3 <= 0:
                    raise ErrorValidacion("Los tres lados deben ser mayores que cero.")

                angulo_a, angulo_b, angulo_c = resolver_triangulo_lados(
                    v1,
                    v2,
                    v3,
                )

                if not all(
                    math.isfinite(angulo) for angulo in (angulo_a, angulo_b, angulo_c)
                ):
                    raise ErrorValidacion(
                        "Los ángulos calculados deben ser valores finitos."
                    )

                texto = (
                    f"Ángulo A: {round(angulo_a, 2)}°\n"
                    f"Ángulo B: {round(angulo_b, 2)}°\n"
                    f"Ángulo C: {round(angulo_c, 2)}°"
                )

            else:
                if v1 <= 0:
                    raise ErrorValidacion("El lado debe ser mayor que cero.")

                if not 0 < v2 < 180 or not 0 < v3 < 180:
                    raise ErrorValidacion(
                        "Cada ángulo debe ser mayor que 0° y menor que 180°."
                    )

                if v2 + v3 >= 180:
                    raise ErrorValidacion(
                        "La suma de los dos ángulos debe ser menor que 180°."
                    )

                lado_b, lado_c, angulo_c = resolver_triangulo_lado_angulo(
                    v1,
                    v2,
                    v3,
                )

                if not all(
                    math.isfinite(valor) for valor in (lado_b, lado_c, angulo_c)
                ):
                    raise ErrorValidacion(
                        "Los resultados calculados deben ser valores finitos."
                    )

                texto = (
                    f"Lado B: {round(lado_b, 2)}\n"
                    f"Lado C: {round(lado_c, 2)}\n"
                    f"Ángulo C: {round(angulo_c, 2)}°"
                )

            self._resultado.setText(texto)

        except ErrorValidacion as error:
            self._resultado.setText(str(error))
