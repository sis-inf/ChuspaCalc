"""
Módulo de la ventana principal de Escuadra.
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


class VentanaPrincipal(QMainWindow):
    """
    Ventana principal de la aplicación Escuadra.

    Configura el título, tamaño, menú superior, área central,
    barra de estado y atajos de teclado. Expone puntos de extensión para que
    otros componentes monten contenido en los menús y acciones.
    """

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setWindowTitle("Escuadra")
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
        accion_salir.triggered.connect(QApplication.quit)
        menu_archivo.addAction(accion_salir)

        # Menu Carrera (vacio, lo llena el constructor dinamico)
        self._menu_carrera: QMenu = barra.addMenu("Carrera")

        # Menu Herramientas (vacio, lo llena el constructor dinamico)
        self._menu_herramientas: QMenu = barra.addMenu("Herramientas")

        # Menu Ayuda
        menu_ayuda = barra.addMenu("Ayuda")
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
            atajo.activated.connect(lambda i=idx: callback(i))

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
