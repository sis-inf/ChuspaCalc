from enum import Enum


class Carrera(Enum):
    """
    Enum que centraliza las carreras soportadas por el MVP.
    Para agregar nuevas carreras en el futuro, simplemente
    añadir un nuevo miembro al enum. Siguiendo el formato: NOMBRE = ("codigo",
    "Nombre Legible")
    """
    SISTEMAS = ("sistemas", "Ingeniería de Sistemas e Informática")
    MATEMATICAS = ("matematicas", "Matemáticas")
    ELECTRICA = ("electrica", "Ingeniería Eléctrica")
    CIVIL = ("civil", "Ingeniería Civil")
    GEOMETRIA = ("geometria", "Geometría")
    def __init__(self, codigo: str, etiqueta: str):
        self.codigo = codigo
        self.etiqueta = etiqueta
