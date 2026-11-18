"""
Tests unitarios para la función convertir_energia del módulo
conversor_energia, verificando conversiones entre unidades de energía
y el manejo de valores negativos y unidades desconocidas.
"""

import pytest
from escuadra.modulos.matematicas.conversor_energia import convertir_energia


def test_convertir_julios_a_kilojulios():
    assert convertir_energia(1000, "J", "kJ") == 1.0


def test_convertir_kilovatios_hora_a_vatios_hora():
    assert convertir_energia(1, "kWh", "Wh") == 1000.0


def test_convertir_kilovatios_hora_a_julios():
    assert convertir_energia(1, "kWh", "J") == 3600000.0


def test_convertir_calorias_a_julios():
    assert convertir_energia(1, "cal", "J") == pytest.approx(4.184)


def test_convertir_valor_negativo_lanza_error():
    with pytest.raises(ValueError):
        convertir_energia(-10, "J", "kJ")


def test_convertir_unidad_origen_desconocida_lanza_error():
    with pytest.raises(ValueError):
        convertir_energia(10, "XYZ", "J")


def test_convertir_unidad_destino_desconocida_lanza_error():
    with pytest.raises(ValueError):
        convertir_energia(10, "J", "XYZ")
