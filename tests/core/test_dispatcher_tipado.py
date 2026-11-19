from unittest.mock import MagicMock, patch

from chuspacalc.core.dispatcher import dispatch


def test_dispatch_rechaza_herramienta_sin_contrato_ejecutable(capsys) -> None:
    herramienta = MagicMock()
    herramienta.return_value = object()

    with patch("chuspacalc.core.registry.buscar_por_nombre", return_value=herramienta):
        assert dispatch("sin_ejecutar") == 1

    assert "no es ejecutable" in capsys.readouterr().err
