import pytest

from chuspacalc.modulos.matematicas.conversor_longitud_extendido import (
    convertir_longitud,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def test_convierte_parsec_a_anio_luz():
    assert convertir_longitud(1, "pc", "al") == pytest.approx(3.086e16 / 9.461e15)


def test_convierte_milla_nautica_a_metros():
    assert convertir_longitud(1, "mn", "m") == pytest.approx(1852.0)


def test_normaliza_espacios_y_mayusculas():
    assert convertir_longitud(1, " KM ", "M") == pytest.approx(1000.0)


@pytest.mark.parametrize("valor", [True, False, "1", None, [1]])
def test_rechaza_tipos_invalidos(valor):
    with pytest.raises(ErrorValidacion, match="número real"):
        convertir_longitud(valor, "m", "km")


@pytest.mark.parametrize("valor", [float("nan"), float("inf"), float("-inf")])
def test_rechaza_no_finitos(valor):
    with pytest.raises(ErrorValidacion, match="debe ser finito"):
        convertir_longitud(valor, "m", "km")


def test_rechaza_negativos():
    with pytest.raises(ErrorValidacion, match="no puede ser negativo"):
        convertir_longitud(-1, "m", "km")


@pytest.mark.parametrize(
    ("origen", "destino", "mensaje"),
    [
        ("xx", "m", "Unidad origen no reconocida"),
        ("m", "xx", "Unidad destino no reconocida"),
        (1, "m", "deben ser texto"),
        ("m", None, "deben ser texto"),
    ],
)
def test_rechaza_unidades_invalidas(origen, destino, mensaje):
    with pytest.raises(ErrorValidacion, match=mensaje):
        convertir_longitud(1, origen, destino)


def test_rechaza_resultado_desbordado():
    with pytest.raises(ErrorValidacion, match="no es finito"):
        convertir_longitud(1e308, "pc", "mm")
