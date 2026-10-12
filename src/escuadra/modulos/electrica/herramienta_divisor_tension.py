from PySide6.QtWidgets import (
    QComboBox,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta


def calcular_vout(vin: float, r1: float, r2: float) -> float:
    if r1 <= 0 or r2 <= 0:
        raise ValueError("Las resistencias deben ser positivas.")

    return vin * r2 / (r1 + r2)


def calcular_r2(vin: float, vout: float, r1: float) -> float:
    if r1 <= 0:
        raise ValueError("R1 debe ser positiva.")

    if vin <= vout:
        raise ValueError("V_in debe ser mayor que V_out.")

    return (vout * r1) / (vin - vout)


def calcular_r1(vin: float, vout: float, r2: float) -> float:
    if r2 <= 0:
        raise ValueError("R2 debe ser positiva.")

    if vout <= 0:
        raise ValueError("V_out debe ser mayor que cero.")

    if vout > vin:
        raise ValueError("V_out no puede ser mayor que V_in.")

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

    def actualizar_modo(self):
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

    def realizar_calculo(self):
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
