"""Módulos de ChuspaCalc."""

from pathlib import Path

# Los aportes estudiantiles históricos bajo ``src/escuadra/modulos`` se
# descubren también desde el namespace canónico, sin duplicar implementaciones.
_modulos_heredados = Path(__file__).resolve().parents[2] / "escuadra" / "modulos"
if _modulos_heredados.is_dir():
    __path__.append(str(_modulos_heredados))
