# Fundamentos matemáticos de los módulos de ingeniería

## 1. Propósito y alcance

Este documento describe las ecuaciones, magnitudes, unidades y supuestos de los módulos de cálculo de **vigas, circuitos eléctricos, figuras geométricas, conversores y subredes IP** de Escuadra.

La documentación se elaboró tomando como referencia la implementación disponible en `src/escuadra/modulos/`. Cuando una función no valida ni convierte explícitamente las unidades, se indica la convención de uso recomendada. El usuario debe introducir magnitudes compatibles entre sí: una fórmula numéricamente correcta puede producir un resultado incorrecto si se mezclan unidades.

## 2. Convenciones generales de unidades

Se recomienda utilizar el Sistema Internacional (SI) como sistema principal:

| Magnitud | Símbolo | Unidad SI |
|---|---:|---|
| Longitud | \(L, x, h, r\) | metro (m) |
| Área | \(A\) | metro cuadrado (m²) |
| Volumen | \(V\) | metro cúbico (m³) |
| Fuerza o carga puntual | \(P, F\) | newton (N) |
| Carga distribuida | \(w\) | newton por metro (N/m) |
| Momento flector | \(M\) | newton metro (N·m) |
| Módulo de elasticidad | \(E\) | pascal (Pa = N/m²) |
| Segundo momento de área | \(I\) | metro a la cuarta (m⁴) |
| Voltaje | \(V\) | voltio (V) |
| Corriente | \(I\) | amperio (A) |
| Resistencia | \(R\) | ohmio (Ω) |
| Potencia | \(P\) | vatio (W) |
| Energía | \(E\) | julio (J) |
| Presión | \(p\) | pascal (Pa) |
| Masa | \(m\) | kilogramo (kg) |
| Velocidad | \(v\) | metro por segundo (m/s) |
| Temperatura | \(T\) | kelvin (K) |

Algunas funciones civiles existentes devuelven resultados rotulados en kN o kN·m. En esos casos debe respetarse la convención específica indicada en cada apartado. No se debe interpretar automáticamente que todas las funciones convierten desde o hacia SI: varias reciben números sin metadatos de unidad.

---

## 3. Módulo de vigas

### 3.1. Modelo estructural considerado

Las funciones revisadas trabajan con una **viga recta, simplemente apoyada**, con apoyos en sus extremos y cargas estáticas. Los cálculos descritos corresponden a casos ideales de resistencia de materiales y estática; no constituyen por sí solos un diseño estructural completo.

### 3.2. Reacciones en los apoyos

Implementación de referencia: `civil/viga.py`, función `calcular_reacciones`.

Para una viga de longitud \(L\), con una carga puntual \(P\) aplicada a una distancia \(a\) desde el apoyo izquierdo:

\[
R_B = \frac{P a}{L}
\]

\[
R_A = P - R_B = \frac{P(L-a)}{L}
\]

Donde:

- \(R_A\): reacción vertical en el apoyo izquierdo.
- \(R_B\): reacción vertical en el apoyo derecho.
- \(P\): carga puntual total.
- \(L\): longitud entre apoyos.
- \(a\): distancia desde el apoyo izquierdo hasta la carga.

Si `posicion` no se proporciona, la función supone una carga distribuida uniforme y simétrica, y calcula:

\[
R_A = R_B = \frac{P}{2}
\]

**Unidades:** la función devuelve `unidad: "kN"`; por coherencia, `carga` debe expresarse como fuerza total en kN. `longitud` y `posicion` deben usar la misma unidad de longitud (preferentemente m). En el caso distribuido, `carga` representa la resultante total de la carga distribuida, no su intensidad por metro.

**Supuestos y límites:**

- La viga está simplemente apoyada y se encuentra en equilibrio estático.
- Solo se consideran cargas verticales.
- La carga puntual debe ubicarse entre los apoyos, incluidos sus extremos.
- La rama sin `posicion` representa una resultante uniformemente distribuida y simétrica.
- La función no calcula esfuerzos, deformaciones ni combinaciones de carga.

