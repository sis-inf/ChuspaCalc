from unittest.mock import patch

import pytest

from chuspacalc import app


def test_error_secundario_del_dialogo_se_registra_y_conserva_salida():
    error_principal = RuntimeError("fallo principal")
    error_dialogo = RuntimeError("fallo secundario")

    with (
        patch.object(app, "configurar_logging"),
        patch.object(app, "QApplication", side_effect=error_principal),
        patch.object(app.QMessageBox, "critical", side_effect=error_dialogo),
        patch.object(app.logger, "critical") as log_critical,
        patch.object(app.logger, "warning") as log_warning,
        patch.object(app.sys, "exit", side_effect=SystemExit(1)) as salir,
        pytest.raises(SystemExit) as salida,
    ):
        app.main()

    assert salida.value.code == 1
    log_critical.assert_called_once()
    log_warning.assert_called_once()
    assert log_warning.call_args.args[1] is error_dialogo
    assert log_warning.call_args.kwargs["exc_info"] is True
    salir.assert_called_once_with(1)
