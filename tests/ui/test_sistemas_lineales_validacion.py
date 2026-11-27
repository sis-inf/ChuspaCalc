"""Pruebas de validación numérica de la herramienta de sistemas lineales."""

import pytest
from PySide6.QtWidgets import QApplication

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.modulos.matematicas.herramienta_sistemas_lineales import (
    HerramientaSistemasLineales,
    _leer_numero,
)


@pytest.fixture
def app():
    """Fixture para la aplicación Qt."""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


@pytest.fixture
def herramienta(app, qtbot):
    """Herramienta con su widget ya creado."""
    herramienta = HerramientaSistemasLineales()
    widget = herramienta.crear_widget()
    qtbot.addWidget(widget)
    return herramienta


def _llenar_validos(herramienta):
    """Rellena todas las celdas con un valor válido."""
    for fila in herramienta._inputs_A:
        for campo in fila:
            campo.setText("1")
    for campo in herramienta._inputs_b:
        campo.setText("1")


class TestLeerNumero:
    """Pruebas de la función que valida cada campo."""

    def test_numero_valido(self):
        assert _leer_numero(" 2.5 ", "A[1][1]") == 2.5

    def test_texto_invalido(self):
        with pytest.raises(ErrorValidacion, match="inválido en A\\[1\\]\\[2\\]"):
            _leer_numero("abc", "A[1][2]")

    def test_campo_vacio(self):
        with pytest.raises(ErrorValidacion, match="inválido"):
            _leer_numero("", "b[1]")

    @pytest.mark.parametrize("texto", ["nan", "inf", "-inf", "Infinity"])
    def test_no_finitos(self, texto):
        with pytest.raises(ErrorValidacion, match="finito"):
            _leer_numero(texto, "A[1][1]")


class TestResolverConValidacion:
    """Pruebas del método _resolver con datos inválidos."""

    def test_nan_muestra_error(self, herramienta):
        _llenar_validos(herramienta)
        herramienta._inputs_A[0][0].setText("nan")
        herramienta._resolver()

        assert "finito" in herramienta._error_label.text()
        assert herramienta._resultado_label.text() == ""

    def test_infinito_muestra_error(self, herramienta):
        _llenar_validos(herramienta)
        herramienta._inputs_b[0].setText("inf")
        herramienta._resolver()

        assert "finito" in herramienta._error_label.text()

    def test_mensaje_indica_la_celda(self, herramienta):
        _llenar_validos(herramienta)
        herramienta._inputs_A[1][0].setText("xyz")
        herramienta._resolver()

        assert "A[2][1]" in herramienta._error_label.text()

    def test_sistema_singular(self, herramienta):
        _llenar_validos(herramienta)
        herramienta._resolver()

        assert "singular" in herramienta._error_label.text()

    def test_solucion_fuera_de_rango(self, herramienta):
        # Sistema cuya solución es enorme: no debe mostrarse un resultado
        # con infinitos ni con NaN.
        valores_A = [["1", "0"], ["0", "1e-300"]]
        for i, fila in enumerate(valores_A):
            for j, texto in enumerate(fila):
                herramienta._inputs_A[i][j].setText(texto)
        herramienta._inputs_b[0].setText("1")
        herramienta._inputs_b[1].setText("1e300")
        herramienta._resolver()

        texto_error = herramienta._error_label.text()
        texto_resultado = herramienta._resultado_label.text()
        assert "inf" not in texto_resultado.lower()
        assert "nan" not in texto_resultado.lower()
        assert texto_error != "" or texto_resultado != ""
