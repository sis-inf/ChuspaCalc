import ast
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

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

MAX_LONGITUD_EXPRESION = 256
MAX_NODOS_LOGICOS = 128
MAX_PROFUNDIDAD_LOGICA = 24


class _EvaluadorLogico:
    """Evalúa el AST lógico convertido sin ejecutar código Python."""

    def __init__(self, valores: dict[str, int]) -> None:
        self._valores = valores

    def evaluar(self, expresion: str) -> bool:
        arbol = ast.parse(expresion, mode="eval")
        if len(list(ast.walk(arbol))) > MAX_NODOS_LOGICOS:
            raise ErrorValidacion("La expresión lógica es demasiado compleja.")
        return self._evaluar_nodo(arbol.body, profundidad=1)

    def _evaluar_nodo(self, nodo: ast.AST, profundidad: int) -> bool:
        if profundidad > MAX_PROFUNDIDAD_LOGICA:
            raise ErrorValidacion("La expresión excede la profundidad permitida.")

        if isinstance(nodo, ast.Name):
            if nodo.id not in self._valores:
                raise ErrorValidacion(f"Variable no permitida: {nodo.id}")
            return bool(self._valores[nodo.id])

        if isinstance(nodo, ast.Constant):
            if isinstance(nodo.value, bool):
                return nodo.value
            if isinstance(nodo.value, int) and nodo.value in (0, 1):
                return bool(nodo.value)
            raise ErrorValidacion("Solo se permiten las constantes 0 y 1.")

        if isinstance(nodo, ast.UnaryOp) and isinstance(nodo.op, ast.Not):
            return not self._evaluar_nodo(nodo.operand, profundidad + 1)

        if isinstance(nodo, ast.BoolOp):
            valores = [
                self._evaluar_nodo(valor, profundidad + 1) for valor in nodo.values
            ]
            if isinstance(nodo.op, ast.And):
                return all(valores)
            if isinstance(nodo.op, ast.Or):
                return any(valores)

        if isinstance(nodo, ast.BinOp) and isinstance(nodo.op, ast.BitXor):
            izquierda = self._evaluar_nodo(nodo.left, profundidad + 1)
            derecha = self._evaluar_nodo(nodo.right, profundidad + 1)
            return izquierda != derecha

        raise ErrorValidacion(
            f"Construcción lógica no permitida: {type(nodo).__name__}"
        )


class HerramientaTablasVerdad(Herramienta):
    nombre = "Tablas de verdad"
    carrera = Carrera.SISTEMAS
    descripcion = (
        "Genera la tabla de verdad de una expresión booleana con hasta 4 variables."
    )

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout()

        help_text = QLabel(
            "Operadores soportados:\n"
            "AND (también &, *, ∧) | OR (también |, +, ∨) | "
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

    def generar_tabla_ui(self) -> None:
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
        except ErrorValidacion as e:
            self.error_label.setText(str(e))
            return
        except ValueError as e:
            self.error_label.setText(str(e))
            return
        except Exception as e:
            self.error_label.setText(f"Error al procesar la expresión: {e}")
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

    def generar_tabla(
        self, expresion: str
    ) -> tuple[list[str], list[list[int]], list[bool]]:
        if not isinstance(expresion, str):
            raise ErrorValidacion("La expresión debe ser una cadena de texto.")

        if not expresion.strip():
            raise ErrorValidacion("La expresión booleana no puede estar vacía.")
        if len(expresion) > MAX_LONGITUD_EXPRESION:
            raise ErrorValidacion("La expresión excede la longitud permitida.")

        if not re.fullmatch(r"[A-Z0-9()\s&|!~^+*∧∨¬]+", expresion):
            raise ErrorValidacion("La expresión contiene caracteres no permitidos.")

        # Solo se permiten los valores numéricos del dominio booleano.
        valores_numericos = re.findall(r"\d+", expresion)

        for valor in valores_numericos:
            if valor not in ("0", "1"):
                raise ErrorValidacion("Los valores numéricos deben ser 0 o 1.")

        # Excluir palabras reservadas al identificar las variables.
        expresion_sin_operadores = re.sub(
            r"\b(?:AND|OR|NOT|XOR)\b",
            " ",
            expresion,
        )

        variables_encontradas = re.findall(r"\b[A-Z]\b", expresion_sin_operadores)
        variables = sorted(set(variables_encontradas))

        if not variables:
            raise ErrorValidacion(
                "No se encontraron variables en la expresión "
                "(use letras mayúsculas A-Z)."
            )

        if len(variables) > 4:
            raise ErrorValidacion(
                f"Se encontraron {len(variables)} variables. "
                "Por favor, simplifique la expresión a "
                "4 variables o menos."
            )

        expresion_python = self.convertir_expresion(expresion)

        filas: list[list[int]] = []
        resultados: list[bool] = []

        for combinacion in itertools.product((0, 1), repeat=len(variables)):
            namespace = {var: valor for var, valor in zip(variables, combinacion)}

            try:
                resultado_booleano = _EvaluadorLogico(namespace).evaluar(
                    expresion_python
                )
            except SyntaxError as e:
                raise ErrorValidacion(f"Error al evaluar la expresión: {e}") from e

            filas.append(list(combinacion))
            resultados.append(resultado_booleano)

        return variables, filas, resultados

    def convertir_expresion(self, expresion: str) -> str:
        if not isinstance(expresion, str):
            raise ErrorValidacion("La expresión debe ser una cadena de texto.")

        if not expresion.strip():
            raise ErrorValidacion("La expresión no puede estar vacía.")

        # Reemplazar operadores escritos como palabras completas.
        expresion = re.sub(r"\bAND\b", " and ", expresion)
        expresion = re.sub(r"\bOR\b", " or ", expresion)
        expresion = re.sub(r"\bNOT\b", " not ", expresion)
        expresion = re.sub(r"\bXOR\b", " ^ ", expresion)

        # Reemplazar operadores simbólicos.
        expresion = expresion.replace("&", " and ")
        expresion = expresion.replace("|", " or ")
        expresion = expresion.replace("!", " not ")
        expresion = expresion.replace("~", " not ")
        expresion = expresion.replace("∧", " and ")
        expresion = expresion.replace("∨", " or ")
        expresion = expresion.replace("¬", " not ")

        expresion = expresion.replace("*", " and ")
        expresion = expresion.replace("+", " or ")

        return expresion.strip()

    def copiar_portapapeles(self) -> None:
        if self.result_table.rowCount() == 0:
            return

        tsv_content = ""

        for col in range(self.result_table.columnCount()):
            header = self.result_table.horizontalHeaderItem(col)
            tsv_content += header.text() if header else ""

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
