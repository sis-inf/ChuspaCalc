from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QInputDialog, QListWidgetItem, QMessageBox, QWidget


class PanelHistorial(QWidget):
    # ... resto del código previo ...

    @Slot()
    def _refrescar_lista(self):
        """
        Limpia y vuelve a cargar la lista de historial desde el core.
        Este método es vital para que la nota aparezca al editarla.
        """
        self.lista_historial.clear()
        try:
            # Obtenemos la lista actualizada del modelo
            entradas = self.historial.obtener_historial()
        except Exception as exc:  # El core puede fallar de formas imprevistas
            QMessageBox.warning(
                self, "Historial", f"No se pudo cargar el historial: {exc}"
            )
            return

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

    @Slot()
    def _editar_nota_seleccionada(self):
        """Pide una nota nueva para la entrada seleccionada y la guarda en el core."""
        seleccionados = self.lista_historial.selectedItems()
        if len(seleccionados) != 1:
            # Feedback claro en vez de no hacer nada
            QMessageBox.information(
                self, "Anotar entrada", "Selecciona una sola entrada para anotarla."
            )
            return

        datos = self._obtener_datos(seleccionados[0])
        if not datos:
            QMessageBox.warning(
                self, "Anotar entrada", "No se pudieron leer los datos de la entrada."
            )
            return

        nota_actual = datos.get("nota", "")
        nueva_nota, ok = QInputDialog.getText(
            self, "Anotar entrada", "Comentario:", text=nota_actual
        )
        if not ok:
            return  # El usuario canceló

        try:
            # El core valida y persiste la nota
            self.historial.editar_nota(datos["timestamp"], nueva_nota)
        except (ValueError, KeyError) as exc:
            # Errores de validación o entrada inexistente en el core
            QMessageBox.warning(self, "Nota no válida", str(exc))
            return

        # Solo refrescamos si el guardado fue exitoso
        self._refrescar_lista()