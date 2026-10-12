"""
Tests unitarios para la clase base Herramienta.
"""

import pytest
from PySide6.QtWidgets import QLabel, QWidget

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta


# Subclase válida para pruebas
class HerramientaDummy(Herramienta):
    nombre = "Herramienta de prueba"
    carrera = Carrera.SISTEMAS
    descripcion = "Descripción de prueba."

    def crear_widget(self) -> QWidget:
        return QLabel("Dummy")


def test_herramienta_abstracta_no_instanciable():
    # Herramienta es abstracta, no debe poder instanciarse directamente
    with pytest.raises(TypeError):
        Herramienta()


def test_subclase_valida_instanciable():
    # Una subclase con todos los atributos debe instanciarse sin errores
    herramienta = HerramientaDummy()
    assert herramienta is not None


def test_subclase_sin_nombre_falla():
    # Omitir nombre debe lanzar error al definir la subclase
    with pytest.raises(ValueError):

        class HerramientaSinNombre(Herramienta):
            nombre = ""
            carrera = Carrera.SISTEMAS
            descripcion = "Sin nombre."

            def crear_widget(self) -> QWidget:
                return QLabel("x")


def test_subclase_sin_carrera_falla():
    # Omitir carrera debe lanzar error al definir la subclase
    with pytest.raises(ValueError):

        class HerramientaSinCarrera(Herramienta):
            nombre = "Sin carrera"
            carrera = None
            descripcion = "Sin carrera."

            def crear_widget(self) -> QWidget:
                return QLabel("x")


def test_subclase_sin_descripcion_falla():
    # Omitir descripcion debe lanzar error al definir la subclase
    with pytest.raises(ValueError):

        class HerramientaSinDescripcion(Herramienta):
            nombre = "Sin descripcion"
            carrera = Carrera.SISTEMAS
            descripcion = ""

            def crear_widget(self) -> QWidget:
                return QLabel("x")


def test_metadatos_devuelve_dict():
    # metadatos() debe devolver dict con claves nombre, carrera, descripcion
    meta = HerramientaDummy.metadatos()
    assert isinstance(meta, dict)
    assert "nombre" in meta
    assert "carrera" in meta
    assert "descripcion" in meta


def test_metadatos_llamable_en_clase():
    # metadatos() debe poder llamarse en la clase sin instanciar
    meta = HerramientaDummy.metadatos()
    assert meta["nombre"] == "Herramienta de prueba"
    assert meta["carrera"] == Carrera.SISTEMAS
    assert meta["descripcion"] == "Descripción de prueba."
