"""
Herramienta de conversión de unidades eléctricas para Escuadra.
Convierte entre unidades de potencia y energía.
"""

from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta

# Función pura de conversión


def convertir_unidad(
    valor: float, de_unidad: str, a_unidad: str, categoria: str
) -> float:
    """
    Convierte un valor entre unidades de la misma categoría.

    Args:
        valor: Valor numérico a convertir.
        de_unidad: Unidad de origen.
        a_unidad: Unidad de destino.
        categoria: Categoría de conversión ('Potencia' o 'Energía').

    Returns:
        Valor convertido a la unidad destino.

    Raises:
        ValueError: Si la categoría o alguna unidad no es reconocida.
    """
    factores: dict[str, dict[str, float]] = {
        "Potencia": {
            "W": 1,
            "kW": 1_000,
            "MW": 1_000_000,
            "HP": 745.7,
            "CV": 735.5,
        },
        "Energía": {
            "J": 1,
            "kJ": 1_000,
            "Wh": 3_600,
            "kWh": 3_600_000,
            "MJ": 1_000_000,
        },
    }

    if categoria not in factores:
        raise ValueError(f"Categoría no reconocida: {categoria}")

    tabla = factores[categoria]

    if de_unidad not in tabla:
        raise ValueError(f"Unidad origen no reconocida: {de_unidad}")

    if a_unidad not in tabla:
        raise ValueError(f"Unidad destino no reconocida: {a_unidad}")

    valor_base = valor * tabla[de_unidad]
    return valor_base / tabla[a_unidad]


# Widget


class HerramientaConversionElectrica(Herramienta):
    nombre = "Conversión de unidades eléctricas"
    carrera = Carrera.ELECTRICA
    descripcion = (
        "Convierte entre unidades de potencia (W, kW, HP)"
        "y unidades de energía (Wh, kWh, J)."
    )

    _UNIDADES: dict[str, list[str]] = {
        "Potencia": ["W", "kW", "MW", "HP", "CV"],
        "Energía": ["J", "kJ", "Wh", "kWh", "MJ"],
    }

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        root = QVBoxLayout()
        root.setSpacing(10)

        # Selector de categoría
        fila_cat = QHBoxLayout()
        fila_cat.addWidget(QLabel("Categoría:"))
        self._combo_categoria = QComboBox()
        self._combo_categoria.addItems(list(self._UNIDADES.keys()))
        self._combo_categoria.currentTextChanged.connect(self._actualizar_unidades)
        fila_cat.addWidget(self._combo_categoria)
        root.addLayout(fila_cat)

        # Selector de unidad origen
        fila_de = QHBoxLayout()
        fila_de.addWidget(QLabel("De unidad:"))
        self._combo_de = QComboBox()
        fila_de.addWidget(self._combo_de)
        root.addLayout(fila_de)

        # Selector de unidad destino
        fila_a = QHBoxLayout()
        fila_a.addWidget(QLabel("A unidad:"))
        self._combo_a = QComboBox()
        fila_a.addWidget(self._combo_a)
        root.addLayout(fila_a)

        # Campo de entrada
        fila_valor = QHBoxLayout()
        fila_valor.addWidget(QLabel("Valor:"))
        self._input_valor = QLineEdit()
        self._input_valor.setPlaceholderText("Ingrese el valor numérico")
        fila_valor.addWidget(self._input_valor)
        root.addLayout(fila_valor)

        # Botón convertir
        self._btn_convertir = QPushButton("Convertir")
        self._btn_convertir.clicked.connect(self._convertir)
        root.addWidget(self._btn_convertir)

        # Campo de resultado
        fila_resultado = QHBoxLayout()
        fila_resultado.addWidget(QLabel("Resultado:"))
        self._output_resultado = QLineEdit()
        self._output_resultado.setReadOnly(True)
        self._output_resultado.setPlaceholderText("—")
        fila_resultado.addWidget(self._output_resultado)
        root.addLayout(fila_resultado)

        # Error
        self._error_label = QLabel("")
        self._error_label.setStyleSheet("color: red;")
        root.addWidget(self._error_label)

        root.addStretch()
        widget.setLayout(root)

        self._actualizar_unidades()
        return widget

    def _actualizar_unidades(self) -> None:
        categoria = self._combo_categoria.currentText()
        unidades = self._UNIDADES.get(categoria, [])

        self._combo_de.blockSignals(True)
        self._combo_a.blockSignals(True)

        self._combo_de.clear()
        self._combo_a.clear()
        self._combo_de.addItems(unidades)
        self._combo_a.addItems(unidades)

        if len(unidades) > 1:
            self._combo_a.setCurrentIndex(1)

        self._combo_de.blockSignals(False)
        self._combo_a.blockSignals(False)

        self._output_resultado.clear()
        self._error_label.setText("")

    def _convertir(self) -> None:
        self._error_label.setText("")
        self._output_resultado.clear()

        texto = self._input_valor.text().strip()
        if not texto:
            self._error_label.setText("Error: ingrese un valor numérico.")
            return

        try:
            valor = float(texto)
        except ValueError:
            self._error_label.setText(f"Error: «{texto}» no es un número válido.")
            return

        categoria = self._combo_categoria.currentText()
        de_unidad = self._combo_de.currentText()
        a_unidad = self._combo_a.currentText()

        try:
            resultado = convertir_unidad(valor, de_unidad, a_unidad, categoria)
        except ValueError as e:
            self._error_label.setText(str(e))
            return

        self._output_resultado.setText(str(round(resultado, 6)))
