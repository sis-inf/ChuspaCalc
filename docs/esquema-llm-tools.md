# Esquema JSON para integración con asistentes de IA (Function Calling)

## Introducción

Este documento describe el esquema JSON propuesto para exponer las
herramientas de ChuspaCalc a asistentes de IA mediante function calling,
permitiendo que un LLM invoque directamente las funciones de cálculo
del proyecto a partir de su descripción estructurada.

> **Nota:** Al momento de escribir este documento, este esquema **no
> está implementado** en el código del proyecto. Las herramientas
> actuales (clases que heredan de `Herramienta`) solo exponen
> `nombre`, `carrera`, `descripcion` y `crear_widget()`, pensados para
> la interfaz gráfica, no para function calling. Este documento
> describe la propuesta de diseño para una futura implementación.

---

## Formato estándar de function calling

Los asistentes de IA (OpenAI, Anthropic, etc.) usan un formato común
basado en JSON Schema para describir funciones invocables:

```json
{
  "name": "nombre_de_la_funcion",
  "description": "Qué hace la función",
  "parameters": {
    "type": "object",
    "properties": {
      "parametro1": {
        "type": "number",
        "description": "Descripción del parámetro"
      }
    },
    "required": ["parametro1"]
  }
}
```

---

## Ejemplo: esquema generado para `HerramientaCalculoArea`

Tomando como referencia la herramienta real
`src/escuadra/modulos/geometria/herramienta_calculo_area.py`, que
calcula el área de triángulos, círculos, rectángulos y trapecios, el
esquema JSON propuesto para una de sus variantes (triángulo) sería:

```json
{
  "name": "calcular_area_triangulo",
  "description": "Calcula el área de un triángulo dada su base y altura.",
  "parameters": {
    "type": "object",
    "properties": {
      "base": {
        "type": "number",
        "description": "Base del triángulo en metros. Debe ser mayor que 0."
      },
      "altura": {
        "type": "number",
        "description": "Altura del triángulo en metros. Debe ser mayor que 0."
      }
    },
    "required": ["base", "altura"]
  }
}
```

Y para la variante de círculo:

```json
{
  "name": "calcular_area_circulo",
  "description": "Calcula el área de un círculo dado su radio.",
  "parameters": {
    "type": "object",
    "properties": {
      "radio": {
        "type": "number",
        "description": "Radio del círculo en metros. Debe ser mayor que 0."
      }
    },
    "required": ["radio"]
  }
}
```

---

## Mapeo entre `Herramienta` y el esquema

| Elemento de `Herramienta` | Elemento del esquema JSON |
|----------------------------|---------------------------|
| `nombre` | usado para derivar `name` (en snake_case) |
| `descripcion` | usado como `description` |
| Campos del formulario (ej. "Base", "Altura") | `properties` del esquema, uno por campo |
| Validaciones de la función de cálculo (ej. `> 0`) | reflejadas en la `description` de cada propiedad |
| Función `calcular` interna (ej. `area_triangulo`) | función real invocada al ejecutar la llamada |

---

## Flujo de invocación propuesto

1. El asistente de IA recibe la lista de esquemas de todas las herramientas disponibles.
2. El usuario hace una solicitud en lenguaje natural (ej. "calcula el área de un triángulo de base 10 y altura 5").
3. El LLM selecciona la función `calcular_area_triangulo` y construye los argumentos `{"base": 10, "altura": 5}`.
4. La aplicación valida los argumentos y llama internamente a `area_triangulo(10, 5)`.
5. El resultado se devuelve al asistente para que lo presente al usuario.

---

## Consideraciones para la implementación futura

* Cada figura dentro de una herramienta multi-figura (como `HerramientaCalculoArea`) debería exponerse como una función independiente en el esquema, no como una sola función con un parámetro de "tipo de figura", para que el LLM pueda elegir directamente la operación correcta.
* Las validaciones que hoy viven en la función de cálculo (ej. lanzar `ValueError` si un valor es negativo) deben reflejarse en el esquema (`minimum`, descripciones claras) para reducir llamadas inválidas del LLM.
* Se recomienda generar el esquema de forma automática a partir de los metadatos de cada `Herramienta`, en lugar de mantenerlo escrito a mano por cada módulo.

---

## Referencias

* `src/escuadra/core/herramienta.py` — clase base de las herramientas actuales.
* `src/escuadra/modulos/geometria/herramienta_calculo_area.py` — ejemplo de herramienta usada como base para este documento.
* `docs/como-agregar-modulo.md` — guía general para agregar nuevos módulos.