### 3.3. Momento flector máximo

Implementación de referencia: `civil/momento_flector.py`, función `calcular_momento_max`.

Para una carga puntual centrada:

\[
M_{\max} = \frac{P L}{4}
\]

Para una carga uniformemente distribuida a lo largo de toda la viga:

\[
M_{\max} = \frac{w L^2}{8}
\]

Donde:

- \(M_{\max}\): momento flector máximo, en el centro del vano.
- \(P\): carga puntual central.
- \(w\): intensidad de carga distribuida por unidad de longitud.
- \(L\): longitud de la viga.

**Unidades:** el resultado se identifica como kN·m. Para obtenerlo directamente, usar \(P\) en kN y \(L\) en m en el caso puntual; para el caso distribuido, usar \(w\) en kN/m y \(L\) en m.

**Supuestos y límites:**

- Viga simplemente apoyada.
- Carga puntual aplicada exactamente en el centro o carga uniforme sobre todo el vano.
- No se contemplan cargas excéntricas, momentos aplicados ni varios tipos de carga simultáneos.
- La posición informada del máximo es \(L/2\).

### 3.4. Deflexión máxima

Implementación de referencia: `civil/deflexion_viga.py`, función `calcular_deflexion_max`.

Para una carga puntual centrada:

\[
\delta_{\max} = \frac{P L^3}{48 E I}
\]

Para una carga uniformemente distribuida:

\[
\delta_{\max} = \frac{5 w L^4}{384 E I}
\]

Donde:

- \(\delta_{\max}\): deflexión máxima.
- \(P\): carga puntual central, en N.
- \(w\): intensidad de carga distribuida, en N/m.
- \(L\): longitud, en m.
- \(E\): módulo de elasticidad, en Pa.
- \(I\): segundo momento de área de la sección, en m⁴.

La función calcula la deflexión en unidades de metro a partir de entradas SI y multiplica el resultado por 1000 para devolver `deflexion_max` en **milímetros (mm)**. También informa la posición \(L/2\), expresada en metros.

**Supuestos y límites:**

- Viga simplemente apoyada, prismática y con comportamiento elástico lineal.
- Material homogéneo y módulo de elasticidad constante.
- Se supone teoría de pequeñas deformaciones y se desprecia la deformación por cortante.
- Los casos soportados son únicamente `puntual_central` y `distribuida`.
- La intensidad de carga distribuida debe introducirse en N/m, no como carga total.
- La función valida que los parámetros sean positivos, pero no puede detectar si se introdujeron unidades incompatibles.

### 3.5. Carga distribuida parcial

Implementación de referencia: `civil/carga_distribuida.py`, función `calcular_reacciones_carga_parcial`.

Para una carga uniforme de intensidad \(w\), aplicada desde \(x_i\) hasta \(x_f\):

\[
\ell_c = x_f - x_i
\]

\[
F_R = w \ell_c
\]

\[
x_R = \frac{x_i+x_f}{2}
\]

\[
R_B = \frac{F_R x_R}{L}
\qquad
R_A = F_R - R_B
\]

Donde \(F_R\) es la resultante equivalente y \(x_R\) su posición medida desde el apoyo izquierdo.

**Unidades recomendadas:** \(w\) en N/m, longitudes en m y reacciones en N. La función no añade una etiqueta de unidad ni realiza conversiones.

**Supuestos y límites:** carga uniforme en un único tramo, viga simplemente apoyada y equilibrio estático. Se requiere \(0 \leq x_i < x_f \leq L\).

---

## 4. Módulo de circuitos eléctricos

### 4.1. Ley de Ohm

Implementación de referencia: `electrica/ley_ohm.py`, función `calcular_ohm`.

\[
V = I R
\]

Despejes implementados:

\[
I = \frac{V}{R}
\qquad
R = \frac{V}{I}
\]

Donde:

- \(V\): diferencia de potencial o voltaje, en V.
- \(I\): corriente eléctrica, en A.
- \(R\): resistencia, en Ω.

