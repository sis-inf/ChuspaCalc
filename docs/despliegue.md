# Guía de Despliegue

Esta guía describe el proceso de instalación y ejecución de ChuspaCalc en sistemas Windows, Linux y macOS. Incluye la configuración del entorno virtual, la instalación del proyecto mediante pip y la verificación del funcionamiento de la interfaz de línea de comandos (CLI).

---

# Prerrequisitos

Antes de instalar ChuspaCalc, asegúrese de tener instalado:

* Python 3.10 o superior
* pip (incluido con Python)
* Git

> ChuspaCalc requiere Python 3.10 o superior. Versiones anteriores no están soportadas.

Verificar las versiones instaladas:

```bash
python --version
pip --version
git --version
```

> En algunos sistemas Linux o macOS puede ser necesario utilizar `python3` en lugar de `python`.

---

# Obtener el código fuente

## Clonar el repositorio

Si desea utilizar ChuspaCalc como usuario:

```bash
git clone https://github.com/sis-inf/ChuspaCalc.git
cd ChuspaCalc
```

Si trabaja mediante el flujo de contribución del proyecto, clone primero su fork personal:

```bash
git clone https://github.com/TU-USUARIO/ChuspaCalc.git
cd ChuspaCalc
```

Para más detalles sobre el flujo de contribución consulte:

```text
docs/guia-contribuidor-primeros-pasos.md
```

---

# Entorno virtual en Linux/macOS

Crear el entorno virtual:

```bash
python -m venv .venv
```

Activarlo:

```bash
source .venv/bin/activate
```

Cuando el entorno esté activo, la terminal mostrará un prefijo similar a:

```text
(.venv)
```

---

# Entorno virtual en Windows

Crear el entorno virtual:

```powershell
python -m venv .venv
```

Activar en PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Activar en CMD:

```cmd
.venv\Scripts\activate
```

Cuando el entorno esté activo, la terminal mostrará un prefijo similar a:

```text
(.venv)
```

---

# Instalación con pip

Desde el directorio raíz del proyecto ejecutar:

```bash
pip install -e .
```

La opción `-e` (*editable*) instala el proyecto enlazándolo al código fuente local. Esto permite que los cambios realizados en el código se reflejen inmediatamente sin necesidad de reinstalar el paquete.

La instalación registra además el comando:

```bash
chuspacalc
```

definido en el archivo `pyproject.toml`.

---

# Dependencias de desarrollo (opcional)

Si va a contribuir al proyecto o ejecutar pruebas, instale también las dependencias de desarrollo:

```bash
pip install -e ".[dev]"
```

Estas dependencias incluyen herramientas para pruebas, validación de código y empaquetado.

---

# Verificar la instalación

Verificar que ChuspaCalc esté disponible:

```bash
chuspacalc --help
```

Consultar la versión instalada:

```bash
chuspacalc --version
```

También es posible ejecutar la aplicación mediante:

```bash
python -m chuspacalc --help
```

Si la instalación fue exitosa, se mostrará la ayuda de la aplicación o la versión instalada.

---

# Ejecución

Mostrar la ayuda general:

```bash
chuspacalc --help
```

Ejecutar el paquete directamente:

```bash
python -m chuspacalc
```

---

# Desactivar el entorno virtual

Cuando finalice su sesión de trabajo:

```bash
deactivate
```

---

# Problemas comunes

## El comando `python` no es reconocido

Verifique que Python esté instalado correctamente y agregado al PATH del sistema.

## El comando `pip` no es reconocido

Reinstale Python asegurándose de habilitar la opción:

```text
Add Python to PATH
```

durante la instalación.

## El comando `chuspacalc` no funciona

Verifique que:

1. El entorno virtual esté activo.
2. La instalación se haya realizado correctamente.
3. Se haya ejecutado:

```bash
pip install -e .
```

## Error por dependencias faltantes

Reinstale las dependencias del proyecto:

```bash
pip install -e .
```

---
# Verificación de integridad de los ejecutables

Las versiones publicadas mediante GitHub Releases incluyen un archivo `SHA256SUMS.txt` junto al ejecutable. Este archivo contiene el checksum SHA256 del ejecutable distribuido y permite verificar que la descarga no haya sido modificada o corrompida.

## Linux

Ejecute el siguiente comando desde el directorio donde se encuentran el ejecutable y `SHA256SUMS.txt`:

```bash
sha256sum -c SHA256SUMS.txt
```

Si la verificación es correcta, se mostrará un resultado similar a:

```text
chuspacalc: OK
```

## macOS

Calcule el checksum del ejecutable:

```bash
shasum -a 256 chuspacalc
```

Compare el valor obtenido con el correspondiente en `SHA256SUMS.txt`.

## Windows (PowerShell)

Calcule el checksum mediante:

```powershell
Get-FileHash .\chuspacalc -Algorithm SHA256
```

Compare el valor mostrado con el registrado en `SHA256SUMS.txt`.

---

# Documentación relacionada

* README.md
* docs/guia-contribuidor-primeros-pasos.md
* docs/arquitectura.md
* pyproject.toml