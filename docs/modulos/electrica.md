# Módulo Eléctrico

## Descripción

Este módulo proporciona herramientas fundamentales para el análisis y cálculo de circuitos eléctricos en corriente continua (DC). Está diseñado para ingenieros, estudiantes y técnicos que necesitan realizar cálculos rápidos y precisos en el diseño y análisis de sistemas eléctricos. El módulo cubre desde los conceptos básicos como la Ley de Ohm hasta análisis más complejos de circuitos serie y paralelo, cálculo de potencia eléctrica, caída de tensión en conductores y divisores de tensión. Estas herramientas son esenciales para el diseño de circuitos electrónicos, sistemas de alimentación, instalaciones eléctricas residenciales e industriales, y cualquier aplicación que requiera análisis de circuitos eléctricos.

## Ley de Ohm

La Ley de Ohm es uno de los principios fundamentales de la electricidad y establece la relación entre voltaje, corriente y resistencia en un circuito eléctrico. Fue formulada por el físico alemán Georg Simon Ohm en 1827 y se expresa matemáticamente como:

**V = I · R**

Donde:
- **V** es el voltaje o diferencia de potencial, medido en voltios (V)
- **I** es la corriente eléctrica, medido en amperios (A)
- **R** es la resistencia eléctrica, medido en ohmios (Ω)

Esta ley indica que la corriente que fluye a través de un conductor es directamente proporcional al voltaje aplicado e inversamente proporcional a la resistencia del conductor. Es decir, si aumentamos el voltaje, la corriente aumentará proporcionalmente, y si aumentamos la resistencia, la corriente disminuirá proporcionalmente.

El triángulo de Ohm es una herramienta mnemotécnica útil para recordar las tres formas de la ley:

```
    V
   /|\
  / | \
 /  |  \
I---R--- 
```

- Para calcular V: cubre V → V = I · R
- Para calcular I: cubre I → I = V / R
- Para calcular R: cubre R → R = V / I

**Ejemplos de uso:**
- Si tenemos una resistencia de 100 Ω con una corriente de 0.5 A, el voltaje es: V = 0.5 A · 100 Ω = 50 V
- Si aplicamos 12 V a una resistencia de 24 Ω, la corriente es: I = 12 V / 24 Ω = 0.5 A
- Si circula una corriente de 2 A a través de un componente con 10 V, la resistencia es: R = 10 V / 2 A = 5 Ω

## Análisis de circuitos DC

El análisis de circuitos en corriente continua (DC) se basa en entender cómo se comportan los componentes cuando están conectados en diferentes configuraciones. Las dos configuraciones fundamentales son los circuitos en serie y en paralelo, cada una con características distintivas que afectan el voltaje, la corriente y la resistencia total del circuito.

### Circuitos en serie

En un circuito en serie, los componentes están conectados uno después del otro, formando un único camino para la corriente eléctrica. Las características principales son:

- **La corriente es la misma en todos los componentes:** La corriente que sale de la fuente es la misma que fluye a través de cada componente. Esto se debe a que no hay puntos donde la corriente pueda dividirse.
  - I_total = I₁ = I₂ = I₃ = ...

- **El voltaje total se divide entre los componentes:** La suma de los voltajes individuales es igual al voltaje de la fuente.
  - V_total = V₁ + V₂ + V₃ + ...

- **Resistencia total:** La resistencia total es la suma de todas las resistencias individuales.
  - R_total = R₁ + R₂ + R₃ + ...

- **Si un componente falla (se abre), todo el circuito se interrumpe:** Esto es una desventaja importante en aplicaciones críticas.

**Ejemplo:** Tres resistencias de 10 Ω, 20 Ω y 30 Ω conectadas en serie tienen una resistencia total de 60 Ω. Si se aplican 12 V, la corriente es I = 12 V / 60 Ω = 0.2 A, y esta misma corriente fluye a través de cada resistencia.

### Circuitos en paralelo

