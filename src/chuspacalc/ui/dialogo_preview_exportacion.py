
import csv

from PySide6.QtGui import QFontDatabase, QGuiApplication
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
)

DELIMITADORES = ("\t", ";", ",")


class DialogoPreviewExportacion(QDialog):
    """
    Componente encargado de mostrar una vista previa del contenido
    en su formato destino antes de confirmar la exportación.
    """

    def __init__(self, formato: str, contenido: str, parent=None):
        super().__init__(parent)

        self.formato = formato
        self.contenido = contenido
        self.confirmado = False
        self._vista_cruda = False

        self.setWindowTitle(f"Vista previa de exportación [{formato.upper()}]")
        self.resize(640, 420)

        self._visor = QPlainTextEdit(self)
        self._visor.setReadOnly(True)
        self._visor.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self._visor.setFont(
            QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        )

        # Preparar la vista previa sin impedir que se abra el diálogo.
        try:
            self._texto_preliminar = self._generar_vista_preliminar(contenido)
        except (ValueError, csv.Error, TypeError) as error:
            self._texto_preliminar = contenido
            self._mostrar_error(
                "Error al generar la vista previa",
                f"No se pudo procesar el contenido. Se mostrará el texto original.\n{error}",
            )

        # Conectar las señales de los botones con sus respectivos slots.
        self._btn_alternar = QPushButton(self)
        self._btn_alternar.clicked.connect(self.alternar_vista)

        self._btn_copiar = QPushButton("Copiar", self)
        self._btn_copiar.clicked.connect(self.copiar_al_portapapeles)

        self._btn_confirmar = QPushButton("Confirmar exportación", self)
        self._btn_confirmar.clicked.connect(self.confirmar_exportacion)

        self._btn_cancelar = QPushButton("Cancelar", self)
        self._btn_cancelar.clicked.connect(self.cancelar_exportacion)

        botones = QHBoxLayout()
        botones.addWidget(self._btn_alternar)
        botones.addWidget(self._btn_copiar)
        botones.addStretch()
        botones.addWidget(self._btn_cancelar)
        botones.addWidget(self._btn_confirmar)

        layout = QVBoxLayout(self)
        layout.addWidget(self._visor)
        layout.addLayout(botones)

        self._actualizar_visor()

    def mostrar(self) -> bool:
        """Muestra el diálogo y devuelve si se confirmó la exportación."""
        self.confirmado = False
        self.exec()
        return self.confirmado

    def confirmar_exportacion(self) -> None:
        """Confirma la operación y cierra el diálogo."""
        self.confirmado = True
        self.accept()

    def cancelar_exportacion(self) -> None:
        """Cancela la operación y cierra el diálogo."""
        self.confirmado = False
        self.reject()

    def alternar_vista(self) -> None:
        """Alterna entre la vista preliminar y la vista cruda."""
        try:
            self._vista_cruda = not self._vista_cruda
            self._actualizar_visor()
        except (RuntimeError, ValueError) as error:
            self._mostrar_error(
                "Error al cambiar la vista",
                f"No se pudo actualizar la visualización.\n{error}",
            )

    def copiar_al_portapapeles(self) -> None:
        """Copia al portapapeles el texto de la vista actual."""
        try:
            QGuiApplication.clipboard().setText(self._texto_visible())
        except (RuntimeError, TypeError) as error:
            self._mostrar_error(
                "Error al copiar",
                f"No se pudo copiar el contenido al portapapeles.\n{error}",
            )

    def _texto_visible(self) -> str:
        """Obtiene el texto correspondiente a la vista seleccionada."""
        return self.contenido if self._vista_cruda else self._texto_preliminar

    def _actualizar_visor(self) -> None:
        """Actualiza el contenido y el texto del botón de alternancia."""
        self._visor.setPlainText(self._texto_visible())
        self._btn_alternar.setText(
            "Ver preliminar" if self._vista_cruda else "Ver crudo"
        )

    def _mostrar_error(self, titulo: str, mensaje: str) -> None:
        """Muestra un mensaje descriptivo cuando ocurre un error."""
        QMessageBox.warning(self, titulo, mensaje)

    @classmethod
    def _generar_vista_preliminar(cls, contenido: str) -> str:
        """
        Devuelve el contenido como tabla con columnas alineadas.

        Si el contenido no es tabular, lo devuelve sin cambios.
        """
        if not isinstance(contenido, str):
            raise TypeError("El contenido debe ser una cadena de texto.")

        lineas = [linea for linea in contenido.splitlines() if linea.strip()]
        filas = cls._leer_markdown(lineas) or cls._leer_delimitado(lineas)

        if not filas:
            return contenido

        columnas = max(len(fila) for fila in filas)
        filas = [fila + [""] * (columnas - len(fila)) for fila in filas]
        anchos = [
            max(len(fila[i]) for fila in filas)
            for i in range(columnas)
        ]

        return "\n".join(
            " | ".join(
                celda.ljust(ancho)
                for celda, ancho in zip(fila, anchos)
            ).rstrip()
            for fila in filas
        )

    @staticmethod
    def _leer_markdown(lineas: list[str]) -> list[list[str]]:
        """Lee una tabla Markdown; devuelve [] si las líneas no lo son."""
        if not lineas or not all(
            linea.strip().startswith("|") for linea in lineas
        ):
            return []

        filas = []

        for linea in lineas:
            linea = linea.strip()[1:].removesuffix("|")
            celdas = [celda.strip() for celda in linea.split("|")]

            es_separador = all(
                celda and set(celda) <= set("-: ")
                for celda in celdas
            )

            if not es_separador:
                filas.append(celdas)

        return filas

    @staticmethod
    def _leer_delimitado(lineas: list[str]) -> list[list[str]]:
        """Lee datos delimitados; devuelve [] si las líneas no lo son."""
        if len(lineas) < 2:
            return []

        for delimitador in DELIMITADORES:
            try:
                filas = list(csv.reader(lineas, delimiter=delimitador))
            except csv.Error:
                continue

            if not filas:
                continue

            columnas = len(filas[0])

            if columnas > 1 and all(
                len(fila) == columnas for fila in filas
            ):
                return [
                    [celda.strip() for celda in fila]
                    for fila in filas
                ]

        return []
