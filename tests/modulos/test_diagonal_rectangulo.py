import pytest

from chuspacalc.modulos.geometria.diagonal_rectangulo import (
    calcular_diagonal_rectangulo,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def test_diagonal_rectangulo_valida():
    assert calcular_diagonal_rectangulo(3, 4) == 5.0
    assert calcular_diagonal_rectangulo(5, 12) == 13.0


def test_diagonal_rectangulo_decimales():
    assert calcular_diagonal_rectangulo(1.5, 2.0) == pytest.approx(2.5)


@pytest.mark.parametrize(
    ("base", "altura"),
    [
        (0, 4),
        (3, 0),
        (-3, 4),
        (3, -4),
        (float("nan"), 4),
        (3, float("nan")),
        (float("inf"), 4),
        (3, float("-inf")),
        ("3", 4),
        (3, "4"),
        (True, 4),
        (3, False),
        (None, 4),
        (4, None),
    ],
)
def test_diagonal_rectangulo_parametros_invalidos(base, altura):
    with pytest.raises(ErrorValidacion):
        calcular_diagonal_rectangulo(base, altura)


def test_diagonal_rectangulo_resultado_no_finito():
    with pytest.raises(ErrorValidacion):
        calcular_diagonal_rectangulo(1.7e308, 1.7e308)
