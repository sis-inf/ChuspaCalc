# Ejemplos de Uso — Suite ChuspaCalc

Este documento presenta ejemplos concretos de entrada y salida para las principales herramientas de ChuspaCalc.

---

## Módulo Civil

### Ejemplo 1: Reacciones en viga con carga distribuida

**Problema planteado:**
Una viga simplemente apoyada de 10 metros soporta una carga total distribuida de 100 kN. Se desea conocer las reacciones en los apoyos.

**Código Python:**

```python
from chuspacalc.modulos.civil.viga import calcular_reacciones

resultado = calcular_reacciones(longitud=10, carga=100)
print(resultado)
```

**Salida esperada:**

```
{'Ra': 50.0, 'Rb': 50.0, 'unidad': 'kN'}
```

---

### Ejemplo 2: Reacciones en viga con carga puntual y momento flector

**Problema planteado:**
Una viga de 6 metros tiene una carga puntual de 10 kN aplicada en el centro. Se desea conocer las reacciones y el momento flector máximo.

**Código Python:**

```python
from chuspacalc.modulos.civil.viga import calcular_reacciones
from chuspacalc.modulos.civil.momento_flector import calcular_momento_max

reacciones = calcular_reacciones(longitud=6, carga=10, posicion=3)
momento = calcular_momento_max(longitud=6, carga=10, tipo_carga='puntual_central')
print(reacciones)
print(momento)
```

**Salida esperada:**

```
{'Ra': 5.0, 'Rb': 5.0, 'unidad': 'kN'}
{'momento_max': 15.0, 'posicion': 3.0, 'unidad': 'kN·m'}
```

---

## Módulo Eléctrica

### Ejemplo 1: Ley de Ohm

**Problema planteado:**
Un circuito tiene una resistencia de 5 Ω y circula una corriente de 2 A. Se desea conocer el voltaje y la potencia disipada.

**Código Python:**

```python
from chuspacalc.modulos.electrica.herramienta_ley_ohm import calcular_voltaje, calcular_potencia

voltaje = calcular_voltaje(corriente=2, resistencia=5)
potencia = calcular_potencia(voltaje=voltaje, corriente=2)
print(f"Voltaje: {voltaje} V")
print(f"Potencia: {potencia} W")
```

**Salida esperada:**

```
Voltaje: 10 V
Potencia: 20 W
```

---

### Ejemplo 2: Caída de tensión en conductor

**Problema planteado:**
Un conductor de cobre de 100 metros y sección de 4 mm² conduce una corriente de 15 A. Se desea verificar si la caída de tensión es admisible.

**Código Python:**

```python
from chuspacalc.modulos.electrica.caida_tension import calcular_caida

resultado = calcular_caida(longitud=100, corriente=15, seccion=4)
print(resultado)
```

**Salida esperada:**

```
{'caida_v': 12.9, 'porcentaje': 5.8636, 'admisible': False}
```

---

## Módulo Matemáticas

### Ejemplo 1: Conversión de longitud

**Problema planteado:**
Un ingeniero necesita convertir 3 pies a metros para unificar datos de un informe técnico.

**Código Python:**

```python
from chuspacalc.modulos.matematicas.conversor_longitud import convertir

resultado = convertir(valor=3, de_unidad='ft', a_unidad='m')
print(resultado)
```

**Salida esperada:**

```
{'valor_original': 3, 'unidad_original': 'ft', 'valor_convertido': 0.9144, 'unidad_destino': 'm'}
```

---

### Ejemplo 2: Estadísticas de mediciones de laboratorio

**Problema planteado:**
Un estudiante realizó 5 mediciones de resistencia eléctrica: 47, 52, 49, 51, 48 Ω. Se desea calcular la media y la desviación estándar.

**Código Python:**

```python
from chuspacalc.modulos.matematicas.estadisticas import calcular

resultado = calcular([47, 52, 49, 51, 48])
print(f"Media: {resultado['media']} Ω")
print(f"Desviación estándar: {resultado['desviacion_estandar']:.2f} Ω")
```

**Salida esperada:**

```
Media: 49.4 Ω
Desviación estándar: 1.96 Ω
```

---

## Módulo Sistemas

### Ejemplo 1: Conversión de bases numéricas

**Problema planteado:**
Un estudiante necesita convertir el número decimal 255 a binario, octal y hexadecimal.

**Código Python:**

```python
from chuspacalc.modulos.sistemas.conversor_bases import convertir

print(convertir('255', 10, 2))
print(convertir('255', 10, 8))
print(convertir('255', 10, 16))
```

**Salida esperada:**

```
{'numero_original': '255', 'base_origen': 10, 'resultado': '11111111', 'base_destino': 2}
{'numero_original': '255', 'base_origen': 10, 'resultado': '377', 'base_destino': 8}
{'numero_original': '255', 'base_origen': 10, 'resultado': 'FF', 'base_destino': 16}
```

---

### Ejemplo 2: Sistemas de ecuaciones lineales

**Problema planteado:**
Resolver el sistema: 2x + y = 4, x + 3y = 5.

**Código Python:**

```python
from chuspacalc.modulos.matematicas.herramienta_sistemas_lineales import resolver_sistema

solucion = resolver_sistema([[2, 1], [1, 3]], [4, 5])
print(f"x1 = {solucion[0]}, x2 = {solucion[1]}")
```

**Salida esperada:**

```
x1 = 1.4, x2 = 1.2
```

---

## Módulo Geometría

### Ejemplo 1: Área de un triángulo

**Problema planteado:**
Calcular el área de un triángulo con base de 10 m y altura de 5 m.

**Código Python:**

```python
from chuspacalc.modulos.geometria.calculo_area import area_triangulo

resultado = area_triangulo(base=10, altura=5)
print(f"Área: {resultado} m²")
```

**Salida esperada:**

```
Área: 25.0 m²
```

---

### Ejemplo 2: Área de un círculo

**Problema planteado:**
Calcular el área de una sección circular de tubería con radio de 0.5 m.

**Código Python:**

```python
from chuspacalc.modulos.geometria.calculo_area import area_circulo

resultado = area_circulo(radio=0.5)
print(f"Área: {resultado:.4f} m²")
```

**Salida esperada:**

```
Área: 0.7854 m²
```

