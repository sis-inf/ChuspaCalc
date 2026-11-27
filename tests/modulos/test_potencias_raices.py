"""
Tests unitarios para las funciones del módulo potencias_raices,
verificando potencias, raíces y logaritmos, así como el manejo de
valores fuera de dominio.
"""

import pytest

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.matematicas.potencias_raices import (
    logaritmo_base,
    logaritmo_base10,
    logaritmo_natural,
    potencia,
    raiz_cuadrada,
    raiz_n,
)


def test_potencia_de_2_elevado_a_10():
    # 2 elevado a la 10 es 1024
    assert potencia(2, 10) == 1024.0


def test_raiz_cuadrada_de_9():
    # La raíz cuadrada de 9 es 3
    assert raiz_cuadrada(9) == 3.0


def test_raiz_cuadrada_de_negativo_lanza_error():
    # No existe raíz cuadrada real de un número negativo
    with pytest.raises(ValueError):
        raiz_cuadrada(-1)


def test_raiz_n_cubica_de_27():
    # La raíz cúbica de 27 es 3 (con tolerancia por el cálculo en decimales)
    assert raiz_n(27, 3) == pytest.approx(3.0)


def test_raiz_n_par_de_negativo_lanza_error():
    # No existe raíz par real de un número negativo
    with pytest.raises(ValueError):
        raiz_n(-8, 2)


def test_raiz_n_con_indice_cero_lanza_error():
    # El índice n debe ser mayor que 0
    with pytest.raises(ValueError):
        raiz_n(4, 0)


def test_logaritmo_natural_de_1_es_cero():
    # ln(1) es 0
    assert logaritmo_natural(1) == 0.0


def test_logaritmo_base10_de_1000():
    # log10(1000) es 3
    assert logaritmo_base10(1000) == pytest.approx(3.0)


def test_logaritmo_base_2_de_8():
    # log en base 2 de 8 es 3
    assert logaritmo_base(8, 2) == pytest.approx(3.0)


def test_logaritmo_base_1_lanza_error():
    # La base debe ser positiva y distinta de 1
    with pytest.raises(ValueError):
        logaritmo_base(8, 1)


def test_logaritmo_natural_de_cero_lanza_error():
    # El logaritmo solo está definido para valores mayores que 0
    with pytest.raises(ValueError):
        logaritmo_natural(0)


@pytest.mark.parametrize("valor", [float("nan"), float("inf"), float("-inf")])
def test_funciones_rechazan_no_finitos(valor):
    for funcion in (
        raiz_cuadrada,
        logaritmo_natural,
        logaritmo_base10,
    ):
        with pytest.raises(ErrorValidacion):
            funcion(valor)
    with pytest.raises(ErrorValidacion):
        potencia(valor, 2)
    with pytest.raises(ErrorValidacion):
        potencia(2, valor)
    with pytest.raises(ErrorValidacion):
        raiz_n(valor, 3)
    with pytest.raises(ErrorValidacion):
        logaritmo_base(valor, 2)
    with pytest.raises(ErrorValidacion):
        logaritmo_base(8, valor)


@pytest.mark.parametrize("valor", [True, False])
def test_funciones_rechazan_booleanos(valor):
    with pytest.raises(ErrorValidacion):
        potencia(valor, 2)
    with pytest.raises(ErrorValidacion):
        potencia(2, valor)
    with pytest.raises(ErrorValidacion):
        raiz_cuadrada(valor)
    with pytest.raises(ErrorValidacion):
        raiz_n(valor, 2)
    with pytest.raises(ErrorValidacion):
        raiz_n(4, valor)
    with pytest.raises(ErrorValidacion):
        logaritmo_natural(valor)
    with pytest.raises(ErrorValidacion):
        logaritmo_base10(valor)
    with pytest.raises(ErrorValidacion):
        logaritmo_base(8, valor)


def test_cero_con_exponente_negativo_lanza_error_validacion():
    with pytest.raises(ErrorValidacion):
        potencia(0, -1)


def test_raiz_par_de_negativo_lanza_error_validacion():
    with pytest.raises(ErrorValidacion):
        raiz_n(-8, 2)
    with pytest.raises(ErrorValidacion):
        raiz_cuadrada(-1)


@pytest.mark.parametrize("base", [0, -2, 1])
def test_bases_logaritmicas_invalidas_lanzan_error_validacion(base):
    with pytest.raises(ErrorValidacion):
        logaritmo_base(8, base)


def test_potencia_con_resultado_desbordado_lanza_error_validacion():
    with pytest.raises(ErrorValidacion):
        potencia(10.0, 400)


def test_resultados_validos_no_cambian():
    assert potencia(2, 10) == 1024.0
    assert raiz_n(-27, 3) == pytest.approx(-3.0)
    assert logaritmo_base(8, 2) == pytest.approx(3.0)
