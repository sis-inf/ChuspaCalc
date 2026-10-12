import itertools
import re

from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta


class HerramientaTablasVerdad(Herramienta):
    nombre = "Tablas de verdad"
    carrera = Carrera.SISTEMAS
    descripcion = (
        "Genera la tabla de verdad de una expresión booleana con hasta 4 variables."
    )

    def crear_widget(self):
        widget = QWidget()
        layout = QVBoxLayout()

        help_text = QLabel(
            "Operadores soportados:\n"
            "AND (también &, *, ∧) | OR (también |, +, ∨) |"
            "NOT (también !, ~, ¬) | XOR (también ^)\n"
            "Ejemplo: A AND (B OR C)"
        )
        layout.addWidget(help_text)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Ingrese la expresión booleana...")
        layout.addWidget(self.input_field)

        self.generate_button = QPushButton("Generar tabla")
        self.generate_button.clicked.connect(self.generar_tabla_ui)
        layout.addWidget(self.generate_button)

        self.result_table = QTableWidget()
        self.result_table.setColumnCount(0)
        self.result_table.setRowCount(0)
        layout.addWidget(self.result_table)

        self.copy_button = QPushButton("Copiar tabla al portapapeles")
        self.copy_button.clicked.connect(self.copiar_portapapeles)
        self.copy_button.setEnabled(False)
        layout.addWidget(self.copy_button)

        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")
        layout.addWidget(self.error_label)

        widget.setLayout(layout)
        return widget

    def generar_tabla_ui(self):
        expresion = self.input_field.text().strip()
        self.error_label.setText("")
        self.result_table.setRowCount(0)
        self.result_table.setColumnCount(0)
        self.copy_button.setEnabled(False)

        if not expresion:
            self.error_label.setText("Ingrese una expresión booleana.")
            return

        try:
            variables, filas, resultados = self.generar_tabla(expresion)
        except ValueError as e:
            self.error_label.setText(str(e))
            return
        except Exception as e:
            self.error_label.setText(f"Error al procesar la expresión: {str(e)}")
            return

        self.result_table.setColumnCount(len(variables) + 1)
        self.result_table.setRowCount(len(filas))

        headers = variables + ["Resultado"]
        self.result_table.setHorizontalHeaderLabels(headers)

        for row_idx, (fila, resultado) in enumerate(zip(filas, resultados)):
            for col_idx, valor in enumerate(fila):
                item = QTableWidgetItem(str(valor))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.result_table.setItem(row_idx, col_idx, item)

            result_item = QTableWidgetItem(str(int(resultado)))
            result_item.setFlags(result_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.result_table.setItem(row_idx, len(variables), result_item)

        self.copy_button.setEnabled(True)

    def generar_tabla(self, expresion):
        expresion = expresion.replace(" ", "")

        if not re.match(r"^[A-Z0-9\(\)\&\|\!\~\^\+\*∧∨¬]+$", expresion):
            raise ValueError("Expresión contiene caracteres no permitidos.")

        variables_encontradas = re.findall(r"\b[A-Z]\b", expresion)
        variables = sorted(set(variables_encontradas))

        if len(variables) == 0:
            raise ValueError(
                "No se encontraron variables en la expresión"
                "(use letras mayúsculas A-Z)."
            )

        if len(variables) > 4:
            raise ValueError(
                f"Se encontraron {len(variables)} variables."
                "Por favor, simplifique la expresión a 4 variables o menos."
            )

        expresion_python = self.convertir_expresion(expresion)

        filas = []
        resultados = []

        for combinacion in itertools.product([0, 1], repeat=len(variables)):
            namespace = {var: valor for var, valor in zip(variables, combinacion)}
            namespace["__builtins__"] = {}

            try:
                resultado = eval(expresion_python, namespace)
            except Exception as e:
                raise ValueError(f"Error al evaluar la expresión: {str(e)}")

            filas.append(list(combinacion))
            resultados.append(bool(resultado))

        return variables, filas, resultados

    def convertir_expresion(self, expresion):
        expresion = expresion.replace("AND", " and ")
        expresion = expresion.replace("OR", " or ")
        expresion = expresion.replace("NOT", " not ")
        expresion = expresion.replace("XOR", " ^ ")

        expresion = expresion.replace("&", " and ")
        expresion = expresion.replace("|", " or ")
        expresion = expresion.replace("~", " not ")
        expresion = expresion.replace("∧", " and ")
        expresion = expresion.replace("∨", " or ")
        expresion = expresion.replace("¬", " not ")

        expresion = expresion.replace("*", " and ")
        expresion = expresion.replace("+", " or ")

        return expresion

    def copiar_portapapeles(self):
        if self.result_table.rowCount() == 0:
            return

        tsv_content = ""

        for col in range(self.result_table.columnCount()):
            header = self.result_table.horizontalHeaderItem(col).text()
            tsv_content += header
            if col < self.result_table.columnCount() - 1:
                tsv_content += "\t"
        tsv_content += "\n"

        for row in range(self.result_table.rowCount()):
            for col in range(self.result_table.columnCount()):
                item = self.result_table.item(row, col)
                tsv_content += item.text() if item else ""
                if col < self.result_table.columnCount() - 1:
                    tsv_content += "\t"
            tsv_content += "\n"

        clipboard = QGuiApplication.clipboard()
        clipboard.setText(tsv_content)

        QMessageBox.information(None, "Éxito", "Tabla copiada al portapapeles.")
