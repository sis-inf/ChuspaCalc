# Arquitectura del Sistema - Proyecto ChuspaCalc

## 1. Visión General

El proyecto **ChuspaCalc** está diseñado como una plataforma modular de herramientas orientadas a distintas ramas de la ingeniería. La arquitectura sigue un principio de **Separación de Responsabilidades**, permitiendo que cada área de ingeniería implemente sus propias soluciones de forma independiente.

El sistema prioriza la escalabilidad, permitiendo agregar nuevas herramientas sin afectar el funcionamiento general.

---

## 2. Stack Tecnológico

| Componente           | Tecnología | Versión | Justificación                                                                     |
| -------------------- | ---------- | ------- | --------------------------------------------------------------------------------- |
| **Lenguaje Base**    | Python     | 3.10+   | Amplio soporte para cálculo numérico y facilidad de uso                           |
| **Interfaz gráfica** | PySide6    | 6.6+    | Framework Qt oficial para Python; permite crear UIs de escritorio multiplataforma |
| **Testing**          | pytest     | 8+      | Framework estándar para pruebas en Python                                         |
| **Linter**           | ruff       | 0.4+    | Análisis estático y formateo de código rápido                                     |
| **Gestión de deps**  | pip        | ---     | Manejo de dependencias mediante requirements.txt y pyproject.toml                 |
| **Documentación**    | Markdown   | ---     | Estándar para documentación en repositorios Git                                   |

---

## 3. Por qué Python y no Node.js

El repositorio fue inicialmente documentado con instrucciones de Node.js (npm install, node index.js), lo que generaba ambigüedad. La decisión de usar Python se basa en:

- Todo el código fuente del proyecto (src/ChuspaCalc/) está escrito en Python.
- Los módulos de cálculo de ingeniería (civil, eléctrica, matemáticas, sistemas) utilizan Python puro.
- El sistema de empaquetado usa pyproject.toml y setuptools, herramientas del ecosistema Python.
- PySide6 es una librería Python para interfaces gráficas, sin dependencia de Node.js.
- Los tests están escritos con pytest, no con ningún framework de JavaScript.

---

## 4. Componentes Principales

- Core (src/ChuspaCalc/core/): Lógica central del sistema, dispatcher y registro de herramientas.
- Módulos de ingeniería (src/ChuspaCalc/modulos/): Cada rama de ingeniería tiene su propio subdirectorio con herramientas independientes.
- Interfaz de usuario (src/ChuspaCalc/ui/): Componentes visuales basados en PySide6.
- Utilidades (src/ChuspaCalc/utils/): Funciones auxiliares, validaciones y helpers compartidos.
- Configuración (src/ChuspaCalc/config/): Carga y gestión de configuración del proyecto.
- IO (src/ChuspaCalc/io/): Parsers para leer archivos de entrada como CSV.
- Matemáticas (src/ChuspaCalc/math/): Operaciones matemáticas reutilizables como matrices, estadísticas y sistemas lineales.
- CLI (src/ChuspaCalc/cli.py): Interfaz de línea de comandos para acceder a las herramientas.

---

## 5. Organización por Ramas de Ingeniería

**El sistema está estructurado en módulos independientes según cada área:**

```text
ChuspaCalc/
├── src/
│   └── ChuspaCalc/
│       ├── core/           # Dispatcher y registro de herramientas
│       ├── io/             # Parsers de archivos de entrada (CSV, etc.)
│       ├── math/           # Operaciones matemáticas reutilizables
│       ├── modulos/
│       │   ├── civil/      # Herramientas de ingeniería civil
│       │   ├── electrica/  # Herramientas de ingeniería eléctrica
│       │   ├── geometria/  # Herramientas de geometría
│       │   ├── matematicas/# Herramientas matemáticas
│       │   └── sistemas/   # Herramientas de ingeniería de sistemas
│       ├── ui/             # Componentes de interfaz (PySide6)
│       ├── utils/          # Utilidades compartidas
│       └── config/         # Configuración
├── docs/                   # Documentación del proyecto
├── tests/                  # Pruebas automatizadas
├── requirements.txt        # Dependencias de producción
├── requirements-dev.txt    # Dependencias de desarrollo
└── pyproject.toml          # Metadatos y configuración del paquete
```

---

## 6. Decisiones de Diseño

### Decisión 1: Arquitectura Modular por rama de Ingeniería

**Contexto:** El proyecto cubre múltiples áreas de ingeniería con necesidades distintas.  
**Decisión:** Separar cada rama en módulos independientes dentro de src/ChuspaCalc/modulos/  
**Consecuencias:** Permite desarrollo paralelo sin conflictos y facilita agregar nuevas herramientas.

---

### Decisión 2: Interfaz gráfica con PySide6

**Contexto:** Se requiere una aplicación de escritorio accesible para estudiantes y profesionales.  
**Decisión:** Usar PySide6 como framework de UI, con componentes reutilizables en src/ChuspaCalc/ui/.  
**Consecuencias:** Interfaz multiplataforma (Windows, Linux, macOS) con el binding oficial de Qt para Python.

---

### Decisión 3: Módulos de cálculo independientes de la UI

**Contexto:** Las funciones de cálculo deben poder usarse desde la UI, la CLI o directamente como librería.  
**Decisión:** Separar la lógica de cálculo (módulos) de la capa de presentación (ui, cli).  
**Consecuencias:** Código reutilizable y más fácil de testear de forma aislada.

---

## 7. Flujo de Datos

1. El usuario interactúa con la UI (PySide6) o la CLI.
2. La interfaz recibe los parámetros de entrada y los valida.
3. Se invoca la función del módulo correspondiente (ej. calcular_reacciones).
4. El módulo procesa los datos usando matemática pura de Python.
5. El resultado se devuelve a la interfaz y se muestra al usuario.
