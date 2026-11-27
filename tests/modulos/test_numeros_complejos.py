"""
Tests unitarios para las funciones del módulo numeros_complejos,
verificando las operaciones aritméticas, el módulo, el conjugado y las
conversiones entre forma rectangular y polar.
"""

import math

import pytest

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.matematicas.numeros_complejos import (
    conjugado,
    dividir,
    modulo,
    multiplicar,
    polar_a_rectangular,
    rectangular_a_polar,
    restar,
    sumar,
)


def test_sumar_dos_complejos():
    # (1+2j) + (3+4j) = 4+6j
    assert sumar(1 + 2j, 3 + 4j) == 4 + 6j


def test_restar_dos_complejos():
    # (3+4j) - (1+2j) = 2+2j
    assert restar(3 + 4j, 1 + 2j) == 2 + 2j


def test_multiplicar_dos_complejos():
    # (1+2j) * (3+4j) = -5+10j
    assert multiplicar(1 + 2j, 3 + 4j) == -5 + 10j


def test_dividir_entre_cero_lanza_error():
    # No se puede dividir entre un complejo igual a cero
    with pytest.raises(ZeroDivisionError):
        dividir(1 + 0j, 0j)


def test_modulo_de_3_mas_4j():
    # |3+4j| = 5 (triángulo 3-4-5)
    assert modulo(3 + 4j) == 5.0


def test_conjugado_de_3_mas_4j():
    # El conjugado de 3+4j es 3-4j
    assert conjugado(3 + 4j) == 3 - 4j


def test_rectangular_a_polar_de_j():
    # 1j tiene módulo 1 y ángulo pi/2 (con tolerancia por los decimales)
    assert rectangular_a_polar(1j) == pytest.approx((1.0, math.pi / 2))


def test_polar_a_rectangular_con_angulo_cero():
    # Módulo 2 y ángulo 0 equivale a 2+0j
    assert polar_a_rectangular(2, 0) == 2 + 0j


def test_polar_a_rectangular_con_modulo_negativo_lanza_error():
    # El módulo no puede ser negativo
    with pytest.raises(ValueError):
        polar_a_rectangular(-1, 0)


@pytest.mark.parametrize(
    "dividendo, divisor, esperado",
    [
        (complex(1e308, 1e308), complex(1e308, 1e308), 1 + 0j),
        (1 + 1j, complex(1e308, 1e308), complex(1e-308, 0)),
        (complex(1e308, 0), complex(1e308, 1e308), 0.5 - 0.5j),
        (complex(-1e308, 1e308), complex(1e308, 1e308), 1j),
        (complex(1e308, 1e308), complex(-1e308, -1e308), -1 + 0j),
    ],
)
def test_division_de_complejos_finitos_no_rechaza_cociente_representable(
    dividendo, divisor, esperado
):
    resultado = dividir(dividendo, divisor)
    assert math.isfinite(resultado.real)
    assert math.isfinite(resultado.imag)
    assert resultado.real == pytest.approx(esperado.real, rel=1e-14, abs=0)
    assert resultado.imag == pytest.approx(esperado.imag, rel=1e-14, abs=0)


def test_division_grande_conserva_resultado_pequeno_representable():
    resultado = dividir(complex(1e-308, 1e-308), 1 + 1j)
    assert resultado.real == pytest.approx(1e-308, abs=0)
    assert resultado.imag == 0


def test_division_rechaza_cociente_fuera_de_rango():
    with pytest.raises(ErrorValidacion, match="rango"):
        dividir(complex(1e308, 1e308), complex(1e-308, 0))
