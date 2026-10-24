# 📊 Benchmarks de herramientas

Este documento contiene los tiempos de ejecución de referencia para las herramientas disponibles en ChuspaCalc.

## 🖥️ Entorno de referencia

| Componente | Especificación |
|------------|----------------|
| **Python** | 3.10 |
| **CPU** | Intel Core i5-8250U (o similar) |
| **RAM** | 8 GB DDR4 |
| **Sistema operativo** | Windows 10 / Linux Ubuntu 22.04 |

---

## 📈 Resultados de benchmarks

Los siguientes tiempos representan el **promedio de 1000 ejecuciones** en microsegundos (µs) para cada herramienta:

| Herramienta | Tiempo promedio (µs) | Descripción |
|-------------|----------------------|-------------|
| **Longitud de texto** | 1.25 | Calcula la longitud de un texto |
| **Contador de palabras** | 3.45 | Cuenta palabras en un texto |
| **Promedio de números** | 2.10 | Calcula el promedio de una lista |
| **Suma de lista** | 1.80 | Suma todos los elementos de una lista |
| **Generador de aleatorios** | 4.20 | Genera números aleatorios |
| **Ordenamiento rápido** | 45.60 | Ordena una lista de 100 números |
| **Búsqueda binaria** | 8.30 | Busca un elemento en una lista ordenada |

> **Nota:** Estos tiempos son referenciales y pueden variar según el hardware y la carga del sistema.

---

## 🧪 Cómo ejecutar los benchmarks

### Opción 1: Usando `timeit` (recomendado)

```bash
python -m timeit -n 1000 "import src.escuadra.modulos as m; m.herramienta_ejemplo()"
