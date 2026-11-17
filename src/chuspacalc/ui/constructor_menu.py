"""
Constructor dinámico de menú para ChuspaCalc.
Conecta el registry de herramientas con los menús de la ventana principal.
"""

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu, QMessageBox

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta
from chuspacalc.ui.ventana_principal import VentanaPrincipal


def construir_menu(
    ventana: VentanaPrincipal,
    herramientas_por_carrera: dict[Carrera, list[type[Herramienta]]],
    callback_seleccion,
) -> None:
    """
    Construye los menús dinámicos de la ventana principal.

    Args:
        ventana: Ventana principal de la aplicación.
        herramientas_por_carrera: Diccionario con las herramientas agrupadas
            por carrera.
        callback_seleccion: Función que recibe la clase de la herramienta
            seleccionada.
    """
    menu_carrera = ventana.menu_carrera()
    menu_herramientas = ventana.menu_herramientas()

    # Limpiar los menús para evitar duplicar acciones al reconstruirlos.
    menu_carrera.clear()
    menu_herramientas.clear()

    # Reunir todas las herramientas disponibles.
    todas: list[type[Herramienta]] = []

    for herramientas in herramientas_por_carrera.values():
        todas.extend(herramientas)

    def ejecutar_seleccion(clase: type[Herramienta]) -> None:
        """
        Ejecuta el callback de selección y captura posibles errores.
        """
        try:
            callback_seleccion(clase)
        except ValueError as error:
            QMessageBox.warning(
                ventana,
                "Datos no válidos",
                f"No se pudo seleccionar la herramienta:\n{error}",
            )
        except Exception:
            QMessageBox.critical(
                ventana,
                "Error al seleccionar herramienta",
                "Ocurrió un error al abrir la herramienta. "
                "Intente nuevamente.",
            )

    # Crear un submenú para cada carrera que tenga herramientas.
    for carrera, herramientas in herramientas_por_carrera.items():
        if not herramientas:
            continue

        submenu: QMenu = menu_carrera.addMenu(carrera.etiqueta)

        for clase in herramientas:
            accion = QAction(clase.nombre, ventana)

            # Capturar la clase actual para evitar problemas con el cierre
            # de variables dentro de las funciones lambda.
            accion.triggered.connect(
                lambda checked=False, c=clase: ejecutar_seleccion(c)
            )

            submenu.addAction(accion)

    # Agregar todas las herramientas al menú general.
    if not todas:
        accion_vacia = QAction("Sin herramientas disponibles", ventana)
        accion_vacia.setEnabled(False)
        menu_herramientas.addAction(accion_vacia)
    else:
        for clase in todas:
            accion = QAction(clase.nombre, ventana)

            accion.triggered.connect(
                lambda checked=False, c=clase: ejecutar_seleccion(c)
            )

            menu_herramientas.addAction(accion)
