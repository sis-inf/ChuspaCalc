"""Pruebas de validación de entradas y casos borde de exportador_json."""

import json

import pytest

from chuspacalc.io.exportador_json import exportar_lista, exportar_resultado
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def test_exportar_resultado_valido_escribe_json(tmp_path):
    ruta = tmp_path / "sub" / "salida.json"
    exportar_resultado({"a": 1, "b": "ñ"}, str(ruta))
    assert json.loads(ruta.read_text(encoding="utf-8")) == {"a": 1, "b": "ñ"}


def test_exportar_lista_valida_escribe_json(tmp_path):
    ruta = tmp_path / "lista.json"
    exportar_lista([1, 2, 3], str(ruta))
    assert json.loads(ruta.read_text(encoding="utf-8")) == [1, 2, 3]


@pytest.mark.parametrize("invalido", [None, [1], "texto", 5])
def test_resultado_no_dict_lanza_error_validacion_y_type_error(tmp_path, invalido):
    with pytest.raises(ErrorValidacion):
        exportar_resultado(invalido, str(tmp_path / "x.json"))
    with pytest.raises(TypeError):
        exportar_resultado(invalido, str(tmp_path / "x.json"))


@pytest.mark.parametrize("invalido", [None, {"a": 1}, "texto", 5])
def test_lista_no_list_lanza_error_validacion_y_type_error(tmp_path, invalido):
    with pytest.raises(ErrorValidacion):
        exportar_lista(invalido, str(tmp_path / "x.json"))
    with pytest.raises(TypeError):
        exportar_lista(invalido, str(tmp_path / "x.json"))


@pytest.mark.parametrize("ruta", [None, 5, ["a.json"]])
def test_ruta_no_texto_lanza_error_validacion(ruta):
    with pytest.raises(ErrorValidacion, match="La ruta debe ser texto"):
        exportar_resultado({"a": 1}, ruta)
    with pytest.raises(ErrorValidacion, match="La ruta debe ser texto"):
        exportar_lista([1], ruta)


@pytest.mark.parametrize("ruta", ["", "   "])
def test_ruta_vacia_lanza_error_validacion(ruta):
    with pytest.raises(ErrorValidacion, match="no puede estar vacía"):
        exportar_resultado({"a": 1}, ruta)
    with pytest.raises(ErrorValidacion, match="no puede estar vacía"):
        exportar_lista([1], ruta)


def test_datos_no_serializables_no_dejan_archivo(tmp_path):
    ruta = tmp_path / "malo.json"
    with pytest.raises(ErrorValidacion, match="no se pueden serializar"):
        exportar_resultado({"a": {1, 2}}, str(ruta))
    assert not ruta.exists()


def test_referencia_circular_lanza_error_validacion(tmp_path):
    circular = {}
    circular["self"] = circular
    with pytest.raises(ErrorValidacion, match="no se pueden serializar"):
        exportar_resultado(circular, str(tmp_path / "c.json"))


def test_archivo_existente_sin_sobreescribir_lanza_file_exists(tmp_path):
    ruta = tmp_path / "x.json"
    exportar_resultado({"a": 1}, str(ruta))
    with pytest.raises(FileExistsError):
        exportar_resultado({"a": 2}, str(ruta))
    exportar_resultado({"a": 2}, str(ruta), sobreescribir=True)
    assert json.loads(ruta.read_text(encoding="utf-8")) == {"a": 2}
