from PySide6.QtWidgets import QWidget, QInputDialog, QListWidgetItem
from PySide6.QtCore import Qt

class PanelHistorial(QWidget):
    # ... resto del código previo ...

    def _refrescar_lista(self):
        """
        Limpia y vuelve a cargar la lista de historial desde el core.
        Este método es vital para que la nota aparezca al editarla.
        """
        self.lista_historial.clear()
        # Obtenemos la lista actualizada del modelo
        entradas = self.historial.obtener_historial()

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
                self.historial.editar_nota(datos["timestamp"], nueva_nota)
                # Refrescamos la vista para mostrar el cambio al usuario
                self._refrescar_lista()
