# Decisiones de Arquitectura (ADR)

Este documento registra las decisiones arquitectónicas clave del proyecto ChuspaCalc. Cada ADR documenta el contexto, la decisión tomada y sus consecuencias.

## Índice

- [ADR-001: Uso de argparse para el CLI](#adr-001-uso-de-argparse-para-el-cli)
- [ADR-002: Patrón Registry+Dispatcher para módulos](#adr-002-patrón-registrydispatcher-para-módulos)
- [ADR-003: Separación de módulos de cálculo del core](#adr-003-separación-de-módulos-de-cálculo-del-core)
- [ADR-004: Implementación manual de cálculos sin numpy](#adr-004-implementación-manual-de-cálculos-sin-numpy)

---

## ADR-001: Uso de argparse para el CLI

**Estado:** Aceptado

**Contexto:**
- El proyecto necesita una interfaz CLI para invocar los diferentes módulos (matemáticas, civil, eléctrica)
- Existen múltiples opciones en el ecosistema Python: `argparse` (biblioteca estándar), `click` (terceros, más declarativo), `typer` (moderno, basado en type hints), `docopt` (basado en documentación)
- El proyecto debe mantener cero dependencias externas innecesarias
- Los colaboradores tienen diferentes niveles de experiencia

**Decisión:**
Usar `argparse` de la biblioteca estándar de Python para implementar el CLI.

**Consecuencias:**
- ✅ Positivas: Sin dependencias externas, disponible en cualquier instalación de Python, curva de aprendizaje baja, suficiente para las necesidades actuales
- ❌ Negativas: Código más verboso que `click` o `typer`, menos características declarativas
- 📝 Neutral: Requiere escribir más líneas de código para comandos complejos

---

## ADR-002: Patrón Registry+Dispatcher para módulos

**Estado:** Aceptado

**Contexto:**
- El sistema debe soportar múltiples módulos de cálculo (matemáticas, civil, eléctrica)
- Cada módulo tiene múltiples herramientas/funciones
- Se necesita descubrir módulos automáticamente sin modificar el núcleo
- Es común que contribuidores agreguen nuevos módulos
- Alternativas evaluadas: importación estática (hardcoding), plugin system complejo (entry_points de setuptools), registro manual en archivo central

**Decisión:**
Implementar un patrón Registry + Dispatcher donde:
- Cada módulo se auto-registra en un registro central
- El dispatcher resuelve qué módulo/herramienta ejecutar basado en argumentos CLI
- El descubrimiento es por convención: escanear el directorio `modulos/`

**Consecuencias:**
- ✅ Positivas: Alta cohesión interna en cada módulo, bajo acoplamiento con el core, fácil agregar nuevos módulos sin tocar código existente, registro explícito que ayuda a depuración
- ❌ Negativas: Complejidad adicional al inicio, requiere que los desarrolladores sigan la convención de registro
- 📝 Neutral: Se necesita documentación clara sobre cómo registrar nuevos módulos

---

## ADR-003: Separación de módulos de cálculo del core

**Estado:** Aceptado

**Contexto:**
- El proyecto tiene funcionalidades de cálculo muy diversas (matemáticas, ingeniería civil, eléctrica)
- Cada área tiene sus propias fórmulas, unidades y casos de uso
- El core (`main.py`, `cli.py`) debe ser simple y estable
- Los módulos cambian con mayor frecuencia que el core
- Riesgo de que el core se convierta en un "god object" con toda la lógica

**Decisión:**
Separar físicamente los módulos de cálculo en el directorio `modulos/`, cada uno en su propio archivo. El core solo maneja el descubrimiento, dispatcher y orquestación básica. Cada módulo es independiente y autocontenido.

**Consecuencias:**
- ✅ Positivas: Core pequeño y mantenible, módulos pueden desarrollarse en paralelo por diferentes personas, pruebas aisladas por módulo, facilidad para eliminar o agregar módulos
- ❌ Negativas: Mayor complejidad inicial para entender la arquitectura, overhead de comunicación entre core y módulos
- 📝 Neutral: Se deben definir interfaces claras entre core y módulos

---

## ADR-004: Implementación manual de cálculos sin numpy

**Estado:** Aceptado

**Contexto:**
- El proyecto realiza cálculos matemáticos, estadísticos, trigonométricos y de ingeniería
- `numpy` es el estándar de facto para cálculos numéricos en Python
- `numpy` tiene un peso significativo (~30-40 MB)
- El proyecto está diseñado para ser liviano y fácil de instalar
- Los cálculos requeridos son relativamente simples (no matrices grandes ni operaciones vectorizadas complejas)

**Decisión:**
Implementar todos los cálculos manualmente usando solo funciones nativas de Python (`math` para trigonometría, operadores básicos para aritmética). No incluir `numpy` como dependencia.

**Consecuencias:**
- ✅ Positivas: Cero dependencias externas, instalación ultraligera, tiempo de importación mínimo, mayor comprensión de los algoritmos subyacentes
- ❌ Negativas: Mayor código a mantener, pérdida de optimizaciones de numpy (relevante solo para datos muy grandes), implementaciones manuales pueden tener bugs
- 📝 Neutral: El módulo `math` de Python sí está permitido (es parte de la stdlib)

---

## Historial de cambios

| Fecha | ADR | Cambio |
|-------|-----|--------|
| 2026-06-13 | ADR-001 a ADR-004 | Documentación inicial |
