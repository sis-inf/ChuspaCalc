# Generación de ejecutables standalone con PyInstaller

Esta guía describe cómo generar un ejecutable standalone de ChuspaCalc utilizando
PyInstaller y el archivo de configuración `ChuspaCalc.spec` incluido en la raíz
del proyecto.

## Requisitos previos

Antes de generar el ejecutable, asegúrese de contar con:

- Python 3.10 o superior.
- Un entorno virtual activo.
- Las dependencias de desarrollo instaladas.

Si aún no ha instalado las dependencias del proyecto, ejecute:

```bash
pip install -e ".[dev]"
```

Esta instalación incluye PyInstaller como dependencia de desarrollo.

## Archivos utilizados

El proceso de compilación utiliza los siguientes archivos del proyecto:

| Archivo | Descripción |
|---------|-------------|
| `ChuspaCalc.spec` | Configuración utilizada por PyInstaller para generar el ejecutable. |
| `build_app.py` | Script auxiliar que ejecuta PyInstaller utilizando el archivo `.spec`. |

## Comando exacto

Desde la raíz del repositorio ejecute:

```bash
pyinstaller ChuspaCalc.spec
```

También es posible utilizar el script incluido en el proyecto:

```bash
python build_app.py
```

Este script ejecuta internamente el comando anterior utilizando el archivo
`ChuspaCalc.spec`.

> **Importante:** Ejecute cualquiera de los comandos desde la raíz del
> repositorio para que PyInstaller pueda localizar correctamente el archivo
> `ChuspaCalc.spec`.

## Configuración incluida en `ChuspaCalc.spec`

El archivo `ChuspaCalc.spec` define la configuración utilizada durante la
compilación, incluyendo:

- El punto de entrada de la aplicación (`src/ChuspaCalc/app.py`).
- Los módulos adicionales (`hiddenimports`) necesarios para PySide6.
- El nombre del ejecutable generado (`ChuspaCalc`).
- La ejecución como aplicación gráfica (`console=False`).

## Resultado de la compilación

Al finalizar correctamente el proceso, PyInstaller crea los archivos generados
en el directorio:

```text
dist/
```

El ejecutable generado tendrá el nombre **ChuspaCalc** (o **ChuspaCalc.exe** en
Windows).

## Plataformas soportadas

PyInstaller genera ejecutables para el sistema operativo donde se ejecuta la
compilación. No realiza compilación cruzada entre plataformas.

| Plataforma | Soporte |
|------------|---------|
| Windows | ✅ Compatible |
| Linux | ✅ Compatible |
| macOS | ✅ Compatible |

Para distribuir ChuspaCalc en varias plataformas es necesario ejecutar el proceso
de compilación por separado en cada una de ellas.

## Solución de problemas

### PyInstaller no está disponible

Instale las dependencias de desarrollo:

```bash
pip install -e ".[dev]"
```

o instale PyInstaller manualmente:

```bash
pip install pyinstaller
```

### No se genera el directorio `dist`

Verifique que:

- Está ejecutando el comando desde la raíz del proyecto.
- El archivo `ChuspaCalc.spec` existe.
- No hubo errores durante la compilación.

## Documentación relacionada

- [Empaquetado](empaquetado.md)
- [Instalación](instalacion.md)
- [Despliegue](despliegue.md)
