"""
Clase base abstracta para todas las herramientas del sistema.
"""

from abc import ABC, abstractmethod

from PySide6.QtWidgets import QWidget

from escuadra.core.carrera import Carrera


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

    def __init_subclass__(cls, **kwargs):
        """
        Valida que las subclases definan correctamente
        los atributos requeridos.
        """
        super().__init_subclass__(**kwargs)

        if cls.__name__ == "Herramienta":
            return

        if cls.nombre == "":
            raise ValueError("La subclase debe definir el atributo 'nombre'.")

        if cls.carrera is None:
            raise ValueError("La subclase debe definir el atributo 'carrera'.")

        if cls.descripcion == "":
            raise ValueError("La subclase debe definir el atributo 'descripcion'.")

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
