# Módulo de Sistemas e Informática

## Descripción

El módulo `sistemas` agrupa las herramientas orientadas a informática y computación. Sus herramientas son especialmente útiles en cursos de **arquitectura de computadoras**, **lógica digital** y **programación de sistemas**, ya que cubren los fundamentos numéricos y lógicos sobre los que se construye el software y el hardware.

El módulo contiene las siguientes herramientas principales:

- `conversor_bases` — conversión entre sistemas de numeración (binario, octal, decimal, hexadecimal)
- `herramienta_tablas_verdad` — generación de tablas de verdad para expresiones booleanas
- `tabla_ascii` — consulta y conversión de caracteres y códigos ASCII
- `conversor_color` — conversión de colores entre los modelos RGB, HEX y HSL
- `calculadora_subred` — cálculo de red, broadcast, máscara y rango de hosts de una subred IPv4/CIDR

---

## Herramientas de sistemas de numeración

### `conversor_bases`

Convierte números entre las bases 2, 8, 10 y 16. Acepta el número de entrada en cualquiera de las cuatro bases y entrega el resultado en la base de destino.

**Bases soportadas:**

| Base | Nombre      | Dígitos válidos        |
|------|-------------|------------------------|
| 2    | Binario     | `0`, `1`               |
| 8    | Octal       | `0` – `7`              |
| 10   | Decimal     | `0` – `9`              |
| 16   | Hexadecimal | `0` – `9`, `A` – `F`  |

**Ejemplos de conversión:**

| Número original | Base origen | Resultado | Base destino |
|-----------------|-------------|-----------|--------------|
| `255`           | 10          | `FF`      | 16           |
| `255`           | 10          | `11111111`| 2            |
| `255`           | 10          | `377`     | 8            |
| `FF`            | 16          | `255`     | 10           |
| `11111111`      | 2           | `FF`      | 16           |
| `1A3`           | 16          | `419`     | 10           |
| `644`           | 8           | `420`     | 10           |

**Uso desde código:**

```python
from ChuspaCalc.modulos.sistemas.conversor_bases import convertir

# Decimal a hexadecimal
resultado = convertir("255", base_origen=10, base_destino=16)
# {"numero_original": "255", "base_origen": 10, "resultado": "FF", "base_destino": 16}

# Hexadecimal a binario
resultado = convertir("FF", base_origen=16, base_destino=2)
# {"numero_original": "FF", "base_origen": 16, "resultado": "11111111", "base_destino": 2}

# Binario a octal
resultado = convertir("11111111", base_origen=2, base_destino=8)
# {"numero_original": "11111111", "base_origen": 2, "resultado": "377", "base_destino": 8}
```

---

## Herramientas de lógica digital

### `herramienta_tablas_verdad`

Genera la tabla de verdad completa de cualquier expresión booleana con hasta **4 variables** (A–Z en mayúsculas). Evalúa todas las combinaciones posibles de valores de entrada (0 y 1) y muestra el resultado de la expresión para cada una.

**Operadores soportados:**

| Operación | Notaciones aceptadas         |
|-----------|------------------------------|
| AND       | `AND`, `&`, `*`, `∧`        |
| OR        | `OR`, `\|`, `+`, `∨`        |
| NOT       | `NOT`, `!`, `~`, `¬`        |
| XOR       | `XOR`, `^`                  |

**Ejemplos de tablas de verdad:**

Expresión `A AND B`:

| A | B | Resultado |
|---|---|-----------|
| 0 | 0 | 0         |
| 0 | 1 | 0         |
| 1 | 0 | 0         |
| 1 | 1 | 1         |

Expresión `A OR B`:

| A | B | Resultado |
|---|---|-----------|
| 0 | 0 | 0         |
| 0 | 1 | 1         |
| 1 | 0 | 1         |
| 1 | 1 | 1         |

Expresión `NOT A`:

| A | Resultado |
|---|-----------|
| 0 | 1         |
| 1 | 0         |

Expresión `A XOR B`:

| A | B | Resultado |
|---|---|-----------|
| 0 | 0 | 0         |
| 0 | 1 | 1         |
| 1 | 0 | 1         |
| 1 | 1 | 0         |

Expresión `A AND (B OR C)` (3 variables):

| A | B | C | Resultado |
|---|---|---|-----------|
| 0 | 0 | 0 | 0         |
| 0 | 0 | 1 | 0         |
| 0 | 1 | 0 | 0         |
| 0 | 1 | 1 | 0         |
| 1 | 0 | 0 | 0         |
| 1 | 0 | 1 | 1         |
| 1 | 1 | 0 | 1         |
| 1 | 1 | 1 | 1         |

