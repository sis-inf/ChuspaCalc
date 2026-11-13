# Guía rápida de comandos del CLI

Referencia rápida para invocar las herramientas de ChuspaCalc desde la terminal.
Complementa a [cli-referencia.md](cli-referencia.md), [cli-modo-interactivo.md](cli-modo-interactivo.md)
y [cli-autocompletado.md](cli-autocompletado.md).

> **Estado actual:** el CLI todavía no arranca en `dev`. El código del CLI importa
> el paquete `chuspacalc`, pero en `src/` el paquete sigue llamándose `escuadra`,
> así que cualquier comando termina con `ModuleNotFoundError: No module named 'chuspacalc'`.
> Además, `cli_interactivo.py` importa `obtener_herramientas` de `chuspacalc.registry`,
> un módulo que todavía no existe. Las salidas esperadas de esta guía salen de leer
> `src/escuadra/cli.py` y van a valer cuando se resuelvan esos dos puntos.

## Sintaxis general

```bash
chuspacalc [--help] [--version] [--json] <comando> [opciones del comando]
```

- El ejecutable se llama `chuspacalc` (sección `[project.scripts]` de `pyproject.toml`)
  y se instala con `pip install -e .`.
- Las opciones globales (`--json`, `--version`) van **antes** del comando.
- Sin comando, el CLI muestra la ayuda general y termina con código 0.

### Opciones globales

| Opción | Corto | Qué hace |
|--------|-------|----------|
| `--help` | `-h` | Muestra la ayuda general y sale |
| `--version` | `-v` | Muestra `chuspacalc 0.1.0` y sale |
| `--json` | | Devuelve el resultado de una herramienta en formato JSON |

### Comandos generales

| Comando | Opciones | Qué hace |
|---------|----------|----------|
| `listar` | `--carrera CARRERA` (opcional) | Lista las herramientas agrupadas por especialidad |
| `version` | | Muestra la versión de ChuspaCalc, Python, PySide6 y la plataforma |
| `interactivo` | | Abre el modo interactivo paso a paso (REPL) |
| `<herramienta>` | | Ejecuta una herramienta por su nombre (ver tabla de abajo) |

Valores de `--carrera`: `civil`, `electrica`, `geometria`, `matematicas`, `sistemas`.

## Ayuda (`--help`)

```bash
chuspacalc --help            # ayuda general: opciones globales y lista de comandos
chuspacalc listar --help     # ayuda de un comando concreto
```

Cada herramienta también acepta `--help`. Como hoy las herramientas no definen
parámetros propios en el CLI, su ayuda solo muestra la opción `-h, --help`.

## Comandos por especialidad

Cada herramienta se registra como un comando con su nombre exacto, que lleva
espacios y tildes: hay que escribirlo **entre comillas**. Hoy los comandos de
herramienta no reciben parámetros por la terminal; para ingresar datos está
pensado `chuspacalc interactivo`, y mientras tanto se usa la interfaz gráfica.

| Especialidad (`--carrera`) | Comandos |
|----------------------------|----------|
| Ingeniería Civil (`civil`) | `"Carga Crítica de Euler"`, `"Combinación de cargas"`, `"Diseño Vial"` |
| Ingeniería Eléctrica (`electrica`) | `"Conversión de unidades eléctricas"`, `"Divisor de tensión"`, `"Ley de Ohm"`, `"Potencia Trifásica"` |
| Geometría (`geometria`) | `"Cálculo de áreas"`, `"Figuras Compuestas"`, `"Resolución de triángulos"`, `"Transformaciones Geométricas"` |
| Matemáticas (`matematicas`) | `"Calculadora científica"`, `"Conversión de unidades"`, `"Matemática financiera"`, `"Números complejos"`, `"Sistemas de ecuaciones lineales"` |
| Ingeniería de Sistemas e Informática (`sistemas`) | `"Complemento a 2"`, `"Conversión de bases"`, `"Mapas de Karnaugh"`, `"Tabla ASCII"`, `"Tablas de verdad"` |

`chuspacalc listar` siempre muestra la lista actualizada, porque se arma al vuelo
con las clases `Herramienta` de los archivos `herramienta_*.py` de `src/escuadra/modulos/`.

## Formatos de salida y exportación

- **Texto** (por defecto): el resultado se imprime tal cual en la terminal.
- **JSON** (`--json`): imprime un objeto con las claves `herramienta`,
  `parametros` y `resultado`. Es el único formato de exportación del CLI y solo
  se aplica cuando una herramienta llega a ejecutarse; `listar` y `version` lo ignoran.

```bash
chuspacalc --json "Ley de Ohm"
```

Desde la interfaz gráfica se puede exportar además a Markdown y LaTeX
([exportar-markdown.md](exportar-markdown.md), [exportar-latex.md](exportar-latex.md)).

## Ejemplos

### Listar las herramientas de una especialidad

```bash
chuspacalc listar --carrera civil
```

Salida esperada:

```text

Ingeniería Civil
────────────────
  Carga Crítica de Euler         Calcula la carga crítica de pandeo para columnas a compresión.
  Combinación de cargas          Calcula una combinación simplificada de cargas vivas y muertas.
  Diseño Vial                    Calcula pendiente y peralte de curva para diseño vial.
```

Con una carrera que no existe:

```bash
chuspacalc listar --carrera quimica
```

```text
No se encontraron herramientas para la carrera 'quimica'.
Carreras disponibles: civil, electrica, geometria, matematicas, sistemas
```

### Ver la versión

```bash
chuspacalc --version
```

```text
chuspacalc 0.1.0
```

```bash
chuspacalc version
```

```text
ChuspaCalc:      0.1.0
Python:        3.12.3
PySide6:       6.x.x
Plataforma:    Linux-...
```

Los valores de Python, PySide6 y Plataforma dependen del equipo.

### Ejecutar una herramienta de cada especialidad

```bash
chuspacalc "Diseño Vial"                  # civil
chuspacalc "Ley de Ohm"                   # electrica
chuspacalc "Cálculo de áreas"             # geometria
chuspacalc "Números complejos"            # matematicas
chuspacalc "Conversión de bases"          # sistemas
```

Salida esperada, en el mismo orden:

```text
La herramienta 'Diseño Vial' aún está en construcción y no está disponible.
La herramienta 'Ley de Ohm' aún está en construcción y no está disponible.
La herramienta 'Cálculo de áreas' aún está en construcción y no está disponible.
La herramienta 'Números complejos' aún está en construcción y no está disponible.
La herramienta 'Conversión de bases' aún está en construcción y no está disponible.
```

El CLI reconoce el nombre, pero todavía no puede ejecutar la herramienta: busca
un módulo `chuspacalc.modulos.<nombre>` que no existe. Por ahora, el cálculo
completo se hace desde la interfaz gráfica.

### Modo interactivo

```bash
chuspacalc interactivo
```

Cuando esté disponible, muestra la lista numerada de herramientas y pide los
parámetros uno por uno:

```text

=== ChuspaCalc MODO INTERACTIVO ===

1. ...
0. Salir

Selecciona una herramienta:
```

## Códigos de salida

| Código | Cuándo |
|--------|--------|
| `0` | Ejecución normal, o se llamó sin comando (muestra la ayuda) |
| `1` | Python menor a 3.10 o PySide6 no instalado |
| `2` | Opción o comando inválido (error de `argparse`) |
| `130` | Operación cancelada con Ctrl+C |
