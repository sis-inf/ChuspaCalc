import os

import pytest
from PySide6.QtWidgets import QApplication

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")


@pytest.fixture(scope="session")
def app_qt():
    """
    QApplication reutilizable para tests de componentes Qt
    en modo headless/offscreen.
    """
    app = QApplication.instance()

    if app is None:
        app = QApplication([])

    return app


@pytest.fixture
def mock_config():
    """Fixture que simula la carga de configuración YAML sin archivo real"""
    return {
        "database": {"host": "localhost", "port": 5432, "name": "test_db"},
        "api": {"timeout": 30, "retries": 3},
        "logging": {"level": "DEBUG", "file": "test.log"},
    }
