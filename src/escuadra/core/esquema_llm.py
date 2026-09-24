"""
Exportación del esquema de herramientas de Escuadra en formato JSON Schema
compatible con integraciones de function-calling de LLMs (OpenAI, Anthropic, etc.).

Uso:
    from escuadra.core.esquema_llm import exportar_esquema_llm
    esquema = exportar_esquema_llm()

    # O desde la CLI:
    python -m escuadra.core.esquema_llm
"""

from __future__ import annotations

import json
from escuadra.core.registry import descubrir_herramientas


# Mapa de tipos Python a tipos JSON Schema
_TIPO_JSON: dict[str, str] = {
    "str": "string",
    "int": "integer",
    "float": "number",
    "bool": "boolean",
    "list": "array",
    "dict": "object",
}


def _tipo_json(anotacion: str) -> str:
    """Convierte una anotación de tipo Python a tipo JSON Schema."""
    return _TIPO_JSON.get(anotacion, "string")


def _herramienta_a_funcion(herramienta: type) -> dict:
    """
    Convierte una clase Herramienta al formato de función
    compatible con function-calling de LLMs.

    El esquema generado sigue el estándar usado por OpenAI y Anthropic:
    {
        "name": "nombre_herramienta",
        "description": "descripción de la herramienta",
        "parameters": {
            "type": "object",
            "properties": { ... },
            "required": [ ... ]
        }
    }
    """
    import inspect

    nombre = herramienta.nombre.lower().replace(" ", "_").replace("á", "a") \
        .replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u") \
        .replace("ñ", "n").replace("ü", "u").replace(",", "").replace(".", "")

    descripcion = herramienta.descripcion
    carrera = herramienta.carrera.value if herramienta.carrera else "general"

    propiedades: dict = {}
    requeridos: list[str] = []

    # Inspeccionar métodos públicos que no sean crear_widget ni metadatos
    for nombre_metodo, metodo in inspect.getmembers(herramienta, predicate=inspect.isfunction):
        if nombre_metodo.startswith("_") or nombre_metodo in ("crear_widget", "metadatos"):
            continue

        sig = inspect.signature(metodo)
        params_metodo: dict = {}
        req_metodo: list[str] = []

        for param_nombre, param in sig.parameters.items():
            if param_nombre in ("self", "cls"):
                continue

            anotacion = "string"
            if param.annotation != inspect.Parameter.empty:
                anotacion = _tipo_json(param.annotation.__name__
                                       if hasattr(param.annotation, "__name__")
                                       else str(param.annotation))

            params_metodo[param_nombre] = {
                "type": anotacion,
                "description": f"Parámetro '{param_nombre}' de {nombre_metodo}",
            }

            if param.default is inspect.Parameter.empty:
                req_metodo.append(param_nombre)

        if params_metodo:
            propiedades[nombre_metodo] = {
                "type": "object",
                "description": f"Llamar al método {nombre_metodo}",
                "properties": params_metodo,
                "required": req_metodo,
            }

    # Si no hay métodos con parámetros, usar esquema genérico
    if not propiedades:
        propiedades = {
            "entrada": {
                "type": "string",
                "description": "Valor de entrada para la herramienta",
            }
        }
        requeridos = ["entrada"]

    return {
        "name": nombre,
        "description": f"[{carrera}] {descripcion}",
        "parameters": {
            "type": "object",
            "properties": propiedades,
            "required": requeridos,
        },
    }


def exportar_esquema_llm() -> list[dict]:
    """
    Exporta el esquema de todas las herramientas del registry
    en formato function-calling compatible con LLMs.

    Returns:
        Lista de diccionarios con el esquema de cada herramienta.
    """
    herramientas = descubrir_herramientas()
    return [_herramienta_a_funcion(h) for h in herramientas]


def exportar_esquema_json(indent: int = 2) -> str:
    """
    Exporta el esquema como string JSON.

    Args:
        indent: Indentación del JSON (por defecto 2).

    Returns:
        String JSON con el esquema de todas las herramientas.
    """
    return json.dumps(exportar_esquema_llm(), ensure_ascii=False, indent=indent)


if __name__ == "__main__":
    print(exportar_esquema_json())
