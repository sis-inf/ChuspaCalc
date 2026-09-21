# Instaladores Nativos por Plataforma

> **Nota Estado Actual:** La compilacion mediante `pyinstaller escuadra.spec` y `python build_app.py` genera **ejecutables directores/portables** en la carpeta `dist/`. Los instaladores con asistentes interactivos (.msi, .dmg, .deb) descritos en este documento no estan implementados aun y se consideran trabajo futuro (**Roadmap**). 

## Descripcion general

Escuadra genera ejecutables segun el sistema operativo usando PyInstaller. La creacion de estos paquetes de instalacion con asistente se encuentra en la hoja de ruta de proyecto.

## Formatos disponibles

| Plataforma | Formato | Extension | Estado |
|---|---|---|---|
| Windows | Microsoft Installer | .msi | Roadmap |
| macOS | Disk Image | .dmg | Roadmap |
| Linux (Debian/Ubuntu) | Debian Package | .deb | Roadmap |

## Windows MSI (Roadmap)

Requisitos: Windows 10+, Python 3.10+, PyInstaller, Inno Setup.

Generar ejecutable:

    pyinstaller escuadra.spec

El archivo queda en dist/. La integracion con asistente de instalacion e integracion con el menu Inicio.

## macOS DMG (Roadmap)

Requisitos: macOS 11+, Python 3.10+, PyInstaller.

Generar bundle:

    pyinstaller escuadra.spec

El archivo queda en dist/. Compatible con Apple Silicon e Intel.

## Linux DEB (Roadmap)

Requisitos: Ubuntu 20.04+ o Debian 11+, Python 3.10+, dpkg-deb.

Instalar:

    sudo dpkg -i dist/escuadra.deb

Desinstalar:

    sudo dpkg -r escuadra

## Comparacion de formatos

| Caracteristica | MSI | DMG | DEB |
|---|---|---|---|
| Sistema operativo | Windows | macOS | Linux Debian/Ubuntu |
| Requiere admin | Si | No | Si |
| Desinstalacion | Panel de Control | Arrastrar a papelera | dpkg -r |

## Generar todos los instaladores

    python build_app.py

Los archivos ejecutables directos quedan en `dist/`.
