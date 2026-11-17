import threading

from chuspacalc.ui.mensajes import mostrar_error_contextualizado
from chuspacalc.ui.progress import ProgressIndicator
from PySide6.QtCore import Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QPushButton, QVBoxLayout, QWidget


class WidgetHerramienta(QWidget):
    """
    Clase base para todas las herramientas de la interfaz.
    Proporciona de manera consistente el layout base, encabezado visual
    y el botón para copiar los resultados calculados al portapapeles.
    """

    def __init__(self, nombre, descripcion, parent=None):
        super().__init__(parent)

        # Layout principal de la herramienta
        self.layout_principal = QVBoxLayout(self)

        # Encabezado visual (Aporte de tu compañero)
        encabezado = QFrame()
        encabezado.setStyleSheet("""
            background-color: #EAEAEA;
            padding: 10px;
            border-radius: 5px;
        """)

        layout_encabezado = QVBoxLayout(encabezado)

        label_nombre = QLabel(nombre)
        fuente_titulo = QFont()
        fuente_titulo.setPointSize(14)
        fuente_titulo.setBold(True)
        label_nombre.setFont(fuente_titulo)

        label_descripcion = QLabel(descripcion)
        fuente_descripcion = QFont()
        fuente_descripcion.setItalic(True)
        label_descripcion.setFont(fuente_descripcion)

        layout_encabezado.addWidget(label_nombre)
        layout_encabezado.addWidget(label_descripcion)

        separador = QFrame()
        separador.setFrameShape(QFrame.HLine)
        separador.setFrameShadow(QFrame.Sunken)

        # Área donde las subclases renderizan sus componentes internos
        self._contenido = QWidget()

        # Botón dedicado para copiar resultados (Tu funcionalidad del Issue #704)
        self.btn_copiar = QPushButton("Copiar resultado")
        # La señal clicked se conecta al slot copiar_al_portapapeles, que está
        # decorado con @Slot() y no recibe el parámetro 'checked' de la señal.
        self.btn_copiar.clicked.connect(self.copiar_al_portapapeles)

        # Construcción ordenada de la interfaz base
        self.layout_principal.addWidget(encabezado)
        self.layout_principal.addWidget(separador)
        self.layout_principal.addWidget(self._contenido)
        # Tu botón se posiciona al final de manera fija
        self.layout_principal.addWidget(self.btn_copiar)

    def area_contenido(self):
        """
        Devuelve el área de contenido para que las subclases añadan sus componentes.
        """
        return self._contenido

    def obtener_resultado_formateado(self) -> str:
        """
        Método virtual: Las subclases de cada herramienta específica
        deben sobrescribir este método para devolver el string de su resultado.
        """
        return ""

    @Slot()
    def copiar_al_portapapeles(self):
        """
        Obtiene el resultado formateado de la herramienta y lo copia
        al portapapeles del sistema usando QApplication.clipboard.

        Si la herramienta lanza una excepción al validar o calcular el
        resultado, se muestra un mensaje de error en la interfaz en lugar
        de dejar que la excepción se propague fuera del slot.
        """
        try:
            resultado = self.obtener_resultado_formateado()
        except Exception as error:
            mostrar_error_contextualizado(self, error)
            return
        if resultado:
            portapapeles = QApplication.clipboard()
            portapapeles.setText(str(resultado))


def ejecutar_con_progreso_ui(funcion, *args, umbral=0.5, **kwargs):
    """
    Ejecuta una función mostrando indicador de progreso si tarda demasiado.
    (Mantenido por compatibilidad con los nuevos módulos de dev)
    """
    resultado = [None]
    terminado = threading.Event()

    def tarea():
        # Se ejecuta en un hilo aparte; guarda el resultado o la excepción
        # para reportarla después en el hilo principal de la interfaz.
        try:
            resultado[0] = funcion(*args, **kwargs)
        except Exception as error:
            resultado[0] = error
        finally:
            terminado.set()

    hilo = threading.Thread(target=tarea)
    hilo.start()

    # Espera hasta 'umbral' segundos; si la tarea sigue activa se muestra
    # el indicador de progreso hasta que termine.
    hilo.join(timeout=umbral)

    if not terminado.is_set():
        progress = ProgressIndicator()
        progress.start()
        hilo.join()
        progress.stop()
    else:
        hilo.join()

    # Si la tarea falló, se informa al usuario con un mensaje claro
    # y se devuelve None para que el llamador no use un resultado inválido.
    if isinstance(resultado[0], Exception):
        mostrar_error_contextualizado(None, resultado[0])
        return None

    return resultado[0]
