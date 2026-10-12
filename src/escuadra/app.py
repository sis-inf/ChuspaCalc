"""
Punto de entrada principal de la aplicación Escuadra.
Integra todos los componentes: registry, ventana principal,
constructor de menú y cargador de herramientas.
"""

import logging
import sys

from PySide6.QtWidgets import QApplication, QMessageBox

from escuadra.config.loader import load_font_scale
from escuadra.core.registry import descubrir_herramientas, herramientas_por_carrera
from escuadra.ui.cargador_herramienta import CargadorHerramienta
from escuadra.ui.constructor_menu import construir_menu
from escuadra.ui.dialogo_acerca_de import mostrar_acerca_de
from escuadra.ui.ventana_principal import VentanaPrincipal
from escuadra.utils.logging_config import configurar_logging

logger = logging.getLogger(__name__)


def main() -> None:
    """
    Función principal de la aplicación Escuadra.

    Flujo de arranque:
    1. Configura el logging.
    2. Crea la QApplication.
    3. Descubre las herramientas disponibles.
    4. Crea la ventana principal.
    5. Crea el cargador de herramientas.
    6. Construye el menú dinámico.
    7. Conecta el menú Acerca de.
    8. Muestra la ventana e inicia el event loop.
    """
    configurar_logging()

    try:
        app = QApplication(sys.argv)

        # Aplicar escala de fuente global
        font_scale = load_font_scale()
        base_font = app.font()
        base_font.setPointSizeF(base_font.pointSizeF() * font_scale)
        app.setFont(base_font)

        # Descubrir herramientas
        herramientas = descubrir_herramientas()
        if not herramientas:
            logger.warning("No se encontraron herramientas disponibles.")

        por_carrera = herramientas_por_carrera()

        # Crear ventana principal y cargador
        ventana = VentanaPrincipal()
        cargador = CargadorHerramienta(ventana)

        # Construir menú dinámico
        construir_menu(
            ventana,
            por_carrera,
            callback_seleccion=lambda clase: cargador.cargar(clase),
        )

        # Conectar Acerca de
        ventana.accion_acerca_de().triggered.connect(
            lambda: mostrar_acerca_de(parent=ventana)
        )

        ventana.show()
        sys.exit(app.exec())

    except Exception as error:
        logger.critical(
            "Error fatal al arrancar la aplicación: %s", error, exc_info=True
        )
        try:
            QMessageBox.critical(
                None,
                "Error fatal",
                f"La aplicación no pudo iniciarse:\n{error}",
            )
        except Exception:
            pass
        sys.exit(1)


if __name__ == "__main__":
    main()
