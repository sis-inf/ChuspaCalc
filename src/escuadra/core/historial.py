"""
Historial en memoria de los cálculos realizados durante la sesión.
"""

from datetime import datetime
from typing import Any


class Historial:
    """
    Historial en memoria de los últimos 20 cálculos realizados.

    Cada entrada es un diccionario con las claves ``timestamp``,
    ``herramienta``, ``parametros`` y ``resultado``. La clave ``nota``
    se agrega al editar una entrada con ``editar_nota``.

    Attributes:
        LIMITE: Cantidad máxima de entradas que se conservan.
    """

    LIMITE: int = 20

    def __init__(self) -> None:
        """
        Inicializa un historial vacío.
        """
        self._historial: list[dict[str, Any]] = []

    def agregar_calculo(
        self,
        herramienta: str,
        parametros: dict[str, Any],
        resultado: dict[str, Any],
    ) -> None:
        """
        Agrega un cálculo al historial con timestamp.

        Si el historial supera ``LIMITE`` entradas, se descarta la más antigua.

        Args:
            herramienta: Nombre de la herramienta que realizó el cálculo.
            parametros: Parámetros de entrada usados en el cálculo.
            resultado: Resultado devuelto por la herramienta.
        """
        entrada = {
            "timestamp": datetime.now().isoformat(),
            "herramienta": herramienta,
            "parametros": parametros,
            "resultado": resultado,
        }

        self._historial.append(entrada)

        if len(self._historial) > self.LIMITE:
            self._historial.pop(0)

    def editar_nota(self, timestamp: str, nota: str) -> bool:
        """
        Actualiza la nota de una entrada identificada por su timestamp.

        Args:
            timestamp: Marca de tiempo de la entrada que se editará.
            nota: Texto de la nueva nota.

        Returns:
            True si se actualizó la nota; False si la entrada no existe.
        """
        for entrada in self._historial:
            if entrada["timestamp"] == timestamp:
                entrada["nota"] = nota
                return True

        return False

    def obtener_historial(self) -> list[dict[str, Any]]:
        """
        Retorna el historial con la entrada más reciente primero.

        Returns:
            Lista de entradas, de la más reciente a la más antigua.
            Está vacía si no hay cálculos registrados.
        """
        return list(reversed(self._historial))

    def obtener_ultimo(self) -> dict[str, Any] | None:
        """
        Retorna el último registro o None si está vacío.

        Returns:
            La entrada más reciente, o None si el historial está vacío.
        """
        if not self._historial:
            return None

        return self._historial[-1]

    def limpiar(self) -> None:
        """
        Vacía el historial.
        """
        self._historial.clear()
