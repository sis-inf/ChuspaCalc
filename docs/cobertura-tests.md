# Estado actual de cobertura de tests por módulo

## Tabla de cobertura

| Archivo | Líneas totales | Líneas cubiertas | Porcentaje |
| :--- | :--- | :--- | :--- |
| `src/ChuspaCalc/app.py` | 33 | 0 | 0% |
| `src/ChuspaCalc/core/carrera.py` | 71 | 24 | 33% |
| `src/ChuspaCalc/core/herramienta.py` | 23 | 23 | 100% |
| `src/ChuspaCalc/core/registry.py` | 18 | 15 | 83% |
| `src/ChuspaCalc/core/tutorial.py` | 52 | 41 | 78% |
| `src/ChuspaCalc/modulos/electrica/herramienta_ley_ohm.py` | 23 | 0 | 0% |
| `src/ChuspaCalc/modulos/electrica/herramienta_divisor_tension.py` | 16 | 0 | 0% |
| `src/ChuspaCalc/modulos/sistemas/herramienta_complemento_a_2.py` | 58 | 19 | 32% |
| `src/ChuspaCalc/modulos/sistemas/herramienta_tablas_verdad.py` | 38 | 32 | 84% |
| `src/ChuspaCalc/modulos/matematicas/calculo_area.py` | 27 | 0 | 0% |
| `src/ChuspaCalc/modulos/matematicas/herramienta_calculadora_cientifica.py` | 99 | 0 | 0% |

## Módulos con cobertura baja

Los siguientes módulos presentan una cobertura crítica **inferior al 70%** y requieren la creación prioritaria de pruebas unitarias:

* **`src/ChuspaCalc/app.py`** (0%)
* **`src/ChuspaCalc/core/carrera.py`** (33%)
* **`src/ChuspaCalc/modulos/electrica/herramienta_ley_ohm.py`** (0%)
* **`src/ChuspaCalc/modulos/electrica/herramienta_divisor_tension.py`** (0%)
* **`src/ChuspaCalc/modulos/sistemas/herramienta_complemento_a_2.py`** (32%)
* **`src/ChuspaCalc/modulos/matematicas/calculo_area.py`** (0%)
* **`src/ChuspaCalc/modulos/matematicas/herramienta_calculadora_cientifica.py`** (0%)

## Cómo mejorar la cobertura

Para agregar tests a un módulo específico y mejorar estos porcentajes, sigue estos pasos:

1. **Identificar las líneas faltantes:** Revisa el reporte detallado ejecutando `pytest --cov=src/ChuspaCalc --cov-report=term-missing` y observa los rangos numéricos de la columna `Missing`. Esas son las líneas de código exactas que ninguna prueba ha ejecutado.
2. **Localizar o crear el archivo de pruebas:** Ve al directorio `tests/modulos/` (o la subcarpeta correspondiente) y abre el archivo de test relacionado (por ejemplo, `test_ley_ohm.py`). Si el archivo no existe, créalo bajo la nomenclatura estándar `test_*.py`.
3. **Escribir nuevos casos de prueba:** Redacta funciones `def test_...():` utilizando aserciones estándar de Python (`assert`) para validar los cálculos matemáticos, límites de datos y manejo de excepciones del módulo.
4. **Verificar el progreso:** Ejecuta nuevamente el comando de cobertura para confirmar que el porcentaje del archivo ha aumentado y que las líneas salieron de la lista `Missing`.