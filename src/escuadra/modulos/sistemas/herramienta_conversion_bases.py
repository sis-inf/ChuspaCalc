"""
Herramienta de conversión de bases numéricas para Escuadra.
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

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta

# Logica de conversion


def convertir_desde_decimal(entero: int) -> dict[str, str]:
    """Convierte un entero a sus representaciones en las cuatro bases."""
    signo = "-" if entero < 0 else ""
    magnitud = abs(entero)
    return {
        "decimal": str(entero),
        "binario": signo + bin(magnitud)[2:],
        "octal": signo + oct(magnitud)[2:],
        "hexadecimal": signo + hex(magnitud)[2:].upper(),
    }


def parsear_valor(texto: str, base: int) -> int:
    """Convierte texto en la base indicada a entero. Soporta negativos en decimal."""
    texto = texto.strip()
    if base == 10:
        return int(texto)  # acepta signo '-'
    negativo = texto.startswith("-")
    magnitud = texto.lstrip("-")
    valor = int(magnitud, base)
    return -valor if negativo else valor


# Widget
class HerramientaConversionBases(Herramienta):
    nombre = "Conversión de bases"
    carrera = Carrera.SISTEMAS
    descripcion = "Convierte un número entre decimal, binario, octal y hexadecimal."

    # Configuración de cada campo: etiqueta, base, placeholder
    _CAMPOS = [
        ("Decimal", 10, "Ej: 255"),
        ("Binario", 2, "Ej: 11111111"),
        ("Octal", 8, "Ej: 377"),
        ("Hexadecimal", 16, "Ej: FF"),
    ]

    def crear_widget(self) -> QWidget:
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
        except ValueError:
            self._error_label.setText(f"Valor inválido para base {base}: «{texto}»")
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
