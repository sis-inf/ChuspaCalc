"""
Herramienta de la Ley de Ohm para Escuadra.

Calcula voltaje, corriente o resistencia a partir de las otras dos
magnitudes.
"""

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta
from escuadra.modulos.electrica.ley_ohm import calcular_ohm


def calcular_potencia(voltaje: float, corriente: float) -> float:
    """Calcula la potencia eléctrica."""
    return voltaje * corriente


class HerramientaLeyOhm(Herramienta):
    nombre = "Ley de Ohm"
    carrera = Carrera.ELECTRICA
    descripcion = (
        "Calcula voltaje, corriente o resistencia a partir de las otras dos magnitudes."
    )

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        root = QVBoxLayout()
        root.setSpacing(10)

        ayuda = QLabel("Ingresa dos valores y deja vacío el tercero para calcularlo.")
        ayuda.setWordWrap(True)
        root.addWidget(ayuda)

        self._campos: dict[str, QLineEdit] = {}

        for etiqueta, clave in (
            ("Voltaje (V)", "V"),
            ("Corriente (A)", "I"),
            ("Resistencia (Ω)", "R"),
        ):
            fila = QHBoxLayout()

            label = QLabel(etiqueta)
            label.setFixedWidth(120)

            campo = QLineEdit()
            campo.setPlaceholderText("Dejar vacío para calcular")

            fila.addWidget(label)
            fila.addWidget(campo)

            root.addLayout(fila)
            self._campos[clave] = campo

        botones = QHBoxLayout()

        btn_calcular = QPushButton("Calcular")
        btn_calcular.clicked.connect(self._calcular)

        btn_limpiar = QPushButton("Limpiar")
        btn_limpiar.clicked.connect(self._limpiar)

        botones.addWidget(btn_calcular)
        botones.addWidget(btn_limpiar)

        root.addLayout(botones)

        fila_p = QHBoxLayout()
        fila_p.addWidget(QLabel("Potencia (W):"))

        self._potencia_output = QLineEdit()
        self._potencia_output.setReadOnly(True)
        self._potencia_output.setPlaceholderText("—")

        fila_p.addWidget(self._potencia_output)
        root.addLayout(fila_p)

        self._error_label = QLabel("")
        self._error_label.setStyleSheet("color: red;")
        self._error_label.setWordWrap(True)
        root.addWidget(self._error_label)

        root.addStretch()
        widget.setLayout(root)

        return widget

    def _calcular(self) -> None:
        self._error_label.setText("")
        self._potencia_output.clear()

        valores: dict[str, float | None] = {}

        for clave in ("V", "I", "R"):
            texto = self._campos[clave].text().strip()

            if texto == "":
                valores[clave] = None
                continue

            try:
                valor = float(texto)
            except ValueError:
                self._error_label.setText(f"Error: «{texto}» no es un número válido.")
                return

            if valor < 0:
                self._error_label.setText(
                    f"Error: el valor de {clave} debe ser positivo."
                )
                return

            valores[clave] = valor

        vacios = [k for k, v in valores.items() if v is None]

        if len(vacios) == 0:
            self._error_label.setText("Deja vacío el campo que deseas calcular.")
            return

        if len(vacios) > 1:
            self._error_label.setText("Ingresa exactamente dos valores.")
            return

        try:
            resultado = calcular_ohm(
                voltaje=valores["V"],
                corriente=valores["I"],
                resistencia=valores["R"],
            )
        except ValueError as error:
            self._error_label.setText(str(error))
            return

        self._campos["V"].setText(str(round(resultado["voltaje"], 4)))
        self._campos["I"].setText(str(round(resultado["corriente"], 4)))
        self._campos["R"].setText(str(round(resultado["resistencia"], 4)))

        potencia = calcular_potencia(
            resultado["voltaje"],
            resultado["corriente"],
        )
        self._potencia_output.setText(str(round(potencia, 4)))

    def _limpiar(self) -> None:
        self._error_label.setText("")
        self._potencia_output.clear()

        for campo in self._campos.values():
            campo.clear()
