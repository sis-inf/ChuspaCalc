"""
Tests unitarios para el registry de herramientas.
"""


from PySide6.QtWidgets import QLabel, QWidget

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta
from escuadra.core.registry import (
    buscar_por_nombre,
    descubrir_herramientas,
    herramientas_por_carrera,
    limpiar_cache,
)


# Subclases dummy para pruebas
class HerramientaAlfa(Herramienta):
    nombre = "Alfa"
    carrera = Carrera.SISTEMAS
    descripcion = "Herramienta alfa de prueba."

    def crear_widget(self) -> QWidget:
        return QLabel("Alfa")


class HerramientaBeta(Herramienta):
    nombre = "Beta"
    carrera = Carrera.SISTEMAS
    descripcion = "Herramienta beta de prueba."

    def crear_widget(self) -> QWidget:
        return QLabel("Beta")


class HerramientaGamma(Herramienta):
    nombre = "Gamma"
    carrera = Carrera.MATEMATICAS
    descripcion = "Herramienta gamma de prueba."

    def crear_widget(self) -> QWidget:
        return QLabel("Gamma")


def setup_function():
    # Limpiar cache antes de cada test para evitar interferencias
    limpiar_cache()


def test_descubrir_herramientas_devuelve_lista():
    # descubrir_herramientas() debe devolver una lista
    resultado = descubrir_herramientas()
    assert isinstance(resultado, list)


def test_descubrir_herramientas_incluye_herramientas_reales():
    # Las herramientas del proyecto deben ser descubiertas
    resultado = descubrir_herramientas()
    nombres = [h.nombre for h in resultado]
    assert "Ley de Ohm" in nombres


def test_herramientas_por_carrera_agrupa_correctamente():
    # herramientas_por_carrera() debe agrupar por carrera
    resultado = herramientas_por_carrera()
    assert isinstance(resultado, dict)
    for carrera, herramientas in resultado.items():
        assert isinstance(carrera, Carrera)
        assert all(h.carrera == carrera for h in herramientas)
    # verificacion explicita en presencia de 5 mienbros del Enum Carrera
    carreras_esperadas = {
        Carrera.SISTEMAS,
        Carrera.MATEMATICAS,
        Carrera.ELECTRICA,
        Carrera.CIVIL,
        Carrera.GEOMETRIA,
    }
    # comprobar que las carreras presentes en el resultado pertenezcan al conjunto esperado
    assert set (resultado.keys()).issubset(carreras_esperadas)


def test_herramientas_por_carrera_ordenadas_alfabeticamente():
    # Las herramientas dentro de cada carrera deben estar ordenadas por nombre
    resultado = herramientas_por_carrera()
    for herramientas in resultado.values():
        nombres = [h.nombre for h in herramientas]
        assert nombres == sorted(nombres)


def test_buscar_por_nombre_existente():
    # buscar_por_nombre debe devolver la clase si existe
    resultado = buscar_por_nombre("Ley de Ohm")
    assert resultado is not None
    assert resultado.nombre == "Ley de Ohm"


def test_buscar_por_nombre_inexistente():
    # buscar_por_nombre debe devolver None si no existe
    resultado = buscar_por_nombre("Herramienta que no existe")
    assert resultado is None


def test_modulo_con_error_no_rompe_descubrimiento():
    # El registry debe continuar aunque un modulo falle al importarse
    # Las herramientas validas deben seguir siendo descubiertas
    resultado = descubrir_herramientas()
    assert isinstance(resultado, list)
    assert len(resultado) > 0


def test_limpiar_cache_permite_redescubrir():
    # Tras limpiar_cache(), descubrir_herramientas() vuelve a escanear
    primera = descubrir_herramientas()
    limpiar_cache()
    segunda = descubrir_herramientas()
    assert [h.nombre for h in primera] == [h.nombre for h in segunda]
