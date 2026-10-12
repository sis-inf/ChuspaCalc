#!/usr/bin/env python3
"""
Script para compilar Escuadra con PyInstaller
Ejecutar: python build_app.py
"""

import subprocess
import sys


def main():
    print("🚀 Compilando Escuadra con PyInstaller...")
    result = subprocess.run(
        [sys.executable, "-m", "PyInstaller", "escuadra.spec"], capture_output=False
    )
    if result.returncode == 0:
        print("✅ ¡Compilación exitosa!")
        print("📁 El ejecutable se encuentra en: dist/")
    else:
        print("❌ Error en la compilación")
        sys.exit(1)


if __name__ == "__main__":
    main()
