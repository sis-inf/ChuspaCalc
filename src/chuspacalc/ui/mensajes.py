from PySide6.QtWidgets import QMessageBox


def mostrar_error(parent, titulo, mensaje):
    """Muestra un cuadro de diálogo con ícono de error crítico."""
    QMessageBox.critical(parent, titulo, mensaje)


def mostrar_advertencia(parent, titulo, mensaje):
    """Muestra un cuadro de diálogo con ícono de advertencia."""
    QMessageBox.warning(parent, titulo, mensaje)


def mostrar_informacion(parent, titulo, mensaje):
    """Muestra un cuadro de diálogo con ícono de información."""
    QMessageBox.information(parent, titulo, mensaje)


def mostrar_error_contextualizado(parent, excepcion):
    """
    Muestra mensajes de error según el tipo de excepción producida.
    """

    nombre_error = type(excepcion).__name__
    mensaje = str(excepcion)

    if nombre_error == "ErrorParametros":
        mostrar_advertencia(
            parent,
            "Parámetros inválidos",
            mensaje
        )

    elif nombre_error == "ErrorCalculo":
        mostrar_error(
            parent,
            "Error de cálculo",
            f"{mensaje}\n\nRevise los valores ingresados e intente nuevamente."
        )

    elif nombre_error == "ErrorValidacion":
        mostrar_error(
            parent,
            "Error de validación",
            f"{mensaje}\n\nVerifique que los valores estén dentro del rango permitido."
        )

    else:
        mostrar_error(
            parent,
            "Error inesperado",
            mensaje
        )


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
