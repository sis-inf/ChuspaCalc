"""
Limpieza portátil de artefactos generados dentro del repositorio.

Solo elimina los nombres de una lista explícita, no sigue enlaces
simbólicos ni uniones de Windows y valida todos los destinos antes de
borrar el primero.

Uso:
    python scripts/clean.py [--dry-run]
"""

import argparse
import os
import shutil
import stat
import sys
from pathlib import Path

RAIZ_REPOSITORIO = Path(__file__).resolve().parent.parent

# Directorios que se eliminan en cualquier nivel del repositorio.
DIRECTORIOS_EN_CUALQUIER_NIVEL = frozenset(
    {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
)
# Directorios que solo se eliminan en la raíz del repositorio.
DIRECTORIOS_EN_RAIZ = frozenset({"htmlcov", "build", "dist"})
EXTENSION_PERMITIDA = ".pyc"
# Directorios en los que nunca se entra.
DIRECTORIOS_PROTEGIDOS = frozenset({".git", ".venv", "venv", "env", "node_modules"})


class DestinoInseguroError(Exception):
    """Un destino es ambiguo, es un enlace o queda fuera del repositorio."""


def es_enlace(ruta: Path) -> bool:
    """
    Indica si la ruta es un enlace simbólico, una unión o un punto de montaje.

    Args:
        ruta: Ruta existente que se va a inspeccionar.

    Returns:
        True si recorrer la ruta podría llevar a otra ubicación.
    """
    info = os.lstat(ruta)
    atributos = getattr(info, "st_file_attributes", 0)
    return (
        stat.S_ISLNK(info.st_mode)
        or bool(atributos & stat.FILE_ATTRIBUTE_REPARSE_POINT)
        or os.path.ismount(ruta)
    )


def _validar_destino(ruta: Path, raiz: Path) -> None:
    """
    Comprueba que un destino y todo su contenido se puedan borrar.

    Args:
        ruta: Destino candidato.
        raiz: Raíz resuelta del repositorio.

    Raises:
        DestinoInseguroError: Si hay un enlace o la ruta sale del repositorio.
    """
    if es_enlace(ruta):
        raise DestinoInseguroError(f"{ruta} es un enlace o una unión")

    resuelta = ruta.resolve()
    if resuelta != ruta or raiz not in resuelta.parents:
        raise DestinoInseguroError(f"{ruta} apunta fuera de su ubicación esperada")

    if ruta.is_dir():
        for hijo in ruta.iterdir():
            _validar_destino(hijo, raiz)


def buscar_destinos(raiz: Path) -> list[Path]:
    """
    Busca y valida los artefactos que se pueden eliminar.

    Args:
        raiz: Raíz del repositorio.

    Returns:
        Lista ordenada de destinos validados.

    Raises:
        DestinoInseguroError: Si algún destino es ambiguo o inseguro.
        OSError: Si no se puede leer algún directorio.
    """
    raiz = raiz.resolve()
    destinos: list[Path] = []
    pendientes = [raiz]

    while pendientes:
        actual = pendientes.pop()
        for ruta in actual.iterdir():
            nombre = ruta.name
            if nombre in DIRECTORIOS_PROTEGIDOS:
                continue

            es_directorio_permitido = nombre in DIRECTORIOS_EN_CUALQUIER_NIVEL or (
                actual == raiz and nombre in DIRECTORIOS_EN_RAIZ
            )
            es_archivo_permitido = ruta.suffix == EXTENSION_PERMITIDA

            if es_directorio_permitido or es_archivo_permitido:
                _validar_destino(ruta, raiz)
                tipo_correcto = (
                    ruta.is_dir() if es_directorio_permitido else ruta.is_file()
                )
                if not tipo_correcto:
                    raise DestinoInseguroError(f"{ruta} no es del tipo esperado")
                destinos.append(ruta)
            elif (
                not es_enlace(ruta)
                and ruta.is_dir()
                # Un entorno virtual con otro nombre tampoco se toca.
                and not (ruta / "pyvenv.cfg").exists()
            ):
                pendientes.append(ruta)

    return sorted(destinos)


def limpiar(raiz: Path, dry_run: bool = False) -> list[Path]:
    """
    Elimina los artefactos permitidos del repositorio.

    Args:
        raiz: Raíz del repositorio.
        dry_run: Si es True, solo devuelve los destinos sin eliminarlos.

    Returns:
        Lista de destinos eliminados, o que se eliminarían.

    Raises:
        DestinoInseguroError: Si algún destino es inseguro. No se borra nada.
        OSError: Si falla la lectura o el borrado.
    """
    destinos = buscar_destinos(raiz)
    if not dry_run:
        for destino in destinos:
            if destino.is_dir():
                shutil.rmtree(destino)
            else:
                destino.unlink()
    return destinos


def main(argv: list[str] | None = None) -> int:
    """
    Punto de entrada de la línea de comandos.

    Args:
        argv: Argumentos sin el nombre del programa. No admite rutas.

    Returns:
        0 si termina bien, 1 si falla el sistema de archivos y 2 si se
        aborta por un destino inseguro.
    """
    parser = argparse.ArgumentParser(
        description="Elimina artefactos generados del repositorio.",
        allow_abbrev=False,
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="listar sin eliminar nada"
    )
    args = parser.parse_args(argv)

    try:
        destinos = limpiar(RAIZ_REPOSITORIO, dry_run=args.dry_run)
    except DestinoInseguroError as error:
        print(f"Abortado, no se borró nada: {error}", file=sys.stderr)
        return 2
    except OSError as error:
        print(f"Error del sistema de archivos: {error}", file=sys.stderr)
        return 1

    accion = "Se eliminaría" if args.dry_run else "Eliminado"
    for destino in destinos:
        print(f"{accion}: {destino.relative_to(RAIZ_REPOSITORIO).as_posix()}")
    print(f"Total: {len(destinos)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