La función requiere exactamente dos de los tres parámetros para calcular el tercero. No admite resistencia igual a cero y, al calcular resistencia, tampoco admite corriente igual a cero.

**Supuestos y límites:** modelo de elemento óhmico con resistencia constante. La relación se aplica directamente a magnitudes eléctricas compatibles; no modela por sí sola componentes no lineales ni transitorios.

### 4.2. Resistencias en serie

Implementación de referencia: `electrica/circuito_serie_paralelo.py`, función `resistencia_serie`.

\[
R_{eq} = R_1 + R_2 + \cdots + R_n
\]

La corriente es la misma a través de todos los elementos conectados en serie y las caídas de tensión se suman.

**Unidades:** todas las resistencias en Ω; el resultado \(R_{eq}\) queda en Ω.

### 4.3. Resistencias en paralelo

Implementación de referencia: `electrica/circuito_serie_paralelo.py`, función `resistencia_paralelo`.

\[
\frac{1}{R_{eq}} =
\frac{1}{R_1}+\frac{1}{R_2}+\cdots+\frac{1}{R_n}
\]

Para dos resistencias:

\[
R_{eq} = \frac{R_1 R_2}{R_1+R_2}
\]

**Unidades:** resistencias de entrada y resultado en Ω. Se requieren al menos dos resistencias y todas deben ser positivas.

**Supuestos y límites de serie/paralelo:** los componentes deben estar conectados realmente en la topología indicada; las funciones no analizan redes arbitrarias ni incluyen resistencias internas o tolerancias.

### 4.4. Divisor resistivo de tensión

Implementación de referencia: `electrica/divisor_tension.py`.

Para dos resistencias en serie, con salida tomada sobre \(R_2\):

\[
V_{out}=V_{in}\frac{R_2}{R_1+R_2}
\]

Para calcular \(R_2\) a partir de una tensión de salida deseada:

\[
R_2=\frac{V_{out}R_1}{V_{in}-V_{out}}
\]

Donde \(V_{in}\) y \(V_{out}\) se expresan en V, y \(R_1\) y \(R_2\) en Ω.

**Supuestos y límites:** divisor ideal sin carga conectada a la salida. Si se conecta una carga, esta queda en paralelo con \(R_2\) y modifica la tensión de salida; el modelo implementado no contempla ese efecto.

### 4.5. Potencia eléctrica

Implementación de referencia: `electrica/potencia.py`.

Se implementan tres expresiones equivalentes para un elemento resistivo:

\[
P=VI
\]

\[
P=I^2R
\]

\[
P=\frac{V^2}{R}
\]

Donde \(P\) se obtiene en W cuando \(V\) está en V, \(I\) en A y \(R\) en Ω.

**Supuestos y límites:** las expresiones se aplican a condiciones resistivas y valores compatibles. En corriente alterna, el cálculo de potencia activa requiere considerar valores eficaces y factor de potencia; estas funciones no calculan explícitamente ese factor.

---

## 5. Módulo de figuras geométricas

Las funciones geométricas operan con dimensiones lineales. Si las dimensiones se ingresan en metros, las áreas se obtienen en m² y los volúmenes en m³. Si se utiliza otra unidad lineal, el resultado queda expresado en la unidad correspondiente elevada al cuadrado o al cubo.

### 5.1. Áreas planas

Implementación de referencia: `geometria/calculo_area.py`.

**Triángulo:**

\[
A=\frac{b h}{2}
\]

\(b\): base; \(h\): altura perpendicular a la base.

**Círculo:**

\[
A=\pi r^2
\]

\(r\): radio. La implementación utiliza la aproximación \(\pi \approx 3.1416\).

**Rectángulo:**

\[
A=b h
\]

\(b\): base; \(h\): altura.

**Unidades:** entradas en m y salidas en m² si se emplea SI.