**Ejemplos de expresiones válidas:**

```
A AND B
A OR (NOT B)
(A AND B) OR (NOT A AND C)
A XOR B XOR C
NOT (A AND B)
A & B | ~C
```

---

## Herramientas de código ASCII

### `tabla_ascii`

Permite consultar y convertir caracteres ASCII (rango 0–127) entre sus distintas representaciones: carácter, decimal, hexadecimal, octal y binario.

**Funciones disponibles:**

- `caracter_a_ascii(char)` — recibe un carácter y devuelve todas sus representaciones
- `ascii_a_caracter(codigo)` — recibe un código decimal y devuelve el carácter y sus representaciones
- `listar_ascii_rango(inicio, fin)` — retorna una lista de entradas para un rango de códigos

**Ejemplos:**

```python
from ChuspaCalc.modulos.sistemas.tabla_ascii import caracter_a_ascii, ascii_a_caracter, listar_ascii_rango

# Carácter a código
caracter_a_ascii("A")
# {"caracter": "A", "decimal": 65, "hexadecimal": "0x41", "octal": "0o101", "binario": "0b1000001"}

caracter_a_ascii("a")
# {"caracter": "a", "decimal": 97, "hexadecimal": "0x61", "octal": "0o141", "binario": "0b1100001"}

caracter_a_ascii(" ")
# {"caracter": " ", "decimal": 32, "hexadecimal": "0x20", "octal": "0o40", "binario": "0b100000"}

# Código a carácter
ascii_a_caracter(65)
# {"caracter": "A", "decimal": 65, "hexadecimal": "0x41", "octal": "0o101", "binario": "0b1000001"}

# Rango de caracteres (letras mayúsculas)
listar_ascii_rango(65, 90)
# Lista con las 26 entradas de A (65) a Z (90)
```

**Rangos ASCII de referencia:**

| Rango decimal | Contenido                    |
|---------------|------------------------------|
| 0 – 31        | Caracteres de control        |
| 32 – 47       | Espacios y signos de puntuación |
| 48 – 57       | Dígitos `0` – `9`           |
| 65 – 90       | Letras mayúsculas `A` – `Z` |
| 97 – 122      | Letras minúsculas `a` – `z` |

---

## Conversión de colores

### `conversor_color`

Convierte colores entre los modelos RGB, HEX y HSL. Útil para comprender cómo se representan los colores en sistemas digitales y en desarrollo web.

**Funciones disponibles:**

- `rgb_a_hex(r, g, b)` — convierte RGB (0–255) a cadena hexadecimal `#RRGGBB`
- `hex_a_rgb(hex_str)` — convierte `#RRGGBB` (o `RRGGBB`) a tupla `(r, g, b)`
- `rgb_a_hsl(r, g, b)` — convierte RGB a tupla HSL `(h, s, l)` donde H ∈ [0, 360] y S, L ∈ [0, 100]

**Ejemplos:**

```python
from ChuspaCalc.modulos.sistemas.conversor_color import rgb_a_hex, hex_a_rgb, rgb_a_hsl

# RGB a HEX
rgb_a_hex(255, 0, 0)      # "#FF0000"  — rojo puro
rgb_a_hex(0, 255, 0)      # "#00FF00"  — verde puro
rgb_a_hex(0, 0, 255)      # "#0000FF"  — azul puro
rgb_a_hex(255, 255, 255)  # "#FFFFFF"  — blanco
rgb_a_hex(0, 0, 0)        # "#000000"  — negro

# HEX a RGB
hex_a_rgb("#FF0000")      # (255, 0, 0)
hex_a_rgb("1A2B3C")       # (26, 43, 60)

# RGB a HSL
rgb_a_hsl(255, 0, 0)      # (0, 100, 50)   — rojo: matiz 0°, saturación 100%, luminosidad 50%
rgb_a_hsl(0, 128, 0)      # (120, 100, 25) — verde oscuro
rgb_a_hsl(128, 128, 128)  # (0, 0, 50)     — gris neutro
```

---

## Redes

### `calculadora_subred`

Calcula la **dirección de red**, la **dirección de broadcast**, la **máscara de subred**, el **rango de hosts** y el **número total de hosts** de una dirección IPv4 con su prefijo CIDR (1 a 32).

**Fórmulas utilizadas:**

```
Red       = IP AND Máscara
Broadcast = IP OR (NOT Máscara)
Hosts     = Red + 1  →  Broadcast - 1
Total     = 2^(32 - prefijo) - 2
```

Para los prefijos `/31` y `/32` no hay hosts asignables: `primer_host` y `ultimo_host` valen `"N/A"` y `total_hosts` es `0`.

