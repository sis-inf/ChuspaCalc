from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

from chuspacalc.modulos.sistemas import herramienta_tablas_verdad as modulo_tablas
from chuspacalc.modulos.sistemas.herramienta_tablas_verdad import (
    HerramientaTablasVerdad,
)


class _Portapapeles:
    texto = ""

    def setText(self, texto: str) -> None:
        self.texto = texto


class _AplicacionGui:
    portapapeles = _Portapapeles()

    @classmethod
    def clipboard(cls) -> _Portapapeles:
        return cls.portapapeles


class _CuadroMensaje:
    @staticmethod
    def information(*_args) -> None:
        return None


def test_copiar_tabla_admite_encabezado_ausente(qapp, monkeypatch):
    portapapeles = _Portapapeles()
    _AplicacionGui.portapapeles = portapapeles
    monkeypatch.setattr(modulo_tablas, "QGuiApplication", _AplicacionGui)
    monkeypatch.setattr(modulo_tablas, "QMessageBox", _CuadroMensaje)
    herramienta = HerramientaTablasVerdad()
    herramienta.result_table = QTableWidget(1, 1)
    herramienta.result_table.setItem(0, 0, QTableWidgetItem("1"))

    herramienta.copiar_portapapeles()

    assert portapapeles.texto == "\n1\n"
