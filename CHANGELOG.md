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
- refactor(validation): normalización de validaciones numéricas, valores no finitos y contratos de entrada en módulos de cálculo
- refactor(typing): corrección de anotaciones, valores opcionales, parámetros y retornos para validar el paquete con mypy
- refactor(packaging): consolidación del namespace `chuspacalc` manteniendo el shim de compatibilidad `escuadra`
- chore(dependencies): incorporación de `pytest-qt` a las dependencias de desarrollo utilizadas por la suite y CI
- chore(quality): normalización selectiva del código y las pruebas para Ruff y Black
- chore(ui): normalización de señales y slots y captura segura de errores en `widget_herramienta` (#2044)

### Security
- security(evaluators): sustitución de evaluación dinámica insegura por evaluadores matemáticos y lógicos con listas blancas y límites de complejidad
- security(inputs): endurecimiento de validaciones de expresiones, exponentes, resultados no finitos y datos suministrados por el usuario

### Fixed
- fix(changelog): corrección de entradas faltantes del sprint actual
- chore(lint): limpieza de espacios en blanco y newlines finales (ruff W293/W292)
- fix(herramienta_resolucion_triangulos): herramienta registrada en Geometría en lugar de Matemáticas y documentada
- fix(civil): restauración de los contratos compatibles de cálculo de momento flector y corrección de validaciones estructurales
- fix(calculations): corrección de contratos y casos límite en cálculos civiles, eléctricos, geométricos, matemáticos y de sistemas
- fix(tests): corrección de la colección de pytest y adición de pruebas de regresión para seguridad, tipado, compatibilidad y módulos integrados
- fix(packaging): inclusión de módulos descubiertos dinámicamente y de los módulos estudiantiles conservados bajo el namespace histórico
- fix(pyinstaller): exclusión selectiva de bibliotecas ICU incompatibles procedentes de `OpenAI.CodexPrimaryRuntime` al construir el ejecutable Qt

## [0.1.0] - 2026-04-19

### Agregado
- Inicio del proyecto
- Creación del repositorio
