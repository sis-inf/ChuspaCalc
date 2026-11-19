"""
Pruebas para el módulo config/loader.py
"""

import os
import tempfile

import pytest
import yaml

from chuspacalc.config.loader import load


class TestConfigLoader:
    """Pruebas para el cargador de configuración"""

    def test_load_valid_yaml(self):
        """Verifica que carga un archivo YAML válido correctamente"""
        config_data = {
            "app": {"name": "ChuspaCalc", "version": "0.1.0"},
            "logging": {"level": "INFO"},
        }

        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
            yaml.dump(config_data, f)
            temp_path = f.name

        try:
            result = load(temp_path)
            assert result == config_data
        finally:
            os.unlink(temp_path)

    def test_load_empty_yaml(self):
        """Verifica que rechaza un archivo YAML vacío indicando el archivo"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
            f.write("")
            temp_path = f.name

        try:
            with pytest.raises(yaml.YAMLError) as excinfo:
                load(temp_path)

            assert temp_path in str(excinfo.value)
        finally:
            os.unlink(temp_path)

    def test_load_raiz_mapa(self, tmp_path):
        """Verifica que una raíz de tipo mapa se carga como antes"""
        archivo = tmp_path / "config.yaml"
        archivo.write_text("font_scale: 1.25\n", encoding="utf-8")

        assert load(str(archivo)) == {"font_scale": 1.25}

    @pytest.mark.parametrize(
        "contenido, tipo",
        [
            ("- a\n- b\n", "list"),
            ("hola\n", "str"),
            ("42\n", "int"),
            ("3.5\n", "float"),
            ("true\n", "bool"),
            ("null\n", "NoneType"),
        ],
    )
    def test_load_raiz_no_mapa(self, tmp_path, contenido, tipo):
        """Verifica que rechaza raíces que no son mapas indicando archivo y tipo"""
        archivo = tmp_path / "config.yaml"
        archivo.write_text(contenido, encoding="utf-8")

        with pytest.raises(yaml.YAMLError) as excinfo:
            load(str(archivo))

        assert str(archivo) in str(excinfo.value)
        assert tipo in str(excinfo.value)

    def test_load_file_not_found(self):
        """Verifica que lanza FileNotFoundError si el archivo no existe"""
        with pytest.raises(FileNotFoundError) as excinfo:
            load("/ruta/inexistente/config.yaml")

        assert "Archivo de configuración no encontrado" in str(excinfo.value)

    def test_load_malformed_yaml(self):
        """Verifica que lanza YAMLError si el archivo está malformado"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
            f.write("invalid: yaml: content: [")
            temp_path = f.name

        try:
            with pytest.raises(yaml.YAMLError) as excinfo:
                load(temp_path)

            assert "Error al parsear el archivo YAML" in str(excinfo.value)
        finally:
            os.unlink(temp_path)

    def test_load_with_comments(self):
        """Verifica que carga YAML con comentarios correctamente"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
            f.write("""
# Comentario
app:
  name: ChuspaCalc  # Comentario inline
  version: 0.1.0
""")
            temp_path = f.name

        try:
            result = load(temp_path)
            assert result["app"]["name"] == "ChuspaCalc"
            assert result["app"]["version"] == "0.1.0"
        finally:
            os.unlink(temp_path)

    def test_load_nested_config(self):
        """Verifica que carga configuración anidada correctamente"""
        config_data = {
            "app": {"name": "ChuspaCalc", "settings": {"debug": True, "theme": "dark"}},
            "database": {"host": "localhost", "port": 5432},
        }

        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
            yaml.dump(config_data, f)
            temp_path = f.name

        try:
            result = load(temp_path)
            assert result["app"]["settings"]["debug"] is True
            assert result["app"]["settings"]["theme"] == "dark"
            assert result["database"]["host"] == "localhost"
            assert result["database"]["port"] == 5432
        finally:
            os.unlink(temp_path)
