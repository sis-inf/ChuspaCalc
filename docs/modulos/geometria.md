# Módulo de Geometría

## Descripción

El módulo de geometría proporciona funciones para calcular áreas, perímetros y volúmenes de diferentes figuras geométricas. Además, incluye una herramienta interactiva para el cálculo de áreas de figuras planas.

---

## Figuras planas soportadas

### Área

| Figura     | Función                         | Fórmula                 |
| ---------- | ------------------------------- | ----------------------- |
| Triángulo  | `area_triangulo(base, altura)`  | A = (base × altura) / 2 |
| Círculo    | `area_circulo(radio)`           | A = π × r²              |
| Rectángulo | `area_rectangulo(base, altura)` | A = base × altura       |

### Perímetro

| Figura           | Función                              | Fórmula                 |
| ---------------- | ------------------------------------ | ----------------------- |
| Círculo          | `perimetro_circulo(radio)`           | P = 2 × π × r           |
| Cuadrado         | `perimetro_cuadrado(lado)`           | P = 4 × lado            |
| Rectángulo       | `perimetro_rectangulo(largo, ancho)` | P = 2 × (largo + ancho) |
| Triángulo        | `perimetro_triangulo(a, b, c)`       | P = a + b + c           |
| Hexágono regular | `perimetro_hexagono_regular(lado)`   | P = 6 × lado            |

---

## Sólidos geométricos soportados

| Sólido         | Función                                      | Fórmula                  |
| -------------- | -------------------------------------------- | ------------------------ |
| Cubo           | `volumen_cubo(lado)`                         | V = lado³                |
| Esfera         | `volumen_esfera(radio)`                      | V = (4/3) × π × r³       |
| Cilindro       | `volumen_cilindro(radio, altura)`            | V = π × r² × h           |
| Cono           | `volumen_cono(radio, altura)`                | V = (π × r² × h) / 3     |
| Paralelepípedo | `volumen_paralelepipedo(largo, ancho, alto)` | V = largo × ancho × alto |

---

## Resolución de triángulos

La herramienta **Resolución de triángulos** calcula los elementos faltantes de un triángulo usando la ley de cosenos y la ley de senos. Los ángulos se expresan en grados.

| Caso conocido         | Función                                                 | Resultado               |
| --------------------- | ------------------------------------------------------- | ----------------------- |
| Los tres lados        | `resolver_triangulo_lados(a, b, c)`                     | Ángulos A, B y C        |
| Un lado y dos ángulos | `resolver_triangulo_lado_angulo(a, angulo_a, angulo_b)` | Lados b y c, y ángulo C |

Las funciones lanzan `ValueError` si los datos no forman un triángulo válido (lados no positivos, desigualdad triangular incumplida o ángulos que suman 180° o más).

---

## Ejemplos de uso

### Cálculo de áreas

```python
from ChuspaCalc.modulos.geometria.calculo_area import (
    area_triangulo,
    area_circulo,
    area_rectangulo,
)

print(area_triangulo(10, 5))
print(area_circulo(3))
print(area_rectangulo(8, 4))
```

### Cálculo de perímetros

```python
from ChuspaCalc.modulos.geometria.perimetro import (
    perimetro_circulo,
    perimetro_cuadrado,
)

print(perimetro_circulo(5))
print(perimetro_cuadrado(4))
```

### Cálculo de volúmenes

```python
from ChuspaCalc.modulos.geometria.volumen import (
    volumen_cubo,
    volumen_esfera,
)

print(volumen_cubo(3))
print(volumen_esfera(2))
```

### Resolución de triángulos

```python
from ChuspaCalc.modulos.geometria.resolucion_triangulos import (
    resolver_triangulo_lados,
    resolver_triangulo_lado_angulo,
)

# Tres lados conocidos: devuelve los ángulos A, B y C
print(resolver_triangulo_lados(3, 4, 5))
# (36.87..., 53.13..., 90.0)

# Un lado y dos ángulos: devuelve los lados b y c, y el ángulo C
print(resolver_triangulo_lado_angulo(10, 30, 60))
# (17.32..., 20.00..., 90)
```