**Supuestos y límites:** figuras planas ideales. La función de área de círculo usa una aproximación decimal de π, por lo que puede diferir ligeramente de un cálculo con precisión completa. Las funciones de área simples no incorporan validaciones de dimensiones positivas en el propio archivo revisado; se recomienda ingresar medidas mayores que cero.

### 5.2. Perímetros

Implementación de referencia: `geometria/perimetro.py`.

**Círculo:**

\[
P=2\pi r
\]

**Cuadrado:**

\[
P=4l
\]

**Rectángulo:**

\[
P=2(a+b)
\]

**Triángulo:**

\[
P=a+b+c
\]

La función verifica la desigualdad triangular:

\[
a+b>c,\quad a+c>b,\quad b+c>a
\]

**Hexágono regular:**

\[
P=6l
\]

Donde \(r\) es el radio, \(l\) el lado y \(a,b,c\) las longitudes de los lados o dimensiones correspondientes.

**Unidades:** entradas y resultado en la misma unidad lineal; con SI, metros (m).

**Supuestos y límites:** el hexágono considerado es regular; el perímetro del triángulo requiere lados que formen un triángulo válido. Las funciones del archivo validan dimensiones positivas.

### 5.3. Volúmenes

Implementación de referencia: `geometria/volumen.py`.

**Cubo:**

\[
V=l^3
\]

**Esfera:**

\[
V=\frac{4}{3}\pi r^3
\]

**Cilindro:**

\[
V=\pi r^2 h
\]

**Cono:**

\[
V=\frac{1}{3}\pi r^2 h
\]

**Paralelepípedo rectangular:**

\[
V=a b c
\]

Donde \(l\) es el lado, \(r\) el radio, \(h\) la altura y \(a,b,c\) las dimensiones ortogonales.

**Unidades:** dimensiones en m y volumen en m³.

**Supuestos y límites:** sólidos geométricos ideales; cilindro y cono circulares rectos, esfera perfecta y paralelepípedo definido por tres dimensiones perpendiculares. Las dimensiones deben ser positivas.

### 5.4. Áreas de secciones

Implementación de referencia: `civil/area_seccion.py`.

También se calculan áreas de secciones transversales:

- Rectangular: \(A=bh\).
- Circular maciza: \(A=\pi r^2\).
- Circular hueca: \(A=\pi(r_e^2-r_i^2)\).
- Perfil I simplificado: \(A=2b_f t_f+h_w t_w\).
- Perfil T simplificado: \(A=b_f t_f+h_w t_w\).

Las dimensiones deben expresarse en la misma unidad lineal. Con dimensiones en metros, el área queda en m². Para la sección circular hueca se exige \(r_i<r_e\).

**Limitación:** las expresiones de perfiles I y T representan la suma de rectángulos definida por los parámetros del código; no sustituyen la consulta de dimensiones normalizadas ni consideran radios de acuerdo, chaflanes u otras particularidades de perfiles comerciales.

---

## 6. Módulo de conversores

### 6.1. Principio general

Los conversores multiplican el valor de entrada por un factor para llevarlo a una unidad de referencia y luego dividen por el factor de la unidad destino:

\[
x_{base}=x_{origen}\,f_{origen}
\]

\[
x_{destino}=\frac{x_{base}}{f_{destino}}
\]

Los factores se encuentran definidos en los respectivos módulos. El conversor no realiza mediciones físicas: transforma valores numéricos entre unidades conocidas.

### 6.2. Longitud

Implementación de referencia: `matematicas/conversor_longitud.py` y `conversor_longitud_extendido.py`.

Unidad base: metro (m).

| Unidad | Equivalencia en metros |
|---|---:|
| m | 1 |
| cm | 0.01 |
| mm | 0.001 |
| km | 1000 |
| in (pulgada) | 0.0254 |
| ft (pie) | 0.3048 |
| ua (unidad astronómica) | \(1.496 \times 10^{11}\) |
| al (año luz) | \(9.461 \times 10^{15}\) |
| mn (milla náutica) | 1852 |
| pc (parsec) | \(3.086 \times 10^{16}\) |

