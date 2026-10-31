from ChuspaCalc.core.carrera import Carrera
from ChuspaCalc.core.herramienta import Herramienta
from ChuspaCalc.modulos.matematicas.numeros_complejos import (
    conjugado,
    dividir,
    modulo,
    multiplicar,
    polar_a_rectangular,
    rectangular_a_polar,
    restar,
    sumar,
)
from PySide6.QtWidgets import QWidget


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
