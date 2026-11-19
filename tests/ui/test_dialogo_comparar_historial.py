"""Pruebas para el diálogo de comparación de historial."""

from unittest.mock import MagicMock, patch

import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion
from chuspacalc.ui.dialogo_comparar_historial import DialogoCompararHistorial

RUTA_MENSAJE = "chuspacalc.ui.dialogo_comparar_historial.mostrar_error_contextualizado"


@pytest.fixture
def mostrar_error(monkeypatch):
    """Intercepta el mensaje de error para no abrir ventanas modales."""
    simulado = MagicMock()
    monkeypatch.setattr(RUTA_MENSAJE, simulado)
    return simulado


def _textos_etiquetas(dialogo):
    return [etiqueta.text() for etiqueta in dialogo.findChildren(QLabel)]


class TestDialogoCompararHistorial:
    """Pruebas para el diálogo de comparación de historial."""

    def test_se_instancia_con_entradas_validas(self, qtbot, mostrar_error):
        """Con entradas válidas se crea el diálogo sin mostrar errores."""
        dialogo = DialogoCompararHistorial({"expresion": "2+2"}, {"expresion": "3+3"})
        qtbot.addWidget(dialogo)

        assert dialogo.windowTitle() == "Comparación de historial"
        mostrar_error.assert_not_called()

    def test_entrada_invalida_muestra_error(self, qtbot, mostrar_error):
        """Una entrada que no es mapeo muestra el error y no rompe el diálogo."""
        dialogo = DialogoCompararHistorial(None, {"expresion": "3+3"})  # type: ignore[arg-type]
        qtbot.addWidget(dialogo)

        mostrar_error.assert_called_once()
        padre, error = mostrar_error.call_args.args
        assert padre is None
        assert isinstance(error, ErrorValidacion)
        assert "entrada 1" in str(error)

    def test_entrada_invalida_usa_paneles_vacios(self, qtbot, mostrar_error):
        """Tras un error de validación ambos paneles indican que no hay datos."""
        dialogo = DialogoCompararHistorial("texto", 5)  # type: ignore[arg-type]
        qtbot.addWidget(dialogo)

        assert dialogo.entrada1 == {}
        assert dialogo.entrada2 == {}
        assert _textos_etiquetas(dialogo).count("No hay datos disponibles.") == 2

    def test_boton_cerrar_esta_conectado(self, qtbot, mostrar_error):
        """Hacer clic en 'Cerrar' dispara el slot y acepta el diálogo."""
        with patch.object(DialogoCompararHistorial, "accept") as aceptar:
            dialogo = DialogoCompararHistorial({"a": 1}, {"a": 2})
            qtbot.addWidget(dialogo)

            qtbot.mouseClick(dialogo.boton_cerrar, Qt.MouseButton.LeftButton)

        aceptar.assert_called_once_with()
        mostrar_error.assert_not_called()

    def test_cerrar_captura_errores_inesperados(self, qtbot, mostrar_error):
        """Si accept() falla, el error se muestra en lugar de propagarse."""
        error = RuntimeError("fallo al cerrar")
        with patch.object(DialogoCompararHistorial, "accept", side_effect=error):
            dialogo = DialogoCompararHistorial({"a": 1}, {"a": 2})
            qtbot.addWidget(dialogo)

            dialogo._on_cerrar()

        mostrar_error.assert_called_once_with(dialogo, error)

    def test_formatear_entrada_escapa_html(self):
        """Los valores se escapan y el campo 'id' se omite."""
        texto = DialogoCompararHistorial._formatear_entrada(
            {"id": 7, "expresion": "<script>alert(1)</script>"}
        )

        assert "&lt;script&gt;" in texto
        assert "<script>" not in texto
        assert "id" not in texto.replace("&lt;", "")

    def test_formatear_entrada_vacia(self):
        """Una entrada vacía devuelve el mensaje de datos no disponibles."""
        assert DialogoCompararHistorial._formatear_entrada({}) == "No hay datos disponibles."
