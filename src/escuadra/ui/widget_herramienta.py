import time
import threading

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget, QPushButton, QApplication

from escuadra.ui.progress import ProgressIndicator
from escuadra.ui.mensajes import mostrar_error_contextualizado


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
        self.btn_copiar.clicked.connect(self.copiar_al_portapapeles)

        # Construcción ordenada de la interfaz base
        self.layout_principal.addWidget(encabezado)
        self.layout_principal.addWidget(separador)
        self.layout_principal.addWidget(self._contenido)
        self.layout_principal.addWidget(self.btn_copiar)  # Tu botón se posiciona al final de manera fija

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

    def copiar_al_portapapeles(self):
        """
        Obtiene el resultado formateado de la herramienta y lo copia
        al portapapeles del sistema usando QApplication.clipboard.
        """
        resultado = self.obtener_resultado_formateado()
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
        try:
            resultado[0] = funcion(*args, **kwargs)
        except Exception as error:
            resultado[0] = error
        finally:
            terminado.set()

    hilo = threading.Thread(target=tarea)
    hilo.start()

    hilo.join(timeout=umbral)

    if not terminado.is_set():
        progress = ProgressIndicator()
        progress.start()
        hilo.join()
        progress.stop()
    else:
        hilo.join()

    if isinstance(resultado[0], Exception):
        mostrar_error_contextualizado(None, resultado[0])
        return None

    return resultado[0]
