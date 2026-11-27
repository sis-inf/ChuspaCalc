# Catálogo de herramientas de la suite ChuspaCalc

Este documento describe las herramientas actualmente disponibles en la suite ChuspaCalc.

Las herramientas listadas corresponden a clases que implementan la interfaz base
`Herramienta` y que son descubiertas correctamente por el sistema de registro
(`ChuspaCalc.core.registry`).

## Herramientas disponibles

| Herramienta                       | Módulo                               | Descripción                                                                           |
| --------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------- |
| Calculadora científica            | Matemáticas                          | Calculadora con operaciones aritméticas, trigonométricas, logarítmicas y constantes.  |
| Conversión de unidades            | Matemáticas                          | Convierte valores entre unidades de longitud, masa, tiempo y temperatura.             |
| Matemática financiera             | Matemáticas                          | Calcula valor futuro, valor presente e interés compuesto.                             |
| Sistemas de ecuaciones lineales   | Matemáticas                          | Resuelve sistemas A·x = b para tamaños entre 2x2 y 5x5.                               |
| Resolución de triángulos          | Matemáticas                          | Calcula triángulos usando ley de senos y cosenos.                                     |
| Conversión de unidades eléctricas | Ingeniería Eléctrica                 | Convierte entre unidades de potencia (W, kW, HP) y unidades de energía (Wh, kWh, J).  |
| Divisor de tensión                | Ingeniería Eléctrica                 | Calcula el voltaje de salida o las resistencias necesarias en un divisor de tensión.  |
| Ley de Ohm                        | Ingeniería Eléctrica                 | Calcula voltaje, corriente o resistencia a partir de las otras dos magnitudes.        |
| Potencia Trifásica                | Ingeniería Eléctrica                 | Calcula la potencia activa, reactiva y aparente en sistemas trifásicos.               |
| Complemento a 2                   | Ingeniería de Sistemas e Informática | Convierte entre decimal con signo y representación en complemento a 2.                |
| Conversión de bases               | Ingeniería de Sistemas e Informática | Convierte un número entre decimal, binario, octal y hexadecimal.                      |
| Mapas de Karnaugh                 | Ingeniería de Sistemas e Informática | Genera mapas de Karnaugh y realiza simplificaciones básicas de expresiones booleanas. |
| Tablas de verdad                  | Ingeniería de Sistemas e Informática | Genera la tabla de verdad de una expresión booleana con hasta 4 variables.            |

---

# Organización por módulo

## Matemáticas

### Calculadora científica

Permite evaluar expresiones matemáticas utilizando:

- Operaciones aritméticas básicas.
- Potencias y raíces.
- Funciones trigonométricas.
- Logaritmos y logaritmos naturales.
- Constantes matemáticas.

---

### Conversión de unidades

Permite realizar conversiones entre diferentes categorías:

- Longitud.
- Masa.
- Tiempo.
- Temperatura.

---

### Matemática financiera

Permite realizar cálculos financieros relacionados con:

- Valor futuro.
- Valor presente.
- Interés compuesto.

---

### Sistemas de ecuaciones lineales

Resuelve sistemas de ecuaciones lineales mediante métodos matriciales.

Características:

- Soporte para sistemas desde 2x2 hasta 5x5.
- Resolución del sistema A·x = b.
- Manejo de matrices numéricas.

---

### Resolución de triángulos

Permite calcular elementos desconocidos de un triángulo utilizando:

- Ley de senos.
- Ley de cosenos.

---

# Ingeniería Eléctrica

## Ley de Ohm

Calcula magnitudes eléctricas a partir de valores conocidos:

- Voltaje.
- Corriente.
- Resistencia.

---

## Divisor de tensión

Permite calcular:

- Voltaje de salida.
- Resistencias necesarias en un divisor resistivo.

Utiliza la relación entre resistencias y tensión de entrada.

---

## Conversión de unidades eléctricas

Realiza conversiones entre unidades de:

### Potencia

- W.
- kW.
- HP.

### Energía

- J.
- Wh.
- kWh.

---

## Potencia Trifásica

Permite calcular parámetros de sistemas trifásicos:

- Potencia activa.
- Potencia reactiva.
- Potencia aparente.

---

# Ingeniería de Sistemas e Informática

## Complemento a 2

Permite realizar conversiones entre:

- Decimal con signo.
- Representación binaria en complemento a 2.

Soporta diferentes tamaños de palabra.

---

## Conversión de bases

Permite convertir números entre diferentes sistemas:

- Decimal.
- Binario.
- Octal.
- Hexadecimal.

---

## Mapas de Karnaugh

Permite generar y simplificar expresiones booleanas mediante mapas de Karnaugh.

Incluye soporte para simplificación de expresiones lógicas.

---

## Tablas de verdad

Genera tablas de verdad para expresiones booleanas.

Características:

- Soporte de hasta cuatro variables.
- Operadores lógicos básicos.
- Generación de resultados tabulados.
