"""
Herramienta de resolución de sistemas de ecuaciones lineales para ChuspaCalc.
Resuelve sistemas A·x = b usando eliminación gaussiana con pivoteo parcial.
"""

import math

from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta
from chuspacalc.math.sistemas_lineales_nxn import resolver_sistema
from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
)


def _leer_numero(texto: str, nombre: str) -> float:
    """Convierte el texto de un campo en un número real finito.

    Args:
        texto: Contenido escrito por el usuario en el campo.
        nombre: Nombre de la celda (por ejemplo ``A[1][2]``) para el mensaje.

    Returns:
        El valor numérico como float.

    Raises:
        ErrorValidacion: Si el texto no es un número, o si es NaN o infinito.
    """
    try:
        valor = float(texto.strip())
    except ValueError:
        raise ErrorValidacion(f"valor inválido en {nombre}: «{texto}»") from None
    # validar_numero rechaza NaN e infinitos (por ejemplo "nan" o "inf").
    return validar_numero(valor, nombre)


# ── Widget ───────────────────────────────────────────────────────────────────


class HerramientaSistemasLineales(Herramienta):
    nombre = "Sistemas de ecuaciones lineales"
    carrera = Carrera.MATEMATICAS
    descripcion = "Resuelve sistemas A·x = b para tamaños entre 2x2 y 5x5."

    def crear_widget(self) -> QWidget:
        self._widget = QWidget()
        root = QVBoxLayout()
        root.setSpacing(10)

        # ── Selector de tamaño ───────────────────────────────────────────
        fila_size = QHBoxLayout()
        fila_size.addWidget(QLabel("Tamaño del sistema:"))
        self._spinbox = QSpinBox()
        self._spinbox.setMinimum(2)
        self._spinbox.setMaximum(5)
        self._spinbox.setValue(2)
        self._spinbox.valueChanged.connect(self._reconstruir_grilla)
        fila_size.addWidget(self._spinbox)
        fila_size.addStretch()
        root.addLayout(fila_size)

        # ── Contenedor de la grilla ──────────────────────────────────────
        self._grilla_container = QVBoxLayout()
        root.addLayout(self._grilla_container)

        # ── Botones ──────────────────────────────────────────────────────
        botones = QHBoxLayout()
        btn_resolver = QPushButton("Resolver")
        btn_resolver.clicked.connect(self._resolver)
        btn_limpiar = QPushButton("Limpiar")
        btn_limpiar.clicked.connect(self._limpiar)
        botones.addWidget(btn_resolver)
        botones.addWidget(btn_limpiar)
        root.addLayout(botones)

        # ── Resultado ────────────────────────────────────────────────────
        self._resultado_label = QLabel("")
        self._resultado_label.setWordWrap(True)
        root.addWidget(self._resultado_label)

        # ── Error ────────────────────────────────────────────────────────
        self._error_label = QLabel("")
        self._error_label.setStyleSheet("color: red;")
        self._error_label.setWordWrap(True)
        root.addWidget(self._error_label)

        root.addStretch()
        self._widget.setLayout(root)

        # Construir grilla inicial
        self._inputs_A: list[list[QLineEdit]] = []
        self._inputs_b: list[QLineEdit] = []
        self._reconstruir_grilla(2)

        return self._widget

    # ── Helpers ──────────────────────────────────────────────────────────────

    def _reconstruir_grilla(self, n: int) -> None:
        """Reconstruye la grilla de inputs conservando valores que aún encajan."""

        # Guardar valores anteriores
        valores_A = [
            [self._inputs_A[i][j].text() for j in range(len(self._inputs_A[i]))]
            for i in range(len(self._inputs_A))
        ]
        valores_b = [self._inputs_b[i].text() for i in range(len(self._inputs_b))]

        # Limpiar grilla anterior
        while self._grilla_container.count():
            item = self._grilla_container.takeAt(0)
            if item is None:
                continue
            widget = item.widget()
            layout = item.layout()
            if widget is not None:
                widget.deleteLater()
            elif layout is not None:
                self._limpiar_layout(layout)

        # Crear nueva grilla
        grilla = QGridLayout()
        grilla.setSpacing(6)

        # Encabezados
        for j in range(n):
            grilla.addWidget(QLabel(f"x{j+1}"), 0, j + 1)
        grilla.addWidget(QLabel("b"), 0, n + 2)

        self._inputs_A = []
        self._inputs_b = []

        for i in range(n):
            grilla.addWidget(QLabel(f"Ec {i+1}:"), i + 1, 0)
            fila_inputs: list[QLineEdit] = []
            for j in range(n):
                campo = QLineEdit()
                campo.setPlaceholderText("0")
                campo.setFixedWidth(60)
                # Restaurar valor si existía
                if i < len(valores_A) and j < len(valores_A[i]):
                    campo.setText(valores_A[i][j])
                grilla.addWidget(campo, i + 1, j + 1)
                fila_inputs.append(campo)
            self._inputs_A.append(fila_inputs)

            # Separador visual entre A y b
            grilla.addWidget(QLabel("|"), i + 1, n + 1)

            # Campo b
            campo_b = QLineEdit()
            campo_b.setPlaceholderText("0")
            campo_b.setFixedWidth(60)
            if i < len(valores_b):
                campo_b.setText(valores_b[i])
            grilla.addWidget(campo_b, i + 1, n + 2)
            self._inputs_b.append(campo_b)

        contenedor = QWidget()
        contenedor.setLayout(grilla)
        self._grilla_container.addWidget(contenedor)

    def _limpiar_layout(self, layout: QLayout) -> None:
        """Elimina todos los widgets de un layout."""
        while layout.count():
            item = layout.takeAt(0)
            if item is None:
                continue
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def _resolver(self) -> None:
        """Lee los campos, valida los datos y muestra la solución del sistema.

        Cualquier error de validación o de cálculo se muestra en la etiqueta
        de error en lugar de interrumpir la aplicación.
        """
        self._error_label.setText("")
        self._resultado_label.setText("")
        n = self._spinbox.value()

        try:
            # Leer y validar la matriz A
            A: list[list[float]] = [
                [
                    _leer_numero(self._inputs_A[i][j].text(), f"A[{i+1}][{j+1}]")
                    for j in range(n)
                ]
                for i in range(n)
            ]

            # Leer y validar el vector b
            b: list[float] = [
                _leer_numero(self._inputs_b[i].text(), f"b[{i+1}]") for i in range(n)
            ]

            # Resolver
            solucion = resolver_sistema(A, b)
        except ValueError as error:
            # Incluye ErrorValidacion, que hereda de ValueError.
            self._error_label.setText(f"Error: {error}")
            return
        except Exception as error:
            # Captura segura: cualquier otro fallo se informa en la interfaz.
            self._error_label.setText(
                f"Error inesperado al resolver el sistema: {error}"
            )
            return

        if solucion is None:
            self._error_label.setText(
                "El sistema no tiene solución única (matriz singular)."
            )
            return

        # Una solución con NaN o infinitos no es presentable.
        if not all(math.isfinite(v) for v in solucion):
            self._error_label.setText(
                "La solución está fuera del rango numérico representable."
            )
            return

        lineas = [f"x{i+1} = {round(v, 6)}" for i, v in enumerate(solucion)]
        self._resultado_label.setText("Solución:\n" + "\n".join(lineas))

    def _limpiar(self) -> None:
        """Borra los campos, el resultado y los mensajes de error."""
        self._error_label.setText("")
        self._resultado_label.setText("")
        for fila in self._inputs_A:
            for campo in fila:
                campo.clear()
        for campo in self._inputs_b:
            campo.clear()
