# Guía Teórica del Módulo Eléctrica

Este documento presenta los fundamentos teóricos utilizados en el módulo eléctrica para el análisis de circuitos de corriente continua (DC). Es importante destacar que este módulo está diseñado exclusivamente para circuitos DC y no implementa funcionalidades para corriente alterna (CA).

## Alcance: Solo Circuitos DC

El módulo eléctrica de ChuspaCalc está limitado al análisis de circuitos de corriente continua (DC, por sus siglas en inglés: Direct Current). Esta restricción es intencional y se fundamenta en las siguientes razones:

**Diferencias fundamentales entre DC y CA:**
- **DC:** La corriente fluye en una sola dirección constante en el tiempo. El voltaje es constante (o variable lentamente). Los cálculos se realizan con valores instantáneos y no hay consideraciones de fase o frecuencia.
- **CA:** La corriente cambia periódicamente de dirección. El voltaje varía sinusoidalmente con el tiempo. Requiere análisis fasorial, consideraciones de impedancia (no solo resistencia), y cálculos de potencia compleja.

**Por qué el módulo NO implementa CA:**
1. **Complejidad matemática:** El análisis de CA requiere números complejos, fasores y transformaciones de Fourier, lo cual aumenta significativamente la complejidad del módulo.
2. **Elementos reactivos:** Los circuitos CA típicamente incluyen capacitores e inductores, cuyo comportamiento depende de la frecuencia. El módulo actual asume solo resistencias puras.
3. **Régimen transitorio:** La respuesta transitoria en circuitos CA con elementos reactivos requiere ecuaciones diferenciales, mientras que en DC con resistencias puras el análisis es algebraico.
4. **Enfoque educativo:** El módulo está diseñado como una introducción a los circuitos eléctricos, comenzando con el caso más simple de DC.

## Ley de Ohm

La Ley de Ohm es la relación fundamental que describe el comportamiento de los componentes resistivos en circuitos eléctricos. Establece una relación lineal entre voltaje, corriente y resistencia.

**Formulación matemática:**
$$ V = I \cdot R $$

Donde:
- $ V $ es el voltaje o diferencia de potencial, medido en voltios (V)
- $ I $ es la corriente eléctrica, medida en amperios (A)
- $ R $ es la resistencia eléctrica, medida en ohmios (Ω)

**Relación entre las variables:**
- **Voltaje:** Es la "presión" eléctrica que impulsa el flujo de electrones. Un mayor voltaje produce una mayor corriente para una resistencia dada.
- **Corriente:** Es el flujo de carga eléctrica a través del conductor. Es proporcional al voltaje e inversamente proporcional a la resistencia.
- **Resistencia:** Es la oposición al flujo de corriente. Una mayor resistencia reduce la corriente para un voltaje dado.

**Formas alternativas de la Ley de Ohm:**
$$ I = \frac{V}{R} $$
$$ R = \frac{V}{I} $$

La Ley de Ohm es válida para materiales óhmicos (conductores metálicos típicos) en condiciones normales de temperatura y presión. No se aplica a componentes no lineales como diodos o transistores.

## Potencia Eléctrica

La potencia eléctrica es la tasa a la cual se transfiere energía eléctrica en un circuito. En circuitos DC con resistencias puras, la potencia puede calcularse de tres formas equivalentes.

**Primera forma (definición básica):**
$$ P = V \cdot I $$

Esta es la definición fundamental de potencia eléctrica: el producto del voltaje entre dos puntos y la corriente que fluye entre ellos. Se deriva directamente de la definición de potencia como trabajo por unidad de tiempo.

**Segunda forma (usando la Ley de Ohm):**
$$ P = I^2 \cdot R $$

**Derivación:** Partiendo de $ P = V \cdot I $ y sustituyendo $ V = I \cdot R $ (Ley de Ohm):
$$ P = (I \cdot R) \cdot I = I^2 \cdot R $$

