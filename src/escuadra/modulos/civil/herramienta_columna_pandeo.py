"""
Herramienta de Carga Crítica de Euler para Escuadra.
Calcula la carga crítica de pandeo para columnas a compresión.
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
from escuadra.modulos.civil.columna_pandeo import calcular_carga_critica_euler


class HerramientaColumnaPandeo(Herramienta):
    nombre = "Carga Crítica de Euler"
    carrera = Carrera.CIVIL
    descripcion = "Calcula la carga crítica de pandeo para columnas a compresión."

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        root = QVBoxLayout()
        root.setSpacing(10)

        # Mensaje de ayuda
        ayuda = QLabel(
            "Ingresa el módulo de elasticidad, momento de inercia y longitud "
            "para calcular la carga crítica de pandeo de Euler."
        )
        ayuda.setWordWrap(True)
        root.addWidget(ayuda)

        # Campos de entrada
        self._campos: dict[str, QLineEdit] = {}

        for etiqueta, clave, placeholder in [
            ("Módulo de elasticidad (Pa)", "modulo_elasticidad", "Ej: 200e9"),
            ("Momento de inercia (m⁴)", "momento_inercia", "Ej: 8.33e-6"),
            ("Longitud (m)", "longitud", "Ej: 3.0"),
        ]:
            fila = QHBoxLayout()
            label = QLabel(etiqueta)
            label.setFixedWidth(200)
            campo = QLineEdit()
            campo.setPlaceholderText(placeholder)
            fila.addWidget(label)
            fila.addWidget(campo)
            root.addLayout(fila)
            self._campos[clave] = campo

        # Selector de condición de apoyo
        fila_condicion = QHBoxLayout()
        label_condicion = QLabel("Condición de apoyo:")
        label_condicion.setFixedWidth(200)
        self._condicion_combo = QComboBox()
        self._condicion_combo.addItem("Biarticulada (K=1.0)", "biarticulada")
        self._condicion_combo.addItem("Empotrada-Libre (K=2.0)", "empotrada-libre")
        self._condicion_combo.addItem(
            "Empotrada-Empotrada (K=0.5)", "empotrada-empotrada"
        )
        self._condicion_combo.addItem(
            "Empotrada-Articulada (K=0.7)", "empotrada-articulada"
        )
        fila_condicion.addWidget(label_condicion)
        fila_condicion.addWidget(self._condicion_combo)
        root.addLayout(fila_condicion)

        # Botones
        botones = QHBoxLayout()
        btn_calcular = QPushButton("Calcular")
        btn_calcular.clicked.connect(self._calcular)
        btn_limpiar = QPushButton("Limpiar")
        btn_limpiar.clicked.connect(self._limpiar)
        botones.addWidget(btn_calcular)
        botones.addWidget(btn_limpiar)
        root.addLayout(botones)

        # Resultados
        fila_resultado = QHBoxLayout()
        label_resultado = QLabel("Carga crítica (N):")
        label_resultado.setFixedWidth(200)
        self._carga_critica_output = QLineEdit()
        self._carga_critica_output.setReadOnly(True)
        self._carga_critica_output.setPlaceholderText("—")
        fila_resultado.addWidget(label_resultado)
        fila_resultado.addWidget(self._carga_critica_output)
        root.addLayout(fila_resultado)

        # Error
        self._error_label = QLabel("")
        self._error_label.setStyleSheet("color: red;")
        self._error_label.setWordWrap(True)
        root.addWidget(self._error_label)

        root.addStretch()
        widget.setLayout(root)
        return widget

    def _leer_campo(self, clave: str) -> float | None:
        texto = self._campos[clave].text().strip()
        if texto == "":
            return None
        return float(texto)

    def _calcular(self) -> None:
        self._error_label.setText("")
        self._carga_critica_output.clear()

        # Leer valores
        valores: dict[str, float | None] = {}
        for clave in ("modulo_elasticidad", "momento_inercia", "longitud"):
            texto = self._campos[clave].text().strip()
            if texto == "":
                self._error_label.setText(f"Error: el campo {clave} es obligatorio.")
                return
            try:
                v = float(texto)
                if v < 0:
                    self._error_label.setText(
                        f"Error: el valor de {clave} debe ser positivo."
                    )
                    return
                valores[clave] = v
            except ValueError:
                self._error_label.setText(f"Error: «{texto}» no es un número válido.")
                return

        # Obtener condición de apoyo
        condicion_apoyo = self._condicion_combo.currentData()

        # Calcular carga crítica
        try:
            carga_critica = calcular_carga_critica_euler(
                modulo_elasticidad=valores["modulo_elasticidad"],
                momento_inercia=valores["momento_inercia"],
                longitud=valores["longitud"],
                condicion_apoyo=condicion_apoyo,
            )
        except ValueError as e:
            self._error_label.setText(str(e))
            return

        # Mostrar resultado
        self._carga_critica_output.setText(f"{carga_critica:.4e}")

    def _limpiar(self) -> None:
        self._error_label.setText("")
        for campo in self._campos.values():
            campo.clear()
        self._carga_critica_output.clear()
        self._condicion_combo.setCurrentIndex(0)
