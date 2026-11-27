"""
Herramienta de Potencia Trifásica para ChuspaCalc.

Calcula la potencia activa, reactiva y aparente en sistemas trifásicos.
"""

from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta
from chuspacalc.modulos.electrica.potencia_trifasica import (
    calcular_potencia_trifasica,
)
from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
    validar_rango,
)


class HerramientaPotenciaTrifasica(Herramienta):
    nombre = "Potencia Trifásica"
    carrera = Carrera.ELECTRICA
    descripcion = (
        "Calcula la potencia activa, reactiva y aparente en sistemas trifásicos."
    )

    def crear_widget(self) -> QWidget:
        """Construye la interfaz gráfica de la herramienta.

        Returns:
            Widget principal con los campos de entrada y resultados.
        """
        widget = QWidget()
        root = QVBoxLayout()
        root.setSpacing(10)

        # Mensaje de ayuda
        ayuda = QLabel(
            "Ingresa el voltaje de línea, corriente de línea y factor de potencia "
            "para calcular las potencias trifásicas."
        )
        ayuda.setWordWrap(True)
        root.addWidget(ayuda)

        # Campos de entrada
        self._campos: dict[str, QLineEdit] = {}

        for etiqueta, clave, placeholder in [
            ("Voltaje de línea (V)", "voltaje", "Ej: 400"),
            ("Corriente de línea (A)", "corriente", "Ej: 10"),
            ("Factor de potencia", "factor_potencia", "0.0 - 1.0"),
        ]:
            fila = QHBoxLayout()
            label = QLabel(etiqueta)
            label.setFixedWidth(180)

            campo = QLineEdit()
            campo.setPlaceholderText(placeholder)

            fila.addWidget(label)
            fila.addWidget(campo)
            root.addLayout(fila)

            self._campos[clave] = campo

        # Selector del tipo de conexión
        fila_conexion = QHBoxLayout()
        label_conexion = QLabel("Tipo de conexión:")
        label_conexion.setFixedWidth(180)

        self._conexion_combo: QComboBox = QComboBox()
        self._conexion_combo.addItem("Estrella (Y)", "estrella")
        self._conexion_combo.addItem("Triángulo (Δ)", "triangulo")

        fila_conexion.addWidget(label_conexion)
        fila_conexion.addWidget(self._conexion_combo)
        root.addLayout(fila_conexion)

        # Botones
        botones = QHBoxLayout()

        btn_calcular = QPushButton("Calcular")
        btn_calcular.clicked.connect(self._calcular)

        btn_limpiar = QPushButton("Limpiar")
        btn_limpiar.clicked.connect(self._limpiar)

        botones.addWidget(btn_calcular)
        botones.addWidget(btn_limpiar)
        root.addLayout(botones)

        # Resultados
        self._resultados: dict[str, QLineEdit] = {}

        for etiqueta, clave in [
            ("Potencia Activa (W)", "potencia_activa"),
            ("Potencia Reactiva (VAR)", "potencia_reactiva"),
            ("Potencia Aparente (VA)", "potencia_aparente"),
        ]:
            fila = QHBoxLayout()
            label = QLabel(etiqueta)
            label.setFixedWidth(180)

            campo = QLineEdit()
            campo.setReadOnly(True)
            campo.setPlaceholderText("—")

            fila.addWidget(label)
            fila.addWidget(campo)
            root.addLayout(fila)

            self._resultados[clave] = campo

        # Mensajes de error
        self._error_label: QLabel = QLabel("")
        self._error_label.setStyleSheet("color: red;")
        self._error_label.setWordWrap(True)
        root.addWidget(self._error_label)

        root.addStretch()
        widget.setLayout(root)

        return widget

    def _leer_campo(self, clave: str) -> float:
        """Lee y valida un campo numérico de entrada.

        Args:
            clave: Identificador del campo que se desea leer.

        Returns:
            Valor numérico finito validado.

        Raises:
            ErrorValidacion: Si el campo está vacío, contiene texto
                inválido, no es finito o está fuera del dominio permitido.
        """
        texto = self._campos[clave].text().strip()

        if texto == "":
            raise ErrorValidacion(f"El campo {clave} es obligatorio.")

        try:
            valor = float(texto)
        except ValueError:
            raise ErrorValidacion(
                f"El valor «{texto}» de {clave} no es un número válido."
            ) from None

        valor = validar_numero(valor, clave)

        if clave in ("voltaje", "corriente"):
            if valor <= 0:
                raise ErrorValidacion(f"El valor de {clave} debe ser mayor que cero.")

        elif clave == "factor_potencia":
            valor = validar_rango(
                valor,
                clave,
                minimo=0.0,
                maximo=1.0,
            )

        else:
            raise ErrorValidacion(f"El campo {clave} no es reconocido.")

        return valor

    def _calcular(self) -> None:
        """Valida las entradas, calcula las potencias y muestra los resultados."""
        self._error_label.setText("")

        for campo in self._resultados.values():
            campo.clear()

        try:
            # Leer y validar los parámetros numéricos
            valores: dict[str, float] = {
                clave: self._leer_campo(clave)
                for clave in ("voltaje", "corriente", "factor_potencia")
            }

            # Validar el tipo de conexión
            conexion_seleccionada = self._conexion_combo.currentData()

            if not isinstance(
                conexion_seleccionada, str
            ) or conexion_seleccionada not in (
                "estrella",
                "triangulo",
            ):
                raise ErrorValidacion(
                    "El tipo de conexión debe ser 'estrella' o 'triangulo'."
                )

            conexion: str = conexion_seleccionada

            # Calcular las potencias trifásicas
            resultados = calcular_potencia_trifasica(
                voltaje_linea=valores["voltaje"],
                corriente_linea=valores["corriente"],
                factor_potencia=valores["factor_potencia"],
                conexion=conexion,
            )

            # Validar que los resultados sean números finitos
            resultados_validados: dict[str, float] = {
                clave: validar_numero(resultados[clave], clave)
                for clave in (
                    "potencia_activa",
                    "potencia_reactiva",
                    "potencia_aparente",
                )
            }

        except ErrorValidacion as error:
            self._error_label.setText(f"Error: {error}")
            return

        except ValueError as error:
            self._error_label.setText(f"Error: {error}")
            return

        # Mostrar resultados
        self._resultados["potencia_activa"].setText(
            str(round(resultados_validados["potencia_activa"], 4))
        )
        self._resultados["potencia_reactiva"].setText(
            str(round(resultados_validados["potencia_reactiva"], 4))
        )
        self._resultados["potencia_aparente"].setText(
            str(round(resultados_validados["potencia_aparente"], 4))
        )

    def _limpiar(self) -> None:
        """Limpia las entradas, los resultados y los mensajes de error."""
        self._error_label.setText("")

        for campo in self._campos.values():
            campo.clear()

        for campo in self._resultados.values():
            campo.clear()

        self._conexion_combo.setCurrentIndex(0)
