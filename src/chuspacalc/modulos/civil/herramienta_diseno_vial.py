"""
Herramienta de Diseño Vial para ChuspaCalc.
"""

import math
from numbers import Real

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
from chuspacalc.modulos.civil.diseno_vial import (
    ErrorDisenoVial,
    calcular_pendiente,
    calcular_peralte_curva,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def _validar_numero(valor: object, nombre: str) -> float:
    """
    Valida que un parámetro sea numérico y finito.

    Args:
        valor: Valor que se desea validar.
        nombre: Nombre del parámetro para el mensaje de error.

    Returns:
        Valor numérico convertido a float.

    Raises:
        ErrorValidacion: Si el valor no es numérico o no es finito.
    """
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(
            f"{nombre} debe ser un número, " f"se recibió {type(valor).__name__}"
        )

    try:
        numero = float(valor)
    except OverflowError:
        raise ErrorValidacion(f"{nombre} es demasiado grande para procesarse") from None

    if not math.isfinite(numero):
        raise ErrorValidacion(f"{nombre} debe ser un número finito")

    return numero


def _validar_dominio(
    distancia_horizontal: float,
    velocidad_diseno: float,
    radio_curva: float,
    friccion_lateral: float,
) -> None:
    """
    Valida los límites físicos de los parámetros de diseño vial.

    Raises:
        ErrorValidacion: Si un parámetro está fuera de su dominio.
    """
    if distancia_horizontal <= 0:
        raise ErrorValidacion("La distancia horizontal debe ser mayor que 0")

    if velocidad_diseno <= 0:
        raise ErrorValidacion("La velocidad de diseño debe ser mayor que 0")

    if radio_curva <= 0:
        raise ErrorValidacion("El radio de curva debe ser mayor que 0")

    if friccion_lateral < 0:
        raise ErrorValidacion("La fricción lateral no puede ser negativa")

    if friccion_lateral >= 1:
        raise ErrorValidacion("La fricción lateral debe ser menor que 1")


def _validar_resultado(valor: float, nombre: str) -> float:
    """
    Comprueba que un resultado calculado sea finito.

    Raises:
        ErrorValidacion: Si el resultado es NaN o infinito.
    """
    if not math.isfinite(valor, bool) or not isinstance(valor, Real) or not math.isfinite(valor):
        raise ErrorValidacion(f"El resultado de {nombre} no es un número finito")

    return float(valor)

def _ejecutar_calculos(
    elevacion_inicial: float,
    elevacion_final: float,
    distancia_horizontal: float,
    velocidad_diseno: float,
    radio_curva: float,
    friccion_lateral: float,
) -> tuple[float, float]:
    """
    Ejecuta los cálculos de pendiente y peralte controlando desbordamientos
    y errores numéricos inesperados.

    Raises:
        ErrorDisenoVial: Si el módulo de diseño vial reporta un error propio.
        ErrorValidacion: Si ocurre un desbordamiento, error numérico o
            resultado no finito.
    """
    try:
        pendiente = calcular_pendiente(
            elevacion_inicial, elevacion_final, distancia_horizontal
        )
    except ErrorDisenoVial:
        raise
    except OverflowError:
        raise ErrorValidacion(
            "Los valores ingresados provocan un desbordamiento numérico "
            "al calcular la pendiente"
        ) from None
    except (ArithmeticError, ValueError):
        raise ErrorValidacion(
            "Error numérico al calcular la pendiente con los valores ingresados"
        ) from None

    try:
        peralte = calcular_peralte_curva(
            velocidad_diseno, radio_curva, friccion_lateral
        )
    except ErrorDisenoVial:
        raise
    except OverflowError:
        raise ErrorValidacion(
            "Los valores ingresados provocan un desbordamiento numérico "
            "al calcular el peralte"
        ) from None
    except (ArithmeticError, ValueError):
        raise ErrorValidacion(
            "Error numérico al calcular el peralte con los valores ingresados"
        ) from None

    pendiente = _validar_resultado(pendiente, "la pendiente")
    peralte = _validar_resultado(peralte, "el peralte")

    return pendiente, peralte

class HerramientaDisenoVial(Herramienta):
    nombre = "Diseño Vial"
    carrera = Carrera.CIVIL
    descripcion = "Calcula pendiente y peralte de curva para diseño vial."

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        root = QVBoxLayout()
        root.setSpacing(10)

        ayuda = QLabel(
            "Ingresa datos de rasante y curva para calcular pendiente y peralte."
        )
        ayuda.setWordWrap(True)
        root.addWidget(ayuda)

        self._campos: dict[str, QLineEdit] = {}
        campos_configuracion: list[tuple[str, str, str]] = [
            ("Elevación inicial (m)", "elevacion_inicial", "Ej: 100"),
            ("Elevación final (m)", "elevacion_final", "Ej: 105"),
            ("Dist. horizontal (m)", "distancia_horizontal", "Ej: 200"),
            ("Vel. diseño (km/h)", "velocidad_diseno", "Ej: 60"),
            ("Radio curva (m)", "radio_curva", "Ej: 120"),
            ("Fricción lateral", "friccion_lateral", "Ej: 0.15"),
        ]
        for etiqueta, clave, placeholder in campos_configuracion:
            fila = QHBoxLayout()
            lab = QLabel(etiqueta)
            lab.setFixedWidth(180)
            campo = QLineEdit()
            campo.setPlaceholderText(placeholder)
            if clave == "friccion_lateral":
                campo.setText("0.15")
            fila.addWidget(lab)
            fila.addWidget(campo)
            root.addLayout(fila)
            self._campos[clave] = campo

        botones = QHBoxLayout()
        btn_calc = QPushButton("Calcular")
        btn_calc.clicked.connect(self._calcular)
        btn_lim = QPushButton("Limpiar")
        btn_lim.clicked.connect(self._limpiar)
        botones.addWidget(btn_calc)
        botones.addWidget(btn_lim)
        root.addLayout(botones)

        self._resultado = QLineEdit()
        self._resultado.setReadOnly(True)
        self._resultado.setPlaceholderText("—")
        root.addWidget(self._resultado)

        self._error = QLabel("")
        self._error.setStyleSheet("color: red;")
        self._error.setWordWrap(True)
        root.addWidget(self._error)

        root.addStretch()
        widget.setLayout(root)
        return widget

    def _calcular(self) -> None:
        """Valida los datos ingresados y presenta los cálculos."""
        self._error.setText("")
        self._resultado.clear()
        try:
            valores: dict[str, float] = {}
            for clave, campo in self._campos.items():
                texto = campo.text().strip()
                if clave == "friccion_lateral" and not texto:
                    valores[clave] = 0.15
                    continue
                if not texto:
                    raise ErrorValidacion(f"El campo '{clave}' es obligatorio")

                try:
                    valor = float(texto)
                except (ValueError, OverflowError):
                    raise ErrorValidacion(
                        f"El campo '{clave}' debe contener un número válido"
                    ) from None
                valores[clave] = _validar_numero(valor, clave)

            _validar_dominio(
                valores["distancia_horizontal"],
                valores["velocidad_diseno"],
                valores["radio_curva"],
                valores["friccion_lateral"],
            )

            pendiente, peralte = _ejecutar_calculos(
                valores["elevacion_inicial"],
                valores["elevacion_final"],
                valores["distancia_horizontal"],
                valores["velocidad_diseno"],
                valores["radio_curva"],
                valores["friccion_lateral"],
            )

            self._resultado.setText(
                f"PENDIENTE: {pendiente:.2f}% | PERALTE: {peralte:.4f}"
            )
        except (ErrorValidacion, ErrorDisenoVial) as e:
            self._error.setText(f"Error: {e}")

    def _limpiar(self) -> None:
        self._error.setText("")
        self._resultado.clear()
        for c in self._campos.values():
            c.clear()

        self._campos["friccion_lateral"].setText("0.15")


def herramienta_diseno_vial(
    elevacion_inicial: float,
    elevacion_final: float,
    distancia_horizontal: float,
    velocidad_diseno: float,
    radio_curva: float,
    friccion_lateral: float = 0.15,
) -> str:
    """
    Calcula la pendiente y el peralte de una curva vial.

    Args:
        elevacion_inicial: Elevación inicial en metros.
        elevacion_final: Elevación final en metros.
        distancia_horizontal: Distancia horizontal en metros.
        velocidad_diseno: Velocidad de diseño en km/h.
        radio_curva: Radio de la curva en metros.
        friccion_lateral: Coeficiente de fricción lateral (0 <= f < 1).

    Returns:
        Texto con los resultados de pendiente y peralte, o un mensaje con el
        formato ``"ERROR: ..."`` si ocurre ``ErrorDisenoVial``.

    Raises:
        ErrorValidacion: Si los parámetros son inválidos, están fuera del
            dominio permitido o provocan un desbordamiento numérico.
    """

    elevacion_inicial = _validar_numero(elevacion_inicial, "La elevación inicial")
    elevacion_final = _validar_numero(elevacion_final, "La elevación final")
    distancia_horizontal = _validar_numero(
        distancia_horizontal, "La distancia horizontal"
    )
    velocidad_diseno = _validar_numero(velocidad_diseno, "La velocidad de diseño")
    radio_curva = _validar_numero(radio_curva, "El radio de curva")
    friccion_lateral = _validar_numero(friccion_lateral, "La fricción lateral")
    _validar_dominio(
        elevacion_inicial,
        elevacion_final,
        distancia_horizontal,
        velocidad_diseno,
        radio_curva,
        friccion_lateral,
    )
    try:
        pendiente, peralte = _ejecutar_calculos(
            elevacion_inicial,
            elevacion_final,
            distancia_horizontal,
            velocidad_diseno,
            radio_curva,
            friccion_lateral,
        )
    except ErrorDisenoVial as e:
        return f"ERROR: {e}"

    return f"PENDIENTE: {pendiente:.2f}%\n" f"PERALTE: {peralte:.4f}"
