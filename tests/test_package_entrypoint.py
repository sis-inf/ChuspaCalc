"""Pruebas del punto de entrada del paquete chuspacalc."""

import os
import runpy
import subprocess
import sys
from unittest.mock import Mock

import pytest


def test_modulo_invoca_cli_main_una_sola_vez(monkeypatch: pytest.MonkeyPatch) -> None:
    """Ejecutar el paquete llama exactamente una vez a cli.main."""
    main_falso = Mock()
    monkeypatch.setattr("chuspacalc.cli.main", main_falso)

    runpy.run_module("chuspacalc", run_name="__main__")

    main_falso.assert_called_once_with()


@pytest.mark.parametrize("codigo", [0, 1, 2, 130])
def test_modulo_propaga_codigo_de_system_exit(
    monkeypatch: pytest.MonkeyPatch, codigo: int
) -> None:
    """El código de SystemExit de cli.main se conserva sin cambios."""
    main_falso = Mock(side_effect=SystemExit(codigo))
    monkeypatch.setattr("chuspacalc.cli.main", main_falso)

    with pytest.raises(SystemExit) as excinfo:
        runpy.run_module("chuspacalc", run_name="__main__")

    assert excinfo.value.code == codigo
    main_falso.assert_called_once_with()


def test_help_termina_correctamente_sin_gui() -> None:
    """La opción --help finaliza con código 0 sin abrir una interfaz gráfica."""
    entorno = {
        **os.environ,
        "QT_QPA_PLATFORM": "offscreen",
        "PYTHONIOENCODING": "utf-8",
        "NO_COLOR": "1",
    }

    resultado = subprocess.run(
        [sys.executable, "-m", "chuspacalc", "--help"],
        capture_output=True,
        encoding="utf-8",
        env=entorno,
        timeout=60,
        check=False,
    )

    assert resultado.returncode == 0, resultado.stderr
    assert "chuspacalc" in resultado.stdout
    assert "--help" in resultado.stdout
