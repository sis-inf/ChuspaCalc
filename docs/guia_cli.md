# Guía de comandos de Escuadra (CLI)

Esta guía describe la interfaz de línea de comandos que está definida en `src/escuadra/cli.py` en la versión revisada del proyecto. Se documentan únicamente los comandos y opciones que aparecen en el código. La presencia de una herramienta en el listado no implica que su ejecución individual esté terminada.

## 1. Requisitos e instalación

- Python 3.10 o superior.
- PySide6 instalado. El CLI comprueba esta dependencia antes de procesar los argumentos, incluso cuando se solicita la ayuda.
- Dependencias del proyecto, incluida `argcomplete`.

Desde la raíz del repositorio, se puede instalar el proyecto en modo editable:

```bash
python -m pip install -e .
```

El punto de entrada `escuadra` está declarado en `pyproject.toml`. También se puede iniciar el paquete con:

```bash
python -m escuadra
```

## 2. Sintaxis general

```text
escuadra [--version | -v] [--json] <comando> [argumentos]
```

Los comandos definidos por el CLI son:

| Comando | Función implementada en el CLI |
|---|---|
| `listar` | Muestra las herramientas registradas, agrupadas por especialidad. |
| `version` | Muestra la versión de Escuadra y datos del entorno. |
| `interactivo` | Intenta iniciar el modo interactivo. En el código revisado, el módulo importa `escuadra.registry`, ruta que no existe en el paquete entregado; por tanto, el comando no puede completarse en este estado. |
| `<nombre de herramienta>` | El parser registra subcomandos a partir del nombre visible de cada herramienta. La ejecución individual todavía tiene limitaciones descritas en la sección 5. |

Si se ejecuta `escuadra` sin un subcomando, el parser muestra la ayuda general.

## 3. Ayuda y versión

La ayuda se genera con `argparse`:

```bash
escuadra --help
escuadra listar --help
```

`--help` muestra la ayuda general o la ayuda del subcomando indicado. Como el programa verifica primero el entorno, Python y PySide6 deben cumplir los requisitos para que la ayuda llegue a mostrarse.

Hay dos formas de consultar la versión:

```bash
escuadra --version
escuadra -v
```

Estas opciones imprimen la versión del paquete (actualmente `0.1.0`). El subcomando de diagnóstico:

```bash
escuadra version
```

muestra la versión de Escuadra, la versión de Python, la versión de PySide6 y la plataforma.

## 4. Listar herramientas por especialidad

El subcomando `listar` admite la opción `--carrera` para filtrar las herramientas. Los códigos válidos se obtienen del enum `Carrera`:

| Código | Especialidad |
|---|---|
| `civil` | Ingeniería Civil |
| `electrica` | Ingeniería Eléctrica |
| `geometria` | Geometría |
| `matematicas` | Matemáticas |
| `sistemas` | Ingeniería de Sistemas e Informática |

Sintaxis:

```bash
escuadra listar [--carrera CARRERA]
```

Ejemplos de consulta (uno por especialidad):

```bash
escuadra listar --carrera civil
escuadra listar --carrera electrica
escuadra listar --carrera geometria
escuadra listar --carrera matematicas
escuadra listar --carrera sistemas
```

Sin `--carrera`, `escuadra listar` muestra todas las especialidades y sus herramientas. Si el código no coincide con una especialidad registrada, el CLI informa que no encontró herramientas e imprime los códigos disponibles.

### Herramientas registradas en el código

Los nombres siguientes proceden de las clases que heredan de `Herramienta` y que descubre el registro del proyecto. Son los nombres que se muestran al listar; no son una promesa de que exista una invocación individual funcional para cada una.

**Ingeniería Civil (`civil`)**

- `Diseño Vial`
- `Combinación de cargas`
- `Carga Crítica de Euler`

**Ingeniería Eléctrica (`electrica`)**

