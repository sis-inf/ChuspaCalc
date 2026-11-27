.DEFAULT_GOAL := help

.PHONY: help install test test-cov lint format build run clean

help:
	@echo "Targets disponibles:"
	@echo "  install       Instalar dependencias de desarrollo"
	@echo "  test          Ejecutar pruebas"
	@echo "  test-cov      Ejecutar pruebas con cobertura"
	@echo "  lint          Ejecutar ruff check"
	@echo "  format        Aplicar ruff format"
	@echo "  build         Generar paquetes de distribución"
	@echo "  run           Ejecutar la aplicación"
	@echo "  clean         Limpiar archivos temporales"

install:
	pip install -e ".[dev]"
	pre-commit install

test:
	pytest

test-cov:
	pytest --cov=src/chuspacalc tests/

lint:
	ruff check .

format:
	ruff format .

build:
	python -m build

run:
	python -m chuspacalc

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf htmlcov
