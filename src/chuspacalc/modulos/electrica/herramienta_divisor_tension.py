from PySide6.QtWidgets import (
    QComboBox,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta
from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
)


def calcular_vout(vin: float, r1: float, r2: float) -> float:
    """Calcula el voltaje de salida de un divisor de tensión.

    Args:
        vin: Voltaje de entrada en Volts.
        r1: Resistencia superior en Ohms (mayor que cero).
        r2: Resistencia inferior en Ohms (mayor que cero).

    Returns:
        Voltaje de salida en Volts.

    Raises:
        ErrorValidacion: Si algún valor no es un número real finito o si
            las resistencias no son positivas.
    """
    vin = validar_numero(vin, "vin")
    r1 = validar_numero(r1, "r1")
    r2 = validar_numero(r2, "r2")

    if r1 <= 0 or r2 <= 0:
        raise ErrorValidacion("Las resistencias deben ser positivas.")

    return vin * r2 / (r1 + r2)


def calcular_r2(vin: float, vout: float, r1: float) -> float:
    """Calcula la resistencia R2 necesaria para obtener un voltaje de salida.

    Args:
        vin: Voltaje de entrada en Volts (mayor que vout).
        vout: Voltaje de salida deseado en Volts.
        r1: Resistencia superior en Ohms (mayor que cero).

    Returns:
        Resistencia R2 en Ohms.

    Raises:
        ErrorValidacion: Si algún valor no es un número real finito, si R1
            no es positiva o si vin no es mayor que vout.
    """
    vin = validar_numero(vin, "vin")
    vout = validar_numero(vout, "vout")
    r1 = validar_numero(r1, "r1")

    if r1 <= 0:
        raise ErrorValidacion("R1 debe ser positiva.")

    if vin <= vout:
        raise ErrorValidacion("V_in debe ser mayor que V_out.")

    return (vout * r1) / (vin - vout)


def calcular_r1(vin: float, vout: float, r2: float) -> float:
    """Calcula la resistencia R1 necesaria para obtener un voltaje de salida.

    Args:
        vin: Voltaje de entrada en Volts.
        vout: Voltaje de salida deseado en Volts (mayor que cero y no mayor
            que vin).
        r2: Resistencia inferior en Ohms (mayor que cero).

    Returns:
        Resistencia R1 en Ohms.

    Raises:
        ErrorValidacion: Si algún valor no es un número real finito, si R2
            no es positiva, si vout no es mayor que cero o si vout es mayor
            que vin.
    """
    vin = validar_numero(vin, "vin")
    vout = validar_numero(vout, "vout")
    r2 = validar_numero(r2, "r2")

    if r2 <= 0:
        raise ErrorValidacion("R2 debe ser positiva.")

    if vout <= 0:
        raise ErrorValidacion("V_out debe ser mayor que cero.")

    if vout > vin:
        raise ErrorValidacion("V_out no puede ser mayor que V_in.")

    return r2 * (vin - vout) / vout


class HerramientaDivisorTension(Herramienta):
    nombre = "Divisor de tensión"
    carrera = Carrera.ELECTRICA
    descripcion = (
        "Calcula el voltaje de salida o las resistencias "
        "necesarias en un divisor de tensión."
    )

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        self.modo = QComboBox()
        self.modo.addItems(
            [
                "Calcular V_out conociendo V_in, R1 y R2",
                "Calcular R2 conociendo V_in, V_out y R1",
                "Calcular R1 conociendo V_in, V_out y R2",
            ]
        )

        layout.addWidget(self.modo)

        esquema = QLabel("V_in ─[R1]─┬─[R2]─ GND\n" "           │\n" "          V_out")

        layout.addWidget(esquema)

        layout.addWidget(QLabel("V_in (V)"))
        self.vin = QLineEdit()
        layout.addWidget(self.vin)

        layout.addWidget(QLabel("V_out (V)"))
        self.vout = QLineEdit()
        layout.addWidget(self.vout)

        layout.addWidget(QLabel("R1 (Ω)"))
        self.r1 = QLineEdit()
        layout.addWidget(self.r1)

        layout.addWidget(QLabel("R2 (Ω)"))
        self.r2 = QLineEdit()
        layout.addWidget(self.r2)

        boton = QPushButton("Calcular")
        layout.addWidget(boton)

        self.modo.currentIndexChanged.connect(self.actualizar_modo)

        boton.clicked.connect(self.realizar_calculo)

        self.actualizar_modo()

        return widget

    def actualizar_modo(self) -> None:
        self.vin.setReadOnly(False)
        self.vout.setReadOnly(False)
        self.r1.setReadOnly(False)
        self.r2.setReadOnly(False)

        modo = self.modo.currentIndex()

        if modo == 0:
            self.vout.setReadOnly(True)

        elif modo == 1:
            self.r2.setReadOnly(True)

        else:
            self.r1.setReadOnly(True)

    def realizar_calculo(self) -> None:
        try:
            modo = self.modo.currentIndex()

            if modo == 0:
                vin = float(self.vin.text())
                r1 = float(self.r1.text())
                r2 = float(self.r2.text())

                resultado = calcular_vout(vin, r1, r2)

                self.vout.setText(f"{resultado:.2f}")

            elif modo == 1:
                vin = float(self.vin.text())
                vout = float(self.vout.text())
                r1 = float(self.r1.text())

                resultado = calcular_r2(vin, vout, r1)

                self.r2.setText(f"{resultado:.2f}")

            else:
                vin = float(self.vin.text())
                vout = float(self.vout.text())
                r2 = float(self.r2.text())

                resultado = calcular_r1(vin, vout, r2)

                self.r1.setText(f"{resultado:.2f}")

        except ValueError as error:
            QMessageBox.warning(None, "Error", str(error))
