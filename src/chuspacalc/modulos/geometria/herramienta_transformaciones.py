"""
Herramienta de transformaciones geométricas para ChuspaCalc.

Permite rotar, trasladar y escalar puntos en el plano cartesiano,
validando los parámetros de entrada y los resultados obtenidos.
"""

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

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta
from chuspacalc.modulos.geometria.transformaciones import (
    escalar_punto,
    rotar_punto,
    trasladar_punto,
)
from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
    validar_rango,
)

LIMITE_COORDENADAS: float = 1_000_000.0
LIMITE_ANGULO: float = 360_000.0


class HerramientaTransformaciones(Herramienta):
    """Interfaz gráfica para realizar transformaciones geométricas 2D."""

    nombre: str = "Transformaciones Geométricas"
    carrera: Carrera = Carrera.GEOMETRIA
    descripcion: str = (
        "Permite rotar, trasladar y escalar puntos en el plano cartesiano."
    )

    @staticmethod
    def _validar_valor(
        valor: object,
        nombre: str,
        minimo: float,
        maximo: float,
    ) -> float:
        """Valida un parámetro numérico y sus límites permitidos.

        Args:
            valor: Valor numérico que se desea validar.
            nombre: Nombre del parámetro para el mensaje de error.
            minimo: Límite inferior permitido.
            maximo: Límite superior permitido.

        Returns:
            El valor validado como float.

        Raises:
            ErrorValidacion: Si el valor no es numérico, no es finito
                o está fuera del rango permitido.
        """
        return validar_rango(
            valor,
            nombre,
            minimo=minimo,
            maximo=maximo,
        )

    def crear_widget(self) -> QWidget:
        """Construye la interfaz gráfica de las transformaciones.

        Returns:
            Widget principal con los campos de entrada y resultados.
        """
        widget = QWidget()
        layout = QVBoxLayout(widget)
        formulario = QFormLayout()

        self.entrada_x = QDoubleSpinBox()
        self.entrada_x.setRange(
            -LIMITE_COORDENADAS,
            LIMITE_COORDENADAS,
        )
        self.entrada_x.setDecimals(4)
        self.entrada_x.setValue(1.0)

        self.entrada_y = QDoubleSpinBox()
        self.entrada_y.setRange(
            -LIMITE_COORDENADAS,
            LIMITE_COORDENADAS,
        )
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
        self.angulo.setRange(-LIMITE_ANGULO, LIMITE_ANGULO)
        self.angulo.setDecimals(4)
        self.angulo.setValue(90.0)

        self.rotacion_centro_x = QDoubleSpinBox()
        self.rotacion_centro_x.setRange(
            -LIMITE_COORDENADAS,
            LIMITE_COORDENADAS,
        )
        self.rotacion_centro_x.setDecimals(4)

        self.rotacion_centro_y = QDoubleSpinBox()
        self.rotacion_centro_y.setRange(
            -LIMITE_COORDENADAS,
            LIMITE_COORDENADAS,
        )
        self.rotacion_centro_y.setDecimals(4)

        formulario_rotacion.addRow("Ángulo (grados):", self.angulo)
        formulario_rotacion.addRow("Centro X:", self.rotacion_centro_x)
        formulario_rotacion.addRow("Centro Y:", self.rotacion_centro_y)

        self.parametros.addWidget(pagina_rotacion)

        # Parámetros exclusivos de la traslación.
        pagina_traslacion = QWidget()
        formulario_traslacion = QFormLayout(pagina_traslacion)

        self.desplazamiento_x = QDoubleSpinBox()
        self.desplazamiento_x.setRange(
            -LIMITE_COORDENADAS,
            LIMITE_COORDENADAS,
        )
        self.desplazamiento_x.setDecimals(4)
        self.desplazamiento_x.setValue(1.0)

        self.desplazamiento_y = QDoubleSpinBox()
        self.desplazamiento_y.setRange(
            -LIMITE_COORDENADAS,
            LIMITE_COORDENADAS,
        )
        self.desplazamiento_y.setDecimals(4)
        self.desplazamiento_y.setValue(1.0)

        formulario_traslacion.addRow(
            "Desplazamiento X (dx):",
            self.desplazamiento_x,
        )
        formulario_traslacion.addRow(
            "Desplazamiento Y (dy):",
            self.desplazamiento_y,
        )

        self.parametros.addWidget(pagina_traslacion)

        # Parámetros exclusivos del escalado.
        pagina_escalado = QWidget()
        formulario_escalado = QFormLayout(pagina_escalado)

        self.factor_escala = QDoubleSpinBox()
        self.factor_escala.setRange(
            -LIMITE_COORDENADAS,
            LIMITE_COORDENADAS,
        )
        self.factor_escala.setDecimals(4)
        self.factor_escala.setValue(2.0)

        self.escalado_centro_x = QDoubleSpinBox()
        self.escalado_centro_x.setRange(
            -LIMITE_COORDENADAS,
            LIMITE_COORDENADAS,
        )
        self.escalado_centro_x.setDecimals(4)

        self.escalado_centro_y = QDoubleSpinBox()
        self.escalado_centro_y.setRange(
            -LIMITE_COORDENADAS,
            LIMITE_COORDENADAS,
        )
        self.escalado_centro_y.setDecimals(4)

        formulario_escalado.addRow(
            "Factor de escala:",
            self.factor_escala,
        )
        formulario_escalado.addRow(
            "Centro X:",
            self.escalado_centro_x,
        )
        formulario_escalado.addRow(
            "Centro Y:",
            self.escalado_centro_y,
        )

        self.parametros.addWidget(pagina_escalado)

        layout.addWidget(self.parametros)

        self.boton_aplicar = QPushButton("Aplicar transformación")
        layout.addWidget(self.boton_aplicar)

        self.resultado = QLabel("Resultado: pendiente")
        self.resultado.setWordWrap(True)
        layout.addWidget(self.resultado)

        self.selector.currentIndexChanged.connect(self.parametros.setCurrentIndex)
        self.boton_aplicar.clicked.connect(self.aplicar_transformacion)

        return widget

    def aplicar_transformacion(self) -> None:
        """Valida los parámetros y aplica la transformación seleccionada.

        Muestra el resultado cuando la operación es válida y un mensaje
        descriptivo cuando algún parámetro o resultado no es válido.

        Raises:
            ErrorValidacion: Los errores de validación se capturan y
                muestran en la interfaz gráfica.
        """
        try:
            # Validar las coordenadas del punto original.
            punto = (
                self._validar_valor(
                    self.entrada_x.value(),
                    "coordenada X",
                    -LIMITE_COORDENADAS,
                    LIMITE_COORDENADAS,
                ),
                self._validar_valor(
                    self.entrada_y.value(),
                    "coordenada Y",
                    -LIMITE_COORDENADAS,
                    LIMITE_COORDENADAS,
                ),
            )

            indice = self.selector.currentIndex()

            if indice == 0:
                # Validar los parámetros de rotación.
                angulo = self._validar_valor(
                    self.angulo.value(),
                    "ángulo",
                    -LIMITE_ANGULO,
                    LIMITE_ANGULO,
                )

                centro = (
                    self._validar_valor(
                        self.rotacion_centro_x.value(),
                        "centro X de rotación",
                        -LIMITE_COORDENADAS,
                        LIMITE_COORDENADAS,
                    ),
                    self._validar_valor(
                        self.rotacion_centro_y.value(),
                        "centro Y de rotación",
                        -LIMITE_COORDENADAS,
                        LIMITE_COORDENADAS,
                    ),
                )

                resultado = rotar_punto(
                    punto,
                    angulo,
                    centro,
                )

            elif indice == 1:
                # Validar los parámetros de traslación.
                desplazamiento_x = self._validar_valor(
                    self.desplazamiento_x.value(),
                    "desplazamiento X",
                    -LIMITE_COORDENADAS,
                    LIMITE_COORDENADAS,
                )

                desplazamiento_y = self._validar_valor(
                    self.desplazamiento_y.value(),
                    "desplazamiento Y",
                    -LIMITE_COORDENADAS,
                    LIMITE_COORDENADAS,
                )

                resultado = trasladar_punto(
                    punto,
                    desplazamiento_x,
                    desplazamiento_y,
                )

            elif indice == 2:
                # Validar los parámetros de escalado.
                factor = self._validar_valor(
                    self.factor_escala.value(),
                    "factor de escala",
                    -LIMITE_COORDENADAS,
                    LIMITE_COORDENADAS,
                )

                centro = (
                    self._validar_valor(
                        self.escalado_centro_x.value(),
                        "centro X de escalado",
                        -LIMITE_COORDENADAS,
                        LIMITE_COORDENADAS,
                    ),
                    self._validar_valor(
                        self.escalado_centro_y.value(),
                        "centro Y de escalado",
                        -LIMITE_COORDENADAS,
                        LIMITE_COORDENADAS,
                    ),
                )

                resultado = escalar_punto(
                    punto,
                    factor,
                    centro,
                )

            else:
                raise ErrorValidacion("Debe seleccionar una transformación válida.")

            # Comprobar que ambos resultados sean numéricos y finitos.
            resultado = (
                validar_numero(resultado[0], "resultado X"),
                validar_numero(resultado[1], "resultado Y"),
            )

        except ErrorValidacion as error:
            self.resultado.setText(f"Error: {error}")
            return

        self.resultado.setText(
            f"Resultado: X = {resultado[0]:.4f}, " f"Y = {resultado[1]:.4f}"
        )
