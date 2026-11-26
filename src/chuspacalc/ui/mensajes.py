"""
Mensajes de la interfaz: cuadros de diálogo para informar errores,
advertencias y confirmaciones al usuario.

Este módulo solo contiene funciones auxiliares sobre ``QMessageBox``; no
define señales ni slots. Los slots que reciben los eventos de la interfaz
están en los widgets que llaman a estas funciones.
"""

from PySide6.QtWidgets import QMessageBox


def mostrar_error(parent, titulo, mensaje):
    """Muestra un cuadro de diálogo con ícono de error crítico.

    Args:
        parent: Widget padre del diálogo (puede ser None).
        titulo: Texto de la barra de título.
        mensaje: Texto que se muestra al usuario.
    """
    QMessageBox.critical(parent, titulo, mensaje)


def mostrar_advertencia(parent, titulo, mensaje):
    """Muestra un cuadro de diálogo con ícono de advertencia.

    Args:
        parent: Widget padre del diálogo (puede ser None).
        titulo: Texto de la barra de título.
        mensaje: Texto que se muestra al usuario.
    """
    QMessageBox.warning(parent, titulo, mensaje)


def mostrar_informacion(parent, titulo, mensaje):
    """Muestra un cuadro de diálogo con ícono de información.

    Args:
        parent: Widget padre del diálogo (puede ser None).
        titulo: Texto de la barra de título.
        mensaje: Texto que se muestra al usuario.
    """
    QMessageBox.information(parent, titulo, mensaje)


def mostrar_error_contextualizado(parent, excepcion):
    """
    Muestra mensajes de error según el tipo de excepción producida.

    Se revisan los nombres de toda la jerarquía de la excepción, no solo el
    de su clase. Así, una subclase de ``ErrorValidacion`` (por ejemplo
    ``ErrorCIDR``) también recibe el mensaje claro de validación en lugar
    del genérico "Error inesperado".

    Args:
        parent: Widget padre del diálogo (puede ser None).
        excepcion: Excepción capturada por el llamador.
    """

    # Nombres de la clase de la excepción y de todas sus clases base.
    nombres_error = {clase.__name__ for clase in type(excepcion).__mro__}
    mensaje = str(excepcion)

    if "ErrorParametros" in nombres_error:
        mostrar_advertencia(parent, "Parámetros inválidos", mensaje)

    elif "ErrorCalculo" in nombres_error:
        mostrar_error(
            parent,
            "Error de cálculo",
            f"{mensaje}\n\nRevise los valores ingresados e intente nuevamente.",
        )

    elif "ErrorValidacion" in nombres_error:
        mostrar_error(
            parent,
            "Error de validación",
            f"{mensaje}\n\nVerifique que los valores estén dentro del rango permitido.",
        )

    else:
        # Cualquier otra excepción no prevista se muestra con su texto original.
        mostrar_error(parent, "Error inesperado", mensaje)


def confirmar(parent, titulo, mensaje):
    """
    Muestra un diálogo de confirmación con botones Sí/No en español.
    Devuelve True si el usuario confirma, False en caso contrario.
    """

    caja = QMessageBox(parent)
    caja.setWindowTitle(titulo)
    caja.setText(mensaje)
    caja.setIcon(QMessageBox.Icon.Question)

    # Agregar botones personalizados en español
    boton_si = caja.addButton("Sí", QMessageBox.ButtonRole.YesRole)

    # FIX: Se quita la asignación a 'boton_no' porque no se utiliza,
    # evitando el error F841 de ruff. El botón se sigue agregando al diálogo.
    caja.addButton("No", QMessageBox.ButtonRole.NoRole)

    caja.exec()

    return caja.clickedButton() == boton_si