**Ejemplos:**

| IP / CIDR        | Máscara         | Red           | Primer host   | Último host     | Broadcast       | Hosts  |
|------------------|-----------------|---------------|---------------|-----------------|-----------------|--------|
| `192.168.1.0/24` | `255.255.255.0` | `192.168.1.0` | `192.168.1.1` | `192.168.1.254` | `192.168.1.255` | 254    |
| `10.0.0.0/16`    | `255.255.0.0`   | `10.0.0.0`    | `10.0.0.1`    | `10.0.255.254`  | `10.0.255.255`  | 65 534 |

Desarrollo del primer ejemplo (`192.168.1.0/24`):

```
Máscara   = 255.255.255.0   (wildcard: 0.0.0.255)
Red       = 192.168.1.0 AND 255.255.255.0 = 192.168.1.0
Broadcast = 192.168.1.0 OR  0.0.0.255     = 192.168.1.255
Hosts     = 192.168.1.1 → 192.168.1.254
Total     = 2^(32 - 24) - 2 = 254
```

**Uso desde código:**

```python
from escuadra.modulos.sistemas.calculadora_subred import calcular_subred

calcular_subred("192.168.1.0", "24")
# {"red": "192.168.1.0", "broadcast": "192.168.1.255", "mascara": "255.255.255.0",
#  "primer_host": "192.168.1.1", "ultimo_host": "192.168.1.254", "total_hosts": 254}
```

Si la IP no tiene cuatro octetos entre 0 y 255, o el prefijo no es un entero entre 1 y 32, se lanza `ErrorCIDR` (subclase de `ValueError`).

**Solución de problemas:**

| Problema | Solución |
|----------|----------|
| El resultado no coincide | Verificar que el prefijo CIDR sea el correcto (ej. `/24` = `255.255.255.0`) |
| Error en el cálculo | Verificar que la IP tenga cuatro octetos numéricos y que el prefijo sea un entero |

**Referencias:**

- [Subred](https://es.wikipedia.org/wiki/Subred)
- [Notación CIDR](https://es.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
- [Dirección IP](https://es.wikipedia.org/wiki/Direcci%C3%B3n_IP)

---

## Ejemplos de casos de uso en programación de sistemas

### Depuración a nivel de bits

Al trabajar con registros de hardware o protocolos de comunicación, los valores suelen expresarse en hexadecimal o binario. Con `conversor_bases` es posible inspeccionar el valor de un registro en todas las bases simultáneamente:

```python
# Un registro de estado devuelve 0xA3; ¿qué bits están activos?
convertir("A3", base_origen=16, base_destino=2)
# resultado: "10100011"
# → bits 7, 5, 1 y 0 están en 1
```

### Análisis de permisos en sistemas de archivos

Los permisos Unix se expresan en octal. Con `conversor_bases` se puede convertir un permiso a binario para ver exactamente qué bits están activos:

```python
convertir("755", base_origen=8, base_destino=2)
# resultado: "111101101"
# rwxr-xr-x → propietario: 111, grupo: 101, otros: 101
```

### Verificación de compuertas lógicas

Para verificar el comportamiento de una compuerta NAND (NOT AND) se puede expresar como `NOT (A AND B)` en la herramienta de tablas de verdad:

```
Expresión: NOT (A AND B)

| A | B | Resultado |
|---|---|-----------|
| 0 | 0 | 1         |
| 0 | 1 | 1         |
| 1 | 0 | 1         |
| 1 | 1 | 0         |
```

### Localización de caracteres en memoria

En programación de bajo nivel, los caracteres se almacenan como enteros. Con `tabla_ascii` se puede verificar el valor numérico de cualquier carácter y su representación en distintas bases:

```python
caracter_a_ascii("Z")
# decimal: 90, hexadecimal: 0x5A, binario: 0b1011010

# Diferencia entre mayúscula y minúscula en binario:
caracter_a_ascii("A")  # decimal: 65  → 0b1000001
caracter_a_ascii("a")  # decimal: 97  → 0b1100001
# El bit 5 (valor 32) distingue mayúsculas de minúsculas en ASCII
```

### Colores en desarrollo de interfaces

Al diseñar interfaces de bajo nivel o para sistemas embebidos con pantallas de color, la conversión entre modelos es frecuente:

```python
# El diseño especifica un color como HSL; el hardware necesita RGB y HEX
hex_a_rgb("#1E90FF")   # (30, 144, 255) — dodger blue
rgb_a_hsl(30, 144, 255)  # (210, 100, 56) — matiz azul, saturación plena
```