La conversión sigue \(x_m=x f\) y \(x_d=x_m/f_d\). El valor se devuelve en la unidad destino seleccionada.

### 6.3. Masa

Implementación de referencia: `matematicas/conversor_masa.py`.

Unidad base: kilogramo (kg).

| Unidad | Equivalencia en kg |
|---|---:|
| kg | 1 |
| g | 0.001 |
| mg | 0.000001 |
| lb (libra) | 0.453592 |
| oz (onza) | 0.0283495 |
| t (tonelada métrica) | 1000 |
| slug | 14.5939 |

La conversión se realiza primero a kg y luego a la unidad de destino.

### 6.4. Temperatura

Implementación de referencia: `matematicas/conversor_temperatura.py`.

Las escalas Celsius, Fahrenheit y Kelvin requieren transformaciones afines, no solo factores multiplicativos:

\[
F=C\frac{9}{5}+32
\]

\[
C=(F-32)\frac{5}{9}
\]

\[
K=C+273.15
\]

\[
C=K-273.15
\]

Las temperaturas se expresan en °C, °F y K, respectivamente. El código rechaza valores por debajo del cero absoluto: −273.15 °C, −459.67 °F o 0 K.

### 6.5. Energía

Implementación de referencia: `matematicas/conversor_energia.py`.

Unidad base: julio (J).

| Unidad | Equivalencia en J |
|---|---:|
| J | 1 |
| kJ | 1000 |
| MJ | 1 000 000 |
| Wh | 3600 |
| kWh | 3 600 000 |
| cal | 4.184 |
| kcal | 4184 |
| BTU | 1055.06 |
| eV | \(1.602176634 \times 10^{-19}\) |

### 6.6. Presión

Implementación de referencia: `matematicas/conversor_presion.py`.

Unidad base: pascal (Pa).

| Unidad | Equivalencia en Pa |
|---|---:|
| Pa | 1 |
| kPa | 1000 |
| MPa | 1 000 000 |
| bar | 100 000 |
| atm | 101 325 |
| psi | 6894.76 |
| mmHg | 133.322 |

### 6.7. Velocidad

Implementación de referencia: `matematicas/conversor_velocidad.py`.

Unidad base: metro por segundo (m/s).

| Unidad | Equivalencia en m/s |
|---|---:|
| m/s | 1 |
| km/h | \(1/3.6\) |
| mph | 0.44704 |
| nudos | 0.514444 |
| ft/s | 0.3048 |

### 6.8. Ángulos

Implementación de referencia: `matematicas/conversor_angulo.py`.

Las unidades soportadas son grados, radianes y gradianes:

\[
180^\circ=\pi\ \text{rad}=200\ \text{grad}
\]

Por tanto:

\[
\text{radianes}=\text{grados}\frac{\pi}{180}
\]

\[
\text{gradianes}=\text{grados}\frac{10}{9}
\]

El radián es la unidad coherente del SI para ángulos planos; grados y gradianes se admiten como unidades alternativas.

### 6.9. Validaciones y limitaciones de los conversores

- Los conversores de longitud, masa, energía, presión y velocidad revisados rechazan valores negativos.
- El conversor de temperatura valida el límite del cero absoluto.
- Las unidades deben coincidir exactamente con las claves aceptadas por cada función; algunas funciones normalizan espacios y mayúsculas/minúsculas y otras no.
- Los factores almacenados son constantes numéricas; algunos están redondeados, por lo que puede haber pequeñas diferencias frente a tablas de mayor precisión.
- La conversión no verifica si una unidad es apropiada para una aplicación física concreta.
- Los conversores de magnitudes escalares no deben confundirse con conversiones de magnitudes vectoriales.

---

## 7. Módulo de subredes IP

### 7.1. Direccionamiento IPv4 y prefijo CIDR

Implementación de referencia: `sistemas/calculadora_subred.py`, función `calcular_subred`.

El módulo utiliza la biblioteca estándar `ipaddress` de Python para interpretar direcciones IPv4 y prefijos CIDR.