- `Potencia Trifásica`
- `Conversión de unidades eléctricas`
- `Ley de Ohm`
- `Divisor de tensión`

**Geometría (`geometria`)**

- `Resolución de triángulos`
- `Figuras Compuestas`
- `Transformaciones Geométricas`
- `Cálculo de áreas`

**Matemáticas (`matematicas`)**

- `Matemática financiera`
- `Conversión de unidades`
- `Números complejos`
- `Sistemas de ecuaciones lineales`
- `Calculadora científica`

**Ingeniería de Sistemas e Informática (`sistemas`)**

- `Complemento a 2`
- `Tablas de verdad`
- `Tabla ASCII`
- `Mapas de Karnaugh`
- `Conversión de bases`

## 5. Estado de la ejecución individual de herramientas

El CLI crea subcomandos a partir del atributo `nombre` de cada clase de herramienta. Sin embargo, en el código revisado esos subcomandos no reciben argumentos específicos de cálculo. Además, la función de despacho intenta importar `escuadra.modulos.<nombre>` usando el nombre visible de la herramienta, mientras que las clases están organizadas en subpaquetes (por ejemplo, `escuadra.modulos.civil` y `escuadra.modulos.electrica`).

Por esa razón, no se deben documentar llamadas con parámetros como si estuvieran implementadas. En el estado revisado, la ruta de ejecución individual no constituye una interfaz CLI de cálculo utilizable y puede terminar mostrando el mensaje de herramienta no disponible. Los parámetros de las herramientas se ingresan desde sus interfaces correspondientes, no mediante opciones CLI verificadas en este código.

## 6. Salida JSON

El parser define la opción global:

```bash
escuadra --json <comando>
```

La implementación utiliza esta opción para intentar imprimir en JSON el resultado de la ruta de ejecución individual de una herramienta. No es una opción de exportación a archivo y no convierte la salida de `listar` ni la salida del subcomando `version` en JSON. Debido a las limitaciones de despacho indicadas en la sección anterior, no se debe asumir que actualmente produce un cálculo JSON válido para las herramientas registradas.

## 7. Ejemplos de ejecución y salida esperada

Los ejemplos siguientes utilizan `listar`, que sí tiene una implementación directa en el CLI. Se muestran las herramientas registradas con sus descripciones; el orden es alfabético, como establece `herramientas_por_carrera()`.

### Ejemplo 1: consultar herramientas de Ingeniería Civil

```bash
escuadra listar --carrera civil
```

Salida esperada (extracto):

```text
Ingeniería Civil
───────────────
  Carga Crítica de Euler          Calcula la carga crítica de pandeo para columnas a compresión.
  Combinación de cargas           Calcula una combinación simplificada de cargas vivas y muertas.
  Diseño Vial                     Calcula pendiente y peralte de curva para diseño vial.
```

### Ejemplo 2: consultar herramientas de Ingeniería Eléctrica

```bash
escuadra listar --carrera electrica
```

Salida esperada (extracto):

```text
Ingeniería Eléctrica
────────────────────
  Conversión de unidades eléctricas Convierte entre unidades de potencia (W, kW, HP)y unidades de energía (Wh, kWh, J).
  Divisor de tensión                Calcula el voltaje de salida o las resistencias necesarias en un divisor de tensión.
  Ley de Ohm                       Calcula voltaje, corriente o resistencia a partir de las otras dos magnitudes.
  Potencia Trifásica               Calcula la potencia activa, reactiva y aparente en sistemas trifásicos.
```

### Ejemplo 3: consultar herramientas de Geometría

```bash
escuadra listar --carrera geometria
```

Salida esperada (extracto):

```text
Geometría
─────────
  Cálculo de áreas                 Calcula el área de figuras geométricas básicas: triángulo, círculo, rectángulo y trapecio.
  Figuras Compuestas               Calcula el área y volumen total de una figura compuesta.
  Resolución de triángulos         Calcula triángulos usando ley de senos y cosenos.
  Transformaciones Geométricas     Permite rotar, trasladar y escalar puntos en el plano cartesiano.
```

