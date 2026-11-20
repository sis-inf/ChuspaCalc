import math

import pytest

from chuspacalc.modulos.matematicas.discriminante import calcular_discriminante
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


@pytest.mark.parametrize(
    ("a", "b", "c", "esperado"),
    [
        (1, 5, 6, 1),
        (1, 2, 1, 0),
        (1, 1, 1, -3),
        (1, 0, 0, 0),
        (1, 10**400, 0, 10**800),
    ],
)
def test_calcular_discriminante_valido(a, b, c, esperado):
    assert calcular_discriminante(a, b, c) == esperado


@pytest.mark.parametrize(
    ("a", "b", "c"),
    [
        (0, 2, 1),
        (True, 2, 1),
        (1, False, 1),
        (1, 2, None),
        (1, "2", 1),
        (1, math.inf, 1),
        (1, math.nan, 1),
        (1, -math.inf, 1),
    ],
)
def test_calcular_discriminante_rechaza_coeficientes_invalidos(a, b, c):
    with pytest.raises(ErrorValidacion):
        calcular_discriminante(a, b, c)


def test_calcular_discriminante_rechaza_resultado_infinito():
    with pytest.raises(ErrorValidacion):
        calcular_discriminante(1.0, 1e308, 1.0)
