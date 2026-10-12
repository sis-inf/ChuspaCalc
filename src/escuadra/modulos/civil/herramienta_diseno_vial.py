"""
Herramienta de Diseño Vial para Escuadra.
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
from escuadra.modulos.civil.diseno_vial import (
    calcular_pendiente,
    calcular_peralte_curva,
    ErrorDisenoVial,
)


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

        self._campos = {}
        for etiqueta, clave, placeholder in [
            ("Elevación inicial (m)", "elevacion_inicial", "Ej: 100"),
            ("Elevación final (m)", "elevacion_final", "Ej: 105"),
            ("Dist. horizontal (m)", "distancia_horizontal", "Ej: 200"),
            ("Vel. diseño (km/h)", "velocidad_diseno", "Ej: 60"),
            ("Radio curva (m)", "radio_curva", "Ej: 120"),
            ("Fricción lateral", "friccion_lateral", "Ej: 0.15"),
        ]:
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

    def _calcular(self):
        self._error.setText("")
        self._resultado.clear()
        try:
            vals = {}
            for k in self._campos:
                if k == "friccion_lateral" and self._campos[k].text().strip() == "":
                    vals[k] = 0.15
                    continue
                vals[k] = float(self._campos[k].text().strip())

            pendiente = calcular_pendiente(
                vals["elevacion_inicial"],
                vals["elevacion_final"],
                vals["distancia_horizontal"],
            )
            peralte = calcular_peralte_curva(
                vals["velocidad_diseno"], vals["radio_curva"], vals["friccion_lateral"]
            )
            self._resultado.setText(
                f"PENDIENTE: {pendiente:.2f}% | PERALTE: {peralte:.4f}"
            )
        except ValueError as e:
            self._error.setText(f"Error: {e}")
        except ErrorDisenoVial as e:
            self._error.setText(f"ERROR: {str(e)}")
        except Exception as e:
            self._error.setText(f"Error: {e}")

    def _limpiar(self):
        self._error.setText("")
        self._resultado.clear()
        for c in self._campos.values():
            if c.placeholderText() != "Ej: 0.15":
                c.clear()


def herramienta_diseno_vial(
    elevacion_inicial: float,
    elevacion_final: float,
    distancia_horizontal: float,
    velocidad_diseno: float,
    radio_curva: float,
    friccion_lateral: float = 0.15,
) -> str:
    """
    Wrapper de herramienta para diseño vial
    """

    try:
        pendiente = calcular_pendiente(
            elevacion_inicial, elevacion_final, distancia_horizontal
        )

        peralte = calcular_peralte_curva(
            velocidad_diseno, radio_curva, friccion_lateral
        )

        return f"PENDIENTE: {pendiente:.2f}%\n" f"PERALTE: {peralte:.4f}"

    except ErrorDisenoVial as e:
        return f"ERROR: {str(e)}"
