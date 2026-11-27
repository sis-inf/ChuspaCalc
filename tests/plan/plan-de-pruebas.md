# Plan de Pruebas - Proyecto ChuspaCalc

## 1. Objetivo
Garantizar la fiabilidad, precisión numérica y estabilidad de la suite de cálculo de ingeniería **ChuspaCalc**, asegurando que los algoritmos matemáticos entreguen resultados exactos dentro de las tolerancias permitidas y que el sistema responda correctamente ante datos de entrada anómalos.

## 2. Alcance
### En alcance
- Validación de algoritmos de cálculo estructural y estadístico.
- Verificación de la precisión decimal (tolerancia de error 1e-7).
- Pruebas de manejo de excepciones (divisiones por cero, raíces negativas).
- Compatibilidad del entorno de ejecución local y CI.

### Fuera de alcance
- Seguridad de red o ataques externos (Pentesting).
- Pruebas de interfaz gráfica de usuario (UI/UX) avanzadas (el foco es el motor de cálculo).
- Compatibilidad con sistemas operativos móviles.

## 3. Tipos de prueba
- [x] **Unitarias:** Validación de funciones matemáticas individuales.
- [x] **Integración:** Verificación del flujo de datos entre módulos de cálculo.
- [x] **Funcionales manuales:** Validación de casos de uso específicos de ingeniería.
- [x] **Rendimiento:** Evaluación de tiempos de respuesta con grandes matrices de datos.
- [ ] Seguridad
- [x] **Regresión:** Asegurar que nuevos cálculos no afecten fórmulas ya validadas.

## 4. Entornos

| Entorno | SO | Versión |
| --- | --- | --- |
| Local | Windows 10/11 / Linux | Python 3.10 o superior / PySide6 / pytest |
| CI | Ubuntu latest | GitHub Actions |

### Tecnologías y herramientas de pruebas

- Python 3.10 o superior: entorno de ejecución.
- PySide6 (>=6.6,<7.0): interfaz gráfica Qt.
- pytest (>=8,<10): pruebas automatizadas.
- pytest-qt: pruebas de componentes Qt.
- GitHub Actions: integración continua.

Las dependencias se encuentran definidas en `pyproject.toml`.

## 5. Responsables

| Rol | Responsable |
| --- | --- |
| Diseño de casos | BALTAZAR BORRAS |
| Ejecución manual | BALTAZAR BORRAS |
| Automatización | BALTAZAR BORRAS / GitHub Actions |
| Reporte | BALTAZAR BORRAS |

## 6. Criterios de salida
- [x] Cobertura mínima de **80%** de las funciones críticas de cálculo.
- [x] Cero bugs críticos abiertos (especialmente errores de precisión).
- [x] Todos los casos de prueba matemáticos ejecutados y validados.

## 7. Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
| --- | --- | --- | --- |
| Errores de precisión decimal | Alta | Crítico | Uso de `float` de Python y validación con tablas estándar. |
| Desbordamiento de memoria (grandes datos) | Media | Alto | Implementación de pruebas de estrés y límites de entrada. |
| Inconsistencia en CI (Ubuntu) vs Local | Baja | Medio | Uso de contenedores o entornos estandarizados en GitHub Actions. |
| Fórmulas matemáticas mal implementadas | Media | Crítico | Revisión por pares y contraste con software de ingeniería (Matlab/Excel). |

## 8. Plan de pruebas para módulos del sprint actual

### 8.1. Módulo Civil (`modulos/civil/`)

#### Funciones a probar

| Función | Descripción |
| --------- | ------------- |
| `calcular_terreno()` | Calcula áreas y perímetros de terrenos |
| `calcular_materiales()` | Estima cantidad de materiales necesarios |
| `validar_normativa()` | Valida que el diseño cumpla con normativas |

#### Casos de prueba recomendados

| Tipo | Descripción |
| ------ | ------------- |
| **Normales** | Datos típicos de entrada (terrenos regulares) |
| **Borde** | Valores límite (áreas mínimas/máximas) |
| **Error** | Datos inválidos (valores negativos, tipos incorrectos) |

#### Cobertura objetivo

- **Mínimo**: 80%
- **Ideal**: 90%

---

### 8.2. Módulo Eléctrica (`modulos/electrica/`)

#### Funciones a probar

| Función | Descripción |
| --------- | ------------- |
| `calcular_corriente()` | Calcula corriente eléctrica con ley de Ohm |
| `calcular_potencia()` | Calcula potencia eléctrica |
| `calcular_resistencia()` | Calcula resistencia equivalente |

#### Casos de prueba recomendados

| Tipo | Descripción |
| ------ | ------------- |
| **Normales** | Valores típicos de resistencia y voltaje |
| **Borde** | Resistencias cero o infinito (circuitos abiertos) |
| **Error** | Valores negativos, divisiones por cero |

#### Cobertura objetivo

- **Mínimo**: 85%
- **Ideal**: 95%

---

### 8.3. Módulo Geometría (`modulos/geometria/`)

#### Funciones a probar

| Función | Descripción |
| --------- | ------------- |
| `area_circulo()` | Calcula área de un círculo |
| `perimetro_rectangulo()` | Calcula perímetro de un rectángulo |
| `volumen_cilindro()` | Calcula volumen de un cilindro |

#### Casos de prueba recomendados

| Tipo | Descripción |
| ------ | ------------- |
| **Normales** | Figuras con dimensiones típicas |
| **Borde** | Radios o lados iguales a cero |
| **Error** | Tipos de datos incorrectos, valores negativos |

#### Cobertura objetivo

- **Mínimo**: 80%
- **Ideal**: 90%