### Ejemplos adicionales para las otras especialidades

```bash
escuadra listar --carrera matematicas
```

Salida esperada (extracto):

```text
Matemáticas
────────────
  Calculadora científica          Calculadora con operaciones aritméticas, trigonométricas, logarítmicas y constantes.
  Conversión de unidades           Convierte valores entre unidades de longitud, masa, tiempo y temperatura.
  Matemática financiera            Calcula valor futuro, valor presente e interés compuesto.
  Números complejos                Operaciones con números complejos: suma, resta, producto, división, módulo, conjugado y conversiones entre forma rectangular y polar.
  Sistemas de ecuaciones lineales  Resuelve sistemas A·x = b para tamaños entre 2x2 y 5x5.
```

```bash
escuadra listar --carrera sistemas
```

Salida esperada (extracto):

```text
Ingeniería de Sistemas e Informática
────────────────────────────────────
  Complemento a 2      Convierte entre decimal con signo y representación en complemento a 2.
  Conversión de bases  Convierte un número entre decimal, binario, octal y hexadecimal.
  Mapas de Karnaugh    Genera mapas de Karnaugh y realiza simplificaciones básicas de expresiones booleanas.
  Tabla ASCII          Convierte caracteres a código ASCII y lista rangos de la tabla estándar.
  Tablas de verdad     Genera la tabla de verdad de una expresión booleana con hasta 4 variables.
```

En los cinco casos el formato de salida es el mismo: etiqueta de la especialidad, separador y nombres con sus descripciones.

## 8. Formatos de exportación

El código del proyecto contiene utilidades de exportación a los siguientes formatos:

- **JSON**: `src/escuadra/io/exportador_json.py` permite escribir un diccionario o una lista en un archivo JSON.
- **Markdown**: `src/escuadra/io/exportador_markdown.py` contiene funciones para generar contenido Markdown.
- **LaTeX**: `src/escuadra/io/exportador_latex.py` contiene una función para generar tablas LaTeX.

Estas utilidades son módulos de entrada/salida del proyecto; no son subcomandos ni opciones de exportación de la CLI revisada. En particular, no existe en `cli.py` una sintaxis como `--exportar`, `--formato`, `--salida` o `--archivo`. La opción CLI `--json` se refiere a la presentación de una respuesta en la salida estándar cuando la ruta de ejecución de herramienta llega a producir un resultado, no a guardar un archivo.

## 9. Autocompletado

El CLI integra `argcomplete`. La activación depende de la configuración del shell y de tener instalada la dependencia. Por ejemplo, en Bash:

```bash
eval "$(register-python-argcomplete escuadra)"
```

La integración permite completar los argumentos que expone el parser; no agrega parámetros de cálculo que no estén definidos en el CLI.

## 10. Resumen de opciones disponibles

| Opción o comando | Descripción |
|---|---|
| `--help` | Muestra la ayuda del parser o de un subcomando. |
| `--version`, `-v` | Imprime la versión del paquete. |
| `--json` | Solicita salida JSON en la ruta de ejecución individual de herramienta; no exporta a archivo. |
| `listar` | Lista las herramientas registradas. |
| `listar --carrera CARRERA` | Filtra el listado por `civil`, `electrica`, `geometria`, `matematicas` o `sistemas`. |
| `version` | Muestra información de versión y diagnóstico del entorno. |
| `interactivo` | Está registrado, pero no funciona en el estado revisado porque importa `escuadra.registry`, módulo inexistente en el paquete. |

---

**Alcance de esta guía:** refleja el código CLI inspeccionado en esta versión del repositorio. Si se implementa posteriormente el despacho de cálculos y la definición de argumentos por herramienta, esta referencia deberá ampliarse con los parámetros obligatorios y opcionales reales de cada comando.