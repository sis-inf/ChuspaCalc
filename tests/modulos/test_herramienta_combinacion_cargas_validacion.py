import pytest

from chuspacalc.modulos.civil.herramienta_combinacion_cargas import (
    HerramientaCombinacionCargas,
    _validar_carga,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


@pytest.mark.parametrize(
    "valor",
    [-1, float("nan"), float("inf"), float("-inf"), True, "5", None],
)
def test_validar_carga_rechaza_valores_invalidos(valor):
    with pytest.raises(ErrorValidacion):
        _validar_carga("La carga muerta", valor)


@pytest.mark.parametrize("valor", [0, 5, 5.5])
def test_validar_carga_acepta_cero_y_positivos(valor):
    assert _validar_carga("La carga muerta", valor) == valor


def test_calcular_con_valor_no_finito_muestra_error(qtbot, monkeypatch):
    herramienta = HerramientaCombinacionCargas()
    widget = herramienta.crear_widget()
    qtbot.addWidget(widget)

    monkeypatch.setattr(herramienta._carga_muerta, "value", lambda: float("nan"))

    herramienta._calcular()

    assert herramienta._resultado.text().startswith("Error:")
