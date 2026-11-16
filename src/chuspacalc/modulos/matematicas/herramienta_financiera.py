
"""
Herramienta de matemática financiera para ChuspaCalc.

Calcula valor futuro, valor presente e interés compuesto.
"""

import math

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta
from chuspacalc.modulos.matematicas.financiera import (
    calcular_interes_compuesto,
    calcular_valor_futuro,
    calcular_valor_presente,
)
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class HerramientaFinanciera(Herramienta):
    nombre = "Matemática financiera"
    carrera = Carrera.MATEMATICAS
    descripcion = (
        "Calcula valor futuro, valor presente "
        "e interés compuesto."
    )

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        root = QVBoxLayout()
        root.setSpacing(10)

        ayuda = QLabel(
            "Selecciona el cálculo, ingresa los valores "
            "solicitados y pulsa Calcular."
        )
        ayuda.setWordWrap(True)
        root.addWidget(ayuda)

        # Selector del tipo de cálculo.
        fila_tipo = QHBoxLayout()
        fila_tipo.addWidget(QLabel("Tipo de cálculo:"))

        self._tipo_calculo = QComboBox()
        self._tipo_calculo.addItem("Valor futuro", "futuro")
        self._tipo_calculo.addItem("Valor presente", "presente")
        self._tipo_calculo.addItem("Interés compuesto", "interes")

        fila_tipo.addWidget(self._tipo_calculo)
        root.addLayout(fila_tipo)

        # Campos de entrada.
        self._campos: dict[str, QLineEdit] = {}
        self._etiquetas: dict[str, QLabel] = {}

        for clave in ("monto", "tasa", "periodos"):
            fila = QHBoxLayout()

            etiqueta = QLabel()
            etiqueta.setFixedWidth(180)

            campo = QLineEdit()
            campo.setPlaceholderText("Ingresa un valor")

            fila.addWidget(etiqueta)
            fila.addWidget(campo)
            root.addLayout(fila)

            self._etiquetas[clave] = etiqueta
            self._campos[clave] = campo

        # Botones.
        botones = QHBoxLayout()

        btn_calcular = QPushButton("Calcular")
        btn_calcular.clicked.connect(self._calcular)

        btn_limpiar = QPushButton("Limpiar")
        btn_limpiar.clicked.connect(self._limpiar)

        botones.addWidget(btn_calcular)
        botones.addWidget(btn_limpiar)
        root.addLayout(botones)

        # Resultado.
        fila_resultado = QHBoxLayout()
        fila_resultado.addWidget(QLabel("Resultado:"))

        self._resultado_output = QLineEdit()
        self._resultado_output.setReadOnly(True)
        self._resultado_output.setPlaceholderText("—")

        fila_resultado.addWidget(self._resultado_output)
        root.addLayout(fila_resultado)

        # Mensajes de error.
        self._error_label = QLabel("")
        self._error_label.setStyleSheet("color: red;")
        self._error_label.setWordWrap(True)
        root.addWidget(self._error_label)

        # Actualizar los campos según el cálculo seleccionado.
        self._tipo_calculo.currentIndexChanged.connect(
            self._actualizar_campos
        )
        self._actualizar_campos()

        root.addStretch()
        widget.setLayout(root)

        return widget

    def _actualizar_campos(self, indice: int = -1) -> None:
        """Actualiza las etiquetas según el cálculo seleccionado."""
        tipo = self._tipo_calculo.currentData()

        etiquetas = {
            "futuro": {
                "monto": "Valor presente (capital):",
                "tasa": "Tasa de interés decimal:",
                "periodos": "Número de períodos:",
            },
            "presente": {
                "monto": "Valor futuro:",
                "tasa": "Tasa de interés decimal:",
                "periodos": "Número de períodos:",
            },
            "interes": {
                "monto": "Capital inicial:",
                "tasa": "Tasa de interés decimal:",
                "periodos": "Número de períodos:",
            },
        }

        for clave, etiqueta in etiquetas[tipo].items():
            self._etiquetas[clave].setText(etiqueta)

        # Evitar mostrar un resultado de otro cálculo.
        self._resultado_output.clear()
        self._error_label.clear()

    def _calcular(self) -> None:
        """Valida las entradas y ejecuta el cálculo seleccionado."""
        self._error_label.clear()
        self._resultado_output.clear()

        valores: dict[str, float] = {}

        # Leer y validar el monto y la tasa.
        for clave in ("monto", "tasa"):
            texto = self._campos[clave].text().strip()

            if texto == "":
                self._error_label.setText(
                    f"Error: completa el campo "
                    f"«{self._etiquetas[clave].text()}»."
                )
                return

            try:
                valor = float(texto)
            except ValueError:
                self._error_label.setText(
                    f"Error: «{texto}» no es un número válido."
                )
                return

            if not math.isfinite(valor):
                self._error_label.setText(
                    "Error: ingresa valores numéricos finitos."
                )
                return

            valores[clave] = valor

        # El monto debe ser no negativo.
        if valores["monto"] < 0:
            self._error_label.setText(
                "Error: el capital o monto no puede ser negativo."
            )
            return

        # La tasa debe ser mayor que -1 para que las
        # fórmulas tengan un factor de capitalización válido.
        if valores["tasa"] <= -1:
            self._error_label.setText(
                "Error: la tasa debe ser mayor que -1."
            )
            return

        # Leer y validar el número entero de períodos.
        texto_periodos = self._campos["periodos"].text().strip()

        if texto_periodos == "":
            self._error_label.setText(
                "Error: ingresa el número de períodos."
            )
            return

        try:
            periodos = int(texto_periodos)
        except ValueError:
            self._error_label.setText(
                "Error: los períodos deben ser un número entero."
            )
            return

        if periodos < 0:
            self._error_label.setText(
                "Error: los períodos no pueden ser negativos."
            )
            return

        monto = valores["monto"]
        tasa = valores["tasa"]
        tipo = self._tipo_calculo.currentData()

        try:
            if tipo == "futuro":
                resultado = calcular_valor_futuro(
                    valor_presente=monto,
                    tasa=tasa,
                    periodos=periodos,
                )

            elif tipo == "presente":
                resultado = calcular_valor_presente(
                    valor_futuro=monto,
                    tasa=tasa,
                    periodos=periodos,
                )

            else:
                resultado = calcular_interes_compuesto(
                    capital=monto,
                    tasa=tasa,
                    periodos=periodos,
                )

            if not math.isfinite(resultado):
                self._error_label.setText(
                    "Error: el resultado no es un número finito."
                )
                return

        except (ValueError, ZeroDivisionError, OverflowError) as error:
            self._error_label.setText(
                f"Error al realizar el cálculo: {error}"
            )
            return

        self._resultado_output.setText(f"{resultado:.4f}")

    def _limpiar(self) -> None:
        """Limpia las entradas, el resultado y los errores."""
        for campo in self._campos.values():
            campo.clear()

        self._resultado_output.clear()
        self._error_label.clear()
