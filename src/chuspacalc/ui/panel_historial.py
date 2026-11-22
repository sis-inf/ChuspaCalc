"""
Panel de historial de cálculos.

Este panel no define señales ni slots propios: los métodos reciben las
llamadas de forma directa. Los errores de validación que se produzcan al
consultar o editar el historial se capturan y se muestran al usuario con un
mensaje claro, sin cerrar la aplicación.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QInputDialog, QListWidgetItem, QWidget

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.ui.mensajes import mostrar_error_contextualizado


class PanelHistorial(QWidget):
    # ... resto del código previo ...

    def _refrescar_lista(self):
        """
        Vuelve a cargar la lista de historial desde el core.
        Este método es vital para que la nota aparezca al editarla.

        Primero se consultan los datos y solo si la consulta tiene éxito se
        limpia la lista. Si ocurre un ErrorValidacion, se muestra el mensaje
        y los registros que ya estaban visibles se conservan.
        """
        # Obtenemos la lista actualizada del modelo antes de tocar la lista
        try:
            entradas = self.historial.obtener_historial()
        except ErrorValidacion as error:
            # Muestra el error de validación y conserva los registros visibles.
            mostrar_error_contextualizado(self, error)
            return

        self.lista_historial.clear()

        for entrada in entradas:
            # Creamos el ítem con el texto descriptivo
            item = QListWidgetItem(f"{entrada['herramienta']} - {entrada['timestamp']}")

            # GUARDAMOS EL DICCIONARIO COMPLETO EN EL ÍTEM
            # Esto es lo que permite que _obtener_datos funcione después
            item.setData(Qt.ItemDataRole.UserRole, entrada)

            self.lista_historial.addItem(item)

    def _obtener_datos(self, item):
        """
        Recupera el diccionario completo guardado en el ítem.
        """
        # Recuperamos el diccionario que guardamos en _refrescar_lista
        return item.data(Qt.ItemDataRole.UserRole)

    def _editar_nota_seleccionada(self):
        """
        Edita la nota de la entrada seleccionada en la lista.

        Si el historial lanza un ErrorValidacion al guardar la nota, se
        muestra un mensaje claro al usuario en lugar de propagar el error.
        """
        seleccionados = self.lista_historial.selectedItems()
        if len(seleccionados) == 1:
            item = seleccionados[0]
            datos = self._obtener_datos(item)

            # Abrimos diálogo con la nota actual
            nota_actual = datos.get("nota", "")
            nueva_nota, ok = QInputDialog.getText(
                self, "Anotar entrada", "Comentario:", text=nota_actual
            )

            if ok:
                # Actualizamos en el core (historial.py)
                try:
                    self.historial.editar_nota(datos["timestamp"], nueva_nota)
                except ErrorValidacion as error:
                    # Muestra el error de validación y no refresca la vista.
                    mostrar_error_contextualizado(self, error)
                    return
                # Refrescamos la vista para mostrar el cambio al usuario
                self._refrescar_lista()
