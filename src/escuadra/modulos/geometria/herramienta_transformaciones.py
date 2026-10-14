from PySide6.QtWidgets import (
    QComboBox,
    QDoubleSpinBox,
    QFormLayout,
    QLabel,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta
from escuadra.modulos.geometria.transformaciones import (
    escalar_punto,
    rotar_punto,
    trasladar_punto,
)


class HerramientaTransformaciones(Herramienta):
    nombre = "Transformaciones Geométricas"

    carrera = Carrera.GEOMETRIA

    descripcion = (
        "Permite rotar, trasladar y escalar puntos "
        "en el plano cartesiano."
    )

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        formulario = QFormLayout()

        self.entrada_x = QDoubleSpinBox()
        self.entrada_x.setRange(-1000000, 1000000)
        self.entrada_x.setDecimals(4)
        self.entrada_x.setValue(1.0)

        self.entrada_y = QDoubleSpinBox()
        self.entrada_y.setRange(-1000000, 1000000)
        self.entrada_y.setDecimals(4)
        self.entrada_y.setValue(1.0)

        formulario.addRow("Coordenada X:", self.entrada_x)
        formulario.addRow("Coordenada Y:", self.entrada_y)

        self.selector = QComboBox()
        self.selector.addItems(["Rotar", "Trasladar", "Escalar"])
        formulario.addRow("Transformación:", self.selector)

        layout.addLayout(formulario)

        self.parametros = QStackedWidget()

        # Parámetros exclusivos de la rotación.
        pagina_rotacion = QWidget()
        formulario_rotacion = QFormLayout(pagina_rotacion)

        self.angulo = QDoubleSpinBox()
        self.angulo.setRange(-360000, 360000)
        self.angulo.setDecimals(4)
        self.angulo.setValue(90.0)

        self.rotacion_centro_x = QDoubleSpinBox()
        self.rotacion_centro_x.setRange(-1000000, 1000000)
        self.rotacion_centro_x.setDecimals(4)

        self.rotacion_centro_y = QDoubleSpinBox()
        self.rotacion_centro_y.setRange(-1000000, 1000000)
        self.rotacion_centro_y.setDecimals(4)

        formulario_rotacion.addRow("Ángulo (grados):", self.angulo)
        formulario_rotacion.addRow(
            "Centro X:", self.rotacion_centro_x
        )
        formulario_rotacion.addRow(
            "Centro Y:", self.rotacion_centro_y
        )

        self.parametros.addWidget(pagina_rotacion)

        # Parámetros exclusivos de la traslación.
        pagina_traslacion = QWidget()
        formulario_traslacion = QFormLayout(pagina_traslacion)

        self.desplazamiento_x = QDoubleSpinBox()
        self.desplazamiento_x.setRange(-1000000, 1000000)
        self.desplazamiento_x.setDecimals(4)
        self.desplazamiento_x.setValue(1.0)

        self.desplazamiento_y = QDoubleSpinBox()
        self.desplazamiento_y.setRange(-1000000, 1000000)
        self.desplazamiento_y.setDecimals(4)
        self.desplazamiento_y.setValue(1.0)

        formulario_traslacion.addRow(
            "Desplazamiento X (dx):", self.desplazamiento_x
        )
        formulario_traslacion.addRow(
            "Desplazamiento Y (dy):", self.desplazamiento_y
        )

        self.parametros.addWidget(pagina_traslacion)

        # Parámetros exclusivos del escalado.
        pagina_escalado = QWidget()
        formulario_escalado = QFormLayout(pagina_escalado)

        self.factor_escala = QDoubleSpinBox()
        self.factor_escala.setRange(-1000000, 1000000)
        self.factor_escala.setDecimals(4)
        self.factor_escala.setValue(2.0)

        self.escalado_centro_x = QDoubleSpinBox()
        self.escalado_centro_x.setRange(-1000000, 1000000)
        self.escalado_centro_x.setDecimals(4)

        self.escalado_centro_y = QDoubleSpinBox()
        self.escalado_centro_y.setRange(-1000000, 1000000)
        self.escalado_centro_y.setDecimals(4)

        formulario_escalado.addRow(
            "Factor de escala:", self.factor_escala
        )
        formulario_escalado.addRow(
            "Centro X:", self.escalado_centro_x
        )
        formulario_escalado.addRow(
            "Centro Y:", self.escalado_centro_y
        )

        self.parametros.addWidget(pagina_escalado)

        layout.addWidget(self.parametros)

        self.boton_aplicar = QPushButton("Aplicar transformación")
        layout.addWidget(self.boton_aplicar)

        self.resultado = QLabel("Resultado: pendiente")
        self.resultado.setWordWrap(True)
        layout.addWidget(self.resultado)

        self.selector.currentIndexChanged.connect(
            self.parametros.setCurrentIndex
        )
        self.boton_aplicar.clicked.connect(
            self.aplicar_transformacion
        )

        return widget

    def aplicar_transformacion(self) -> None:
        punto = (
            self.entrada_x.value(),
            self.entrada_y.value(),
        )

        indice = self.selector.currentIndex()

        if indice == 0:
            centro = (
                self.rotacion_centro_x.value(),
                self.rotacion_centro_y.value(),
            )

            resultado = rotar_punto(
                punto,
                self.angulo.value(),
                centro,
            )

        elif indice == 1:
            resultado = trasladar_punto(
                punto,
                self.desplazamiento_x.value(),
                self.desplazamiento_y.value(),
            )

        else:
            centro = (
                self.escalado_centro_x.value(),
                self.escalado_centro_y.value(),
            )

            resultado = escalar_punto(
                punto,
                self.factor_escala.value(),
                centro,
            )

        self.resultado.setText(
            f"Resultado: X = {resultado[0]:.4f}, "
            f"Y = {resultado[1]:.4f}"
        )

