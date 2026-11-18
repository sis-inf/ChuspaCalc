"""
Clase base abstracta para todas las herramientas del sistema.
"""

from abc import ABC, abstractmethod
from typing import Any

from PySide6.QtWidgets import QWidget

from chuspacalc.core.carrera import Carrera


class Herramienta(ABC):
    """
    Clase base abstracta para las herramientas.

    Define el contrato que toda herramienta debe cumplir:
    - nombre
    - carrera
    - descripcion
    - crear_widget()

    Attributes:
        nombre: Nombre de la herramienta. No puede estar vacio.
        carrera: Carrera a la que pertenece la herramienta. No puede ser None.
        descripcion: Descripcion breve de la herramienta. No puede estar vacia.
        parametros_requeridos: Nombres de los parametros que deben recibirse
            en `validar_parametros`.
    """

    nombre: str = ""
    carrera: Carrera | None = None
    descripcion: str = ""
    parametros_requeridos: tuple[str, ...] = ()

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """
        Valida que las subclases definan correctamente
        los atributos requeridos.

        Args:
            **kwargs: Argumentos adicionales que se reenvian a
                `super().__init_subclass__`.

        Raises:
            ValueError: Si la subclase no define `nombre`, `carrera`
                o `descripcion`.
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

        Returns:
            QWidget: Widget principal de la herramienta.

        Raises:
            NotImplementedError: Si la subclase no lo implementa.
        """
        raise NotImplementedError

    @classmethod
    def metadatos(cls) -> dict[str, Any]:
        """
        Devuelve los metadatos de la herramienta.

        Returns:
            dict[str, Any]: Diccionario con las claves `nombre`,
            `carrera` y `descripcion`.
        """
        return {
            "nombre": cls.nombre,
            "carrera": cls.carrera,
            "descripcion": cls.descripcion,
        }

    def validar_parametros(self, kwargs: dict[str, Any]) -> None:
        """
        Valida los parámetros recibidos contra `parametros_requeridos`.

        Revisa que cada parámetro requerido esté presente en `kwargs`
        y que su valor no sea None.

        Args:
            kwargs: Parametros recibidos, indexados por nombre.

        Raises:
            ValueError: Si falta un parámetro requerido o su valor es None.
        """
        for nombre in self.parametros_requeridos:
            if nombre not in kwargs:
                raise ValueError(f"Falta el parámetro requerido '{nombre}'.")
            if kwargs[nombre] is None:
                raise ValueError(f"El parámetro '{nombre}' no puede ser None.")
