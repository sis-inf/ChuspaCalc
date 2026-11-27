# Configuración de ChuspaCalc

Esta guía describe cómo cargar y utilizar archivos de configuración en ChuspaCalc mediante el módulo `src/ChuspaCalc/config/loader.py`.

## Archivo de configuración

ChuspaCalc permite cargar archivos de configuración en formato YAML.

La carga se realiza mediante la función `load(path)`, la cual recibe la ruta de un archivo YAML y devuelve su contenido como un diccionario de Python.

Ejemplo:

```python
from ChuspaCalc.config.loader import load

config = load("config.yaml")
```

Si el archivo no existe, se genera una excepción `FileNotFoundError`.

Si el contenido YAML es inválido, se genera una excepción `yaml.YAMLError`.

---

## Opciones disponibles

La siguiente tabla muestra la estructura de configuración utilizada en las pruebas del proyecto.

| Clave           | Tipo    | Valor de ejemplo | Descripción                              |
| --------------- | ------- | ---------------- | ---------------------------------------- |
| `database.host` | string  | `localhost`      | Dirección del servidor de base de datos  |
| `database.port` | integer | `5432`           | Puerto de conexión                       |
| `database.name` | string  | `test_db`        | Nombre de la base de datos               |
| `api.timeout`   | integer | `30`             | Tiempo máximo de espera para solicitudes |
| `api.retries`   | integer | `3`              | Cantidad de reintentos ante fallos       |
| `logging.level` | string  | `DEBUG`          | Nivel de detalle de los registros        |
| `logging.file`  | string  | `test.log`       | Archivo donde se almacenan los registros |

---

## Configuración por variables de entorno

Actualmente el módulo de carga de configuración no implementa lectura de variables de entorno.

---

## Ejemplo de configuración

```yaml
database:
  host: localhost
  port: 5432
  name: test_db

api:
  timeout: 30
  retries: 3

logging:
  level: DEBUG
  file: test.log
```

---

## Prioridad de configuración

Actualmente la configuración se obtiene únicamente desde el archivo YAML especificado por el usuario al llamar a la función `load(path)`.

No se encuentra implementada una jerarquía de prioridad entre argumentos de línea de comandos, variables de entorno, archivos de configuración y valores por defecto.

```
```
