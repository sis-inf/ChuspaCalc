import pytest

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.matematicas.herramienta_conversion_unidades import (
    HerramientaConversionUnidades,
)


@pytest.fixture
def herramienta():
    return HerramientaConversionUnidades()


def test_convierte_km_a_m(herramienta):
    assert herramienta.convertir_lineal(1, "km", "m", "Longitud") == pytest.approx(
        1000.0
    )


def test_convierte_horas_a_minutos(herramienta):
    assert herramienta.convertir_lineal(2, "h", "min", "Tiempo") == pytest.approx(120.0)


def test_convierte_kg_a_g(herramienta):
    assert herramienta.convertir_lineal(1.5, "kg", "g", "Masa") == pytest.approx(1500.0)


def test_convierte_celsius_a_fahrenheit(herramienta):
    assert herramienta.convertir_temperatura(100, "°C", "°F") == pytest.approx(212.0)


def test_convierte_fahrenheit_a_kelvin(herramienta):
    assert herramienta.convertir_temperatura(32, "°F", "K") == pytest.approx(273.15)


def test_convierte_kelvin_a_celsius(herramienta):
    assert herramienta.convertir_temperatura(0, "K", "°C") == pytest.approx(-273.15)


def test_cero_absoluto_es_valido(herramienta):
    assert herramienta.convertir_temperatura(-273.15, "°C", "K") == pytest.approx(0.0)


@pytest.mark.parametrize("valor", [True, False, "1", None, [1]])
def test_lineal_rechaza_tipos_invalidos(herramienta, valor):
    with pytest.raises(ErrorValidacion, match="número finito"):
        herramienta.convertir_lineal(valor, "m", "km", "Longitud")


@pytest.mark.parametrize("valor", [float("nan"), float("inf"), float("-inf")])
def test_lineal_rechaza_no_finitos(herramienta, valor):
    with pytest.raises(ErrorValidacion, match="número finito"):
        herramienta.convertir_lineal(valor, "m", "km", "Longitud")


def test_lineal_rechaza_entero_demasiado_grande(herramienta):
    with pytest.raises(ErrorValidacion, match="demasiado grande"):
        herramienta.convertir_lineal(10**400, "m", "km", "Longitud")


@pytest.mark.parametrize("categoria", ["Volumen", "Temperatura", "", None, 5])
def test_lineal_rechaza_categoria_invalida(herramienta, categoria):
    with pytest.raises(ErrorValidacion, match="Categoría inválida"):
        herramienta.convertir_lineal(1, "m", "km", categoria)


def test_lineal_rechaza_unidad_origen_invalida(herramienta):
    with pytest.raises(ErrorValidacion, match="Unidad de origen inválida"):
        herramienta.convertir_lineal(1, "xx", "m", "Longitud")


def test_lineal_rechaza_unidad_destino_invalida(herramienta):
    with pytest.raises(ErrorValidacion, match="Unidad de destino inválida"):
        herramienta.convertir_lineal(1, "m", "kg", "Longitud")


@pytest.mark.parametrize("unidad", [None, 5, ["m"]])
def test_lineal_rechaza_unidad_no_texto(herramienta, unidad):
    with pytest.raises(ErrorValidacion, match="debe ser texto"):
        herramienta.convertir_lineal(1, unidad, "m", "Longitud")


def test_lineal_rechaza_resultado_desbordado(herramienta):
    with pytest.raises(ErrorValidacion, match="no es finito"):
        herramienta.convertir_lineal(1e308, "d", "s", "Tiempo")


@pytest.mark.parametrize("valor", [True, "1", None, float("nan"), float("inf")])
def test_temperatura_rechaza_valores_invalidos(herramienta, valor):
    with pytest.raises(ErrorValidacion, match="número finito"):
        herramienta.convertir_temperatura(valor, "°C", "K")


def test_temperatura_rechaza_unidad_invalida(herramienta):
    with pytest.raises(ErrorValidacion, match="Unidad de origen inválida"):
        herramienta.convertir_temperatura(10, "C", "K")
    with pytest.raises(ErrorValidacion, match="Unidad de destino inválida"):
        herramienta.convertir_temperatura(10, "°C", "R")


def test_temperatura_rechaza_unidad_no_texto(herramienta):
    with pytest.raises(ErrorValidacion, match="debe ser texto"):
        herramienta.convertir_temperatura(10, None, "K")


@pytest.mark.parametrize(("valor", "unidad"), [(-274, "°C"), (-460, "°F"), (-1, "K")])
def test_temperatura_rechaza_bajo_cero_absoluto(herramienta, valor, unidad):
    with pytest.raises(ErrorValidacion, match="cero absoluto"):
        herramienta.convertir_temperatura(valor, unidad, "°C")
