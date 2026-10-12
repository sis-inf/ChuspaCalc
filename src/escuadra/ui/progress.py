"""
Módulo de indicador de progreso para el CLI de Escuadra.
"""

import time
import threading


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
    def __init__(self, mensaje="Procesando..."):
        self.mensaje = mensaje
        self._activo = False
        self.thread = None

    def start(self):
        self._activo = True
        print(f"\n{self.mensaje}")

        def run():
            while self._activo:
                print(".", end="", flush=True)
                time.sleep(0.5)

        self.thread = threading.Thread(target=run)
        self.thread.start()

    def stop(self):
        self._activo = False

        if self.thread:
            self.thread.join()

        print("\n✔ terminado")