En un circuito en paralelo, los componentes están conectados entre los mismos dos puntos, creando múltiples caminos para la corriente eléctrica. Las características principales son:

- **El voltaje es el mismo en todos los componentes:** Cada componente tiene el mismo voltaje que la fuente.
  - V_total = V₁ = V₂ = V₃ = ...

- **La corriente total se divide entre las ramas:** La suma de las corrientes individuales es igual a la corriente total de la fuente.
  - I_total = I₁ + I₂ + I₃ + ...

- **Resistencia total:** La resistencia total se calcula mediante la recíproca de la suma de las recíprocas.
  - 1/R_total = 1/R₁ + 1/R₂ + 1/R₃ + ...
  - Para dos resistencias: R_total = (R₁ · R₂) / (R₁ + R₂)

- **Si una rama falla, las otras continúan funcionando:** Esto es una ventaja importante en aplicaciones que requieren redundancia.

- **La resistencia total es siempre menor que la menor resistencia individual:** Agregar más ramas en paralelo siempre reduce la resistencia total.

**Ejemplo:** Dos resistencias de 10 Ω y 20 Ω en paralelo tienen una resistencia total de R_total = (10 · 20) / (10 + 20) = 200/30 = 6.67 Ω. Si se aplican 12 V, la corriente total es I = 12 V / 6.67 Ω = 1.8 A, que se divide entre las dos ramas.

## Potencia eléctrica

La potencia eléctrica es la tasa a la que se transfiere energía eléctrica en un circuito. Se mide en vatios (W) y se puede calcular de tres formas diferentes, dependiendo de qué variables se conocen:

**1. Potencia en función de voltaje y corriente:**
P = V · I

Esta es la forma más básica y se usa cuando conocemos el voltaje aplicado y la corriente que circula. Es útil para calcular la potencia consumida por cualquier dispositivo eléctrico.

**2. Potencia en función de corriente y resistencia:**
P = I² · R

Esta forma se deriva de sustituir V = I · R en la primera ecuación. Es útil cuando conocemos la corriente y la resistencia, pero no el voltaje directamente. Muestra que la potencia disipada como calor en una resistencia es proporcional al cuadrado de la corriente.

**3. Potencia en función de voltaje y resistencia:**
P = V² / R

Esta forma se deriva de sustituir I = V / R en la primera ecuación. Es útil cuando conocemos el voltaje y la resistencia, pero no la corriente directamente. Muestra que para un voltaje fijo, menor resistencia significa mayor potencia.

**Relación entre las tres formas:**
Las tres ecuaciones son equivalentes y se pueden derivar unas de otras usando la Ley de Ohm. La elección de cuál usar depende de qué variables son conocidas o más fáciles de medir en una situación específica.

**Ejemplos:**
- Una resistencia de 100 Ω con 0.5 A: P = (0.5)² · 100 = 25 W
- Un componente con 12 V y 2 A: P = 12 · 2 = 24 W
- Una carga de 50 Ω con 10 V: P = 10² / 50 = 2 W

## Herramientas disponibles

| Herramienta | Fórmulas usadas | Parámetros de entrada |
|-------------|----------------|----------------------|
| `ley_ohm` | V = I · R, I = V / R, R = V / I | Dos de: voltaje, corriente, resistencia |
| `potencia` | P = V · I, P = I² · R, P = V² / R | Dos de: voltaje, corriente, resistencia |
| `circuito_serie` | R_total = R₁ + R₂ + ..., V_total = V₁ + V₂ + ..., I_total = I₁ = I₂ = ... | Lista de resistencias, voltaje de fuente |
| `circuito_paralelo` | 1/R_total = 1/R₁ + 1/R₂ + ..., V_total = V₁ = V₂ = ..., I_total = I₁ + I₂ + ... | Lista de resistencias, voltaje de fuente |
| `caida_tension` | V_caida = I · R_conductor | Corriente, resistencia del conductor |
| `divisor_tension` | V_salida = V_entrada · (R₂ / (R₁ + R₂)) | Voltaje de entrada, resistencias R₁ y R₂ |

