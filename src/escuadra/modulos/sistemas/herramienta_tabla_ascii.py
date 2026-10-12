"""
Herramienta de consulta de tabla ASCII para Escuadra.
Permite convertir caracteres a su codigo ASCII y viceversa,
y listar rangos de la tabla ASCII estándar (0-127).
"""

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta
from escuadra.modulos.sistemas.tabla_ascii import (
    ascii_a_caracter,
    caracter_a_ascii,
    listar_ascii_rango,
)


class HerramientaTablaAscii(Herramienta):
    nombre = "Tabla ASCII"
    carrera = Carrera.SISTEMAS
    descripcion = (
        "Convierte caracteres a código ASCII y lista rangos de la tabla estándar."
    )

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        root = QVBoxLayout()
        root.setSpacing(12)

        # --- Sección: carácter → ASCII ---
        root.addWidget(QLabel("<b>Carácter → ASCII</b>"))

        fila_char = QHBoxLayout()
        self._input_char = QLineEdit()
        self._input_char.setPlaceholderText("Ej: A")
        self._input_char.setMaxLength(1)

        btn_char = QPushButton("Convertir")
        btn_char.clicked.connect(self._convertir_char)

        fila_char.addWidget(QLabel("Carácter:"))
        fila_char.addWidget(self._input_char)
        fila_char.addWidget(btn_char)

        root.addLayout(fila_char)

        self._resultado_char = QLabel("")
        root.addWidget(self._resultado_char)

        # --- Sección: código → carácter ---
        root.addWidget(QLabel("<b>Código ASCII → Carácter</b>"))

        fila_codigo = QHBoxLayout()

        self._input_codigo = QLineEdit()
        self._input_codigo.setPlaceholderText("Ej: 65")

        btn_codigo = QPushButton("Convertir")
        btn_codigo.clicked.connect(self._convertir_codigo)

        fila_codigo.addWidget(QLabel("Código (0-127):"))
        fila_codigo.addWidget(self._input_codigo)
        fila_codigo.addWidget(btn_codigo)

        root.addLayout(fila_codigo)

        self._resultado_codigo = QLabel("")
        root.addWidget(self._resultado_codigo)

        # --- Sección: listar rango ---
        root.addWidget(QLabel("<b>Listar rango ASCII</b>"))

        fila_rango = QHBoxLayout()

        self._input_inicio = QLineEdit()
        self._input_inicio.setPlaceholderText("Inicio (0-127)")

        self._input_fin = QLineEdit()
        self._input_fin.setPlaceholderText("Fin (0-127)")

        btn_rango = QPushButton("Listar")
        btn_rango.clicked.connect(self._listar_rango)

        fila_rango.addWidget(QLabel("Desde:"))
        fila_rango.addWidget(self._input_inicio)
        fila_rango.addWidget(QLabel("Hasta:"))
        fila_rango.addWidget(self._input_fin)
        fila_rango.addWidget(btn_rango)

        root.addLayout(fila_rango)

        self._tabla = QTableWidget(0, 5)
        self._tabla.setHorizontalHeaderLabels(
            ["Carácter", "Decimal", "Hexadecimal", "Octal", "Binario"]
        )
        self._tabla.horizontalHeader().setStretchLastSection(True)
        self._tabla.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        root.addWidget(self._tabla)

        self._error_label = QLabel("")
        self._error_label.setStyleSheet("color: red;")
        root.addWidget(self._error_label)

        btn_limpiar = QPushButton("Limpiar todo")
        btn_limpiar.clicked.connect(self._limpiar)

        root.addWidget(btn_limpiar)

        root.addStretch()
        widget.setLayout(root)

        return widget

    def _convertir_char(self) -> None:
        self._error_label.setText("")

        # No se aplica strip() — el espacio (código 32) es un carácter
        # ASCII válido y debe poder consultarse.
        texto = self._input_char.text()

        try:
            resultado = caracter_a_ascii(texto)

            self._resultado_char.setText(
                f"Decimal: {resultado['decimal']}  "
                f"Hex: {resultado['hexadecimal']}  "
                f"Octal: {resultado['octal']}  "
                f"Binario: {resultado['binario']}"
            )

        except ValueError as error:
            self._error_label.setText(str(error))
            self._resultado_char.setText("")

    def _convertir_codigo(self) -> None:
        self._error_label.setText("")

        try:
            codigo = int(self._input_codigo.text().strip())
            resultado = ascii_a_caracter(codigo)

            self._resultado_codigo.setText(
                f"Carácter: '{resultado['caracter']}'  "
                f"Hex: {resultado['hexadecimal']}  "
                f"Octal: {resultado['octal']}  "
                f"Binario: {resultado['binario']}"
            )

        except ValueError as error:
            self._error_label.setText(str(error))
            self._resultado_codigo.setText("")

    def _listar_rango(self) -> None:
        self._error_label.setText("")
        self._tabla.setRowCount(0)

        try:
            inicio = int(self._input_inicio.text().strip())
            fin = int(self._input_fin.text().strip())

            entradas = listar_ascii_rango(inicio, fin)

            self._tabla.setRowCount(len(entradas))

            for fila, entrada in enumerate(entradas):
                self._tabla.setItem(
                    fila,
                    0,
                    QTableWidgetItem(entrada["caracter"]),
                )
                self._tabla.setItem(
                    fila,
                    1,
                    QTableWidgetItem(str(entrada["decimal"])),
                )
                self._tabla.setItem(
                    fila,
                    2,
                    QTableWidgetItem(entrada["hexadecimal"]),
                )
                self._tabla.setItem(
                    fila,
                    3,
                    QTableWidgetItem(entrada["octal"]),
                )
                self._tabla.setItem(
                    fila,
                    4,
                    QTableWidgetItem(entrada["binario"]),
                )

        except ValueError as error:
            self._error_label.setText(str(error))

    def _limpiar(self) -> None:
        self._error_label.setText("")

        self._input_char.clear()
        self._input_codigo.clear()
        self._input_inicio.clear()
        self._input_fin.clear()

        self._resultado_char.setText("")
        self._resultado_codigo.setText("")

        self._tabla.clearContents()
        self._tabla.setRowCount(0)
