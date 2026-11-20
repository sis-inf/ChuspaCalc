import pytest

from chuspacalc.modulos.matematicas.conversor_masa import convertir_masa
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


@pytest.mark.parametrize(
    "valor, origen, destino, esperado",
    [
        (1, "kg", "g", 1000.0),
        (1000, "g", "kg", 1.0),
        (1, "kg", "lb", 1 / 0.453592),
        (1, "t", "kg", 1000.0),
        (1, "kg", "mg", 1_000_000.0),
        (0, "kg", "g", 0.0),
    ],
)
def test_convertir_masa_valida(valor, origen, destino, esperado):
    assert convertir_masa(valor, origen, destino) == pytest.approx(esperado)


@pytest.mark.parametrize(
    "valor",
    ["10", None, True, False, [], 10**1000],
)
def test_rechaza_valores_no_numericos_o_fuera_de_rango(valor):
    with pytest.raises(ErrorValidacion):
        convertir_masa(valor, "kg", "g")


@pytest.mark.parametrize("valor", [-1, -0.5])
def test_rechaza_masas_negativas(valor):
    with pytest.raises(ErrorValidacion, match="no puede ser negativa"):
        convertir_masa(valor, "kg", "g")


@pytest.mark.parametrize(
    "unidad_origen, unidad_destino",
    [
        ("XYZ", "kg"),
        ("kg", "XYZ"),
        (None, "kg"),
        ("kg", None),
    ],
)
def test_rechaza_unidades_desconocidas(unidad_origen, unidad_destino):
    with pytest.raises(ErrorValidacion):
        convertir_masa(1, unidad_origen, unidad_destino)


@pytest.mark.parametrize("valor", [float("nan"), float("inf"), float("-inf")])
def test_rechaza_valores_no_finitos(valor):
    with pytest.raises(ErrorValidacion, match="debe ser finito"):
        convertir_masa(valor, "kg", "g")


def test_rechaza_resultado_no_finito():
    with pytest.raises(ErrorValidacion, match="no es finito"):
        convertir_masa(1.7e308, "kg", "mg")