## Potencia trifásica

La potencia trifásica es la que entrega un sistema de **tres corrientes alternas** desfasadas 120° entre sí. Es el sistema más usado en instalaciones industriales y comerciales por su mayor eficiencia y capacidad de transmisión.

| Característica | Monofásica | Trifásica |
|----------------|------------|-----------|
| Número de fases | 1 | 3 |
| Aplicación típica | Residencial | Industrial / comercial |
| Potencia | Menor | Mayor |
| Eficiencia | Menor | Mayor |

**Fórmulas (con valores de línea, iguales para estrella y triángulo):**

- Potencia activa: **P = √3 · V_L · I_L · cos(φ)** (W)
- Potencia reactiva: **Q = √3 · V_L · I_L · sen(φ)** (VAR)
- Potencia aparente: **S = √3 · V_L · I_L** (VA)

Donde **V_L** es el voltaje de línea (V), **I_L** la corriente de línea (A) y **cos(φ)** el factor de potencia (entre 0 y 1).

**Estrella (Y) vs triángulo (Δ):**

| Característica | Estrella (Y) | Triángulo (Δ) |
|----------------|--------------|---------------|
| Voltaje de fase | V_f = V_L / √3 | V_f = V_L |
| Corriente de fase | I_f = I_L | I_f = I_L / √3 |
| Potencia activa | P = √3 · V_L · I_L · cos(φ) | P = √3 · V_L · I_L · cos(φ) |
| Ventaja | Menor voltaje por fase | Menor corriente por fase |

**Ejemplos:**

- Estrella, V_L = 400 V, I_L = 10 A, cos(φ) = 0.85: P = 1.732 · 400 · 10 · 0.85 ≈ 5889 W ≈ 5.89 kW
- Triángulo, V_L = 220 V, I_L = 15 A, cos(φ) = 0.90: P = 1.732 · 220 · 15 · 0.90 ≈ 5144 W ≈ 5.14 kW

**Uso desde código:**

```python
from chuspacalc.modulos.electrica.potencia_trifasica import calcular_potencia_trifasica

calcular_potencia_trifasica(400, 10, 0.85, conexion="estrella")
# {"potencia_activa": 5888.97..., "potencia_reactiva": 3649.66..., "potencia_aparente": 6928.20...}
```

`conexion` acepta `"estrella"` (por defecto) o `"triangulo"`. Se lanza `ValueError` si el voltaje o la corriente no son mayores que 0 y finitos, o si el factor de potencia no está entre 0 y 1.

**Solución de problemas:**

| Problema | Solución |
|----------|----------|
| El resultado no coincide | Verificar que el factor de potencia esté entre 0 y 1 |
| Error en el cálculo | Verificar que se usen valores de **línea** (no de fase) de voltaje y corriente |

**Referencias:**

