# Changelog

Todos los cambios notables de este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es/1.1.0/)
y este proyecto sigue el versionado [SemVer](https://semver.org/lang/es/).

## Generación automática

El archivo `CHANGELOG.md` puede generarse automáticamente a partir del historial de commits utilizando **git-cliff**, siguiendo la convención de Conventional Commits.

Para generar o actualizar el changelog ejecute:

```bash
./scripts/generar-changelog.sh
```

El script genera las entradas del changelog a partir de los commits desde el último tag disponible.

## [Unreleased]

### Added
- feat(conversor_longitud): agregado módulo de conversión de longitud
- feat(herramienta_calculo_area): agregada herramienta de cálculo de áreas
- feat(caida_tension): agregado cálculo de caída de tensión
- feat(tablas_verdad): agregada generación de tablas de verdad
- feat(conversor_bases): agregado conversor entre sistemas numéricos
- feat(viga): agregado módulo de cálculo para vigas

### Changed
- chore(changelog): actualización de módulos documentados en desarrollo

### Fixed
- fix(changelog): corrección de entradas faltantes del sprint actual
- chore(lint): limpieza de espacios en blanco y newlines finales (ruff W293/W292)

## [0.1.0] - 2026-04-19

### Agregado
- Inicio del proyecto
- Creación del repositorio