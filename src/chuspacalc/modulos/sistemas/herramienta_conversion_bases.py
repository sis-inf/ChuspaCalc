"""
Herramienta de conversión de bases numéricas para ChuspaCalc.
Convierte entre decimal, binario, octal y hexadecimal.
"""

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.sistemas.conversor_bases import (
    BASES_SOPORTADAS,
    DIGITOS_POR_BASE,
)

# Logica de conversion


def convertir_desde_decimal(entero: int) -> dict[str, str]:
    """
    Convierte un entero a sus representaciones en las cuatro bases.

    Args:
        entero: Número entero, positivo, negativo o cero.

    Returns:
        Diccionario con las claves "decimal", "binario", "octal" y
        "hexadecimal".

    Raises:
        ErrorValidacion: Si entero no es un int (incluye bool, NaN e
            infinitos) o es demasiado grande para mostrarse en decimal.
    """
    if isinstance(entero, bool) or not isinstance(entero, int):
        raise ErrorValidacion("El valor a convertir debe ser un número entero.")

    try:
        decimal = str(entero)
    except ValueError as error:
        raise ErrorValidacion("El número es demasiado grande.") from error

    signo = "-" if entero < 0 else ""
    magnitud = abs(entero)
    return {
        "decimal": decimal,
        "binario": signo + bin(magnitud)[2:],
        "octal": signo + oct(magnitud)[2:],
        "hexadecimal": signo + hex(magnitud)[2:].upper(),
    }


def parsear_valor(texto: str, base: int) -> int:
    """
    Convierte un texto escrito en la base indicada a entero.

    Args:
        texto: Dígitos de la base, con un signo opcional al inicio.
        base: Base del texto (2, 8, 10 o 16).

    Returns:
        Valor entero.

    Raises:
        ErrorValidacion: Si la base no está soportada, el texto no es una
            cadena, está vacío, tiene caracteres inválidos o es demasiado
            largo.
    """
    if (
        isinstance(base, bool)
        or not isinstance(base, int)
        or base not in BASES_SOPORTADAS
    ):
        raise ErrorValidacion(f"Base no soportada: {base!r}")

    if not isinstance(texto, str):
        raise ErrorValidacion("El valor debe ser una cadena de texto.")

    texto = texto.strip()
    magnitud = texto[1:] if texto[:1] in ("+", "-") else texto

    if not magnitud:
        raise ErrorValidacion("Ingrese al menos un dígito.")

    if any(c not in DIGITOS_POR_BASE[base] for c in magnitud.upper()):
        raise ErrorValidacion(f"Valor inválido para base {base}: «{texto}»")

    try:
        return int(texto, base)
    except ValueError as error:
        raise ErrorValidacion("El número es demasiado grande.") from error


# Widget
class HerramientaConversionBases(Herramienta):
    """Interfaz para convertir números entre cuatro bases."""

    nombre: str = "Conversión de bases"
    carrera: Carrera | None = Carrera.SISTEMAS
    descripcion: str = (
        "Convierte un número entre decimal, binario, octal y hexadecimal."
    )

    # Configuración de cada campo: etiqueta, base, placeholder
    _CAMPOS: list[tuple[str, int, str]] = [
        ("Decimal", 10, "Ej: 255"),
        ("Binario", 2, "Ej: 11111111"),
        ("Octal", 8, "Ej: 377"),
        ("Hexadecimal", 16, "Ej: FF"),
    ]

    def crear_widget(self) -> QWidget:
        """
        Crea el widget con un campo por cada base.

        Returns:
            Widget principal de la herramienta.
        """
        widget = QWidget()
        root = QVBoxLayout()
        root.setSpacing(10)

        # Campos de entrada
        self._inputs: dict[int, QLineEdit] = {}  # base → QLineEdit

        for etiqueta, base, placeholder in self._CAMPOS:
            fila = QHBoxLayout()
            label = QLabel(f"{etiqueta}:")
            label.setFixedWidth(100)
            campo = QLineEdit()
            campo.setPlaceholderText(placeholder)
            campo.editingFinished.connect(lambda b=base: self._on_edicion(b))
            fila.addWidget(label)
            fila.addWidget(campo)
            root.addLayout(fila)
            self._inputs[base] = campo

        # Botones
        botones = QHBoxLayout()
        btn_convertir = QPushButton("Convertir")
        btn_convertir.clicked.connect(self._convertir_campo_activo)
        btn_limpiar = QPushButton("Limpiar")
        btn_limpiar.clicked.connect(self._limpiar)
        botones.addWidget(btn_convertir)
        botones.addWidget(btn_limpiar)
        root.addLayout(botones)

        # Error
        self._error_label = QLabel("")
        self._error_label.setStyleSheet("color: red;")
        root.addWidget(self._error_label)

        root.addStretch()
        widget.setLayout(root)

        # Guardamos que campo fue editado por ultima vez
        self._ultima_base: int | None = None
        for base, campo in self._inputs.items():
            campo.textEdited.connect(lambda _, b=base: self._marcar_activo(b))

        return widget

    # Slots

    def _marcar_activo(self, base: int) -> None:
        self._ultima_base = base

    def _on_edicion(self, base: int) -> None:
        self._ultima_base = base
        self._convertir_campo_activo()

    def _convertir_campo_activo(self) -> None:
        if self._ultima_base is None:
            return
        base = self._ultima_base
        texto = self._inputs[base].text().strip()

        if not texto:
            self._limpiar_silencioso(excepto=base)
            self._error_label.setText("")
            return

        try:
            entero = parsear_valor(texto, base)
            resultados = convertir_desde_decimal(entero)
        except ErrorValidacion as error:
            self._error_label.setText(str(error))
            return

        self._error_label.setText("")
        mapa = {10: "decimal", 2: "binario", 8: "octal", 16: "hexadecimal"}

        for b, campo in self._inputs.items():
            if b != base:
                campo.blockSignals(True)
                campo.setText(resultados[mapa[b]])
                campo.blockSignals(False)

    def _limpiar(self) -> None:
        self._error_label.setText("")
        self._ultima_base = None
        for campo in self._inputs.values():
            campo.blockSignals(True)
            campo.clear()
            campo.blockSignals(False)

    def _limpiar_silencioso(self, excepto: int) -> None:
        for base, campo in self._inputs.items():
            if base != excepto:
                campo.blockSignals(True)
                campo.clear()
                campo.blockSignals(False)
