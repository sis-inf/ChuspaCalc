import pytest

from chuspacalc.io.exportador_markdown import (
    exportar_codigo,
    exportar_lista,
    exportar_markdown,
    exportar_tabla,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def test_exportar_markdown_incluye_titulo_parametros_y_resultado_con_unidad():
    resultado = exportar_markdown("Viga", {"L": 5}, 12.5, unidad="kN")

    assert "# Viga" in resultado.splitlines()
    assert "| L | 5 |" in resultado.splitlines()
    assert "12.5 kN" in resultado.splitlines()


def test_exportar_markdown_incluye_descripcion_en_negrita():
    resultado = exportar_markdown("Viga", {"L": 5}, 12.5, descripcion="Reacción")

    assert "**Reacción**" in resultado.splitlines()


def test_exportar_tabla_incluye_titulo_encabezados_separador_y_fila():
    resultado = exportar_tabla("T", ["a", "b"], [[1, 2]])

    assert "## T" in resultado.splitlines()
    assert "| a | b |" in resultado.splitlines()
    assert "| --- | --- |" in resultado.splitlines()
    assert "| 1 | 2 |" in resultado.splitlines()


def test_exportar_codigo_usa_python_por_defecto():
    resultado = exportar_codigo("C", "x=1")

    assert "```python\nx=1\n```" in resultado


def test_exportar_lista_ordenada_numera_los_elementos():
    resultado = exportar_lista("L", ["a", "b"], ordenada=True)

    assert "1. a" in resultado.splitlines()
    assert "2. b" in resultado.splitlines()


def test_exportar_lista_no_ordenada_usa_vinetas():
    resultado = exportar_lista("L", ["a", "b"], ordenada=False)

    assert "- a" in resultado.splitlines()
    assert "- b" in resultado.splitlines()


@pytest.mark.parametrize("titulo", [None, 1, "", "   "])
@pytest.mark.parametrize(
    "funcion, argumentos",
    [
        (exportar_markdown, ({}, 1)),
        (exportar_tabla, (["A"], [])),
        (exportar_codigo, ("x=1",)),
        (exportar_lista, (["A"],)),
    ],
)
def test_exportadores_rechazan_titulos_invalidos(titulo, funcion, argumentos):
    with pytest.raises(ErrorValidacion, match="titulo"):
        funcion(titulo, *argumentos)


@pytest.mark.parametrize(
    "encabezados, filas",
    [
        (None, []),
        ("A", []),
        ([], []),
        ([None], []),
        (["A"], None),
        (["A"], "abc"),
        (["A"], [None]),
        (["A"], [[1, 2]]),
        (["A", "B"], [[1]]),
        (["A"], [[1], [2, 3]]),
    ],
)
def test_tabla_rechaza_tipos_y_dimensiones_incompatibles(encabezados, filas):
    with pytest.raises(ErrorValidacion):
        exportar_tabla("Tabla", encabezados, filas)


@pytest.mark.parametrize("parametros", [None, [], "x=1"])
def test_markdown_rechaza_parametros_que_no_son_diccionario(parametros):
    with pytest.raises(ErrorValidacion, match="parametros"):
        exportar_markdown("T", parametros, 1)


def test_markdown_rechaza_resultado_nulo_y_opcionales_de_tipo_incorrecto():
    with pytest.raises(ErrorValidacion, match="resultado"):
        exportar_markdown("T", {}, None)
    with pytest.raises(ErrorValidacion, match="descripcion"):
        exportar_markdown("T", {}, 0, descripcion=1)
    with pytest.raises(ErrorValidacion, match="unidad"):
        exportar_markdown("T", {}, 0, unidad=1)


@pytest.mark.parametrize(
    "codigo, lenguaje",
    [
        (None, "python"),
        (1, "python"),
        ("x", None),
        ("x", "py\n# roto"),
        ("x", "`python"),
    ],
)
def test_codigo_rechaza_tipos_y_delimitadores_invalidos(codigo, lenguaje):
    with pytest.raises(ErrorValidacion):
        exportar_codigo("Código", codigo, lenguaje)


@pytest.mark.parametrize(
    "elementos, ordenada",
    [(None, False), ("abc", False), ([None], False), (["A"], "si"), (["A"], 1)],
)
def test_lista_rechaza_tipos_invalidos(elementos, ordenada):
    with pytest.raises(ErrorValidacion):
        exportar_lista("Lista", elementos, ordenada)


def test_tabla_conserva_escape_de_celdas_y_admite_cero_filas():
    tabla = exportar_tabla("T", ["A|B", "C"], [["x|y", "línea 1\nlínea 2"]])
    assert "A\\|B" in tabla
    assert "x\\|y" in tabla
    assert "línea 1 línea 2" in tabla
    assert "| A |" in exportar_tabla("Vacía", ["A"], [])


def test_exportadores_conservan_valores_vacios_validos():
    assert "0" in exportar_markdown("T", {}, 0, descripcion="", unidad="")
    assert exportar_lista("T", []) == "## T\n\n\n"
    assert "```python\n\n```" in exportar_codigo("T", "")
