from unittest.mock import MagicMock, patch

from escuadra.ui.cargador_herramienta import CargadorHerramienta


class HerramientaPrueba:
    def crear_widget(self):
        return MagicMock()


def test_cargar_herramienta_exitosamente():
    ventana = MagicMock()
    cargador = CargadorHerramienta(ventana)

    cargador.cargar(HerramientaPrueba)

    ventana.mostrar_herramienta.assert_called_once()
    ventana.mostrar_mensaje_estado.assert_called_once_with(
        "Herramienta activa: HerramientaPrueba"
    )
    assert isinstance(cargador.herramienta_actual(), HerramientaPrueba)


def test_cargar_herramienta_con_error_muestra_error():
    ventana = MagicMock()
    cargador = CargadorHerramienta(ventana)

    class HerramientaConError:
        def crear_widget(self):
            raise RuntimeError("Error de prueba")

    with patch("escuadra.ui.cargador_herramienta.mostrar_error") as mock_mostrar_error:
        cargador.cargar(HerramientaConError)

    mock_mostrar_error.assert_called_once()

    args = mock_mostrar_error.call_args.args
    assert args[0] is ventana
    assert args[1] == "Error al cargar herramienta"
    assert args[2] == "Error de prueba"
