import pytest

from chuspacalc.modulos.geometria import (
    herramienta_transformaciones as modulo_transformaciones,
)
from chuspacalc.modulos.geometria.herramienta_transformaciones import (
    HerramientaTransformaciones,
)
from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


@pytest.fixture
def herramienta(app_qt):
    """Crea la herramienta gráfica para las pruebas."""
    instancia = HerramientaTransformaciones()
    widget = instancia.crear_widget()

    # Mantiene una referencia al widget durante la prueba.
    instancia._widget_raiz = widget

    yield instancia

    widget.close()
    app_qt.processEvents()


@pytest.mark.parametrize(
    ("indice", "esperado"),
    [
        (0, "Resultado: X = -1.0000, Y = 1.0000"),
        (1, "Resultado: X = 2.0000, Y = 2.0000"),
        (2, "Resultado: X = 2.0000, Y = 2.0000"),
    ],
)
def test_transformaciones_validas_muestran_resultado(
    herramienta,
    indice,
    esperado,
):
    """Comprueba los resultados de las tres transformaciones."""
    herramienta.selector.setCurrentIndex(indice)

    herramienta.aplicar_transformacion()

    assert herramienta.resultado.text() == esperado


def test_escalado_con_factor_cero_es_valido(herramienta):
    """Comprueba que el factor de escala cero sigue siendo válido."""
    herramienta.selector.setCurrentIndex(2)
    herramienta.factor_escala.setValue(0.0)

    herramienta.aplicar_transformacion()

    assert herramienta.resultado.text() == ("Resultado: X = 0.0000, Y = 0.0000")


@pytest.mark.parametrize(
    "valor",
    [
        -1_000_000.0,
        0.0,
        1_000_000.0,
    ],
)
def test_valores_en_limites_permitidos_son_validos(valor):
    """Comprueba que los límites inclusivos son aceptados."""
    resultado = HerramientaTransformaciones._validar_valor(
        valor,
        "coordenada",
        -1_000_000.0,
        1_000_000.0,
    )

    assert resultado == valor


@pytest.mark.parametrize(
    "valor",
    [
        True,
        False,
        "100",
        None,
        float("nan"),
        float("inf"),
        float("-inf"),
        -1_000_001.0,
        1_000_001.0,
    ],
)
def test_valores_invalidos_lanzan_error_validacion(valor):
    """Comprueba el rechazo de tipos incorrectos y valores fuera de rango."""
    with pytest.raises(ErrorValidacion):
        HerramientaTransformaciones._validar_valor(
            valor,
            "coordenada",
            -1_000_000.0,
            1_000_000.0,
        )


def test_error_de_transformacion_se_muestra_en_interfaz(
    herramienta,
    monkeypatch,
):
    """Comprueba que un error matemático se muestra en la etiqueta."""

    def rotacion_invalida(*args):
        raise ErrorValidacion("Parámetro de rotación inválido.")

    monkeypatch.setattr(
        modulo_transformaciones,
        "rotar_punto",
        rotacion_invalida,
    )

    herramienta.selector.setCurrentIndex(0)
    herramienta.aplicar_transformacion()

    assert herramienta.resultado.text() == ("Error: Parámetro de rotación inválido.")


def test_resultados_no_finitos_se_rechazan(
    herramienta,
    monkeypatch,
):
    """Comprueba que la interfaz no muestra resultados NaN o infinitos."""

    def rotacion_no_finita(*args):
        return float("nan"), float("inf")

    monkeypatch.setattr(
        modulo_transformaciones,
        "rotar_punto",
        rotacion_no_finita,
    )

    herramienta.selector.setCurrentIndex(0)
    herramienta.aplicar_transformacion()

    assert herramienta.resultado.text().startswith("Error:")
    assert "finito" in herramienta.resultado.text()


def test_selector_sin_transformacion_muestra_error(herramienta):
    """Comprueba que se rechaza una selección inexistente."""
    herramienta.selector.setCurrentIndex(-1)

    herramienta.aplicar_transformacion()

    assert herramienta.resultado.text() == (
        "Error: Debe seleccionar una transformación válida."
    )