Una dirección IPv4 tiene 32 bits. Un prefijo `/p` indica cuántos bits iniciales corresponden a la parte de red. El número de bits de host es:

\[
h=32-p
\]

La máscara de subred contiene \(p\) bits en 1 seguidos por \(32-p\) bits en 0.

Ejemplo conceptual: `/24` equivale a 24 bits de red y 8 bits de host, con máscara `255.255.255.0`.

### 7.2. Dirección de red y broadcast

La dirección de red se obtiene aplicando una operación AND bit a bit entre la dirección IP y la máscara:

\[
\text{Red}=\text{IP}\ \text{AND}\ \text{Máscara}
\]

La dirección de broadcast se obtiene colocando en 1 todos los bits de host de la dirección de red. Para una subred IPv4 convencional:

\[
\text{Broadcast}=\text{Red}\ \text{OR}\ \text{Wildcard}
\]

donde la wildcard es el complemento de la máscara.

La implementación devuelve:

- `red`: dirección de red.
- `broadcast`: dirección de difusión.
- `mascara`: máscara IPv4.
- `primer_host`: primera dirección que la biblioteca considera utilizable.
- `ultimo_host`: última dirección que la biblioteca considera utilizable.
- `total_hosts`: cantidad de direcciones devueltas por `red.hosts()`.

### 7.3. Cantidad de hosts

Para subredes IPv4 tradicionales con prefijos entre `/0` y `/30`, la cantidad habitual de hosts utilizables es:

\[
N=2^{32-p}-2
\]

La resta excluye la dirección de red y la dirección de broadcast. Sin embargo, esta regla no se aplica de la misma manera a los prefijos `/31` y `/32`: la biblioteca `ipaddress` aplica el tratamiento especial definido para esos casos. Por esa razón, el programa obtiene la cantidad mediante `len(red.hosts())` en lugar de aplicar manualmente la fórmula anterior.

### 7.4. Entradas, salidas y validaciones

- **Entrada `ip`:** dirección IPv4 en notación decimal punteada, por ejemplo `192.168.1.10`.
- **Entrada `prefijo_cidr`:** entero entre 0 y 32, escrito como texto o convertible a entero.
- **Salidas:** direcciones IPv4 y máscara en texto; `total_hosts` como entero sin unidad física.

La función acepta direcciones con bits de host activos y utiliza `strict=False`; por ello, normaliza la dirección ingresada a la dirección de red correspondiente al prefijo. Rechaza direcciones o prefijos con formato inválido.

**Supuestos y límites:**

- El cálculo está limitado a IPv4 (32 bits); no implementa IPv6.
- No comprueba disponibilidad real de direcciones en una red ni detecta conflictos.
- No considera VLAN, rutas, DHCP, reglas de firewall ni topología física.
- La validez de una dirección como host depende del prefijo; los casos `/31` y `/32` tienen tratamiento particular.
- El módulo calcula información de direccionamiento, no configura dispositivos de red.

---

## 8. Consideraciones generales y límites de uso

1. **Unidades coherentes:** antes de calcular, convertir todas las entradas a un sistema compatible. Por ejemplo, no combinar longitud en milímetros con módulo de elasticidad en Pa e inercia en m⁴ sin conversión.
2. **Precisión numérica:** los cálculos utilizan números de punto flotante. Los resultados pueden contener pequeñas diferencias de redondeo.
3. **Validación de entradas:** las validaciones varían entre módulos. Que una función acepte un número no garantiza que la magnitud tenga una unidad correcta o sea físicamente razonable.
4. **Modelos ideales:** las fórmulas de vigas, circuitos y geometría representan modelos simplificados. Para decisiones de ingeniería reales deben contrastarse con normas aplicables, condiciones de operación, propiedades verificadas y revisión profesional.
5. **Alcance de la documentación:** se describen las operaciones identificadas en los archivos fuente citados; no se afirma que el programa implemente análisis más avanzados que los indicados.