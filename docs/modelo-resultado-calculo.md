# Modelo ResultadoCalculo — Contrato de retorno para módulos de cálculo

## Introducción

Este documento define el contrato formal `ResultadoCalculo` que los módulos
de cálculo de ChuspaCalc deben seguir al retornar sus resultados, y describe
la transición gradual desde el estado actual hacia este contrato uniforme.

---

## Estado actual: diccionarios ad-hoc

Actualmente los módulos de cálculo retornan diccionarios con campos
específicos de cada dominio, sin una estructura común entre ellos.

### Ejemplo 1: `civil/viga.py`

```python
def calcular_reacciones(longitud, carga, posicion=None) -> dict:
    ...
    return {
        "Ra": round(Ra, 4),
        "Rb": round(Rb, 4),
        "unidad": "kN"
    }
```

### Ejemplo 2: `electrica/caida_tension.py`

```python
def calcular_caida(longitud, corriente, seccion, material="cobre") -> dict:
    ...
    return {
        "caida_v": round(caida_v, 4),
        "porcentaje": round(porcentaje, 4),
        "admisible": admisible,
    }
```

Cada módulo define sus propios nombres de campo según el dominio. Esto
funciona pero dificulta:

* Mostrar resultados de forma genérica en la UI.
* Comparar o serializar resultados de distintos módulos de manera uniforme.
* Detectar errores o casos de "no aplicable" de forma consistente.

---

## Contrato propuesto: `ResultadoCalculo`

Para resolver esto, se propone un contrato uniforme que envuelva el
resultado específico del dominio dentro de una estructura común.

### Campos

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `valores` | `dict` | Diccionario con los campos específicos del cálculo (lo que hoy retornan los módulos, ej. `Ra`, `Rb`, `caida_v`). |
| `unidad` | `str \| None` | Unidad principal del resultado, si aplica (ej. `"kN"`, `"V"`). |
| `valido` | `bool` | Indica si el resultado es válido/admisible según las reglas del dominio. |
| `mensaje` | `str \| None` | Mensaje descriptivo opcional (advertencias, aclaraciones). |
| `metadatos` | `dict` | Información adicional: nombre del módulo, parámetros usados, etc. |

### Ejemplo de uso (forma propuesta)

```python
from ChuspaCalc.core.resultado import ResultadoCalculo

def calcular_reacciones(longitud, carga, posicion=None) -> ResultadoCalculo:
    ...
    return ResultadoCalculo(
        valores={"Ra": round(Ra, 4), "Rb": round(Rb, 4)},
        unidad="kN",
        valido=True,
        mensaje=None,
        metadatos={"modulo": "civil.viga", "longitud": longitud, "carga": carga}
    )
```

```python
def calcular_caida(longitud, corriente, seccion, material="cobre") -> ResultadoCalculo:
    ...
    return ResultadoCalculo(
        valores={"caida_v": round(caida_v, 4), "porcentaje": round(porcentaje, 4)},
        unidad="V",
        valido=admisible,
        mensaje="Caída de tensión fuera del rango admisible" if not admisible else None,
        metadatos={"modulo": "electrica.caida_tension", "material": material}
    )
```

---

## Transición gradual

La migración hacia `ResultadoCalculo` no requiere reescribir todos los
módulos de golpe. Se sugiere el siguiente enfoque incremental:

1. **Fase 1 — Convivencia:** los módulos nuevos adoptan `ResultadoCalculo`
   desde el inicio; los módulos existentes (`viga.py`, `caida_tension.py`,
   etc.) continúan retornando sus diccionarios ad-hoc sin cambios.
2. **Fase 2 — Adaptador:** se crea una función auxiliar que envuelve el
   diccionario ad-hoc de un módulo viejo en un `ResultadoCalculo`, sin
   modificar el módulo original. Esto permite que la UI consuma ambos
   tipos de forma uniforme.
3. **Fase 3 — Migración del módulo:** cuando se toca un módulo viejo por
   otro motivo (bugfix, nueva feature), se aprovecha para migrar su
   `return` directamente a `ResultadoCalculo`.
4. **Fase 4 — Deprecación del formato viejo:** una vez que todos los
   módulos estén migrados, se puede exigir `ResultadoCalculo` como
   tipo de retorno obligatorio para nuevos módulos vía revisión de PR.

> **Nota:** Al momento de escribir este documento, el contrato
> `ResultadoCalculo` aún no está implementado en el código del proyecto
> (no existe en `src/ChuspaCalc/core/`). Este documento describe la
> propuesta de diseño para guiar su futura implementación y la
> migración de los módulos existentes.

---

## Referencias

* `docs/como-agregar-modulo.md` — guía general para agregar nuevos módulos.
* `src/ChuspaCalc/modulos/civil/viga.py` — ejemplo de módulo con diccionario ad-hoc.
* `src/ChuspaCalc/modulos/electrica/caida_tension.py` — ejemplo de módulo con diccionario ad-hoc.