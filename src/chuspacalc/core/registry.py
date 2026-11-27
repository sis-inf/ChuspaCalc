"""
Registry de herramientas de ChuspaCalc.
Descubre automáticamente todas las clases que heredan de Herramienta
dentro del paquete chuspacalc.modulos.

Mantiene dos estructuras en memoria: un caché con las clases descubiertas
y un diccionario con los metadatos validados mediante `registrar`.
"""

import importlib
import inspect
import logging
import pkgutil
from types import ModuleType

import chuspacalc.modulos as _modulos_pkg
from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta

logger = logging.getLogger(__name__)

# Clases descubiertas; None mientras no se haya hecho el descubrimiento.
_cache: list[type[Herramienta]] | None = None

# Metadatos registrados: {nombre: {"categoria": ..., "descripcion": ...}}.
_registros: dict[str, dict[str, str]] = {}


def descubrir_herramientas() -> list[type[Herramienta]]:
    """
    Recorre el paquete chuspacalc.modulos e importa todos los módulos
    cuyo nombre comience con 'herramienta_'. Devuelve una lista con
    todas las clases encontradas que heredan de Herramienta.

    El resultado se cachea: llamadas posteriores devuelven la lista
    cacheada sin repetir el descubrimiento. Si un módulo no puede
    importarse, se registra el error en el log y se continúa con el resto.

    Returns:
        Lista de clases que heredan de Herramienta.
    """
    global _cache
    if _cache is not None:
        return _cache

    herramientas: list[type[Herramienta]] = []

    for info in pkgutil.walk_packages(
        path=_modulos_pkg.__path__,
        prefix=_modulos_pkg.__name__ + ".",
    ):
        if not info.name.split(".")[-1].startswith("herramienta_"):
            continue

        try:
            modulo: ModuleType = importlib.import_module(info.name)
        except Exception as exc:
            logger.error("No se pudo importar %s: %s", info.name, exc)
            continue

        for _, obj in inspect.getmembers(modulo, inspect.isclass):
            if (
                issubclass(obj, Herramienta)
                and obj is not Herramienta
                and obj.__module__ == modulo.__name__
            ):
                herramientas.append(obj)

    _cache = herramientas
    return _cache


def herramientas_por_carrera() -> dict[Carrera, list[type[Herramienta]]]:
    """
    Devuelve un diccionario agrupando las herramientas por carrera.
    Las herramientas dentro de cada carrera están ordenadas
    alfabéticamente por su atributo nombre. Las herramientas sin carrera
    se omiten y se registra una advertencia en el log.

    Returns:
        Diccionario {Carrera: [clase de herramienta, ...]}, con cada
        lista ordenada por nombre.
    """
    resultado: dict[Carrera, list[type[Herramienta]]] = {}

    for herramienta in descubrir_herramientas():
        carrera: Carrera | None = herramienta.carrera
        if carrera is None:
            logger.warning("Se omitió %s porque no tiene carrera", herramienta.nombre)
            continue
        if carrera not in resultado:
            resultado[carrera] = []
        resultado[carrera].append(herramienta)

    for carrera in resultado:
        resultado[carrera].sort(key=lambda h: h.nombre)

    return resultado


def buscar_por_nombre(nombre: str) -> type[Herramienta] | None:
    """
    Busca una herramienta por su atributo nombre.

    Args:
        nombre: Nombre de la herramienta a buscar.

    Returns:
        La clase de la herramienta, o None si no existe.
    """
    for herramienta in descubrir_herramientas():
        if herramienta.nombre == nombre:
            return herramienta
    return None


def registrar(herramienta: type[Herramienta], metadata: dict[str, str]) -> None:
    """
    Valida y registra los metadatos de una herramienta.

    Los valores se guardan sin espacios al inicio ni al final. Si ya
    existe un registro con el mismo nombre, se reemplaza.

    Args:
        herramienta: Clase de la herramienta a registrar.
        metadata: Diccionario con las claves 'categoria' y 'descripcion'.

    Raises:
        ValueError: Si 'categoria' o 'descripcion' faltan o están vacías.
    """
    categoria = metadata.get("categoria")
    descripcion = metadata.get("descripcion")

    if not categoria or not str(categoria).strip():
        raise ValueError("La metadata debe contener una 'categoria' no vacía.")
    if not descripcion or not str(descripcion).strip():
        raise ValueError("La metadata debe contener una 'descripcion' no vacía.")

    _registros[herramienta.nombre] = {
        "categoria": str(categoria).strip(),
        "descripcion": str(descripcion).strip(),
    }


def obtener_por_categoria(categoria: str) -> list[type[Herramienta]]:
    """
    Devuelve las herramientas descubiertas de la categoría solicitada.

    La categoría se compara con el código de la carrera de cada
    herramienta; no se consultan los metadatos guardados por `registrar`.

    Args:
        categoria: Código de la carrera, por ejemplo "civil".

    Returns:
        Lista de clases de esa carrera, o lista vacía si no hay.
    """
    return [
        herramienta
        for herramienta in descubrir_herramientas()
        if herramienta.carrera is not None and herramienta.carrera.codigo == categoria
    ]


def limpiar_cache() -> None:
    """
    Limpia el cache del descubrimiento para forzar un nuevo escaneo.
    Útil en tests. No borra los metadatos guardados por `registrar`.
    """
    global _cache
    _cache = None
