# Escuadra - Calculadora Técnica para Ingeniería

[![CI](https://github.com/sis-inf/ChuspaCalc/actions/workflows/ci.yml/badge.svg)](https://github.com/sis-inf/ChuspaCalc/actions/workflows/ci.yml)
[![Licencia MIT](https://img.shields.io/badge/licencia-MIT-blue.svg)](LICENSE)

Una aplicación de escritorio que centraliza herramientas de cálculo especializadas para estudiantes y docentes de ingeniería.

---

## Inicio rápido

```bash
# 1. Clonar el repositorio y entrar al directorio
git clone https://github.com/sis-inf/ChuspaCalc.git && cd ChuspaCalc

# 2. Crear entorno virtual e instalar dependencias
python -m venv .venv && source .venv/bin/activate && pip install -e ".[dev]"

# 3. Ejecutar la aplicación
python -m chuspacalc
```

> En Windows reemplaza `source .venv/bin/activate` por `.venv\Scripts\activate`

---

## 📌 ¿Qué es?

**Escuadra** es una aplicación de escritorio desarrollada en Python con PySide6 que proporciona una colección extensible de herramientas de cálculo organizadas por carrera. Su diseño modular permite agregar nuevas funcionalidades sin modificar el núcleo de la aplicación, lo que la convierte en un proyecto vivo y en constante crecimiento.

---

## 🎯 ¿Para quién es?

- **Estudiantes de ingeniería** que necesitan realizar cálculos específicos de su carrera.
- **Docentes** que desean disponer de herramientas rápidas para ejemplificar conceptos en clase.
- **Desarrolladores** interesados en contribuir con nuevas herramientas al ecosistema.

---

## 💡 ¿Qué problema resuelve?

Los estudiantes y docentes de ingeniería suelen necesitar realizar cálculos recurrentes (conversión de sistemas numéricos, análisis de circuitos, operaciones con matrices, etc.) que:

- Requieren múltiples herramientas dispersas (calculadoras físicas, software pesado, hojas de cálculo).
- No están unificadas en una interfaz simple y accesible.
- Dificultan el aprendizaje al no mostrar el paso a paso de los cálculos.

**Escuadra** resuelve esto ofreciendo:

✅ Una interfaz unificada y limpia.
✅ Herramientas organizadas por carrera.
✅ Resultados claros y, cuando es posible, con detalle del proceso.
✅ Un sistema extensible para que cualquier estudiante pueda agregar nuevas herramientas.

---

## 🖥️ Capturas de pantalla

![Ventana principal de Escuadra con la herramienta de conversión de bases cargada](docs/img/ventana-principal.png)

*Ventana principal mostrando la herramienta de conversión entre sistemas numéricos.*

---

## 📚 Carreras y herramientas incluidas

### Ingeniería en Sistemas
- **Conversión de bases**: Binario, Octal, Decimal, Hexadecimal.
- **Complemento a 2**: Representación de números negativos en binario.
- **Tablas de verdad**: Generación de tablas para compuertas lógicas.
- **Conversor de color**: RGB a Hexadecimal y viceversa.
- **Tabla ASCII**: Visualización de caracteres ASCII.

### Ingeniería Matemática
- **Conversión de unidades**: Longitud, masa, temperatura, velocidad, presión, energía, ángulo.
- **Trigonometría**: Cálculo de funciones trigonométricas.
- **Estadísticas**: Media, mediana, moda, desviación estándar.
- **Sistemas lineales**: Resolución de sistemas de ecuaciones.
- **Potencias y raíces**: Cálculo de potencias y raíces.

### Ingeniería Eléctrica
- **Ley de Ohm**: Cálculo de voltaje, corriente y resistencia.
- **Divisor de tensión**: Cálculo de voltaje en circuitos con resistencias.
- **Circuitos en serie/paralelo**: Cálculo de resistencia equivalente.
- **Potencia eléctrica**: Cálculo de potencia en circuitos.

---

## 📦 Requisitos

- **Python**: 3.10 o superior.
- **Sistema operativo**: Linux, macOS o Windows (64 bits).
- **Dependencias**: PySide6 y otras librerías que se instalarán automáticamente.

---

## 🛠️ Instalación desde código fuente

```bash
# Clonar el repositorio
git clone https://github.com/sis-inf/ChuspaCalc.git
cd ChuspaCalc

# Crear y activar entorno virtual
python -m venv .venv

# En Linux/macOS:
source .venv/bin/activate

# En Windows:
.venv\Scripts\activate

# Instalar en modo desarrollo
pip install -e ".[dev]"
```
## Documentación

Ver el [índice general de documentación](docs/indice-general.md) para una lista completa organizada por categoría.
