from chuspacalc.io.exportador_latex import escapar_latex, exportar_tabla


def test_escapar_latex_escapa_porcentaje():
    assert escapar_latex("50%") == r"50\%"


def test_escapar_latex_escapa_guion_bajo_y_convierte_numeros():
    assert escapar_latex("a_b") == r"a\_b"
    assert escapar_latex(5) == "5"


def test_exportar_tabla_contiene_entorno_tabular_y_fila_de_parametro():
    salida = exportar_tabla({"x": 1}, 2)

    assert r"\begin{tabular}" in salida
    assert r"\end{tabular}" in salida
    assert "x & 1 \\\\" in salida


def test_exportar_tabla_con_formula_incluye_bloque_matematico():
    salida = exportar_tabla({"x": 1}, 2, formula="E=mc^2")

    assert r"\[" in salida
    assert "E=mc^2" in salida
    assert r"\]" in salida


def test_exportar_tabla_sin_formula_no_incluye_bloque_matematico():
    salida = exportar_tabla({"x": 1}, 2)

    assert r"\[" not in salida
