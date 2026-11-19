"""
Tests unitarios para la clase PlantillaExportacion, verificando los
valores por defecto, el guardado y la carga desde diccionarios, la
actualización de opciones y la copia independiente de la plantilla.
"""

import pytest

from chuspacalc.io.plantilla_exportacion import PlantillaExportacion


def test_valores_por_defecto():
    plantilla = PlantillaExportacion()

    assert plantilla.formato == "json"
    assert plantilla.incluir_pasos is False
    assert plantilla.campos == []


def test_guardar_devuelve_diccionario_con_las_claves_esperadas():
    datos = PlantillaExportacion().guardar()

    assert isinstance(datos, dict)
    assert set(datos) == {"formato", "incluir_pasos", "campos"}


def test_cargar_conserva_formato_y_rellena_valores_por_defecto():
    plantilla = PlantillaExportacion.cargar({"formato": "csv"})

    assert plantilla.formato == "csv"
    assert plantilla.incluir_pasos is False
    assert plantilla.campos == []


def test_cargar_con_lista_lanza_error_de_tipo():
    with pytest.raises(TypeError):
        PlantillaExportacion.cargar([])


def test_actualizar_cambia_formato_e_ignora_clave_desconocida():
    plantilla = PlantillaExportacion()

    plantilla.actualizar(formato="md", inexistente=1)

    assert plantilla.formato == "md"
    assert not hasattr(plantilla, "inexistente")


def test_copiar_devuelve_instancia_distinta_sin_compartir_la_lista_de_campos():
    original = PlantillaExportacion(campos=["a", "b"])

    copia = original.copiar()
    copia.campos.append("c")

    assert copia is not original
    assert copia.campos is not original.campos
    assert original.campos == ["a", "b"]
