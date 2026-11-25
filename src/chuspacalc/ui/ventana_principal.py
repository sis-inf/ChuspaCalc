"""
Módulo de la ventana principal de ChuspaCalc.
Contiene la clase VentanaPrincipal que hereda de QMainWindow.
"""

from typing import Callable

from PySide6.QtGui import QAction, QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenu,
    QStackedWidget,
    QStatusBar,
    QWidget,
)

from chuspacalc.ui.mensajes import mostrar_error_contextualizado


class VentanaPrincipal(QMainWindow):
    """
    Ventana principal de la aplicación ChuspaCalc.

    Configura el título, tamaño, menú superior, área central,
    barra de estado y atajos de teclado. Expone puntos de extensión para que
    otros componentes monten contenido en los menús y acciones.
    """

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setWindowTitle("ChuspaCalc")
        self.resize(1000, 700)

        self._configurar_menus()
        self._configurar_area_central()
        self._configurar_barra_estado()
        self._configurar_atajos_teclado()

    def _configurar_menus(self) -> None:
        barra = self.menuBar()

        # Menu Archivo
        menu_archivo = barra.addMenu("Archivo")
        accion_salir = QAction("Salir", self)
        # La señal triggered se conecta directo a QApplication.quit, que no
        # necesita el parámetro checked ni validación previa.
        accion_salir.triggered.connect(QApplication.quit)
        menu_archivo.addAction(accion_salir)

        # Menu Carrera (vacio, lo llena el constructor dinamico)
        self._menu_carrera: QMenu = barra.addMenu("Carrera")

        # Menu Herramientas (vacio, lo llena el constructor dinamico)
        self._menu_herramientas: QMenu = barra.addMenu("Herramientas")

        # Menu Ayuda
        menu_ayuda = barra.addMenu("Ayuda")
        # La señal triggered de esta acción se conecta desde la integración
        # a través de accion_acerca_de().
        self._accion_acerca_de = QAction("Acerca de", self)
        menu_ayuda.addAction(self._accion_acerca_de)

    def _configurar_area_central(self) -> None:
        self._area_central = QStackedWidget()
        self.setCentralWidget(self._area_central)

    def _configurar_barra_estado(self) -> None:
        barra_estado = QStatusBar()
        self.setStatusBar(barra_estado)
        barra_estado.showMessage("Lista para usar")

    def _configurar_atajos_teclado(self) -> None:
        """Configura los atajos de teclado Ctrl+1 a Ctrl+9 para herramientas recientes."""
        self._atajos_herramientas_recientes: list[QShortcut] = []
        for i in range(1, 10):
            # Los atajos se crean sin conexión; la integración los conecta
            # mediante conectar_atajos_recientes().
            atajo = QShortcut(QKeySequence(f"Ctrl+{i}"), self)
            self._atajos_herramientas_recientes.append(atajo)

    # API publica

    def menu_carrera(self) -> QMenu:
        """Devuelve el menú Carrera para que el constructor dinámico lo llene."""
        return self._menu_carrera

    def menu_herramientas(self) -> QMenu:
        """Devuelve el menú Herramientas para que el constructor dinámico lo llene."""
        return self._menu_herramientas

    def accion_acerca_de(self) -> QAction:
        """Devuelve la acción Acerca de para conectarla desde la integración."""
        return self._accion_acerca_de

    def atajos_herramientas_recientes(self) -> list[QShortcut]:
        """Devuelve la lista de atajos Ctrl+1 a Ctrl+9 para conectarlos desde la integración."""
        return self._atajos_herramientas_recientes

    def conectar_atajos_recientes(self, callback: Callable[[int], None]) -> None:
        """
        Conecta los atajos de teclado (Ctrl+1 a Ctrl+9) a una función callback externa.

        Args:
            callback: Función que recibe el índice (0 a 8) de la herramienta reciente a abrir.
        """
        for idx, atajo in enumerate(self._atajos_herramientas_recientes):
            # Cada atajo ejecuta el callback a través de _ejecutar_atajo_reciente,
            # que captura errores para que no escapen del bucle de eventos de Qt.
            atajo.activated.connect(
                lambda i=idx: self._ejecutar_atajo_reciente(callback, i)
            )

    def _ejecutar_atajo_reciente(
        self, callback: Callable[[int], None], indice: int
    ) -> None:
        """
        Ejecuta el callback de un atajo reciente capturando cualquier error.

        Los atajos se disparan desde el bucle de eventos de Qt; si el callback
        lanza una excepción, se muestra un mensaje claro en la interfaz en
        lugar de dejar que se propague fuera de la señal.
        """
        try:
            callback(indice)
        except Exception as error:
            mostrar_error_contextualizado(self, error)

    def mostrar_herramienta(self, widget: QWidget) -> None:
        """
        Reemplaza el widget central por el dado.
        Libera el widget anterior para evitar leaks de memoria.

        Args:
            widget: El nuevo widget a mostrar en el área central.
        """
        widget_anterior = self._area_central.currentWidget()
        if widget_anterior is not None:
            self._area_central.removeWidget(widget_anterior)
            widget_anterior.deleteLater()

        self._area_central.addWidget(widget)
        self._area_central.setCurrentWidget(widget)

    def mostrar_mensaje_estado(self, texto: str, timeout_ms: int = 0) -> None:
        """
        Actualiza el mensaje de la barra de estado.

        Args:
            texto: Mensaje a mostrar.
            timeout_ms: Si es mayor que 0, el mensaje se borra
                        automáticamente después de ese tiempo.
        """
        self.statusBar().showMessage(texto, timeout_ms)
