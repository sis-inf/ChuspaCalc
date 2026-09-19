from PySide6.QtWidgets import QWidget

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta



class HerramientaFinanciera(Herramienta):
    nombre = "Matemática financiera"

    carrera = Carrera.MATEMATICAS

    descripcion = (
        "Calcula valor futuro, valor presente "
        "e interés compuesto."
    )

    def crear_widget(self) -> QWidget:
        return QWidget()
