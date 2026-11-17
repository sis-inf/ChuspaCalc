"""
Pruebas unitarias para el módulo combinacion_cargas.

Verifica las combinaciones de cargas mediante el método LRFD,
incluyendo factores personalizados y cargas en cero.
"""

import pytest

from chuspacalc.modulos.civil.combinacion_cargas import (
    combinar_cargas_lrfd,
)


def test_combinar_cargas_lrfd_valores_predeterminados():
    resultado = combinar_cargas_lrfd(10, 5)

    assert resultado == pytest.approx(20.0)


def test_combinar_cargas_lrfd_solo_carga_muerta():
    resultado = combinar_cargas_lrfd(
        carga_muerta=10,
        carga_viva=5,
        factor_muerta=1.4,
        factor_viva=0,
    )

    assert resultado == pytest.approx(14.0)


def test_combinar_cargas_lrfd_cargas_en_cero():
    resultado = combinar_cargas_lrfd(0, 0)

    assert resultado == pytest.approx(0.0)


def test_combinar_cargas_lrfd_factores_personalizados():
    resultado = combinar_cargas_lrfd(
        carga_muerta=10,
        carga_viva=5,
        factor_muerta=1.0,
        factor_viva=1.0,
    )

    assert resultado == pytest.approx(15.0)
