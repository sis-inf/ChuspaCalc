"""Compatibilidad temporal con el namespace histórico ``escuadra``.

Los submódulos se redirigen a ``chuspacalc`` para que ambos namespaces
compartan los mismos objetos y no creen clases duplicadas.
"""

import sys
from importlib import import_module, util
from importlib.abc import Loader, MetaPathFinder
from importlib.machinery import ModuleSpec
from types import ModuleType
from typing import Sequence

import chuspacalc as _canonical_package
from chuspacalc import __version__ as __version__

__all__ = ["__version__"]
# Mantiene disponible la inspección del paquete para herramientas y plugins.
__path__ = list(_canonical_package.__path__)


class _AliasLoader(Loader):
    """Carga un submódulo antiguo usando el módulo canónico de ChuspaCalc."""

    def __init__(self, canonical_name: str) -> None:
        self._canonical_name = canonical_name

    def create_module(self, spec: ModuleSpec) -> ModuleType:
        return import_module(self._canonical_name)

    def exec_module(self, module: ModuleType) -> None:
        """El módulo canónico ya fue inicializado en ``create_module``."""


class _LegacyNamespaceFinder(MetaPathFinder):
    """Mapea ``escuadra.*`` a ``chuspacalc.*`` sin duplicar importaciones."""

    def find_spec(
        self,
        fullname: str,
        path: Sequence[str] | None = None,
        target: ModuleType | None = None,
    ) -> ModuleSpec | None:
        if not fullname.startswith("escuadra."):
            return None

        canonical_name = f"chuspacalc{fullname[len('escuadra') :]}"
        try:
            canonical_spec = util.find_spec(canonical_name)
        except ModuleNotFoundError as error:
            if error.name == canonical_name:
                return None
            raise

        if canonical_spec is None:
            return None

        is_package = canonical_spec.submodule_search_locations is not None
        loader = _AliasLoader(canonical_name)
        return util.spec_from_loader(fullname, loader, is_package=is_package)


if not any(isinstance(finder, _LegacyNamespaceFinder) for finder in sys.meta_path):
    sys.meta_path.insert(0, _LegacyNamespaceFinder())
