import csv

from PySide6.QtGui import QFontDatabase, QGuiApplication
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
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
        self._texto_preliminar = self._generar_vista_preliminar(contenido)

        self.setWindowTitle(f"Vista previa de exportación [{formato.upper()}]")
        self.resize(640, 420)

        self._visor = QPlainTextEdit()
        self._visor.setReadOnly(True)
        self._visor.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self._visor.setFont(
            QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        )

        self._btn_alternar = QPushButton()
        self._btn_alternar.clicked.connect(self.alternar_vista)

        btn_copiar = QPushButton("Copiar")
        btn_copiar.clicked.connect(self.copiar_al_portapapeles)

        btn_confirmar = QPushButton("Confirmar exportación")
        btn_confirmar.clicked.connect(self.confirmar_exportacion)

        btn_cancelar = QPushButton("Cancelar")
        btn_cancelar.clicked.connect(self.cancelar_exportacion)

        botones = QHBoxLayout()
        botones.addWidget(self._btn_alternar)
        botones.addWidget(btn_copiar)
        botones.addStretch()
        botones.addWidget(btn_cancelar)
        botones.addWidget(btn_confirmar)

        layout = QVBoxLayout(self)
        layout.addWidget(self._visor)
        layout.addLayout(botones)

        self._actualizar_visor()

    def mostrar(self) -> bool:
        self.confirmado = False
        self.exec()

        return self.confirmado

    def confirmar_exportacion(self):
        self.confirmado = True
        self.accept()

    def cancelar_exportacion(self):
        self.confirmado = False
        self.reject()

    def alternar_vista(self):
        """Alterna entre la vista preliminar y la vista cruda."""
        self._vista_cruda = not self._vista_cruda
        self._actualizar_visor()

    def copiar_al_portapapeles(self):
        """Copia al portapapeles el texto de la vista actual."""
        QGuiApplication.clipboard().setText(self._texto_visible())

    def _texto_visible(self) -> str:
        return self.contenido if self._vista_cruda else self._texto_preliminar

    def _actualizar_visor(self):
        self._visor.setPlainText(self._texto_visible())
        self._btn_alternar.setText(
            "Ver preliminar" if self._vista_cruda else "Ver crudo"
        )

    @classmethod
    def _generar_vista_preliminar(cls, contenido: str) -> str:
        """
        Devuelve el contenido como tabla con columnas alineadas.

        Si el contenido no es tabular, lo devuelve sin cambios.
        """
        lineas = [linea for linea in contenido.splitlines() if linea.strip()]
        filas = cls._leer_markdown(lineas) or cls._leer_delimitado(lineas)

        if not filas:
            return contenido

        columnas = max(len(fila) for fila in filas)
        filas = [fila + [""] * (columnas - len(fila)) for fila in filas]
        anchos = [max(len(fila[i]) for fila in filas) for i in range(columnas)]

        return "\n".join(
            " | ".join(
                celda.ljust(ancho) for celda, ancho in zip(fila, anchos)
            ).rstrip()
            for fila in filas
        )

    @staticmethod
    def _leer_markdown(lineas: list[str]) -> list[list[str]]:
        """Lee una tabla markdown; devuelve [] si las líneas no lo son."""
        if not lineas or not all(linea.strip().startswith("|") for linea in lineas):
            return []

        filas = []
        for linea in lineas:
            linea = linea.strip()[1:].removesuffix("|")
            celdas = [celda.strip() for celda in linea.split("|")]

            if not all(set(celda) <= set("-: ") and celda for celda in celdas):
                filas.append(celdas)

        return filas

    @staticmethod
    def _leer_delimitado(lineas: list[str]) -> list[list[str]]:
        """Lee datos delimitados; devuelve [] si las líneas no lo son."""
        if len(lineas) < 2:
            return []

        for delimitador in DELIMITADORES:
            filas = list(csv.reader(lineas, delimiter=delimitador))
            columnas = len(filas[0])

            if columnas > 1 and all(len(fila) == columnas for fila in filas):
                return [[celda.strip() for celda in fila] for fila in filas]

        return []
