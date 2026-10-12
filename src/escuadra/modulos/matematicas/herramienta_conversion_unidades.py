from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta


class HerramientaConversionUnidades(Herramienta):
    nombre = "Conversión de unidades"
    carrera = Carrera.MATEMATICAS
    descripcion = (
        "Convierte valores entre unidades de longitud, masa, tiempo y temperatura."
    )

    CATEGORIAS = {
        "Longitud": {
            "m": 1.0,
            "km": 1000.0,
            "cm": 0.01,
            "mm": 0.001,
            "in": 0.0254,
            "ft": 0.3048,
            "mi": 1609.34,
        },
        "Masa": {"kg": 1.0, "g": 0.001, "lb": 0.453592, "oz": 0.0283495, "t": 1000.0},
        "Tiempo": {"s": 1.0, "min": 60.0, "h": 3600.0, "d": 86400.0},
    }

    def crear_widget(self):
        widget = QWidget()
        layout = QVBoxLayout()

        categoria_layout = QHBoxLayout()
        categoria_layout.addWidget(QLabel("Categoría:"))
        self.categoria_combo = QComboBox()
        self.categoria_combo.addItems(["Longitud", "Masa", "Tiempo", "Temperatura"])
        self.categoria_combo.currentTextChanged.connect(self.actualizar_unidades)
        categoria_layout.addWidget(self.categoria_combo)
        layout.addLayout(categoria_layout)

        de_layout = QHBoxLayout()
        de_layout.addWidget(QLabel("De unidad:"))
        self.de_unidad_combo = QComboBox()
        de_layout.addWidget(self.de_unidad_combo)
        layout.addLayout(de_layout)

        a_layout = QHBoxLayout()
        a_layout.addWidget(QLabel("A unidad:"))
        self.a_unidad_combo = QComboBox()
        a_layout.addWidget(self.a_unidad_combo)
        layout.addLayout(a_layout)

        valor_layout = QHBoxLayout()
        valor_layout.addWidget(QLabel("Valor:"))
        self.valor_input = QLineEdit()
        self.valor_input.setPlaceholderText("Ingrese el valor numérico")
        self.valor_input.textChanged.connect(self.convertir_automatico)
        valor_layout.addWidget(self.valor_input)
        layout.addLayout(valor_layout)

        resultado_layout = QHBoxLayout()
        resultado_layout.addWidget(QLabel("Resultado:"))
        self.resultado_output = QLineEdit()
        self.resultado_output.setReadOnly(True)
        resultado_layout.addWidget(self.resultado_output)
        layout.addLayout(resultado_layout)

        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")
        layout.addWidget(self.error_label)

        layout.addStretch()
        widget.setLayout(layout)
        self.actualizar_unidades()
        return widget

    def actualizar_unidades(self):
        categoria = self.categoria_combo.currentText()
        self.de_unidad_combo.clear()
        self.a_unidad_combo.clear()
        self.resultado_output.clear()
        self.error_label.setText("")

        if categoria in self.CATEGORIAS:
            unidades = list(self.CATEGORIAS[categoria].keys())
            self.de_unidad_combo.addItems(unidades)
            self.a_unidad_combo.addItems(unidades)
            if len(unidades) > 1:
                self.a_unidad_combo.setCurrentIndex(1)

    def convertir_automatico(self):
        self.error_label.setText("")
        self.resultado_output.clear()

        valor_texto = self.valor_input.text().strip()
        if not valor_texto:
            return

        try:
            valor = float(valor_texto)
        except ValueError:
            self.error_label.setText("Error: ingrese un valor numérico válido.")
            return

        categoria = self.categoria_combo.currentText()
        de_unidad = self.de_unidad_combo.currentText()
        a_unidad = self.a_unidad_combo.currentText()

        try:
            if categoria == "Temperatura":
                resultado = self.convertir_temperatura(valor, de_unidad, a_unidad)
            else:
                resultado = self.convertir_lineal(valor, de_unidad, a_unidad, categoria)

            self.resultado_output.setText(str(round(resultado, 10)))
        except Exception as e:
            self.error_label.setText(f"Error en la conversión: {str(e)}")

    def convertir_lineal(self, valor, de_unidad, a_unidad, categoria):
        factores = self.CATEGORIAS[categoria]
        valor_en_base = valor * factores[de_unidad]
        resultado = valor_en_base / factores[a_unidad]
        return resultado

    def convertir_temperatura(self, valor, de_unidad, a_unidad):
        celsius = valor

        if de_unidad == "°F":
            celsius = (valor - 32) * 5 / 9
        elif de_unidad == "K":
            celsius = valor - 273.15

        if a_unidad == "°C":
            return celsius
        elif a_unidad == "°F":
            return celsius * 9 / 5 + 32
        elif a_unidad == "K":
            return celsius + 273.15

        return celsius
