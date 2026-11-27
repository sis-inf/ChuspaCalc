# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

from PyInstaller.utils.hooks import collect_submodules


# Estos módulos permanecen físicamente bajo el namespace histórico. Se incluyen
# como datos para que la extensión de ``chuspacalc.modulos.__path__`` también
# funcione dentro del directorio temporal de la aplicación one-file.
modulos_estudiantiles = [
    ("src/escuadra/modulos/estadistica/amplitud_intervalo.py", "escuadra/modulos/estadistica"),
    ("src/escuadra/modulos/estadistica/frecuencia_relativa.py", "escuadra/modulos/estadistica"),
    ("src/escuadra/modulos/estadistica/puntuacion_z.py", "escuadra/modulos/estadistica"),
    ("src/escuadra/modulos/fisica/aceleracion_centripeta.py", "escuadra/modulos/fisica"),
    ("src/escuadra/modulos/fisica/impulso.py", "escuadra/modulos/fisica"),
    ("src/escuadra/modulos/fisica/velocidad_angular.py", "escuadra/modulos/fisica"),
    ("src/escuadra/modulos/quimica/formula_empirica.py", "escuadra/modulos/quimica"),
    ("src/escuadra/modulos/quimica/fraccion_molar.py", "escuadra/modulos/quimica"),
    ("src/escuadra/modulos/quimica/reactivo_limitante.py", "escuadra/modulos/quimica"),
    ("src/escuadra/modulos/quimica/vida_media.py", "escuadra/modulos/quimica"),
]

hiddenimports = (
    collect_submodules("chuspacalc.modulos")
    + collect_submodules("escuadra.modulos")
    + [
        "PySide6.QtCore",
        "PySide6.QtGui",
        "PySide6.QtWidgets",
    ]
)

a = Analysis(
    ["src/chuspacalc/app.py"],
    pathex=[],
    binaries=[],
    datas=modulos_estudiantiles,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

# El entorno de Codex agrega a PATH una distribución de ICU de Poppler cuyos
# símbolos están versionados. PyInstaller la confunde con la ICU del sistema
# que requiere Qt6Core y genera un ejecutable con ERROR_PROC_NOT_FOUND.
# Se excluyen únicamente esas copias externas; no se filtran DLL de PySide6.
a.binaries = [
    entrada
    for entrada in a.binaries
    if not (
        Path(entrada[1]).name.lower() in {"icuuc.dll", "icudt78.dll"}
        and "openai.codexprimaryruntime" in str(entrada[1]).lower()
    )
]

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="chuspacalc",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
