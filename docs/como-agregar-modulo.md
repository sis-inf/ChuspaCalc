# Cómo agregar un nuevo módulo a ChuspaCalc

Esta guía explica cómo crear e integrar una nueva herramienta dentro del proyecto ChuspaCalc.

El objetivo es mantener una estructura clara, consistente y fácil de mantener para todos los contribuidores.

---

# Estructura de módulos

Los módulos deben organizarse según el dominio correspondiente dentro de `src/ChuspaCalc/modulos/`.

Ejemplo de estructura:

```text
src/ChuspaCalc/modulos/
├── civil/
├── electrica/
├── geometria/
├── matematicas/
└── sistemas/
```

Cada carpeta contiene herramientas relacionadas con su área.

Ejemplos:

```text
src/ChuspaCalc/modulos/civil/herramienta_calculo_vigas.py
src/ChuspaCalc/modulos/electrica/herramienta_ley_ohm.py
src/ChuspaCalc/modulos/geometria/herramienta_calculo_area.py
```

---

# Pasos para crear un nuevo módulo

## 1. Elegir el dominio adecuado

Seleccionar la carpeta correspondiente dentro de:

```text
src/ChuspaCalc/modulos/
```

Ejemplo:

```text
src/ChuspaCalc/modulos/civil/
```

---

## 2. Crear `__init__.py` si el dominio es nuevo

Si se crea un dominio que todavía no existe, se debe agregar un archivo:

```text
src/ChuspaCalc/modulos/nuevo_dominio/__init__.py
```

Esto permite que Python reconozca el directorio como un paquete.

---

## 3. Crear el archivo del módulo

El archivo debe crearse dentro del dominio correspondiente y tener un nombre descriptivo usando `snake_case`.

Las herramientas descubiertas automáticamente por ChuspaCalc deben utilizar el prefijo `herramienta_`.

Ejemplos válidos:

```text
herramienta_calculo_vigas.py
herramienta_analisis_circuito.py
herramienta_conversion_temperatura.py
```

Evitar nombres genéricos como:

```text
archivo1.py
modulo.py
prueba123.py
```

---

## 4. Implementar la herramienta

Las herramientas deben heredar de `Herramienta`, definir sus metadatos e implementar el método `crear_widget()`.

Template básico:

```python
from PySide6.QtWidgets import QLabel

from ChuspaCalc.core.carrera import Carrera
from ChuspaCalc.core.herramienta import Herramienta


class HerramientaEjemplo(Herramienta):
    nombre = "Ejemplo"
    carrera = Carrera.SISTEMAS
    descripcion = "Descripción de la herramienta."

    def crear_widget(self):
        return QLabel("Herramienta de ejemplo")
```

# Separación entre lógica pura y wrappers

Los módulos del sistema se dividen en dos capas:

## Módulo de lógica pura
- Contiene únicamente lógica de cálculo o negocio
- No depende de PySide6 ni UI
- Es completamente testeable
- No debe contener clases de herramienta

## Wrapper herramienta_
- Debe comenzar con el prefijo `herramienta_`
- Es detectado automáticamente por el registry
- Solo conecta la UI con la lógica
- Debe importar funciones del módulo puro
- NO debe reimplementar lógica

---

## Anti-patrón

Antes algunos wrappers reimplementaban lógica en lugar de usar el módulo puro.

Ejemplo incorrecto:
```python
def calcular_area(base, altura):
    return (base * altura) / 2
```

---

## 5. Registro de herramientas

Las herramientas son descubiertas automáticamente por el registro definido en:

```text
src/ChuspaCalc/core/registry.py
```

Para que una herramienta sea detectada correctamente:

* Debe estar ubicada dentro de `src/ChuspaCalc/modulos/`
* El archivo debe comenzar con el prefijo `herramienta_`
* Debe contener una clase que herede de `Herramienta`

---

# Agregar pruebas

Cada módulo nuevo debe incluir pruebas básicas.

Ejemplo de estructura:

```text
tests/
├── test_herramienta_calculo_vigas.py
```

Las pruebas deben validar:

* Casos correctos
* Valores límite
* Manejo de errores simples

---

# Ejemplo completo

```python
# Archivo:
# src/ChuspaCalc/modulos/geometria/herramienta_calculo_area.py

from PySide6.QtWidgets import QLabel

from ChuspaCalc.core.carrera import Carrera
from ChuspaCalc.core.herramienta import Herramienta


class HerramientaCalculoArea(Herramienta):
    nombre = "Cálculo de Área"
    carrera = Carrera.GEOMETRIA
    descripcion = "Calcula áreas geométricas."

    def crear_widget(self):
        return QLabel("Herramienta de cálculo de área")
```

---

# Buenas prácticas

* Mantener las herramientas pequeñas y reutilizables
* Documentar el código mediante docstrings cuando corresponda
* Evitar duplicar lógica existente
* Utilizar nombres descriptivos para archivos, clases y funciones
* Mantener consistencia con la estructura y convenciones del proyecto
* Agregar pruebas antes de abrir un Pull Request

---

# Antes de abrir el Pull Request

Verificar que:

* La herramienta funciona correctamente
* El archivo sigue las convenciones del proyecto
* Existen pruebas básicas
* Se agregó `__init__.py` si fue necesario
* La herramienta puede ser descubierta por el registro
* La rama fue creada desde `dev`
* El PR apunta hacia `dev`
* No se modificaron archivos fuera del alcance del issue
