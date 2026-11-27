# Estructura del Proyecto - ChuspaCalc

Este documento describe la arquitectura de software y la organización de directorios del repositorio **ChuspaCalc** para orientar a nuevos desarrolladores y asegurar la escalabilidad del sistema.

## Descripción General del Proyecto

**ChuspaCalc** es una suite de herramientas de ingeniería y utilitarios diseñada bajo una arquitectura modular. El sistema consolida módulos analíticos para la resolución de sistemas lineales, cálculos trigonométricos, potencias, conversión de unidades físicas (masa, energía, temperatura, etc.), herramientas informáticas de bajo nivel (conversión de bases, complemento a dos, tablas ASCII) y una interfaz gráfica de usuario (GUI) para interactuar con estas funciones.

---

## Árbol de Directorios Completo

```text
.
├── .github/              # Flujos de trabajo de GitHub Actions (CI/CD)
├── data/                 # Datasets y recursos estáticos
├── docs/                 # Documentación técnica del proyecto
├── security/             # Herramientas y auditorías de seguridad
├── src/                  # Código fuente de la aplicación
│   └── ChuspaCalc/       # Paquete principal del proyecto
│       ├── modulos/      # Submódulos de lógica de negocio
│       │   ├── matematicas/ # Conversores y calculadoras matemáticas
│       │   └── sistemas/    # Herramientas informáticas y de sistemas
│       └── ui/           # Componentes de la interfaz gráfica de usuario
└── tests/                # Pruebas automatizadas (Pytest)

Descripción Detallada de Directorios y Componentes
1. Núcleo del Código (src/ChuspaCalc/)
Este directorio contiene la lógica ejecutable del programa, organizada en paquetes de Python (.py) utilizando archivos de inicialización __init__.py.

modulos/matematicas/: Contiene los scripts encargados de realizar cálculos científicos y conversiones dimensionales de ingeniería.

Conversores físicos: conversor_angulo.py, conversor_energia.py, conversor_longitud_extendido.py, conversor_masa.py, conversor_presion.py, conversor_temperatura.py, conversor_velocidad.py.

Herramientas analíticas: herramienta_calculadora_cientifica.py, herramienta_sistemas_lineales.py, potencias_raices.py, trigonometria.py.

modulos/sistemas/: Aloja utilitarios orientados a la arquitectura de computadoras y lógica digital.

herramienta_complemento_a_2.py: Lógica para operaciones binarias de cambio de signo.

herramienta_conversion_bases.py: Conversión entre sistemas numéricos (Binario, Octal, Decimal, Hexadecimal).

tabla_ascii.py: Mapeo y manejo de caracteres codificados.

ui/:

ventana_principal.py: Archivo que define la interfaz gráfica de usuario (GUI) principal empleando librerías visuales de Python. Une la lógica de los módulos con controles interactivos.

2. Infraestructura y Soporte
.github/: Aloja archivos de flujo de trabajo en formato .yml (como ci.yml). Configura las máquinas virtuales encargadas de correr el linteo de Ruff y las pruebas unitarias automáticamente en cada Pull Request.

data/: Destinado a albergar datos crudos, archivos .csv o configuraciones persistentes necesarias para los módulos de cálculo.

docs/: Carpeta de documentación técnica en Markdown (.md). Centraliza manuales, este documento de estructura y especificaciones del sistema.

security/: Scripts dedicados al análisis estático en busca de vulnerabilidades, dependencias obsoletas o fugas de credenciales.

tests/: Suite de pruebas automatizadas con la estructura de archivos test_*.py. Contiene scripts de validación como test_linear_solver.py y test_loader.py para asegurar que los cambios de código no rompan la lógica matemática previa.

Archivos Críticos en la Raíz
pyproject.toml: Configuración central estandarizada para el entorno de Python (especifica herramientas como el linter Ruff).

requirements.txt: Listado explícito de dependencias externas del proyecto para una instalación limpia vía pip install -r requirements.txt.

.pre-commit-config.yaml: Automatiza ganchos de Git para revisar el estilo del código localmente antes de permitir un commit.

Makefile: Archivo de automatización que provee alias nativos en la consola Bash para agilizar tareas como limpiar la caché de Python o ejecutar pruebas.