#!/usr/bin/env python3
"""
Script para compilar ChuspaCalc con PyInstaller
Ejecutar: python build_app.py
"""

import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

# Archivos spec en orden de preferencia: primero el nombre oficial y, como
# respaldo, el nombre histórico mientras el archivo no se haya renombrado.
SPEC_CANDIDATOS = ("chuspacalc.spec", "escuadra.spec")


def encontrar_spec():
    """Devuelve la ruta del primer archivo spec que exista, o None."""
    for nombre in SPEC_CANDIDATOS:
        ruta = RAIZ / nombre
        if ruta.is_file():
            return ruta
    return None


def main():
    spec = encontrar_spec()
    if spec is None:
        print("❌ No se encontró ningún archivo spec (se buscó: "
              + ", ".join(SPEC_CANDIDATOS) + ")")
        sys.exit(1)

    if spec.name != SPEC_CANDIDATOS[0]:
        print(f"⚠️  No existe {SPEC_CANDIDATOS[0]}; "
              f"se usa el archivo histórico {spec.name}")
    print(f"📄 Archivo spec seleccionado: {spec.name}")

    print("🚀 Compilando ChuspaCalc con PyInstaller...")
    result = subprocess.run(
        [sys.executable, "-m", "PyInstaller", str(spec)],
        capture_output=False
    )
    if result.returncode == 0:
        print("✅ ¡Compilación exitosa!")
        print("📁 El ejecutable se encuentra en: dist/")
    else:
        print("❌ Error en la compilación")
        sys.exit(1)


if __name__ == "__main__":
    main()
