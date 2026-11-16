"""
Clase base abstracta para todas las herramientas del sistema.
"""

from abc import ABC, abstractmethod

from chuspacalc.core.carrera import Carrera
from PySide6.QtWidgets import QWidget


class Herramienta(ABC):
    """
    Clase base abstracta para las herramientas.

    Define el contrato que toda herramienta debe cumplir:
    - nombre
    - carrera
    - descripcion
    - crear_widget()
    """

    nombre: str = ""
    carrera: Carrera | None = None
    descripcion: str = ""
    parametros_requeridos: tuple[str, ...] = ()

    def __init_subclass__(cls, **kwargs):
        """
        Valida que las subclases definan correctamente
        los atributos requeridos.
        """
        super().__init_subclass__(**kwargs)

        if cls.__name__ == "Herramienta":
            return

        if cls.nombre == "":
            raise ValueError(
                "La subclase debe definir el atributo 'nombre'."
            )

        if cls.carrera is None:
            raise ValueError(
                "La subclase debe definir el atributo 'carrera'."
            )

        if cls.descripcion == "":
            raise ValueError(
                "La subclase debe definir el atributo 'descripcion'."
            )

    @abstractmethod
    def crear_widget(self) -> QWidget:
        """
        Crea y devuelve el widget principal
        de la herramienta.
        """
        raise NotImplementedError

    @classmethod
    def metadatos(cls) -> dict:
        """
        Devuelve los metadatos de la herramienta.
        """
        return {
            "nombre": cls.nombre,
            "carrera": cls.carrera,
            "descripcion": cls.descripcion,
        }

    def validar_parametros(self, kwargs: dict) -> None:
        """
        Valida los parámetros recibidos contra `parametros_requeridos`.

        Revisa que cada parámetro requerido esté presente en `kwargs`
        y que su valor no sea None.

        Raises:
            ValueError: Si falta un parámetro requerido o su valor es None.
        """
        for nombre in self.parametros_requeridos:
            if nombre not in kwargs:
                raise ValueError(f"Falta el parámetro requerido '{nombre}'.")
            if kwargs[nombre] is None:
                raise ValueError(f"El parámetro '{nombre}' no puede ser None.")
