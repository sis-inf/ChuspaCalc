import pytest

from chuspacalc.io.exportador_latex import escapar_latex, exportar_tabla
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def test_escapar_latex_escapa_porcentaje():
    assert escapar_latex("50%") == r"50\%"


def test_escapar_latex_escapa_caracteres_especiales():
    assert escapar_latex("&%$#_") == r"\&\%\$\#\_"


def test_escapar_latex_escapa_guion_bajo_y_convierte_numeros():
    assert escapar_latex("a_b") == r"a\_b"
    assert escapar_latex(5) == "5"
    assert escapar_latex(5.5) == "5.5"


@pytest.mark.parametrize(
    "valor",
    [
        None,
        True,
        False,
        [],
        {},
        float("nan"),
        float("inf"),
        float("-inf"),
    ],
)
def test_escapar_latex_rechaza_valores_invalidos(valor):
    with pytest.raises(ErrorValidacion):
        escapar_latex(valor)


def test_exportar_tabla_contiene_entorno_tabular_y_fila_de_parametro():
    salida = exportar_tabla({"x": 1}, 2)

    assert r"\begin{tabular}" in salida
    assert r"\end{tabular}" in salida
    assert "x & 1 \\\\" in salida


def test_exportar_tabla_escapa_claves_y_valores():
    salida = exportar_tabla(
        {"porcentaje_%": 50},
        100,
    )

    assert r"porcentaje\_\%" in salida
    assert r"50 \\" in salida


def test_exportar_tabla_con_formula_incluye_bloque_matematico():
    salida = exportar_tabla({"x": 1}, 2, formula="E=mc^2")

    assert r"\[" in salida
    assert "E=mc^2" in salida
    assert r"\]" in salida


def test_exportar_tabla_sin_formula_no_incluye_bloque_matematico():
    salida = exportar_tabla({"x": 1}, 2)

    assert r"\[" not in salida


def test_exportar_tabla_con_formula_vacia_no_incluye_bloque_matematico():
    salida = exportar_tabla({"x": 1}, 2, formula="")

    assert r"\[" not in salida


@pytest.mark.parametrize(
    "parametros",
    [
        None,
        [],
        (),
        "parametros",
        123,
    ],
)
def test_exportar_tabla_rechaza_parametros_con_estructura_invalida(parametros):
    with pytest.raises(ErrorValidacion):
        exportar_tabla(parametros, 2)


@pytest.mark.parametrize(
    "parametros",
    [
        {"x": None},
        {"x": True},
        {"x": float("nan")},
        {"x": float("inf")},
        {"x": [1, 2]},
        {None: 1},
    ],
)
def test_exportar_tabla_rechaza_parametros_con_valores_invalidos(parametros):
    with pytest.raises(ErrorValidacion):
        exportar_tabla(parametros, 2)


@pytest.mark.parametrize(
    "resultado",
    [
        None,
        True,
        False,
        [],
        {},
        float("nan"),
        float("inf"),
        float("-inf"),
    ],
)
def test_exportar_tabla_rechaza_resultados_invalidos(resultado):
    with pytest.raises(ErrorValidacion):
        exportar_tabla({"x": 1}, resultado)


@pytest.mark.parametrize(
    "formula",
    [
        123,
        True,
        [],
        {},
    ],
)
def test_exportar_tabla_rechaza_formulas_de_tipo_incorrecto(formula):
    with pytest.raises(ErrorValidacion):
        exportar_tabla({"x": 1}, 2, formula=formula)


def test_exportar_tabla_acepta_parametros_vacios():
    salida = exportar_tabla({}, 2)

    assert r"\begin{tabular}" in salida
    assert "Resultado & 2 \\\\" in salida
