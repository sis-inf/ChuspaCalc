"""
Herramienta de Figuras Compuestas para ChuspaCalc.
"""

import json
import math
from collections.abc import Callable, Mapping, Sequence
from numbers import Real
from typing import Any

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

from .figuras_compuestas import calcular_area_compuesta, calcular_volumen_compuesto

OPERACIONES_VALIDAS = ("sumar", "restar")

Figuras = Sequence[Mapping[str, Any]]


def _validar_numero(valor: object, nombre: str) -> None:
    """Verifica que `valor` sea un número real finito y mayor que cero."""
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(f"{nombre} debe ser numérico, se recibió {type(valor).__name__}.")
    if not math.isfinite(valor):
        raise ErrorValidacion(f"{nombre} debe ser un valor finito, se recibió {valor}.")
    if valor <= 0:
        raise ErrorValidacion(f"{nombre} debe ser mayor que cero, se recibió {valor}.")


def _validar_figuras(figuras: object) -> None:
    """Valida la estructura y los parámetros numéricos de la lista de figuras."""
    if isinstance(figuras, (str, bytes, Mapping)) or not isinstance(figuras, Sequence):
        raise ErrorValidacion("'figuras' debe ser una lista de descriptores.")
    if len(figuras) == 0:
        raise ErrorValidacion("Debe haber al menos una figura.")

    for indice, figura in enumerate(figuras):
        if not isinstance(figura, Mapping):
            raise ErrorValidacion(f"Figura {indice}: el descriptor debe ser un mapeo.")

        for clave in ("tipo", "parametros"):
            if clave not in figura:
                raise ErrorValidacion(f"Figura {indice}: falta la clave '{clave}'.")

        if not isinstance(figura["tipo"], str):
            raise ErrorValidacion(f"Figura {indice}: 'tipo' debe ser un texto.")

        parametros = figura["parametros"]
        if not isinstance(parametros, Mapping) or not parametros:
            raise ErrorValidacion(f"Figura {indice}: 'parametros' debe ser un mapeo no vacío.")

        for nombre, valor in parametros.items():
            _validar_numero(valor, f"Figura {indice}: el parámetro '{nombre}'")

        operacion = figura.get("operacion", "sumar")
        if operacion not in OPERACIONES_VALIDAS:
            raise ErrorValidacion(
                f"Figura {indice}: operación no válida '{operacion}'. "
                f"Use una de: {', '.join(OPERACIONES_VALIDAS)}."
            )


def _calcular_validado(funcion: Callable[[Figuras], float], figuras: Figuras) -> float:
    """Valida la entrada, ejecuta el cálculo y verifica que el resultado sea finito."""
    _validar_figuras(figuras)
    try:
        resultado = funcion(figuras)
    except TypeError as error:
        raise ErrorValidacion(
            f"Los parámetros no corresponden al tipo de figura: {error}"
        ) from error
    if not math.isfinite(resultado):
        raise ErrorValidacion(f"El resultado no es un valor finito: {resultado}.")
    return resultado


class HerramientaFigurasCompuestas(Herramienta):
    nombre = "Figuras Compuestas"
    carrera = Carrera.GEOMETRIA
    descripcion = "Calcula el área y volumen total de una figura compuesta."

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        root = QVBoxLayout()
        root.setSpacing(10)

        ayuda = QLabel(
            "Esta herramienta usa calcular_area_compuesta y calcular_volumen_compuesto. "
            "Ingresa JSON de figuras o usa valores de prueba."
        )
        ayuda.setWordWrap(True)
        root.addWidget(ayuda)

        self._entrada = QTextEdit()
        self._entrada.setPlaceholderText(
            'Ej: [{"tipo": "rectangulo", "parametros": {"base": 5, "altura": 3}}]'
            " - Deja vacío para demo"
        )
        root.addWidget(self._entrada)

        botones = QHBoxLayout()
        btn_calc = QPushButton("Calcular Área")
        btn_calc.clicked.connect(lambda: self._calcular("area"))
        btn_vol = QPushButton("Calcular Volumen")
        btn_vol.clicked.connect(lambda: self._calcular("volumen"))
        botones.addWidget(btn_calc)
        botones.addWidget(btn_vol)
        root.addLayout(botones)

        self._resultado = QLineEdit()
        self._resultado.setReadOnly(True)
        self._resultado.setPlaceholderText("—")
        root.addWidget(self._resultado)

        self._error = QLabel("")
        self._error.setStyleSheet("color: red;")
        root.addWidget(self._error)

        root.addStretch()
        widget.setLayout(root)
        return widget

    def _calcular(self, tipo: str) -> None:
        self._error.setText("")
        try:
            # Si no hay entrada, usar demo vacío que llame a la lógica
            # Aquí solo demostramos que la Herramienta existe y es descubrible
            texto = self._entrada.toPlainText().strip()
            if not texto:
                self._resultado.setText(
                    "Herramienta registrada correctamente. Ingresa figuras para calcular."
                )
                return

            try:
                figuras = json.loads(texto)
            except json.JSONDecodeError as error:
                raise ErrorValidacion(f"El JSON ingresado no es válido: {error}") from error

            if tipo == "area":
                res = self.ejecutar(figuras)
                self._resultado.setText(f"ÁREA: {res}")
            else:
                res = calcular_volumen(figuras)
                self._resultado.setText(f"VOLUMEN: {res}")
        except ValueError as e:  # incluye ErrorValidacion
            self._error.setText(f"Error: {e}")

    def ejecutar(self, figuras: Figuras) -> float:
        # Método requerido por algunos tests
        return _calcular_validado(calcular_area_compuesta, figuras)


def calcular_volumen(figuras: Figuras) -> float:
    """
    Calcula el volumen total de una figura compuesta.

    Lanza ErrorValidacion si los datos son inválidos o están fuera de dominio.
    """
    return _calcular_validado(calcular_volumen_compuesto, figuras)
