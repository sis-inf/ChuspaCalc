from PySide6.QtWidgets import QWidget

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta


class HerramientaNumerosComplejos(Herramienta):
    nombre = "Números complejos"

    carrera = Carrera.MATEMATICAS

    descripcion = (
        "Operaciones con números complejos: suma, resta, "
        "producto, división, módulo, conjugado y "
        "conversiones entre forma rectangular y polar."
    )

    def crear_widget(self) -> QWidget:
        return QWidget()
