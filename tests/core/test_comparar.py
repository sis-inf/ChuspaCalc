"""
Pruebas unitarias para el módulo comparar.py.
"""

import pytest
from escuadra.core.comparar import comparar_resultados


def test_comparar_resultados_equivalentes_con_tolerancia_por_defecto():
    """Verifica que dos valores cercanos sean equivalentes."""
    resultado = comparar_resultados(1.0, 1.0000001)

    assert resultado["equivalente"] is True


def test_comparar_resultados_no_equivalentes():
    """Verifica que dos valores diferentes no sean equivalentes."""
    resultado = comparar_resultados(1.0, 1.1)

    assert resultado["equivalente"] is False
    assert resultado["diferencia"] == pytest.approx(0.1)


def test_comparar_resultados_con_tolerancia_personalizada():
    """Verifica que una tolerancia de 0.2 permita la equivalencia."""
    resultado = comparar_resultados(1.0, 1.1, tolerancia=0.2)

    assert resultado["equivalente"] is True


def test_comparar_resultados_contiene_claves_requeridas():
    """Verifica que el diccionario contenga todas las claves requeridas."""
    resultado = comparar_resultados(1.0, 1.1)

    claves_esperadas = {
        "equivalente",
        "resultado1",
        "resultado2",
        "diferencia",
        "tolerancia",
    }

    assert set(resultado.keys()) == claves_esperadas
