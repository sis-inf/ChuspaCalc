# Módulos de Herramientas

Este paquete contiene las herramientas organizadas por carrera.

## Convención de nombres

Cada herramienta es un archivo Python con el prefijo `herramienta_`:

`src/ChuspaCalc/modulos/<carrera>/herramienta_<nombre_corto>.py`

Ejemplos:
- `src/ChuspaCalc/modulos/sistemas/herramienta_conversion_bases.py`
- `src/ChuspaCalc/modulos/electrica/herramienta_ley_ohm.py`

## Estructura de carpetas
├── sistemas/
├── matematicas/
└── electrica/
## Esqueleto de una herramienta

```python
from ChuspaCalc.base import Herramienta
from PySide6.QtWidgets import QWidget

class HerramientaNombreCorto(Herramienta):
    nombre = "Nombre de la herramienta"
    carrera = "sistemas"
    descripcion = "Descripción breve de lo que hace."

    def crear_widget(self) -> QWidget:
        raise NotImplementedError
```

## Reglas

1. Una herramienta por archivo.
2. El archivo debe exportar una única clase que herede de `Herramienta`.
3. La clase debe declarar `nombre`, `carrera` y `descripcion` como atributos de clase.
4. La clase debe implementar `crear_widget()` que devuelve un `QWidget`.