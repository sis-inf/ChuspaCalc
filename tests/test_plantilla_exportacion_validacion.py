"""Pruebas de validación de entradas y casos borde de PlantillaExportacion."""

import pytest

from chuspacalc.io.plantilla_exportacion import PlantillaExportacion
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


@pytest.mark.parametrize("formato", ["xml", "", None, 5])
def test_formato_invalido_lanza_error_validacion(formato):
    with pytest.raises(ErrorValidacion, match="Formato inválido"):
        PlantillaExportacion(formato=formato)


@pytest.mark.parametrize("campos", ["a", {"a": 1}, 5])
def test_campos_no_lista_lanza_error_validacion_y_type_error(campos):
    with pytest.raises(ErrorValidacion, match="campos debe ser una lista"):
        PlantillaExportacion(campos=campos)
    with pytest.raises(TypeError):
        PlantillaExportacion(campos=campos)


def test_campos_con_elemento_no_str_lanza_error():
    with pytest.raises(ErrorValidacion, match="todos los campos deben ser str"):
        PlantillaExportacion(campos=["a", 1])


@pytest.mark.parametrize("valor", ["si", 1, None])
def test_incluir_pasos_no_bool_lanza_error(valor):
    with pytest.raises(ErrorValidacion, match="incluir_pasos debe ser bool"):
        PlantillaExportacion(incluir_pasos=valor)
    with pytest.raises(TypeError):
        PlantillaExportacion.cargar({"incluir_pasos": valor})
    with pytest.raises(ErrorValidacion):
        PlantillaExportacion().actualizar(incluir_pasos=valor)


@pytest.mark.parametrize("datos", [None, [], "json", 5])
def test_cargar_no_dict_lanza_error_validacion_y_type_error(datos):
    with pytest.raises(ErrorValidacion, match="Se esperaba un dict"):
        PlantillaExportacion.cargar(datos)
    with pytest.raises(TypeError):
        PlantillaExportacion.cargar(datos)


def test_cargar_con_campos_none_usa_lista_vacia():
    assert PlantillaExportacion.cargar({"campos": None}).campos == []


def test_actualizar_no_deja_cambios_a_medias_si_hay_error():
    plantilla = PlantillaExportacion()
    with pytest.raises(ErrorValidacion):
        plantilla.actualizar(formato="csv", incluir_pasos="x")
    assert plantilla.formato == "json"
    assert plantilla.incluir_pasos is False


def test_actualizar_no_pisa_metodos():
    plantilla = PlantillaExportacion()
    plantilla.actualizar(guardar=1, copiar=2)
    assert callable(plantilla.guardar)
    assert callable(plantilla.copiar)


def test_actualizar_copia_la_lista_de_campos():
    lista = ["a"]
    plantilla = PlantillaExportacion()
    plantilla.actualizar(campos=lista)
    lista.append("b")
    assert plantilla.campos == ["a"]


def test_actualizar_valores_validos():
    plantilla = PlantillaExportacion()
    plantilla.actualizar(formato="latex", incluir_pasos=True, campos=["x"])
    assert plantilla.guardar() == {
        "formato": "latex",
        "incluir_pasos": True,
        "campos": ["x"],
    }
