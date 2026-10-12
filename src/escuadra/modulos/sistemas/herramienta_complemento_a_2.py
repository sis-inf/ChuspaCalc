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
from escuadra.modulos.sistemas.complemento_a_2 import (
    complemento_a_decimal,
    decimal_a_complemento,
)


class HerramientaComplementoA2(Herramienta):
    nombre = "Complemento a 2"
    carrera = Carrera.SISTEMAS
    descripcion = (
        "Convierte entre decimal con signo y representación en complemento a 2."
    )

    def crear_widget(self):
        widget = QWidget()
        layout = QVBoxLayout()

        # Selector de bits
        bits_layout = QHBoxLayout()
        bits_layout.addWidget(QLabel("Bits:"))

        self.bits_combo = QComboBox()
        self.bits_combo.addItems(["4", "8", "16", "32"])

        bits_layout.addWidget(self.bits_combo)
        layout.addLayout(bits_layout)

        # Rango representable
        self.rango_label = QLabel("")
        layout.addWidget(self.rango_label)

        # Decimal -> Complemento a 2
        layout.addWidget(QLabel("Número decimal:"))

        self.decimal_input = QLineEdit()
        self.decimal_input.setPlaceholderText("Ejemplo: -5")
        layout.addWidget(self.decimal_input)

        self.btn_decimal = QPushButton("Decimal → Complemento a 2")
        self.btn_decimal.clicked.connect(self._convertir_decimal)
        layout.addWidget(self.btn_decimal)

        self.binario_output = QLineEdit()
        self.binario_output.setReadOnly(True)
        layout.addWidget(self.binario_output)

        # Complemento a 2 -> Decimal
        layout.addWidget(QLabel("Número binario:"))

        self.binario_input = QLineEdit()
        self.binario_input.setPlaceholderText("Ejemplo: 11111011")
        layout.addWidget(self.binario_input)

        self.btn_binario = QPushButton("Complemento a 2 → Decimal")
        self.btn_binario.clicked.connect(self._convertir_binario)
        layout.addWidget(self.btn_binario)

        self.decimal_output = QLineEdit()
        self.decimal_output.setReadOnly(True)
        layout.addWidget(self.decimal_output)

        # Errores
        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")
        layout.addWidget(self.error_label)

        self.bits_combo.currentTextChanged.connect(self._actualizar_rango)

        self._actualizar_rango()

        widget.setLayout(layout)
        return widget

    def _actualizar_rango(self):
        bits = int(self.bits_combo.currentText())

        minimo = -(2 ** (bits - 1))
        maximo = (2 ** (bits - 1)) - 1

        self.rango_label.setText(f"Rango con {bits} bits: {minimo} a {maximo}")

    def _convertir_decimal(self):
        self.error_label.setText("")

        try:
            numero = int(self.decimal_input.text())
            bits = int(self.bits_combo.currentText())

            resultado = decimal_a_complemento(numero, bits)

            self.binario_output.setText(resultado)

        except ValueError as e:
            self.error_label.setText(str(e))

    def _convertir_binario(self):
        self.error_label.setText("")

        try:
            binario = self.binario_input.text().strip()
            bits = int(self.bits_combo.currentText())

            resultado = complemento_a_decimal(binario, bits)

            self.decimal_output.setText(str(resultado))

        except ValueError as e:
            self.error_label.setText(str(e))
