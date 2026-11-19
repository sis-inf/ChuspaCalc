import json

from chuspacalc.core.esquema_llm import (
    _tipo_json,
    exportar_esquema_json,
    exportar_esquema_llm,
)


def test_tipo_json_int():
    assert _tipo_json("int") == "integer"


def test_tipo_json_float():
    assert _tipo_json("float") == "number"


def test_tipo_json_desconocido():
    assert _tipo_json("desconocido") == "string"


def test_exportar_esquema_llm_devuelve_lista():
    resultado = exportar_esquema_llm()

    assert isinstance(resultado, list)

    for elemento in resultado:
        assert "name" in elemento
        assert "description" in elemento
        assert "parameters" in elemento


def test_exportar_esquema_json_devuelve_json_valido():
    resultado = exportar_esquema_json()

    assert isinstance(resultado, str)
    assert isinstance(json.loads(resultado), list)
