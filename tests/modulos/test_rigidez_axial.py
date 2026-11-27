import pytest

from chuspacalc.modulos.civil.rigidez_axial import calcular_rigidez_axial
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


@pytest.mark.parametrize("indice", [0, 1, 2])
@pytest.mark.parametrize(
    "invalido",
    [
        None,
        True,
        False,
        "1",
        1j,
        float("nan"),
        float("inf"),
        -float("inf"),
        10**400,
        0,
        -1,
    ],
)
def test_rigidez_rechaza_parametros_invalidos(indice, invalido):
    parametros = [200e9, 0.01, 2]
    parametros[indice] = invalido
    with pytest.raises(ErrorValidacion):
        calcular_rigidez_axial(*parametros)


@pytest.mark.parametrize(
    "elasticidad, area, longitud, esperado",
    [
        (200e9, 0.01, 2, 1e9),
        (10, 3, 2, 15),
        (1e308, 2, 2, 1e308),
        (1e-308, 1e-308, 1e-308, 1e-308),
    ],
)
def test_rigidez_conserva_formula_incluso_si_un_intermedio_no_es_representable(
    elasticidad, area, longitud, esperado
):
    assert calcular_rigidez_axial(elasticidad, area, longitud) == pytest.approx(
        esperado, abs=0
    )


@pytest.mark.parametrize("parametros", [(1e308, 1e308, 1), (5e-324, 5e-324, 1)])
def test_rigidez_rechaza_resultado_no_representable(parametros):
    with pytest.raises(ErrorValidacion):
        calcular_rigidez_axial(*parametros)
