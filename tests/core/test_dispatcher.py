from unittest.mock import MagicMock, patch

from escuadra.core import dispatcher


def test_despacho_desconocido_devuelve_none():
    with patch("escuadra.core.dispatcher.buscar_por_nombre", return_value=None):
        result = dispatcher.despacho("no_existe")
    assert result is None


def test_despacho_conocido_llama_ejecutar():
    mock_cls = MagicMock()
    mock_instance = MagicMock()
    mock_instance.ejecutar.return_value = "ok"
    mock_cls.return_value = mock_instance

    with patch("escuadra.core.dispatcher.buscar_por_nombre", return_value=mock_cls):
        result = dispatcher.despacho("karnaugh")

    assert result == "ok"
    mock_instance.ejecutar.assert_called_once()
    mock_cls.assert_called_once()


def test_dispatch_alias_devuelve_ejecutar():
    mock_cls = MagicMock()
    mock_instance = MagicMock()
    mock_instance.ejecutar.return_value = 123
    mock_cls.return_value = mock_instance

    with patch("escuadra.core.dispatcher.buscar_por_nombre", return_value=mock_cls):
        result = dispatcher.despacho("karnaugh")

    assert result == 123
