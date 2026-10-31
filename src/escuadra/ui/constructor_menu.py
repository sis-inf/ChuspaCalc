"""
Constructor dinámico de menú para ChuspaCalc.
Conecta el registry de herramientas con los menús de la ventana principal.
"""

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta
from chuspacalc.ui.ventana_principal import VentanaPrincipal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu


def construir_menu(
    ventana: VentanaPrincipal,
    herramientas_por_carrera: dict[Carrera, list[type[Herramienta]]],
    callback_seleccion,
) -> None:
    """
    Construye los menús dinámicos de la ventana principal a partir
    del diccionario de herramientas agrupadas por carrera.

    Args:
        ventana: La ventana principal de la aplicación.
        herramientas_por_carrera: Diccionario {Carrera: [clase_herramienta, ...]}
            devuelto por el registry.
        callback_seleccion: Función que se invoca cuando el usuario selecciona
            una herramienta. Recibe la clase de la herramienta como argumento.
    """
    menu_carrera = ventana.menu_carrera()
    menu_herramientas = ventana.menu_herramientas()

    # Recopilar todas las herramientas en lista plana
    todas: list[type[Herramienta]] = []
    for herramientas in herramientas_por_carrera.values():
        todas.extend(herramientas)

    # Menú Carrera: submenú por cada carrera con herramientas
    for carrera, herramientas in herramientas_por_carrera.items():
        if not herramientas:
            continue

        submenu: QMenu = menu_carrera.addMenu(carrera.etiqueta)

        for clase in herramientas:
            accion = QAction(clase.nombre, ventana)
            accion.triggered.connect(
                lambda checked=False, c=clase: callback_seleccion(c)
            )
            submenu.addAction(accion)

    # Menú Herramientas: lista plana con todas las herramientas
    if not todas:
        accion_vacia = QAction("Sin herramientas disponibles", ventana)
        accion_vacia.setEnabled(False)
        menu_herramientas.addAction(accion_vacia)
    else:
        for clase in todas:
            accion = QAction(clase.nombre, ventana)
            accion.triggered.connect(
                lambda checked=False, c=clase: callback_seleccion(c)
            )
            menu_herramientas.addAction(accion)
