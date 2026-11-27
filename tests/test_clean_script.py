"""Pruebas de scripts/clean.py. Todas trabajan sobre directorios temporales."""

import importlib.util
import os
import sys
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("clean", RAIZ / "scripts" / "clean.py")
assert _spec is not None and _spec.loader is not None
clean = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(clean)


def _crear(ruta: Path) -> Path:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text("x", encoding="utf-8")
    return ruta


def _enlazar(enlace: Path, destino: Path) -> None:
    try:
        enlace.symlink_to(destino, target_is_directory=destino.is_dir())
    except OSError:
        pytest.skip("el sistema no permite crear enlaces simbólicos")


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    raiz = tmp_path / "repo"
    for relativa in (
        "src/pkg/__pycache__/a.cpython-312.pyc",
        "src/pkg/suelto.pyc",
        "src/pkg/modulo.py",
        "tests/__pycache__/t.pyc",
        ".pytest_cache/v",
        ".mypy_cache/v",
        ".ruff_cache/v",
        "htmlcov/index.html",
        "build/salida",
        "dist/paquete.whl",
    ):
        _crear(raiz / relativa)
    return raiz


def _contenido(raiz: Path) -> set[str]:
    return {ruta.relative_to(raiz).as_posix() for ruta in raiz.rglob("*")}


def test_dry_run_enumera_sin_eliminar(repo):
    antes = _contenido(repo)
    destinos = clean.limpiar(repo, dry_run=True)
    assert destinos
    assert _contenido(repo) == antes


def test_elimina_solo_lo_permitido(repo):
    _crear(repo / "notas.txt")
    clean.limpiar(repo)
    assert _contenido(repo) == {
        "notas.txt",
        "src",
        "src/pkg",
        "src/pkg/modulo.py",
        "tests",
    }


@pytest.mark.parametrize("protegido", [".git", ".venv", "venv", "env", "node_modules"])
def test_no_entra_en_directorios_protegidos(repo, protegido):
    archivo = _crear(repo / protegido / "__pycache__" / "x.pyc")
    clean.limpiar(repo)
    assert archivo.exists()


def test_no_toca_entorno_virtual_con_otro_nombre(repo):
    _crear(repo / "mi_entorno" / "pyvenv.cfg")
    archivo = _crear(repo / "mi_entorno" / "x.pyc")
    clean.limpiar(repo)
    assert archivo.exists()


def test_build_y_dist_anidados_se_conservan(repo):
    build = _crear(repo / "src" / "build" / "codigo.py")
    dist = _crear(repo / "docs" / "dist" / "guia.md")
    clean.limpiar(repo)
    assert build.exists() and dist.exists()


@pytest.mark.parametrize("nombre", ["__pycache__", "build", "x.pyc"])
def test_aborta_si_un_destino_es_enlace(tmp_path, repo, nombre):
    externo = tmp_path / "externo"
    archivo = _crear(externo / "importante.txt")
    enlace = repo / "otro" / nombre if nombre != "build" else repo / "build"
    if nombre == "build":
        (repo / "build" / "salida").unlink()
        (repo / "build").rmdir()
    enlace.parent.mkdir(exist_ok=True)
    _enlazar(enlace, externo)
    antes = _contenido(repo)

    with pytest.raises(clean.DestinoInseguroError):
        clean.limpiar(repo)

    assert archivo.exists()
    assert _contenido(repo) == antes


def test_aborta_si_hay_un_enlace_dentro_de_un_destino(tmp_path, repo):
    archivo = _crear(tmp_path / "externo" / "importante.txt")
    _enlazar(repo / "dist" / "enlace", archivo.parent)

    with pytest.raises(clean.DestinoInseguroError):
        clean.limpiar(repo)

    assert archivo.exists()
    assert (repo / "htmlcov" / "index.html").exists()


def test_no_sigue_enlaces_hacia_fuera(tmp_path, repo):
    archivo = _crear(tmp_path / "externo" / "__pycache__" / "x.pyc")
    _enlazar(repo / "atajo", archivo.parent.parent)
    clean.limpiar(repo)
    assert archivo.exists()


def test_aborta_ante_destino_de_tipo_inesperado(repo):
    ambiguo = _crear(repo / "docs" / "__pycache__")
    with pytest.raises(clean.DestinoInseguroError):
        clean.limpiar(repo)
    assert ambiguo.exists()
    assert (repo / "dist" / "paquete.whl").exists()


@pytest.mark.skipif(sys.platform != "win32", reason="las uniones son de Windows")
def test_aborta_ante_union_de_windows(tmp_path, repo):
    import _winapi

    archivo = _crear(tmp_path / "externo" / "importante.txt")
    _winapi.CreateJunction(str(archivo.parent), str(repo / "dist" / "union"))

    with pytest.raises(clean.DestinoInseguroError):
        clean.limpiar(repo)

    assert archivo.exists()


@pytest.mark.parametrize("argumento", ["/tmp", "..", "--ruta=."])
def test_no_acepta_rutas(argumento):
    with pytest.raises(SystemExit) as salida:
        clean.main([argumento])
    assert salida.value.code == 2


def test_main_dry_run_muestra_rutas_portables(repo, monkeypatch, capsys):
    monkeypatch.setattr(clean, "RAIZ_REPOSITORIO", repo.resolve())
    assert clean.main(["--dry-run"]) == 0
    assert "src/pkg/__pycache__" in capsys.readouterr().out
    assert (repo / "src" / "pkg" / "suelto.pyc").exists()


def test_main_devuelve_2_al_abortar(repo, monkeypatch, capsys):
    _crear(repo / "docs" / "__pycache__")
    monkeypatch.setattr(clean, "RAIZ_REPOSITORIO", repo.resolve())
    assert clean.main([]) == 2
    assert "no se borró nada" in capsys.readouterr().err


def test_help_describe_todos_los_objetivos():
    texto = (RAIZ / "Makefile").read_text(encoding="utf-8")
    linea = next(x for x in texto.splitlines() if x.startswith(".PHONY:"))
    objetivos = set(linea.split()[1:]) - {"help"}
    documentados = {
        x.split('"')[1].split()[0]
        for x in texto.splitlines()
        if x.startswith('\t@echo "  ')
    }
    assert documentados == objetivos


def test_la_raiz_es_la_del_repositorio():
    assert os.path.samefile(clean.RAIZ_REPOSITORIO, RAIZ)
