import math
from numbers import Real
from typing import ClassVar

from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

UNIDADES_TEMPERATURA: frozenset[str] = frozenset({"°C", "°F", "K"})
CERO_ABSOLUTO_CELSIUS: float = -273.15
TOLERANCIA_CERO_ABSOLUTO: float = 1e-9


def _validar_valor(valor: float) -> float:
    """Valida que el valor sea un número real finito (sin booleanos)."""
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(f"El valor debe ser un número finito: {valor!r}")

    try:
        es_finito = math.isfinite(valor)
    except OverflowError as error:
        raise ErrorValidacion(
            "El valor debe ser un número finito: es demasiado grande"
        ) from error

    if not es_finito:
        raise ErrorValidacion(f"El valor debe ser un número finito: {valor}")

    return valor


def _validar_resultado(resultado: float) -> float:
    """Valida que el resultado de la conversión sea finito."""
    if not math.isfinite(resultado):
        raise ErrorValidacion(
            f"El resultado de la conversión no es finito: {resultado}"
        )
    return resultado


def _validar_unidad(unidad: str, nombre: str, permitidas: frozenset[str]) -> str:
    """Valida que la unidad sea texto y esté entre las unidades permitidas."""
    if not isinstance(unidad, str):
        raise ErrorValidacion(f"La unidad de {nombre} debe ser texto: {unidad!r}")

    if unidad not in permitidas:
        raise ErrorValidacion(f"Unidad de {nombre} inválida: {unidad!r}")

    return unidad


class HerramientaConversionUnidades(Herramienta):
    nombre = "Conversión de unidades"
    carrera = Carrera.MATEMATICAS
    descripcion = (
        "Convierte valores entre unidades de longitud, masa, tiempo y temperatura."
    )

    CATEGORIAS: ClassVar[dict[str, dict[str, float]]] = {
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

    def crear_widget(self) -> QWidget:
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

    def actualizar_unidades(self) -> None:
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

    def convertir_automatico(self) -> None:
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
        except ErrorValidacion as error:
            self.error_label.setText(f"Error en la conversión: {error}")

    def convertir_lineal(
        self, valor: float, de_unidad: str, a_unidad: str, categoria: str
    ) -> float:
        """
        Convierte un valor entre unidades de una categoría lineal.

        Raises:
            ErrorValidacion: Si el valor no es un número finito, si la categoría
                o las unidades no son válidas, o si el resultado no es finito.
        """
        _validar_valor(valor)

        if not isinstance(categoria, str) or categoria not in self.CATEGORIAS:
            raise ErrorValidacion(f"Categoría inválida: {categoria!r}")

        factores = self.CATEGORIAS[categoria]
        unidades = frozenset(factores)
        _validar_unidad(de_unidad, "origen", unidades)
        _validar_unidad(a_unidad, "destino", unidades)

        if factores[a_unidad] == 0:
            raise ErrorValidacion(f"El factor de la unidad destino es cero: {a_unidad}")

        valor_en_base = _validar_resultado(valor * factores[de_unidad])
        return _validar_resultado(valor_en_base / factores[a_unidad])

    def convertir_temperatura(
        self, valor: float, de_unidad: str, a_unidad: str
    ) -> float:
        """
        Convierte una temperatura entre °C, °F y K.

        Raises:
            ErrorValidacion: Si el valor no es un número finito, si las unidades
                no son válidas, si la temperatura está bajo el cero absoluto o
                si el resultado no es finito.
        """
        _validar_valor(valor)
        _validar_unidad(de_unidad, "origen", UNIDADES_TEMPERATURA)
        _validar_unidad(a_unidad, "destino", UNIDADES_TEMPERATURA)

        celsius = valor

        if de_unidad == "°F":
            celsius = (valor - 32) * 5 / 9
        elif de_unidad == "K":
            celsius = valor - 273.15

        _validar_resultado(celsius)

        if celsius < CERO_ABSOLUTO_CELSIUS - TOLERANCIA_CERO_ABSOLUTO:
            raise ErrorValidacion(
                "La temperatura no puede ser menor al cero absoluto: "
                f"{valor} {de_unidad}"
            )

        if a_unidad == "°F":
            return _validar_resultado(celsius * 9 / 5 + 32)
        if a_unidad == "K":
            return _validar_resultado(celsius + 273.15)

        return celsius
