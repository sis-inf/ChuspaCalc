def test_mock_config_returns_dict(mock_config):
    """Verifica que la fixture retorna un diccionario"""
    assert isinstance(mock_config, dict)
    assert "database" in mock_config
    assert "api" in mock_config
    assert "logging" in mock_config


def test_mock_config_has_expected_values(mock_config):
    """Verifica que la fixture tiene los valores esperados"""
    assert mock_config["database"]["host"] == "localhost"
    assert mock_config["database"]["port"] == 5432
    assert mock_config["api"]["timeout"] == 30
    assert mock_config["api"]["retries"] == 3
    assert mock_config["logging"]["level"] == "DEBUG"
