.DEFAULT_GOAL := help

PYTHON ?= python

.PHONY: help install test test-cov test-ci lint typecheck format quality build run clean clean-dry-run

help:
	@echo "Targets disponibles:"
	@echo "  install        Instalar dependencias de desarrollo"
	@echo "  test           Ejecutar pytest"
	@echo "  test-cov       Ejecutar pruebas con cobertura"
	@echo "  test-ci        Verificar ubicacion de tests y ejecutar pytest como en CI"
	@echo "  lint           Black --check, ruff check y verificacion de PySide6"
	@echo "  typecheck      Ejecutar mypy sobre src/chuspacalc"
	@echo "  format         Aplicar black sobre src/ y tests/"
	@echo "  quality        Ejecutar lint, typecheck y test-ci"
	@echo "  build          Generar paquetes de distribucion"
	@echo "  run            Ejecutar la aplicacion"
	@echo "  clean          Borrar artefactos generados permitidos"
	@echo "  clean-dry-run  Listar lo que borraria clean, sin borrar"

install:
	$(PYTHON) -m pip install -e ".[dev]"
	$(PYTHON) -m pip install -r requirements-dev.txt black
	$(PYTHON) -m pre_commit install

test:
	$(PYTHON) -m pytest

test-cov:
	$(PYTHON) -m pytest --cov=src/chuspacalc tests/

test-ci: export QT_QPA_PLATFORM := offscreen
test-ci:
	bash scripts/verificar-tests-ubicacion.sh
	$(PYTHON) -m pytest -m "not slow" --cov=src/chuspacalc --cov-report=term-missing

lint:
	$(PYTHON) -m black --check src/ tests/
	$(PYTHON) -m ruff check .
	bash scripts/verificar-pyside6.sh

typecheck:
	$(PYTHON) -m mypy src/chuspacalc

format:
	$(PYTHON) -m black src/ tests/

quality: lint typecheck test-ci

build:
	$(PYTHON) -m build

run:
	$(PYTHON) -m chuspacalc

clean:
	$(PYTHON) scripts/clean.py

clean-dry-run:
	$(PYTHON) scripts/clean.py --dry-run