Esta forma es útil cuando se conoce la corriente y la resistencia, y muestra que la potencia disipada en una resistencia es proporcional al cuadrado de la corriente.

**Tercera forma (eliminando la corriente):**
$$ P = \frac{V^2}{R} $$

**Derivación:** Partiendo de $ P = V \cdot I $ y sustituyendo $ I = \frac{V}{R} $ (Ley de Ohm despejada):
$$ P = V \cdot \left(\frac{V}{R}\right) = \frac{V^2}{R} $$

Esta forma es útil cuando se conoce el voltaje y la resistencia, y muestra que la potencia es proporcional al cuadrado del voltaje e inversamente proporcional a la resistencia.

**Unidades:** La potencia se mide en vatios (W), donde 1 W = 1 V × 1 A.

## Circuitos en Serie

Un circuito en serie es aquel donde los componentes están conectados uno después del otro, de modo que la misma corriente fluye a través de todos ellos.

**Resistencia equivalente:**
$$ R_{eq} = R_1 + R_2 + R_3 + \dots + R_n $$

**Demostración:** En un circuito serie, la misma corriente $ I $ fluye a través de todas las resistencias. Aplicando la Ley de Ohm a cada resistencia:
$$ V_1 = I \cdot R_1 $$
$$ V_2 = I \cdot R_2 $$
$$ V_3 = I \cdot R_3 $$

El voltaje total es la suma de los voltajes individuales (Ley de Voltaje de Kirchhoff):
$$ V_{total} = V_1 + V_2 + V_3 = I \cdot R_1 + I \cdot R_2 + I \cdot R_3 = I \cdot (R_1 + R_2 + R_3) $$

La resistencia equivalente se define como $ R_{eq} = \frac{V_{total}}{I} $, por lo que:
$$ R_{eq} = R_1 + R_2 + R_3 $$

Generalizando para $ n $ resistencias:
$$ R_{eq} = \sum_{i=1}^{n} R_i $$

**Características importantes:**
- La corriente es la misma en todos los componentes
- El voltaje se divide entre los componentes
- La resistencia equivalente es mayor que cualquier resistencia individual
- Si un componente falla (circuito abierto), toda la corriente se interrumpe

## Circuitos en Paralelo

Un circuito en paralelo es aquel donde los componentes están conectados entre los mismos dos nodos, de modo que el voltaje es el mismo across todos ellos.

**Resistencia equivalente:**
$$ \frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots + \frac{1}{R_n} $$

**Demostración:** En un circuito paralelo, el mismo voltaje $ V $ se aplica across todas las resistencias. Aplicando la Ley de Ohm a cada resistencia:
$$ I_1 = \frac{V}{R_1} $$
$$ I_2 = \frac{V}{R_2} $$
$$ I_3 = \frac{V}{R_3} $$

La corriente total es la suma de las corrientes individuales (Ley de Corriente de Kirchhoff):
$$ I_{total} = I_1 + I_2 + I_3 = \frac{V}{R_1} + \frac{V}{R_2} + \frac{V}{R_3} = V \cdot \left(\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}\right) $$

La resistencia equivalente se define como $ R_{eq} = \frac{V}{I_{total}} $, por lo que:
$$ \frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} $$

Generalizando para $ n $ resistencias:
$$ \frac{1}{R_{eq}} = \sum_{i=1}^{n} \frac{1}{R_i} $$

**Para dos resistencias en paralelo (caso especial):**
$$ R_{eq} = \frac{R_1 \cdot R_2}{R_1 + R_2} $$

**Características importantes:**
- El voltaje es el mismo en todos los componentes
- La corriente se divide entre los componentes
- La resistencia equivalente es menor que cualquier resistencia individual
- Si un componente falla, los demás continúan funcionando

## Divisor de Tensión

El divisor de tensión es un circuito fundamental que permite obtener un voltaje menor a partir de un voltaje de entrada, utilizando dos resistencias en serie.

