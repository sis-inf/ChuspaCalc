from escuadra.io.exportador_markdown import (
    exportar_codigo,
    exportar_lista,
    exportar_markdown,
    exportar_tabla,
)


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
