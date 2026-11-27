"""
Pruebas unitarias para el registro de herramientas (core/registry.py).
"""

import pytest

pytest.importorskip("chuspacalc.core.registry")

from chuspacalc.core import registry  # noqa: E402
from chuspacalc.core.carrera import Carrera  # noqa: E402
from chuspacalc.core.registry import (  # noqa: E402
    buscar_por_nombre,
    descubrir_herramientas,
    limpiar_cache,
    obtener_por_categoria,
    registrar,
)


class HerramientaDummy:
    nombre = "Dummy de prueba"


@pytest.fixture(autouse=True)
def registro_limpio():
    limpiar_cache()
    registry._registros.clear()
    yield
    registry._registros.clear()
    limpiar_cache()


def test_registrar_herramienta_valida_guarda_metadata():
    registrar(
        HerramientaDummy,
        {"categoria": "electrica", "descripcion": "Herramienta de prueba."},
    )
    assert registry._registros["Dummy de prueba"] == {
        "categoria": "electrica",
        "descripcion": "Herramienta de prueba.",
    }


def test_registrar_elimina_espacios_en_la_metadata():
    registrar(
        HerramientaDummy,
        {"categoria": "  civil  ", "descripcion": "  Con espacios.  "},
    )
    assert registry._registros["Dummy de prueba"]["categoria"] == "civil"
    assert registry._registros["Dummy de prueba"]["descripcion"] == "Con espacios."


@pytest.mark.parametrize(
    "metadata",
    [
        {},
        {"descripcion": "Sin categoria."},
        {"categoria": "civil"},
        {"categoria": "", "descripcion": "Categoria vacia."},
        {"categoria": "   ", "descripcion": "Categoria en blanco."},
        {"categoria": "civil", "descripcion": ""},
        {"categoria": "civil", "descripcion": "   "},
    ],
)
def test_registrar_metadata_invalida_lanza_error(metadata):
    with pytest.raises(ValueError):
        registrar(HerramientaDummy, metadata)
    assert "Dummy de prueba" not in registry._registros


@pytest.mark.parametrize("carrera", list(Carrera))
def test_obtener_por_categoria_retorna_exactamente_las_de_la_carrera(carrera):
    esperado = [h for h in descubrir_herramientas() if h.carrera == carrera]
    resultado = obtener_por_categoria(carrera.codigo)
    assert resultado == esperado
    assert all(h.carrera == carrera for h in resultado)


def test_obtener_por_categoria_incluye_herramienta_conocida():
    nombres = [h.nombre for h in obtener_por_categoria("electrica")]
    assert "Ley de Ohm" in nombres


def test_obtener_por_categoria_inexistente_retorna_lista_vacia():
    assert obtener_por_categoria("categoria_que_no_existe") == []


def test_buscar_por_nombre_inexistente_retorna_none():
    assert buscar_por_nombre("Herramienta que no existe") is None
