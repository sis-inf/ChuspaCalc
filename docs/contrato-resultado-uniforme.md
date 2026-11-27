# 📋 Contrato Uniforme `ResultadoCalculo`

Este documento describe el **contrato uniforme `ResultadoCalculo`**, una estructura estandarizada que todos los módulos de cálculo de ChuspaCalc deben seguir para retornar sus resultados.

---

## 🎯 ¿Qué es `ResultadoCalculo`?

`ResultadoCalculo` es un contrato (interfaz o clase base) que define la estructura común que deben tener los resultados de todas las herramientas de cálculo en ChuspaCalc.

### Propósito

- **Estandarizar** la salida de los módulos de cálculo.
- **Facilitar** la integración con otros componentes (UI, exportadores, etc.).
- **Garantizar** que todos los resultados sean consistentes y predecibles.

---

## 📋 Campos del contrato

| Campo | Tipo | Descripción | Obligatorio |
|-------|------|-------------|-------------|
| `exito` | `bool` | Indica si el cálculo fue exitoso | ✅ Sí |
| `valor` | `float` / `dict` / `list` | Resultado principal del cálculo | ✅ Sí |
| `unidad` | `str` | Unidad del resultado (ej. `"kN·m"`, `"m"`) | ❌ No |
| `mensaje` | `str` | Mensaje adicional (ej. advertencias, notas) | ❌ No |
| `parametros` | `dict` | Parámetros de entrada utilizados | ❌ No |
| `tiempo` | `float` | Tiempo de ejecución en segundos | ❌ No |

---

## 📝 Ejemplo de `ResultadoCalculo`

### Ejemplo en Python

```python
from typing import Optional, Dict, Any

class ResultadoCalculo:
    def __init__(
        self,
        exito: bool,
        valor: Any,
        unidad: Optional[str] = None,
        mensaje: Optional[str] = None,
        parametros: Optional[Dict[str, Any]] = None,
        tiempo: Optional[float] = None,
    ):
        self.exito = exito
        self.valor = valor
        self.unidad = unidad
        self.mensaje = mensaje
        self.parametros = parametros or {}
        self.tiempo = tiempo

    def __repr__(self):
        return f"ResultadoCalculo(exito={self.exito}, valor={self.valor}, unidad={self.unidad})"