- [Sistema trifásico](https://es.wikipedia.org/wiki/Sistema_trif%C3%A1sico)
- [Conexión estrella-triángulo](https://es.wikipedia.org/wiki/Diagrama_estrella-tri%C3%A1ngulo)

## Unidades y conversiones

En el análisis de circuitos eléctricos es fundamental comprender las unidades básicas y sus prefijos para realizar cálculos correctos y evitar errores de magnitud.

**Unidades básicas del SI:**
- **Voltio (V):** Unidad de diferencia de potencial o fuerza electromotriz. Un voltio es la diferencia de potencial que, aplicada a una resistencia de un ohmio, produce una corriente de un amperio.
- **Amperio (A):** Unidad de corriente eléctrica. Un amperio es la corriente que, fluyendo a través de dos conductores paralelos de longitud infinita, separados por un metro en el vacío, produce una fuerza de 2×10⁻⁷ newtons por metro de longitud.
- **Ohmio (Ω):** Unidad de resistencia eléctrica. Un ohmio es la resistencia que, al aplicarle un voltio, permite el paso de un amperio de corriente.
- **Vatio (W):** Unidad de potencia eléctrica. Un vatio es la potencia que corresponde a una energía de un julio por segundo.

**Prefijos del SI más comunes en electricidad:**
- **mili (m):** 10⁻³ = 0.001
  - 1 mV = 0.001 V
  - 1 mA = 0.001 A
  - 1 mΩ = 0.001 Ω
  - 1 mW = 0.001 W

- **kilo (k):** 10³ = 1,000
  - 1 kV = 1,000 V
  - 1 kA = 1,000 A
  - 1 kΩ = 1,000 Ω
  - 1 kW = 1,000 W

- **mega (M):** 10⁶ = 1,000,000
  - 1 MV = 1,000,000 V
  - 1 MA = 1,000,000 A
  - 1 MΩ = 1,000,000 Ω
  - 1 MW = 1,000,000 W

**Conversiones útiles:**
- Para convertir a unidades base: multiplicar por el factor del prefijo
  - 5 kΩ = 5 × 1,000 = 5,000 Ω
  - 250 mA = 250 × 0.001 = 0.25 A

- Para convertir a prefijos: dividir por el factor del prefijo
  - 4,700 Ω = 4,700 / 1,000 = 4.7 kΩ
  - 0.015 A = 0.015 / 0.001 = 15 mA

**Importancia de las unidades:** Es crucial mantener la consistencia de unidades en todos los cálculos. Por ejemplo, al usar la Ley de Ohm, si la resistencia está en kilo-ohmios, el resultado de la corriente estará en miliamperios si el voltaje está en voltios. Siempre es recomendable convertir todas las cantidades a unidades base (V, A, Ω, W) antes de realizar cálculos complejos.

## Ejemplo práctico completo

**Enunciado:** Diseñe un circuito que alimente tres LEDs desde una fuente de 12 V DC. Cada LED requiere aproximadamente 2 V y 20 mA para operar correctamente. Se debe incluir una resistencia limitadora de corriente para cada LED. Calcule el valor de las resistencias, la corriente total del circuito, la potencia total consumida y la caída de tensión en el conductor principal si tiene una resistencia de 0.1 Ω.

**Datos:**
- Voltaje de la fuente (V_fuente): 12 V
- Voltaje de cada LED (V_LED): 2 V
- Corriente de cada LED (I_LED): 20 mA = 0.02 A
- Resistencia del conductor principal (R_conductor): 0.1 Ω
- Número de LEDs: 3

**Desarrollo:**

1. **Configuración del circuito:**
   Dado que los LEDs tienen el mismo voltaje y corriente requerida, los conectaremos en paralelo para que cada uno reciba el voltaje completo de la fuente (menos la caída en el conductor). Cada LED tendrá su propia resistencia limitadora en serie.

2. **Cálculo de la resistencia limitadora para cada LED:**
   Usamos la Ley de Ohm: R = V / I
   - Voltaje que debe caer en la resistencia: V_R = V_fuente - V_LED = 12 V - 2 V = 10 V
   - Corriente deseada: I = 20 mA = 0.02 A
   - R_limitadora = V_R / I = 10 V / 0.02 A = 500 Ω

   Cada LED requiere una resistencia de 500 Ω en serie.

3. **Cálculo de la corriente total del circuito:**
   En configuración paralelo, la corriente total es la suma de las corrientes de cada rama:
   - I_total = 3 × I_LED = 3 × 0.02 A = 0.06 A = 60 mA

4. **Cálculo de la potencia consumida por cada LED y su resistencia:**
   - Potencia del LED: P_LED = V_LED × I_LED = 2 V × 0.02 A = 0.04 W = 40 mW
   - Potencia de la resistencia: P_R = V_R × I = 10 V × 0.02 A = 0.2 W = 200 mW
   - Potencia total por rama: P_rama = P_LED + P_R = 0.04 W + 0.2 W = 0.24 W

5. **Cálculo de la potencia total del circuito:**
   - P_total = 3 × P_rama = 3 × 0.24 W = 0.72 W

   Alternativamente, usando la fuente: P_total = V_fuente × I_total = 12 V × 0.06 A = 0.72 W

6. **Cálculo de la caída de tensión en el conductor principal:**
   - V_caida = I_total × R_conductor = 0.06 A × 0.1 Ω = 0.006 V = 6 mV

   Esta caída es despreciable en este caso, pero en circuitos de mayor corriente podría ser significativa.

7. **Verificación del voltaje real en los LEDs:**
   - Voltaje disponible en los LEDs: V_LED_real = V_fuente - V_caida = 12 V - 0.006 V = 11.994 V
   - La diferencia es mínima, por lo que el diseño es adecuado.

**Resultado esperado:**
- Resistencia limitadora por LED: 500 Ω
- Corriente total del circuito: 60 mA
- Potencia total consumida: 0.72 W
- Caída de tensión en el conductor: 6 mV (despreciable)

**Código Python:**
```python
# Ejemplo práctico completo: Circuito con tres LEDs
import numpy as np

# Datos de entrada
V_fuente = 12.0  # Voltaje de la fuente en V
V_LED = 2.0  # Voltaje de cada LED en V
I_LED = 0.02  # Corriente de cada LED en A (20 mA)
R_conductor = 0.1  # Resistencia del conductor principal en Ω
n_LEDs = 3  # Número de LEDs

# 1. Cálculo de la resistencia limitadora para cada LED
V_R = V_fuente - V_LED  # Voltaje que debe caer en la resistencia
R_limitadora = V_R / I_LED  # Resistencia en Ω

# 2. Cálculo de la corriente total del circuito
I_total = n_LEDs * I_LED  # Corriente total en A

# 3. Cálculo de la potencia consumida por cada LED y su resistencia
P_LED = V_LED * I_LED  # Potencia del LED en W
P_R = V_R * I_LED  # Potencia de la resistencia en W
P_rama = P_LED + P_R  # Potencia total por rama en W

# 4. Cálculo de la potencia total del circuito
P_total = n_LEDs * P_rama  # Potencia total en W

# Verificación usando la fuente
P_total_verif = V_fuente * I_total  # Potencia total verificada en W

# 5. Cálculo de la caída de tensión en el conductor principal
V_caida = I_total * R_conductor  # Caída de tensión en V

# 6. Verificación del voltaje real en los LEDs
V_LED_real = V_fuente - V_caida  # Voltaje real en los LEDs en V

# Resultados
print(f"=== Resultados del Ejemplo Práctico ===")
print(f"\n1. Resistencia limitadora por LED:")
print(f"   R_limitadora = {R_limitadora:.2f} Ω")
print(f"   Valor comercial más cercano: {round(R_limitadora/100)*100} Ω")

print(f"\n2. Corriente total del circuito:")
print(f"   I_total = {I_total*1000:.2f} mA")

print(f"\n3. Potencia por rama:")
print(f"   P_LED = {P_LED*1000:.2f} mW")
print(f"   P_R = {P_R*1000:.2f} mW")
print(f"   P_rama = {P_rama*1000:.2f} mW")

print(f"\n4. Potencia total del circuito:")
print(f"   P_total = {P_total:.3f} W")
print(f"   P_total (verificación) = {P_total_verif:.3f} W")

print(f"\n5. Caída de tensión en el conductor principal:")
print(f"   V_caida = {V_caida*1000:.3f} mV")

print(f"\n6. Voltaje real en los LEDs:")
print(f"   V_LED_real = {V_LED_real:.4f} V")
print(f"   Diferencia con el diseño: {abs(V_LED_real - V_fuente)*1000:.3f} mV")

print(f"\n=== Resumen del diseño ===")
print(f"Se requieren {n_LEDs} resistencias de {R_limitadora:.0f} Ω")
print(f"Potencia total de la fuente: {P_total:.3f} W")
print(f"Corriente total: {I_total*1000:.2f} mA")
print(f"El diseño es adecuado (caída de tensión despreciable)")
```
