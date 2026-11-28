"""
Pruebas unitarias para el solucionador de ecuaciones lineales 2x2
"""

import math
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from chuspacalc.math.linear_solver import solve_linear_2x2
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def test_solve_linear_2x2_simple():
    """Caso simple: sistema con solución única"""
    result = solve_linear_2x2(2, 3, 1, 4, 5, 6)
    assert result is not None
    x, y = result
    assert abs(2 * x + 3 * y - 5) < 1e-10
    assert abs(1 * x + 4 * y - 6) < 1e-10


def test_solve_linear_2x2_identity():
    """Matriz identidad: x = b1, y = b2"""
    result = solve_linear_2x2(1, 0, 0, 1, 10, 20)
    assert result == (10, 20)


def test_solve_linear_2x2_zero_determinant():
    """Determinante cero: sistema sin solución única"""
    result = solve_linear_2x2(1, 1, 1, 1, 2, 3)
    assert result is None


def test_solve_linear_2x2_negative_values():
    """Coeficientes negativos"""
    result = solve_linear_2x2(-2, 3, 1, -4, -5, 6)
    assert result is not None
    x, y = result
    assert abs(-2 * x + 3 * y + 5) < 1e-10
    assert abs(1 * x - 4 * y - 6) < 1e-10


def test_solve_linear_2x2_zero_coefficients():
    """Coeficientes cero en algunas posiciones"""
    result = solve_linear_2x2(0, 2, 3, 0, 4, 6)
    assert result is not None
    x, y = result
    assert abs(0 * x + 2 * y - 4) < 1e-10
    assert abs(3 * x + 0 * y - 6) < 1e-10


@pytest.mark.parametrize("no_finito", [math.nan, math.inf, -math.inf])
@pytest.mark.parametrize("posicion", range(6))
def test_solve_linear_2x2_rechaza_valores_no_finitos(posicion, no_finito):
    """NaN, inf y -inf en cualquier coeficiente o término independiente"""
    datos = [2, 3, 1, 4, 5, 6]
    datos[posicion] = no_finito

    with pytest.raises(ValueError, match="debe ser finito"):
        solve_linear_2x2(*datos)


@pytest.mark.parametrize("invalido", [None, "2", True, [1], 1 + 2j])
@pytest.mark.parametrize("posicion", range(6))
def test_solve_linear_2x2_rechaza_tipos_invalidos(posicion, invalido):
    """None, texto, bool, listas y complejos lanzan ErrorValidacion"""
    datos = [2, 3, 1, 4, 5, 6]
    datos[posicion] = invalido

    with pytest.raises(ErrorValidacion, match="número real"):
        solve_linear_2x2(*datos)


def test_solve_linear_2x2_no_finito_lanza_error_validacion():
    with pytest.raises(ErrorValidacion, match="debe ser finito"):
        solve_linear_2x2(math.nan, 3, 1, 4, 5, 6)


def test_solve_linear_2x2_entero_enorme_lanza_error_validacion():
    with pytest.raises(ErrorValidacion, match="debe ser finito"):
        solve_linear_2x2(10**400, 3, 1, 4, 5, 6)


def test_solve_linear_2x2_determinante_no_finito_lanza_error_validacion():
    with pytest.raises(ErrorValidacion, match="no es finito"):
        solve_linear_2x2(1e200, 0, 0, 1e200, 1, 1)
