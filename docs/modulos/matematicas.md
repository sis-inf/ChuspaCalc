# Módulo de Matemáticas

## Descripción del módulo

El módulo de Matemáticas proporciona un conjunto de herramientas y funciones para realizar cálculos matemáticos esenciales, conversiones de unidades y análisis estadísticos. Este módulo está diseñado para facilitar operaciones comunes en matemáticas aplicadas, desde conversiones básicas de longitud y temperatura hasta cálculos trigonométricos y análisis de datos estadísticos.

El alcance del módulo incluye:
- Conversión entre diferentes unidades de medida (longitud, temperatura, tiempo)
- Cálculos trigonométricos fundamentales
- Análisis estadístico descriptivo
- Operaciones con números complejos
- Cálculos de álgebra lineal básica

## Herramientas disponibles

| Nombre | Descripción | Funciones principales |
|--------|-------------|----------------------|
| conversor_longitud | Convierte valores entre diferentes unidades de longitud (metros, kilómetros, millas, pies, pulgadas) | `metros_a_kilometros()`, `kilometros_a_millas()`, `pies_a_metros()`, `pulgadas_a_centimetros()` |
| conversor_temperatura | Realiza conversiones entre escalas de temperatura (Celsius, Fahrenheit, Kelvin) | `celsius_a_fahrenheit()`, `fahrenheit_a_celsius()`, `celsius_a_kelvin()`, `kelvin_a_celsius()` |
| estadísticas | Calcula medidas estadísticas descriptivas de un conjunto de datos | `media()`, `mediana()`, `moda()`, `desviacion_estandar()`, `varianza()` |
| trigonometría | Proporciona funciones trigonométricas básicas y conversiones de ángulos | `seno()`, `coseno()`, `tangente()`, `grados_a_radianes()`, `radianes_a_grados()` |
| numeros_complejos | Realiza operaciones aritméticas con números complejos | `suma()`, `resta()`, `multiplicacion()`, `division()`, `modulo()`, `conjugado()` |

## Ejemplos de uso

### conversor_longitud

```python
from ChuspaCalc.matematicas.conversor_longitud import metros_a_kilometros, kilometros_a_millas, pies_a_metros

# Convertir metros a kilómetros
distancia_m = 5000
distancia_km = metros_a_kilometros(distancia_m)
print(f"{distancia_m} metros = {distancia_km} kilómetros")

# Convertir kilómetros a millas
distancia_km = 10
distancia_millas = kilometros_a_millas(distancia_km)
print(f"{distancia_km} kilómetros = {distancia_millas:.2f} millas")

# Convertir pies a metros
distancia_pies = 100
distancia_m = pies_a_metros(distancia_pies)
print(f"{distancia_pies} pies = {distancia_m:.2f} metros")
```

### conversor_temperatura

```python
from ChuspaCalc.matematicas.conversor_temperatura import celsius_a_fahrenheit, fahrenheit_a_celsius, celsius_a_kelvin

# Convertir Celsius a Fahrenheit
temp_c = 25
temp_f = celsius_a_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

# Convertir Fahrenheit a Celsius
temp_f = 77
temp_c = fahrenheit_a_celsius(temp_f)
print(f"{temp_f}°F = {temp_c}°C")

# Convertir Celsius a Kelvin
temp_c = 0
temp_k = celsius_a_kelvin(temp_c)
print(f"{temp_c}°C = {temp_k}K")
```

### estadísticas

```python
from ChuspaCalc.matematicas.estadisticas import media, mediana, moda, desviacion_estandar, varianza

# Conjunto de datos de ejemplo
datos = [23, 45, 67, 89, 12, 34, 56, 78, 90, 23]

# Calcular media
promedio = media(datos)
print(f"Media: {promedio}")

# Calcular mediana
mediana_valor = mediana(datos)
print(f"Mediana: {mediana_valor}")

# Calcular moda
moda_valor = moda(datos)
print(f"Moda: {moda_valor}")

# Calcular desviación estándar
desv_est = desviacion_estandar(datos)
print(f"Desviación estándar: {desv_est:.2f}")

# Calcular varianza
var = varianza(datos)
print(f"Varianza: {var:.2f}")
```

### trigonometría

```python
from ChuspaCalc.matematicas.trigonometria import seno, coseno, tangente, grados_a_radianes, radianes_a_grados
import math

# Calcular seno, coseno y tangente de un ángulo en radianes
angulo_rad = math.pi / 4  # 45 grados en radianes
print(f"Seno de π/4: {seno(angulo_rad):.4f}")
print(f"Coseno de π/4: {coseno(angulo_rad):.4f}")
print(f"Tangente de π/4: {tangente(angulo_rad):.4f}")

# Convertir grados a radianes
angulo_grados = 60
angulo_rad = grados_a_radianes(angulo_grados)
print(f"{angulo_grados}° = {angulo_rad:.4f} radianes")

# Convertir radianes a grados
angulo_rad = math.pi / 3
angulo_grados = radianes_a_grados(angulo_rad)
print(f"{angulo_rad:.4f} radianes = {angulo_grados:.2f}°")
```

### numeros_complejos

```python
from ChuspaCalc.matematicas.numeros_complejos import suma, resta, multiplicacion, division, modulo, conjugado

# Definir números complejos como tuplas (parte_real, parte_imaginaria)
z1 = (3, 4)   # 3 + 4i
z2 = (1, -2)  # 1 - 2i

# Suma
resultado = suma(z1, z2)
print(f"Suma: {z1} + {z2} = {resultado}")

# Resta
resultado = resta(z1, z2)
print(f"Resta: {z1} - {z2} = {resultado}")

# Multiplicación
resultado = multiplicacion(z1, z2)
print(f"Multiplicación: {z1} * {z2} = {resultado}")

# División
resultado = division(z1, z2)
print(f"División: {z1} / {z2} = {resultado}")

# Módulo
mod = modulo(z1)
print(f"Módulo de {z1}: {mod:.2f}")

# Conjugado
conj = conjugado(z1)
print(f"Conjugado de {z1}: {conj}")
```

## Cómo agregar una nueva herramienta

Para agregar una nueva herramienta al módulo de Matemáticas, sigue las instrucciones detalladas en la guía de [Cómo agregar un módulo](../como-agregar-modulo.md).

Los pasos principales son:
1. Crear el archivo de la herramienta en el directorio `src/ChuspaCalc/matematicas/`
2. Implementar las funciones necesarias siguiendo los estándares de código del proyecto
3. Documentar las funciones con docstrings en español
4. Agregar pruebas unitarias en el directorio correspondiente
5. Actualizar este archivo para incluir la nueva herramienta en la tabla de herramientas disponibles
6. Agregar ejemplos de uso en la sección de ejemplos

Asegúrate de revisar el archivo `docs/como-agregar-modulo.md` para obtener información detallada sobre los requisitos y convenciones del proyecto.
