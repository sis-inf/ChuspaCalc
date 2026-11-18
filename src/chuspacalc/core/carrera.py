"""
Carreras soportadas por ChuspaCalc.

Define el enum ``Carrera``, que centraliza las carreras y sirve para
agrupar las herramientas de cálculo en el menú, la CLI y el registry.
"""

from enum import Enum


class Carrera(Enum):
    """
    Enum que centraliza las carreras soportadas por el MVP.

    Cada miembro sigue el formato ``NOMBRE = ("codigo", "Nombre Legible")``.
    Para agregar nuevas carreras en el futuro, simplemente se añade un
    nuevo miembro al enum.

    Attributes:
        codigo (str): Identificador corto en minúsculas, usado en la CLI
            y para filtrar herramientas (por ejemplo ``"civil"``).
        etiqueta (str): Nombre legible que se muestra al usuario.

    Example:
        >>> Carrera.CIVIL.codigo
        'civil'
        >>> Carrera.CIVIL.etiqueta
        'Ingeniería Civil'
    """

    SISTEMAS = ("sistemas", "Ingeniería de Sistemas e Informática")
    MATEMATICAS = ("matematicas", "Matemáticas")
    ELECTRICA = ("electrica", "Ingeniería Eléctrica")
    CIVIL = ("civil", "Ingeniería Civil")
    GEOMETRIA = ("geometria", "Geometría")

    def __init__(self, codigo: str, etiqueta: str) -> None:
        """
        Inicializa un miembro del enum con su código y su etiqueta.

        Args:
            codigo: Identificador corto de la carrera.
            etiqueta: Nombre legible de la carrera.
        """
        self.codigo: str = codigo
        self.etiqueta: str = etiqueta
