# Modo de depuración con trazas intermedias

Este documento explica cómo activar el modo de depuración en ChuspaCalc y qué herramientas lo soportan.

## ¿Qué es el modo de depuración?

El modo de depuración permite visualizar los pasos intermedios del cálculo durante la ejecución de las herramientas. En lugar de mostrar únicamente el resultado final, el sistema registra cada etapa del proceso, lo que facilita identificar errores, verificar valores parciales y entender el flujo interno de cada operación.

## Cómo activarlo

El modo de depuración se activa estableciendo el nivel de log en `DEBUG` dentro del archivo de configuración YAML del proyecto.

### Mediante archivo de configuración

Edita o crea un archivo `config.yaml` con el siguiente contenido:

```yaml
logging:
  level: DEBUG
  file: ChuspaCalc-debug.log
```

Luego carga la configuración en tu entorno:

```python
from ChuspaCalc.config.loader import load

config = load("config.yaml")
```

Con esta configuración activa, el sistema registrará las trazas intermedias de cada operación en el archivo indicado.

### Nivel de log recomendado por entorno

| Entorno     | Nivel recomendado |
| ----------- | ----------------- |
| Desarrollo  | `DEBUG`           |
| Pruebas     | `DEBUG`           |
| Producción  | `WARNING`         |

## Herramientas que soportan trazas intermedias

Las siguientes herramientas de ChuspaCalc generan pasos intermedios visibles al activar el modo de depuración:

| Herramienta              | Módulo      | Trazas generadas                                          |
| ------------------------ | ----------- | --------------------------------------------------------- |
| Sistemas de ec. lineales | Matemáticas | Matriz aumentada en cada paso de eliminación gaussiana    |
| Calculadora científica   | Matemáticas | Expresión parseada y resultado de cada suboperación       |
| Conversión de bases      | Sistemas    | Divisiones sucesivas y restos en cada paso                |
| Complemento a 2          | Sistemas    | Representación binaria intermedia antes de complementar   |
| Tablas de verdad         | Sistemas    | Evaluación de cada fila antes de construir la tabla final |
| Ley de Ohm               | Eléctrica   | Magnitud calculada y fórmula aplicada en cada paso        |
| Divisor de tensión       | Eléctrica   | Valores intermedios de R1, R2 y Vout                      |
| Cálculo de áreas         | Geometría   | Fórmula seleccionada y sustitución de valores             |

## Ejemplo de salida con modo DEBUG activo

Al resolver un sistema de ecuaciones lineales con el modo de depuración activado, el log registra cada paso de la eliminación gaussiana: