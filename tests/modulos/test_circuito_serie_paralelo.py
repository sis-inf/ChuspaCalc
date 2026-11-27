"""
Pruebas unitarias para circuito_serie_paralelo.py.
"""

import pytest

from chuspacalc.modulos.electrica.circuito_serie_paralelo import (
    resistencia_paralelo,
    resistencia_serie,
)


def test_tres_resistencias_iguales_en_serie():
    assert resistencia_serie(10, 10, 10) == pytest.approx(30.0)


def test_serie_acepta_lista():
    assert resistencia_serie([5, 15]) == pytest.approx(20.0)


def test_dos_resistencias_iguales_en_paralelo():
    assert resistencia_paralelo(10, 10) == pytest.approx(5.0)


def test_paralelo_resistencias_distintas():
    assert resistencia_paralelo(30, 60) == pytest.approx(20.0)


def test_red_mixta_serie_con_paralelo():
    # 10 ohm en serie con dos de 20 ohm en paralelo (10 ohm) -> 20 ohm
    rama_paralela = resistencia_paralelo(20, 20)
    assert resistencia_serie(10, rama_paralela) == pytest.approx(20.0)


def test_resistencia_cero_es_rechazada():
    # El modulo no admite ramas de 0 ohm (cortocircuito).
    with pytest.raises(ValueError):
        resistencia_paralelo(10, 0)


@pytest.mark.parametrize("funcion", [resistencia_serie, resistencia_paralelo])
def test_resistencia_negativa_lanza_error(funcion):
    with pytest.raises(ValueError):
        funcion(10, -5)
