# Guía de Testing

## Introducción

Las pruebas automatizadas son una parte fundamental del desarrollo en ChuspaCalc. Permiten verificar que los cambios realizados no introduzcan errores y facilitan el mantenimiento del código a largo plazo.

Esta guía explica cómo configurar el entorno de pruebas, ejecutar los distintos tipos de tests, escribir nuevas pruebas y seguir las convenciones utilizadas por el proyecto.

---

## Configuración del entorno de test

Antes de ejecutar las pruebas es necesario instalar las dependencias de desarrollo.

### Crear entorno virtual

```bash
python -m venv .venv
```

Activar el entorno:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Instalar pytest

```bash
pip install pytest
```

### Instalar cobertura

```bash
pip install pytest-cov
```

---

## Ejecutar los tests

### Ejecutar todas las pruebas

```bash
pytest
```

### Ejecutar únicamente pruebas unitarias

```bash
pytest tests/unit
```

### Ejecutar únicamente pruebas de integración

```bash
pytest tests/integration
```

### Ejecutar una prueba específica

```bash
pytest tests/unit/test_calculadora.py
```

### Ejecutar una función específica

```bash
pytest tests/unit/test_calculadora.py::test_sumar_dos_numeros
```

### Ejecutar con cobertura

```bash
pytest --cov=src
```

### Generar reporte HTML de cobertura

```bash
pytest --cov=src --cov-report=html
```

---

## Estructura de un test unitario

Se recomienda utilizar el patrón Given / When / Then.

### Given

Preparación de datos y dependencias.

### When

Ejecución de la acción que se desea probar.

### Then

Verificación de los resultados esperados.

### Ejemplo completo

```python
import pytest

def sumar(a, b):
    return a + b

def test_sumar_dos_numeros():
    # Given
    numero_a = 10
    numero_b = 5

    # When
    resultado = sumar(numero_a, numero_b)

    # Then
    assert resultado == 15
```

Este patrón facilita la lectura y comprensión de las pruebas.

---

## Fixtures disponibles

Las fixtures permiten reutilizar objetos y configuraciones entre múltiples pruebas.

Generalmente se encuentran definidas en:

```text
tests/conftest.py
```

Ejemplos comunes:

| Fixture             | Descripción                                               |
| ------------------- | --------------------------------------------------------- |
| app                 | Instancia principal de la aplicación para pruebas.        |
| cliente             | Cliente de prueba utilizado para solicitudes simuladas.   |
| datos_prueba        | Conjunto de datos reutilizable para distintos escenarios. |
| directorio_temporal | Directorio temporal para pruebas con archivos.            |
| configuracion_mock  | Configuración simulada para entornos controlados.         |

### Ejemplo de uso

```python
def test_usuario_valido(datos_prueba):
    assert datos_prueba is not None
```

Las fixtures ayudan a reducir código duplicado y mejoran la mantenibilidad de las pruebas.

---

## Convenciones de nomenclatura

### Archivos

Los archivos deben comenzar con:

```text
test_
```

Ejemplos:

```text
test_calculadora.py
test_usuario.py
test_configuracion.py
```

### Funciones

Se recomienda utilizar el formato:

```text
test_nombre_funcion_escenario
```

Ejemplos:

```text
test_sumar_dos_numeros_validos
test_login_usuario_existente
test_cargar_configuracion_archivo_valido
```

### Clases

Cuando se utilicen clases para agrupar pruebas:

```python
class TestCalculadora:
    pass
```

---

## Cobertura mínima requerida

La cobertura ayuda a medir qué porcentaje del código está siendo ejecutado por las pruebas.

Se recomienda mantener los siguientes mínimos:

| Módulo      | Cobertura mínima |
| ----------- | ---------------- |
| Core        | 90%              |
| Servicios   | 85%              |
| Utilidades  | 80%              |
| Interfaces  | 70%              |
| Integración | 70%              |

Cuando sea posible, se debe aumentar la cobertura sin sacrificar la calidad de las pruebas.

---

## Buenas prácticas

* Mantener cada prueba enfocada en un único comportamiento.
* Evitar dependencias entre pruebas.
* Utilizar fixtures para reutilizar configuraciones.
* Nombrar claramente los escenarios evaluados.
* Ejecutar todas las pruebas antes de crear un Pull Request.
* Revisar periódicamente los reportes de cobertura.

---

## Conclusión

Las pruebas automatizadas permiten mantener la estabilidad del proyecto y detectar errores tempranamente. Siguiendo las convenciones descritas en esta guía, los contribuyentes podrán ejecutar, escribir y mantener pruebas de forma consistente utilizando pytest y las herramientas de cobertura del proyecto.