**Fórmula del divisor de tensión:**
$$ V_{out} = V_{in} \cdot \frac{R_2}{R_1 + R_2} $$

**Derivación:** Considerando dos resistencias $ R_1 $ y $ R_2 $ en serie con un voltaje de entrada $ V_{in} $:

La corriente que fluye por el circuito es:
$$ I = \frac{V_{in}}{R_1 + R_2} $$

El voltaje de salida se toma across $ R_2 $, por lo que:
$$ V_{out} = I \cdot R_2 = \frac{V_{in}}{R_1 + R_2} \cdot R_2 = V_{in} \cdot \frac{R_2}{R_1 + R_2} $$

**Aplicaciones prácticas:**

1. **Potenciómetros:** Un potenciómetro es esencialmente un divisor de tensión ajustable donde la relación $ \frac{R_2}{R_1 + R_2} $ puede variar de 0 a 1 mediante un control mecánico.

2. **Sensores resistivos:** Muchos sensores (como termistores, fotoresistores, sensores de fuerza) cambian su resistencia con la variable física que miden. Al usarlos como $ R_2 $ en un divisor de tensión, se convierte el cambio de resistencia en un cambio de voltaje que puede leer un microcontrolador.

3. **Referencias de voltaje:** Para crear voltajes de referencia estables a partir de una fuente de alimentación mayor.

4. **Atenuación de señales:** Para reducir la amplitud de señales analógicas sin distorsión significativa.

**Consideraciones de diseño:**
- El divisor de tensión no es ideal si la carga conectada a $ V_{out} $ tiene una resistencia comparable a $ R_2 $, ya que esto afectará la división.
- Para aplicaciones de precisión, se debe considerar el efecto de carga y posiblemente usar un seguidor de voltaje (amplificador operacional).

## Limitaciones Conocidas

El módulo eléctrica de ChuspaCalc tiene varias limitaciones importantes que los usuarios deben tener en cuenta:

**1. Solo resistencias puras:**
El módulo asume que todos los componentes son resistencias puras. No considera capacitores, inductores ni otros componentes reactivos. Esto significa que:
- No se pueden modelar circuitos con filtros RC, RL o RLC
- No hay análisis de respuesta en frecuencia
- No se consideran efectos de desfase entre voltaje y corriente

**2. Sin elementos reactivos:**
Los elementos reactivos (capacitores e inductores) tienen comportamiento que depende del tiempo y la frecuencia:
- **Capacitores:** Se oponen a cambios de voltaje, almacenan energía en campo eléctrico
- **Inductores:** Se oponen a cambios de corriente, almacenan energía en campo magnético
- Estos elementos requieren análisis con ecuaciones diferenciales y números complejos en CA

**3. Solo régimen permanente DC:**
El módulo calcula el estado estacionario del circuito, no la respuesta transitoria:
- No se modela cómo el circuito evoluciona desde el momento en que se conecta la fuente
- No se consideran tiempos de establecimiento
- No se analiza la respuesta a cambios súbitos en el circuito

**4. Sin consideraciones térmicas:**
Las resistencias cambian su valor con la temperatura. El módulo asume resistencias constantes:
- No se modela el auto-calentamiento de componentes
- No se consideran coeficientes de temperatura
- Los cálculos de potencia asumen disipación ideal

**5. Circuitos lineales solamente:**
El módulo no maneja componentes no lineales:
- No se pueden modelar diodos, transistores, LEDs
- No se consideran efectos de saturación
- No hay análisis de puntos de operación (Q-point)

**6. Sin análisis de redes complejas:**
El módulo está limitado a configuraciones básicas:
- No implementa análisis nodal o mallas completo
- No maneja transformadores
- No considera acoplamiento magnético entre componentes

**Recomendación:** Para aplicaciones que requieran alguna de estas funcionalidades, se recomienda utilizar software especializado en análisis de circuitos como SPICE, o extender el módulo con las capacidades necesarias.
