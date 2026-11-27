# Publicación del paquete en PyPI

## Descripción

Este documento describe el proceso de publicación del paquete `ChuspaCalc` en PyPI mediante el workflow de release definido en `.github/workflows/release.yml`.

La publicación se inicia automáticamente cuando se realiza un `push` de un tag cuyo nombre comienza con `v`, por ejemplo:

```bash
git tag v0.1.1
git push origin v0.1.1
```

El workflow construye el paquete, verifica los artefactos generados y posteriormente los publica en PyPI.

## Requisitos previos

Antes de realizar una publicación, verificar lo siguiente:

* Contar con permisos para crear y subir tags al repositorio.
* Tener los cambios que se desean publicar integrados en la rama correspondiente.
* Confirmar que las pruebas y verificaciones del proyecto se hayan realizado correctamente antes de crear el tag.
* Verificar que la versión del paquete esté actualizada en `pyproject.toml`.
* Utilizar un número de versión que todavía no haya sido publicado en PyPI.

## Actualización de la versión

La versión del paquete se define en el archivo `pyproject.toml`.

Ejemplo:

```toml
[project]
version = "0.1.0"
```

Antes de generar una nueva publicación, actualizar este valor según la versión que se desea liberar.

La versión debe corresponder con el contenido que se desea publicar y no debe haber sido publicada previamente en PyPI.

## Verificación local

Antes de crear una nueva versión, se recomienda comprobar que el proyecto funciona correctamente.

Ejecutar las pruebas:

```bash
pytest
```

Ejecutar las verificaciones de estilo:

```bash
ruff check .
```

Estas verificaciones son pasos previos recomendados y no son ejecutadas directamente por el workflow `release.yml`.

## Creación del tag

Una vez que los cambios se encuentren integrados y validados, crear un tag para identificar la nueva versión.

Ejemplo:

```bash
git tag v0.1.1
```

Subir el tag al repositorio remoto:

```bash
git push origin v0.1.1
```

El workflow de release se ejecuta automáticamente cuando GitHub recibe un tag cuyo nombre coincide con el patrón `v*`.

Por ejemplo:

```text
v0.1.0
v0.1.1
v1.0.0
```

## Proceso de publicación

El workflow `.github/workflows/release.yml` realiza el proceso de publicación en dos etapas principales.

### 1. Construcción del paquete

El job `build` realiza las siguientes acciones:

1. Obtiene el código del repositorio mediante `actions/checkout@v4`.
2. Configura Python 3.12 mediante `actions/setup-python@v6`.
3. Actualiza `pip` e instala las herramientas `build` y `twine`.
4. Construye las distribuciones del paquete mediante:

```bash
python -m build
```

Este comando genera los artefactos de distribución, como el archivo fuente (`sdist`) y el paquete `wheel`.

Posteriormente, el workflow verifica los artefactos generados mediante:

```bash
twine check dist/*
```

Finalmente, los archivos de `dist/` se almacenan como artefactos del workflow.

### 2. Publicación en PyPI

El job `publish` depende de que el job `build` termine correctamente.

Primero descarga los artefactos generados durante la construcción.

Después utiliza la acción:

```text
pypa/gh-action-pypi-publish@release/v1
```

para publicar los artefactos en PyPI.

El workflow utiliza además el siguiente permiso:

```yaml
permissions:
  id-token: write
```

También configura el entorno de publicación `pypi`.

La dirección configurada para el proyecto es:

`https://pypi.org/project/ChuspaCalc/`

## Verificación de la publicación

Después de completar la publicación:

1. Revisar el resultado de los jobs en GitHub Actions.
2. Confirmar que el workflow haya finalizado correctamente.
3. Verificar que la nueva versión aparezca disponible en PyPI.
4. Verificar que el paquete pueda instalarse correctamente.

## Instalación de prueba

Para comprobar la publicación, instalar el paquete desde PyPI:

```bash
pip install ChuspaCalc
```

También puede instalarse una versión específica:

```bash
pip install ChuspaCalc==0.1.1
```

## Solución de problemas

### La versión ya existe

PyPI no permite publicar dos veces la misma versión. Si una versión ya fue publicada, incrementar el número de versión y generar un nuevo tag.

Por ejemplo, si `v0.1.1` ya fue publicado, utilizar una nueva versión:

```bash
git tag v0.1.2
git push origin v0.1.2
```

### El workflow no se ejecuta

Verificar que el tag utilizado comience con `v`.

Por ejemplo:

```text
v0.1.1
```

El workflow está configurado para ejecutarse mediante:

```yaml
on:
  push:
    tags:
      - "v*"
```

Por lo tanto, un tag que no comience con `v` no activará este workflow.

### Error durante la construcción o verificación

Revisar los registros del job `build` en GitHub Actions para identificar la causa del error.

Los errores pueden producirse durante la instalación de las herramientas, la construcción del paquete o la verificación mediante `twine check`.

### Error durante la publicación

Revisar los registros del job `publish` en GitHub Actions.

También verificar que el workflow tenga configurados los permisos necesarios para realizar la publicación en PyPI y que el entorno `pypi` esté correctamente configurado.

### Error de instalación

Verificar que la versión publicada aparezca correctamente en PyPI y que las dependencias requeridas estén disponibles.

También se puede comprobar nuevamente la instalación con:

```bash
pip install ChuspaCalc
```
