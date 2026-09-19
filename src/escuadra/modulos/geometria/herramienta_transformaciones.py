from PySide6.QtWidgets import QWidget

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta



class HerramientaTransformaciones(Herramienta):
    nombre = "Transformaciones Geométricas"

    carrera = Carrera.GEOMETRIA

    descripcion = (
        "Permite rotar, trasladar y escalar puntos "
        "en el plano cartesiano."
    )

    def crear_widget(self) -> QWidget:
        return QWidget()
