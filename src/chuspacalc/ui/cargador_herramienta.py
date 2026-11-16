"""
Carga dinámica de herramientas en la ventana principal.
"""

from chuspacalc.ui.mensajes import mostrar_error
from chuspacalc.utils.logging_config import obtener_logger
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel

logger = obtener_logger("cargador_herramienta")


def crear_widget_error(mensaje):
    """
    Crea un widget informativo que reemplaza a la herramienta
    cuando no se puede cargar.
    """
    etiqueta = QLabel(mensaje)
    etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)
    etiqueta.setWordWrap(True)
    return etiqueta


class CargadorHerramienta:
    """
    Router interno que conecta la selección del menú
    con la carga de widgets en la ventana principal.
    """

    def __init__(self, ventana):
        self._ventana = ventana
        self._herramienta_actual = None
        self._widget_actual = None

    def _liberar_widget(self):
        """
        Libera el widget anterior si existe.
        """
        if self._widget_actual is not None:
            self._widget_actual.setParent(None)
            self._widget_actual.deleteLater()

            self._widget_actual = None
            self._herramienta_actual = None

    def _resolver(self, herramienta):
        """
        Devuelve la clase de la herramienta. Si recibe su nombre,
        la busca en el registro central; si recibe una clase, la usa.
        """
        if not isinstance(herramienta, str):
            return herramienta

        from chuspacalc.core.registry import buscar_por_nombre

        return buscar_por_nombre(herramienta)

    def _mostrar_widget_error(self, mensaje):
        """
        Muestra un widget informativo de error en la ventana principal.
        """
        widget = crear_widget_error(mensaje)

        self._ventana.mostrar_herramienta(widget)
        self._ventana.mostrar_mensaje_estado(mensaje)

        self._widget_actual = widget

    def cargar(self, herramienta):
        """
        Instancia una herramienta, crea su widget
        y la muestra en la ventana principal.

        Acepta la clase de la herramienta o su nombre registrado.
        """

        try:
            self._liberar_widget()

            try:
                clase_herramienta = self._resolver(herramienta)
            except ImportError as error:
                logger.error(
                    f"Error al importar el registro de herramientas: {error}",
                    exc_info=True,
                )
                self._mostrar_widget_error(
                    f"No se pudo importar el registro de herramientas: {error}"
                )
                return

            if clase_herramienta is None:
                logger.warning(f"Herramienta no encontrada: {herramienta}")
                mensaje = f"No se encontró la herramienta '{herramienta}'."
                self._mostrar_widget_error(mensaje)
                return

            herramienta_instancia = clase_herramienta()

            widget = herramienta_instancia.crear_widget()

            self._ventana.mostrar_herramienta(widget)

            nombre = clase_herramienta.__name__

            self._ventana.mostrar_mensaje_estado(f"Herramienta activa: {nombre}")

            self._herramienta_actual = herramienta_instancia
            self._widget_actual = widget

        except Exception as error:
            logger.error(f"Error al cargar herramienta: {error}", exc_info=True)

            mostrar_error(
                self._ventana,
                "Error al cargar herramienta",
                str(error),
            )

    def herramienta_actual(self):
        """
        Devuelve la herramienta actualmente cargada.
        """
        return self._herramienta_actual
