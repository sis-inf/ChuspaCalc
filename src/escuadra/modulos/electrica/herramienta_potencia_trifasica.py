"""
Herramienta de Potencia Trifásica para Escuadra.
Calcula la potencia activa, reactiva y aparente en sistemas trifásicos.
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
from escuadra.modulos.electrica.potencia_trifasica import calcular_potencia_trifasica


class HerramientaPotenciaTrifasica(Herramienta):
    nombre = "Potencia Trifásica"
    carrera = Carrera.ELECTRICA
    descripcion = (
        "Calcula la potencia activa, reactiva y aparente en sistemas trifásicos."
    )

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        root = QVBoxLayout()
        root.setSpacing(10)

        # Mensaje de ayuda
        ayuda = QLabel(
            "Ingresa el voltaje de línea, corriente de línea y factor de potencia "
            "para calcular las potencias trifásicas."
        )
        ayuda.setWordWrap(True)
        root.addWidget(ayuda)

        # Campos de entrada
        self._campos: dict[str, QLineEdit] = {}

        for etiqueta, clave, placeholder in [
            ("Voltaje de línea (V)", "voltaje", "Ej: 400"),
            ("Corriente de línea (A)", "corriente", "Ej: 10"),
            ("Factor de potencia", "factor_potencia", "0.0 - 1.0"),
        ]:
            fila = QHBoxLayout()
            label = QLabel(etiqueta)
            label.setFixedWidth(180)
            campo = QLineEdit()
            campo.setPlaceholderText(placeholder)
            fila.addWidget(label)
            fila.addWidget(campo)
            root.addLayout(fila)
            self._campos[clave] = campo

        # Selector de tipo de conexión
        fila_conexion = QHBoxLayout()
        label_conexion = QLabel("Tipo de conexión:")
        label_conexion.setFixedWidth(180)
        self._conexion_combo = QComboBox()
        self._conexion_combo.addItem("Estrella (Y)", "estrella")
        self._conexion_combo.addItem("Triángulo (Δ)", "triangulo")
        fila_conexion.addWidget(label_conexion)
        fila_conexion.addWidget(self._conexion_combo)
        root.addLayout(fila_conexion)

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
        self._resultados: dict[str, QLineEdit] = {}
        for etiqueta, clave in [
            ("Potencia Activa (W)", "potencia_activa"),
            ("Potencia Reactiva (VAR)", "potencia_reactiva"),
            ("Potencia Aparente (VA)", "potencia_aparente"),
        ]:
            fila = QHBoxLayout()
            label = QLabel(etiqueta)
            label.setFixedWidth(180)
            campo = QLineEdit()
            campo.setReadOnly(True)
            campo.setPlaceholderText("—")
            fila.addWidget(label)
            fila.addWidget(campo)
            root.addLayout(fila)
            self._resultados[clave] = campo

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
        for campo in self._resultados.values():
            campo.clear()

        # Leer valores
        valores: dict[str, float | None] = {}
        for clave in ("voltaje", "corriente", "factor_potencia"):
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

        # Obtener tipo de conexión
        conexion = self._conexion_combo.currentData()

        # Calcular potencias
        try:
            resultados = calcular_potencia_trifasica(
                voltaje_linea=valores["voltaje"],
                corriente_linea=valores["corriente"],
                factor_potencia=valores["factor_potencia"],
                conexion=conexion,
            )
        except ValueError as e:
            self._error_label.setText(str(e))
            return

        # Mostrar resultados
        self._resultados["potencia_activa"].setText(
            str(round(resultados["potencia_activa"], 4))
        )
        self._resultados["potencia_reactiva"].setText(
            str(round(resultados["potencia_reactiva"], 4))
        )
        self._resultados["potencia_aparente"].setText(
            str(round(resultados["potencia_aparente"], 4))
        )

    def _limpiar(self) -> None:
        self._error_label.setText("")
        for campo in self._campos.values():
            campo.clear()
        for campo in self._resultados.values():
            campo.clear()
        self._conexion_combo.setCurrentIndex(0)
