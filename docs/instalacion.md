# Guía de instalación de la suite ChuspaCalc

Esta guía cubre todos los pasos necesarios para instalar **ChuspaCalc**, tanto para usuarios que desean utilizar las herramientas disponibles como para colaboradores que desean contribuir al desarrollo del proyecto.

## Requisitos previos

Antes de instalar la suite ChuspaCalc, asegúrate de tener instalado lo siguiente:

- **Sistema operativo:** Linux (Ubuntu/Debian recomendado), macOS o Windows (con WSL2)
- **Python:** Versión 3.10 o superior
- **pip:** Versión 22 o superior
- **Git:** Para clonar y sincronizar el repositorio

### Verificar versiones instaladas

```bash
python --version   # debe ser v3.10 o superior
pip --version      # debe ser v22 o superior
git --version      # debe estar instalado

Los resultados deben indicar versiones compatibles con los requisitos mínimos del proyecto.

> **Nota:** En algunos sistemas Linux y macOS, el comando puede ser `python3` en lugar de `python`.

---

# Instalación rápida

Esta modalidad está orientada a usuarios que únicamente desean utilizar la aplicación sin realizar modificaciones al código fuente.

## 1. Clonar el repositorio

```bash
git clone https://github.com/sis-inf/ChuspaCalc.git
cd ChuspaCalc
```

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

Este comando instalará todas las dependencias necesarias para ejecutar la aplicación.

## 3. Ejecutar la aplicación

```bash
python -m ChuspaCalc
```

Si el paquete está disponible como comando ejecutable:

```bash
ChuspaCalc
```

---

# Instalación para desarrollo

Esta modalidad está dirigida a estudiantes y colaboradores que desean contribuir al proyecto.

## 1. Crear un fork

Desde GitHub, crea un fork del repositorio principal en tu cuenta.

Posteriormente clona tu fork:

```bash
git clone https://github.com/TU-USUARIO/ChuspaCalc.git
cd ChuspaCalc
```

## 2. Configurar el repositorio original como upstream

Para poder sincronizar los cambios realizados en el repositorio principal, agrega el repositorio original como remoto adicional:

```bash
git remote add upstream https://github.com/sis-inf/ChuspaCalc.git
```

Verifica la configuración:

```bash
git remote -v
```

Deberías observar referencias tanto a tu fork (`origin`) como al repositorio principal (`upstream`).

## 3. Crear un entorno virtual

Se recomienda utilizar un entorno virtual para aislar las dependencias del proyecto y evitar conflictos con otras instalaciones de Python.

```bash
python -m venv .venv
```

## 4. Activar el entorno virtual

### Linux y macOS

```bash
source .venv/bin/activate
```

### Windows (CMD)

```cmd
.venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

Cuando el entorno esté activo, la terminal mostrará un prefijo similar a:

```text
(.venv)
```

## 5. Instalar el proyecto en modo editable

```bash
pip install -e .
```

El modo editable permite que los cambios realizados en el código fuente se reflejen inmediatamente sin necesidad de reinstalar el paquete.

## 6. Instalar dependencias de desarrollo

```bash
pip install -e ".[dev]"
```

Este comando instala las dependencias utilizadas para pruebas, validación de código y herramientas de apoyo al desarrollo.

## 7. Instalar hooks de pre-commit

```bash
pre-commit install
```

Los hooks de pre-commit ejecutan verificaciones automáticas antes de cada commit, ayudando a detectar problemas de formato o calidad de código antes de enviar cambios al repositorio.

---

# Verificación de la instalación

Una vez finalizada la instalación, es recomendable verificar que todo funciona correctamente.

## Verificar que la aplicación responde

```bash
ChuspaCalc --help
```

o

```bash
python -m ChuspaCalc
```

La aplicación debería iniciarse sin errores.

## Ejecutar las pruebas

```bash
python -m pytest
```

Si todas las pruebas finalizan correctamente, el entorno está configurado adecuadamente.

## Verificar calidad del código

```bash
ruff check .
```

Este comando valida que el código cumple con los estándares definidos por el proyecto.

---

# Desinstalación

## Desinstalar el paquete

```bash
pip uninstall ChuspaCalc
```

## Eliminar el entorno virtual

Si utilizaste un entorno virtual, también puedes eliminarlo junto con todas las dependencias instaladas.

### Linux y macOS

```bash
deactivate
rm -rf .venv
```

### Windows

```cmd
deactivate
rmdir /s /q .venv
```

## Eliminar el repositorio local

Si ya no necesitas el código fuente:

### Linux y macOS

```bash
cd ..
rm -rf ChuspaCalc
```

### Windows

```cmd
cd ..
rmdir /s /q ChuspaCalc
```

---

# Solución de problemas comunes

### `python: command not found`

Verifica que Python esté instalado correctamente y agregado al PATH del sistema. En algunos sistemas puede ser necesario utilizar:

```bash
python3 --version
```

### `pip install -e ".[dev]"` falla

Asegúrate de que el entorno virtual esté activo antes de instalar dependencias y verifica que tu versión de pip esté actualizada.

### `ChuspaCalc --help` no funciona

Comprueba que la instalación haya finalizado correctamente y que el entorno virtual se encuentre activo.

### Los hooks de pre-commit fallan

Ejecuta manualmente las herramientas de validación para identificar el problema:

```bash
ruff check .
```
## 📦 Instalación con pipx (recomendada para CLI)

[pipx](https://pipx.pypa.io/) instala el paquete en un entorno virtual aislado, evitando conflictos de dependencias con otros paquetes del sistema.

### Requisitos previos

- Python 3.8 o superior
- pipx instalado

```bash
pip install pipx
pipx ensurepath




Instalación de ChuspaCalc
bash
pipx install ChuspaCalc
Verificar la instalación
bash
ChuspaCalc --version
Ejecutar el CLI
bash
ChuspaCalc --help
