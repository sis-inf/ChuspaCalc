from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta
from escuadra.modulos.geometria.calculo_area import (
    area_circulo,
    area_rectangulo,
    area_trapecio,
    area_triangulo,
)

# Configuración de cada figura: nombre visible → (campos requeridos, función de cálculo)
_FIGURAS = {
    "Triángulo": {
        "campos": [("Base", "m"), ("Altura", "m")],
        "calcular": lambda v: area_triangulo(v[0], v[1]),
    },
    "Círculo": {
        "campos": [("Radio", "m")],
        "calcular": lambda v: area_circulo(v[0]),
    },
    "Rectángulo": {
        "campos": [("Base", "m"), ("Altura", "m")],
        "calcular": lambda v: area_rectangulo(v[0], v[1]),
    },
    "Trapecio": {
        "campos": [("Base mayor", "m"), ("Base menor", "m"), ("Altura", "m")],
        "calcular": lambda v: area_trapecio(v[0], v[1], v[2]),
    },
}

_MAX_CAMPOS = 3  # Número máximo de campos entre todas las figuras


class HerramientaCalculoArea(Herramienta):
    nombre = "Cálculo de áreas"
    carrera = Carrera.GEOMETRIA
    descripcion = (
        "Calcula el área de figuras geométricas básicas: "
        "triángulo, círculo, rectángulo y trapecio."
    )

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        root = QVBoxLayout()
        root.setSpacing(12)

        # ── Selector de figura ──────────────────────────────────────────────
        figura_layout = QHBoxLayout()
        figura_layout.addWidget(QLabel("Figura:"))
        self.figura_combo = QComboBox()
        self.figura_combo.addItems(list(_FIGURAS.keys()))
        self.figura_combo.currentTextChanged.connect(self._actualizar_campos)
        figura_layout.addWidget(self.figura_combo)
        root.addLayout(figura_layout)

        # ── Formulario dinámico de campos ───────────────────────────────────
        self.form_layout = QFormLayout()
        self.form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        self._labels: list[QLabel] = []
        self._inputs: list[QLineEdit] = []

        for _ in range(_MAX_CAMPOS):
            label = QLabel()
            campo = QLineEdit()
            campo.setPlaceholderText("Ingrese el valor")
            campo.textChanged.connect(self._limpiar_resultado)
            self.form_layout.addRow(label, campo)
            self._labels.append(label)
            self._inputs.append(campo)

        root.addLayout(self.form_layout)

        # ── Botón calcular ──────────────────────────────────────────────────
        self.btn_calcular = QPushButton("Calcular área")
        self.btn_calcular.clicked.connect(self._calcular)
        root.addWidget(self.btn_calcular)

        # ── Resultado ───────────────────────────────────────────────────────
        resultado_row = QHBoxLayout()
        resultado_row.addWidget(QLabel("Resultado:"))
        self.resultado_output = QLineEdit()
        self.resultado_output.setReadOnly(True)
        self.resultado_output.setPlaceholderText("—")
        resultado_row.addWidget(self.resultado_output)
        resultado_row.addWidget(QLabel("m²"))
        root.addLayout(resultado_row)

        # ── Etiqueta de error ───────────────────────────────────────────────
        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")
        root.addWidget(self.error_label)

        root.addStretch()
        widget.setLayout(root)
        self._actualizar_campos()
        return widget

    # ── Helpers internos ────────────────────────────────────────────────────

    def _actualizar_campos(self) -> None:
        """Muestra u oculta campos según la figura seleccionada."""
        figura = self.figura_combo.currentText()
        config = _FIGURAS[figura]["campos"]

        self.resultado_output.clear()
        self.error_label.setText("")

        for i, (label, campo) in enumerate(zip(self._labels, self._inputs)):
            if i < len(config):
                nombre_campo, unidad = config[i]
                label.setText(f"{nombre_campo} ({unidad}):")
                label.setVisible(True)
                campo.setVisible(True)
                campo.clear()
            else:
                label.setVisible(False)
                campo.setVisible(False)

    def _limpiar_resultado(self) -> None:
        self.resultado_output.clear()
        self.error_label.setText("")

    def _calcular(self) -> None:
        """Lee los campos, valida y muestra el resultado."""
        figura = self.figura_combo.currentText()
        config = _FIGURAS[figura]
        n_campos = len(config["campos"])

        valores: list[float] = []
        for i in range(n_campos):
            texto = self._inputs[i].text().strip()
            if not texto:
                self.error_label.setText(
                    f"Error: el campo «{config['campos'][i][0]}» está vacío."
                )
                return
            try:
                valor = float(texto)
            except ValueError:
                self.error_label.setText(f"Error: «{texto}» no es un número válido.")
                return
            valores.append(valor)

        try:
            resultado = config["calcular"](valores)
        except ValueError as exc:
            self.error_label.setText(str(exc))
            return
        except Exception as exc:
            QMessageBox.critical(None, "Error inesperado", str(exc))
            return

        self.error_label.setText("")
        self.resultado_output.setText(f"{resultado:.6f}")
