import pytest

from chuspacalc.modulos.civil.momento_flector import (
    calcular_momento_max,
    calcular_momento_maximo,
)


def test_momento_max_conserva_contrato_estructurado_puntual():
    resultado = calcular_momento_max(4, 10, "puntual_central")

    assert resultado == {
        "momento_max": pytest.approx(10.0),
        "posicion": pytest.approx(2.0),
        "unidad": "kN·m",
    }


def test_momento_max_conserva_contrato_estructurado_distribuido():
    resultado = calcular_momento_max(4, 10, "distribuida")

    assert resultado["momento_max"] == pytest.approx(20.0)
    assert resultado["posicion"] == pytest.approx(2.0)
    assert resultado["unidad"] == "kN·m"


def test_momento_maximo_conserva_contrato_escalar_y_orden_de_parametros():
    assert calcular_momento_maximo(carga=10, longitud=4) == pytest.approx(10.0)


@pytest.mark.parametrize("valor", [0, -1, float("nan"), float("inf"), True, "4"])
@pytest.mark.parametrize("parametro", ["longitud", "carga"])
def test_ambos_contratos_rechazan_parametros_invalidos(parametro, valor):
    valores = {"longitud": 4, "carga": 10}
    valores[parametro] = valor

    with pytest.raises(ValueError):
        calcular_momento_max(**valores)

    with pytest.raises(ValueError):
        calcular_momento_maximo(carga=valores["carga"], longitud=valores["longitud"])


def test_momento_max_rechaza_tipo_de_carga_desconocido():
    with pytest.raises(ValueError, match="El tipo de carga debe ser"):
        calcular_momento_max(4, 10, "triangular")
