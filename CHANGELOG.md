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
- feat(error_validacion): agregados validadores numericos (tipo, finitud, no cero y rango)

### Changed
- refactor(herramienta_columna_pandeo): la herramienta valida los campos con ErrorValidacion y rechaza cero, NaN e infinito antes de calcular (#1942).
- refactor(circuitos_rc_rl): validación de parámetros numéricos mediante ErrorValidacion y anotaciones de tipo completas (#1955).
- refactor(momento_flector): las entradas inválidas de calcular_momento_max y calcular_momento_maximo lanzan ErrorValidacion; se añade regresión de ambos contratos (#1945).
- refactor(volumen_excavacion): validación de dimensiones finitas y positivas mediante ErrorValidacion y anotaciones de tipo completas (#1951).
- refactor(electrica): validación defensiva y anotaciones de tipo completas en herramienta_circuitos_rc_rl (#1958).
- refactor(terreno): validación de áreas no negativas y longitud positiva mediante ErrorValidacion y anotaciones de tipo completas (#1949).
- chore(utils): documentación y anotaciones de tipos en logging_config (#2048).
- chore(changelog): actualización de módulos documentados en desarrollo
- refactor(validation): normalización de validaciones numéricas, valores no finitos y contratos de entrada en módulos de cálculo
- refactor(matrix): validación de matrices nulas o irregulares y escalares no finitos en operaciones matriciales (#1930).
- refactor(typing): corrección de anotaciones, valores opcionales, parámetros y retornos para validar el paquete con mypy
- refactor(resolucion_triangulos): validación de lados y ángulos finitos mediante ErrorValidacion y tipos de retorno completos (#1986).
- refactor(packaging): consolidación del namespace `chuspacalc` manteniendo el shim de compatibilidad `escuadra`
- refactor(coordenadas): validación de coordenadas finitas, radio polar y límites numéricos mediante ErrorValidacion (#1978).
- chore(dependencies): incorporación de `pytest-qt` a las dependencias de desarrollo utilizadas por la suite y CI
- chore(quality): normalización selectiva del código y las pruebas para Ruff y Black
- chore(ui): captura segura de errores y comentarios descriptivos en `progress` (#2042)
- chore(ui): normalización de señales y captura segura de errores en `ventana_principal` (#2043)
- refactor(csv_parser): validación de rutas y opciones de lectura, con detección de CSV malformado y compatibilidad con Latin-1 (#1923).
- chore(core): agregados docstrings y type hints en la clase base `Herramienta` (#1919)
- chore(core): agregados docstrings y type hints en el despachador `dispatcher` (#1917)
- chore(ui): normalización de señales y slots y captura segura de errores en `widget_herramienta` (#2044)
- test(chuspacalc): migrar imports históricos a chuspacalc en test_correccion_fp.py (#1873)
- refactor(transformaciones): validación de parámetros numéricos finitos, detección de resultados desbordados mediante ErrorValidacion y anotaciones de tipo completas (#1987).
- chore(ui): normalización de señales y captura segura de errores en `dialogo_acerca_de` (#2036)
- chore(ui): normalización de señales y captura segura de errores en `cargador_herramienta`, mostrando un widget informativo cuando falla la carga de una herramienta (#2034)
- refactor(herramienta_financiera): validación de capital, tasa y períodos mediante ErrorValidacion, con tope de períodos y anotaciones de tipo completas (#2005).
- refactor(calculadora_cientifica): validación de expresión y modo angular, errores de dominio de funciones mediante ErrorValidacion y anotaciones de tipo completas (#2003).
- chore(converter): documentación de módulo y docstrings en formato estándar con Args y Returns, y corrección del ejemplo de celsius_to_fahrenheit (#2046).
- chore(ui): normalización de señales y captura segura de errores en `dialogo_comparar_historial` (#2037)
- refactor(geometria): validar parámetros numéricos y tipado en diagonal_rectangulo (#1979).
- refactor(conversor_angulo): validación de valor y unidades mediante ErrorValidacion, rechazo de booleanos, texto y valores no finitos, detección de resultados desbordados y anotaciones de tipo completas (#1991).
- refactor(conversor_longitud): validación de valor y unidades mediante ErrorValidacion, rechazo de booleanos, texto y valores no finitos, y TypedDict preciso para el retorno (#1993).
- refactor(conversor_temperatura): validación de tipos numéricos, NaN e infinitos mediante ErrorValidacion y anotaciones de tipo completas (#1997).
- refactor(matematicas): validar parámetros numéricos y tipado en conversor_energia (#1992).
- refactor(conversor_velocidad): validación de tipos numéricos, NaN, infinitos y unidades mediante ErrorValidacion y anotaciones de tipo completas (#1998).
- refactor(carga_distribuida): validación de tipos numéricos, NaN e infinitos mediante ErrorValidacion y anotaciones de tipo completas (#1936).
- refactor(sistemas): validación de parámetros con `ErrorValidacion` y type hints completos en `tabla_ascii` (#2031)
- chore(ui): las subclases de `ErrorValidacion` (p. ej. `ErrorCIDR`) muestran el mensaje de validación en `mensajes` y se documentan sus funciones (#2039)
- refactor(potencias_raices): validación de valores finitos, booleanos, desbordes, cero con exponente negativo, raíz par negativa y bases logarítmicas inválidas mediante ErrorValidacion y anotaciones de tipo completas (#2011).
- chore(ui): panel_estadisticas_uso captura ErrorValidacion al actualizar estadísticas y muestra el mensaje en la interfaz (#2040)
- chore(ui): panel_historial captura ErrorValidacion al consultar y editar el historial y muestra el mensaje en la interfaz (#2041).
- refactor(electrica): la herramienta de Ley de Ohm valida con ErrorValidacion valores NaN, infinitos, divisores en cero y desbordes, y completa sus type hints (#1962)
- refactor(punto_equilibrio): validación de costos y precios mediante ErrorValidacion, rechazo de booleanos, texto y valores no finitos, detección de márgenes y resultados desbordados, y anotaciones de tipo completas (#1989).
- refactor(herramienta_conversion_unidades): validación de valores, categorías y unidades mediante ErrorValidacion, rechazo de booleanos, texto y valores no finitos, cero absoluto, detección de resultados desbordados y anotaciones de tipo completas (#2004).
- refactor(sistemas_lineales): validación de parámetros numéricos finitos, captura de errores de cálculo mediante ErrorValidacion y anotaciones de tipo completas en la herramienta de sistemas lineales (#2007).
- refactor(numeros_primos): es_numero_primo lanza ErrorValidacion ante valores no enteros, booleanos, NaN o infinitos y completa sus anotaciones de tipo (#2010).
- refactor(progresion_aritmetica): validación de posición, operandos y resultado finitos mediante ErrorValidacion y tipos de retorno completos (#2012).
- fix(trigonometria): rechazo de booleanos mediante ErrorValidacion en seno, coseno, tangente y arcofunciones, con prueba de regresión (#2013).
- refactor(numeros_complejos): validación de operandos complejos finitos, control de desbordes y divisiones por cero mediante ErrorValidacion y anotaciones de tipo completas en el módulo de números complejos (#2006).
- refactor(financiera): validación de parámetros numéricos finitos, control de desbordes y divisiones por cero mediante ErrorValidacion y anotaciones de tipo completas en el módulo de matemática financiera (#2002).
- refactor(esfuerzo_axial): validación de fuerza y área finitas mediante ErrorValidacion y anotaciones de tipo completas (#1941).
- refactor(reacciones_viga): validación de carga y longitud positivas mediante ErrorValidacion y anotaciones de tipo completas (#1947).
- refactor(combinacion_cargas): validación de cargas, factores y viento finitos mediante ErrorValidacion y anotaciones de tipo completas (#1938).
- refactor(potencia): validación de tipos numéricos, NaN, infinitos y desbordamiento de resultados mediante ErrorValidacion y anotaciones de tipo completas (#1965).

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
- fix(utils): `validar_numero` rechaza `nan`, `inf` y `-inf` y se agregan pruebas de IO Unicode y de portapapeles con aislamiento de `QApplication` (#2045).

## [0.1.0] - 2026-04-19

### Agregado
- Inicio del proyecto
- Creación del repositorio
