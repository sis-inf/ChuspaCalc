import pytest


@pytest.fixture
def tmp_dir(tmp_path):
    """Retorna un directorio temporal para pruebas unitarias."""
    return tmp_path


@pytest.fixture
def datos_numericos():
    """Retorna una lista de datos numéricos para pruebas estadísticas."""
    return [1.0, 2.5, 3.7, 4.2, 5.8]


@pytest.fixture
def config_basica():
    """Retorna una configuración mínima válida del proyecto."""
    return {
        "nombre_proyecto": "Escuadra",
        "version": "1.0",
        "modo_debug": False,
    }
