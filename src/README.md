# Estructura del código fuente - ChuspaCalc

Esta carpeta contiene el código fuente principal de ChuspaCalc. El proyecto está organizado de forma modular para facilitar el mantenimiento, la incorporación de nuevas herramientas y la colaboración entre estudiantes y desarrolladores.

La mayor parte de la lógica de la aplicación se encuentra dentro del paquete `chuspacalc`, donde se agrupan los distintos componentes del sistema según su responsabilidad.

## Estructura general

```text
src/
├── README.md
└── chuspacalc/
    ├── app.py
    ├── cli.py
    ├── __init__.py
    ├── __main__.py
    ├── config/
    ├── core/
    ├── io/
    ├── math/
    ├── modulos/
    │   ├── civil/
    │   ├── electrica/
    │   ├── geometria/
    │   ├── matematicas/
    │   └── sistemas/
    ├── ui/
    └── utils/
```

## Archivos principales

### app.py

Contiene la lógica principal de inicialización de la aplicación. Coordina los distintos componentes del sistema y sirve como punto de entrada para la ejecución de ChuspaCalc.

### cli.py

Implementa la interfaz de línea de comandos (CLI). Permite ejecutar funcionalidades del proyecto desde la terminal y gestionar la interacción mediante comandos.

### __init__.py

Identifica a chuspacalc como un paquete de Python y permite la importación de sus módulos desde otras partes del proyecto.

### __main__.py

Define el comportamiento cuando el proyecto es ejecutado mediante:

```bash
python -m chuspacalc
```

Este archivo actúa como punto de entrada del paquete y redirige la ejecución hacia los componentes correspondientes.

## Descripción de directorios

### config/

Contiene configuraciones generales de la aplicación, parámetros de ejecución y componentes relacionados con la inicialización del sistema.

### core/

Agrupa la lógica central compartida por distintos módulos del proyecto. Su objetivo es centralizar funcionalidades fundamentales reutilizadas por varias herramientas.

### io/

Contiene componentes relacionados con entrada y salida de datos, incluyendo lectura, escritura, importación o exportación de información.

### math/

Incluye funciones matemáticas de propósito general utilizadas por diferentes módulos de ingeniería.

Centralizar estos cálculos evita duplicación de código y facilita el mantenimiento.

### modulos/

Es el directorio principal de herramientas de ingeniería. Cada subdirectorio representa un conjunto de funcionalidades específicas para una determinada área.

#### civil/

Herramientas orientadas a ingeniería civil, análisis estructural, vigas, cargas y cálculos relacionados.

#### electrica/

Contiene herramientas para cálculos eléctricos y análisis de circuitos.

#### geometria/

Incluye operaciones geométricas utilizadas por distintos módulos del proyecto.

#### matematicas/

Implementa calculadoras y operaciones matemáticas de uso general.

#### sistemas/

Contiene herramientas relacionadas con ingeniería de sistemas e informática.

### ui/

Incluye los componentes de interfaz de usuario utilizados por la aplicación para interactuar con el usuario.

### utils/

Contiene funciones auxiliares, utilidades y componentes reutilizables que apoyan distintas partes del sistema.

## Ejecutar el proyecto desde el código fuente

Una vez instaladas las dependencias necesarias, el proyecto puede ejecutarse directamente desde la raíz del repositorio mediante:

```bash
python -m chuspacalc
```

Este comando utiliza el archivo `__main__.py` como punto de entrada del paquete.

## Objetivo de la organización

La estructura modular de ChuspaCalc permite separar responsabilidades, facilitar el mantenimiento del código y simplificar la incorporación de nuevas herramientas.

Gracias a esta organización, diferentes colaboradores pueden trabajar simultáneamente en distintos módulos sin afectar otras áreas del proyecto, favoreciendo un desarrollo más ordenado y escalable.
