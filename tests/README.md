# Uso de pytest markers
## Introducción

La carpeta "tests/" contiene todos los recursos relacionados con las pruebas del proyecto ChuspaCalc. Su objetivo es proporcionar una estructura organizada para pruebas automatizadas, pruebas manuales, casos de prueba, datos de prueba y documentación asociada al proceso de aseguramiento de calidad.

Las pruebas permiten verificar que los cambios realizados en el código funcionen correctamente y no introduzcan errores en funcionalidades existentes. Por esta razón, se recomienda ejecutar las pruebas correspondientes antes de enviar cambios al repositorio mediante un Pull Request.

Dentro de la carpeta "tests/" existen diferentes categorías de pruebas. Las pruebas unitarias están enfocadas en validar funciones o componentes individuales de forma aislada. Las pruebas de integración verifican la interacción entre distintos módulos del sistema. Las pruebas end-to-end validan flujos completos desde la perspectiva del usuario o del proceso de negocio.

Además de las pruebas automatizadas, el proyecto incluye directorios destinados a casos de prueba documentados, pruebas manuales, datos de entrada y salida esperados, planes de prueba y reportes. Esta organización facilita la colaboración entre contribuidores y ayuda a mantener una estrategia de pruebas consistente a lo largo del tiempo.

Este documento describe la estructura de carpetas utilizada en el proyecto, los comandos más comunes para ejecutar pruebas, las convenciones de nombres recomendadas y el procedimiento general para agregar nuevos casos de prueba.
Este proyecto utiliza pytest markers para clasificar los tests.

## Objetivo de las pruebas

Las pruebas forman parte fundamental del proceso de desarrollo del proyecto. Su propósito es detectar errores de manera temprana, validar el comportamiento esperado del sistema y reducir el riesgo de introducir fallos durante la incorporación de nuevas funcionalidades o correcciones.

Se recomienda que cada contribución incluya las pruebas correspondientes cuando sea posible. Las pruebas automatizadas permiten verificar rápidamente que los cambios realizados no afecten el funcionamiento existente del proyecto. Asimismo, la organización de los directorios facilita la identificación del tipo de prueba que debe implementarse en cada caso.

Antes de abrir un Pull Request, es recomendable ejecutar las pruebas relevantes y revisar los resultados obtenidos. Esto ayuda a mantener la calidad general del código y mejora la experiencia de colaboración entre los miembros de la comunidad.

## Markers disponibles

### unit
Tests unitarios puros.

```bash
pytest -m unit
```
## Estructura de carpetas

| Directorio | Propósito |
|------------|------------|
| `tests/automatizados/unit/` | Pruebas unitarias de funciones y componentes individuales. |
| `tests/automatizados/integration/` | Pruebas de integración entre módulos. |
| `tests/automatizados/e2e/` | Pruebas end-to-end de flujos completos. |
| `tests/casos/funcionales/` | Casos de prueba funcionales documentados. |
| `tests/casos/no-funcionales/` | Casos relacionados con rendimiento, usabilidad y calidad. |
| `tests/casos/regresion/` | Casos destinados a evitar regresiones. |
| `tests/manuales/checklists/` | Listas de verificación para pruebas manuales. |
| `tests/manuales/evidencias/` | Evidencias obtenidas durante las pruebas. |
| `tests/plan/` | Planificación y estrategia de pruebas. |
| `tests/reportes/` | Reportes generados durante la ejecución de pruebas. |
| `tests/datos/entrada/` | Datos de entrada para los escenarios de prueba. |
| `tests/datos/esperados/` | Resultados esperados para validación. |

## Ejecutar todos los tests

```bash
pytest
```
## Ejecutar tests por categoría

### Unit

```bash
pytest tests/automatizados/unit/
```
o

```bash
pytest -m unit
```
### Integration
```bash
pytest tests/automatizados/integration/
```
o
```bash
pytest -m integration
```
### E2E
```bash
pytest tests/automatizados/e2e/
```
o

```bash
pytest -m e2e
```
## Ejecutar con cobertura

```bash
pytest --cov
```
```bash
pytest --cov --cov-report=term-missing
```
## Agregar un nuevo test

1. Identificar el tipo de prueba a implementar.
2. Seleccionar el directorio adecuado.
3. Crear un archivo siguiendo las convenciones del proyecto.
4. Implementar los casos de prueba utilizando pytest.
5. Ejecutar las pruebas localmente.
6. Verificar que no existan fallos.
7. Confirmar que no se afecten pruebas existentes.
8. Enviar los cambios mediante un Pull Request.

## Convenciones de nombres

Los archivos de prueba deben seguir el formato:

test_nombre_modulo.py

Ejemplos:

test_usuario.py
test_calculadora.py
test_validaciones.py

Las funciones de prueba también deben comenzar con el prefijo "test_" para que pytest las detecte automáticamente.