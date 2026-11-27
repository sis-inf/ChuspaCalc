"""
Módulo de indicador de progreso para el CLI de ChuspaCalc.
"""

import logging
import threading
import time

logger = logging.getLogger(__name__)


def mostrar_progreso(current: int, total: int, width: int = 30) -> None:
    """
    Muestra una barra de progreso en la consola.

    Args:
        current: Valor actual del progreso
        total:   Valor total o máximo
        width:   Ancho de la barra en caracteres (default 30)
    """
    if total == 0:
        return

    porcentaje = current / total
    filled = int(width * porcentaje)
    bar = "=" * filled + "-" * (width - filled)
    print(f"\r[{bar}] {int(porcentaje * 100)}%", end="", flush=True)

    if current == total:
        print()


class ProgressIndicator:
    """
    Indicador de progreso para consola que imprime puntos en un hilo aparte.

    Se usa con start() antes de una tarea larga y con stop() al terminar.
    """

    def __init__(self, mensaje="Procesando..."):
        self.mensaje = mensaje
        self._activo = False
        self.thread = None

    def start(self):
        """Muestra el mensaje e inicia el hilo que imprime los puntos."""
        # Evita crear un segundo hilo si el indicador ya está en ejecución.
        if self._activo and self.thread is not None:
            return

        self._activo = True
        print(f"\n{self.mensaje}")

        def run():
            # Si la salida falla (por ejemplo, el stream está cerrado), el hilo
            # se detiene y registra el error en lugar de mostrar un traceback.
            try:
                while self._activo:
                    print(".", end="", flush=True)
                    time.sleep(0.5)
            except Exception as error:
                self._activo = False
                logger.warning("El indicador de progreso se detuvo: %s", error)

        # Hilo daemon: no impide cerrar el programa si stop() nunca se llama.
        self.thread = threading.Thread(target=run, daemon=True)
        self.thread.start()

    def stop(self):
        """Detiene el hilo de puntos y muestra el mensaje de finalización."""
        self._activo = False

        if self.thread:
            self.thread.join()

        # Algunas consolas de Windows no soportan el símbolo ✔; en ese caso se
        # imprime el mensaje sin él para no interrumpir el flujo del programa.
        try:
            print("\n✔ terminado")
        except UnicodeEncodeError:
            print("\nterminado")
