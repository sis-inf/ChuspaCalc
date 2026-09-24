# Cómo contribuir a este proyecto

¡Gracias por querer contribuir a **Escuadra**!

Este proyecto utiliza el **Forking Workflow**, por lo que cada contribuidor trabaja desde su propio fork antes de enviar cambios al repositorio principal.

Lee este documento antes de empezar.

---

# Requisitos previos

| Herramienta | Versión mínima | Verificar con |
|---|---|---|
| Python | 3.10+ | `python --version` |
| Git | 2.30+ | `git --version` |
| pip | incluido con Python | `pip --version` |

---

# Configuración del entorno

Configura el entorno de desarrollo la primera vez que clones el proyecto.

## 1. Crear el entorno virtual

### Windows / Linux / macOS:

```bash
python -m venv .venv
```

## 2. Activar el entorno virtual

### Linux / macOS

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

> El prefijo `(.venv)` en la terminal confirma que el entorno está activo.

## 3. Instalar dependencias de desarrollo
 
### Windows / Linux / macOS:
 
Este proyecto tiene dependencias en dos fuentes: `requirements-dev.txt` para herramientas como `pre-commit` y `build`, y `pyproject.toml` para las dependencias del proyecto.
 
Instala primero las dependencias de desarrollo:
 
```bash
pip install -r requirements-dev.txt
```
 
Luego instala el proyecto en modo editable:
 
```bash
pip install -e ".[dev]"
```
 
Esto instalará las dependencias necesarias para desarrollo, testing y herramientas de calidad de código, además de permitir que los cambios realizados en el código fuente se reflejen automáticamente sin necesidad de reinstalar el paquete.
 
## 4. Instalar los hooks de pre-commit
 
### Windows / Linux / macOS:
 
```bash
pip install pre-commit && pre-commit install
```
 
Este comando instala los hooks de pre-commit configurados por el proyecto. A partir de este momento, cada vez que realices un commit, Git ejecutará automáticamente las verificaciones definidas por el proyecto antes de aceptar el commit.
 
Para verificar que los hooks quedaron instalados correctamente:
 
```bash
pre-commit run --all-files
```
---

# Flujo de trabajo

Este proyecto usa el **Forking Workflow**.

```text
fork → clone → branch → commit → push → Pull Request
```

Nunca trabajes directamente sobre el repositorio principal.

## 1. Haz fork del repositorio

Presiona el botón **Fork** en la esquina superior derecha del repositorio en GitHub.

Tu fork quedará en:

```text
https://github.com/TU-USUARIO/escuadra
```

## 2. Clona tu fork

```bash
git clone https://github.com/TU-USUARIO/escuadra.git
cd escuadra
```

## 3. Agrega el repositorio original como upstream

```bash
git remote add upstream https://github.com/sis-inf/escuadra.git
```

Verifica que quedó correctamente configurado:

```bash
git remote -v
```

Salida esperada:

```text
origin    https://github.com/TU-USUARIO/escuadra.git (fetch)
origin    https://github.com/TU-USUARIO/escuadra.git (push)
upstream  https://github.com/sis-inf/escuadra.git (fetch)
upstream  https://github.com/sis-inf/escuadra.git (push)
```

## 4. Sincroniza antes de trabajar

Haz esto siempre antes de crear una nueva rama:

```bash
git checkout dev
git pull upstream dev
```

## 5. Crea tu rama de trabajo

```bash
git checkout -b tipo/descripcion-corta
```

Ejemplos:

```bash
git checkout -b feat/calculadora-matrices
git checkout -b fix/error-conversion-binaria
git checkout -b docs/guia-instalacion
```

## 6. Trabaja y crea commits pequeños

```bash
git add .
git commit -m "tipo: descripción corta en presente - Closes #N"
```

Ejemplo:

```bash
git commit -m "fix: corregir conversion hexadecimal - Closes #52"
```

## 7. Sube tu rama a tu Fork

```bash
git push origin tipo/descripcion-corta
```

Ejemplo:

```bash
git push origin fix/error-conversion-binaria
```

## 8. Abre un Pull Request

Desde GitHub, abre un Pull Request con esta configuración:

| Campo | Valor |
|---|---|
| Base repository | `sis-inf/escuadra` |
| Base branch | `dev` |
| Head repository | `TU-USUARIO/escuadra` |
| Compare branch | `tu-rama` |

## Recomendaciones para el PR

- Mantén el PR enfocado en un único objetivo
- Describe claramente qué cambiaste y por qué
- Referencia siempre el issue relacionado (`Closes #N`)
- Evita incluir cambios no relacionados
- Añade evidencia si aplica (logs, capturas, etc.)
---

# Convención de ramas

Formato:

```text
tipo/descripcion-corta
```

| Tipo | Cuándo usarlo |
|---|---|
| `feat/` | Nueva funcionalidad |
| `fix/` | Corrección de errores |
| `docs/` | Documentación |
| `test/` | Pruebas |
| `chore/` | Configuración o tareas generales |
| `refactor/` | Mejoras internas sin cambiar comportamiento |
| `security/` | Mejoras de seguridad |
| `data/` | Análisis de datos |

Ejemplos:

```text
feat/calculadora-matrices
fix/error-conversion-binaria
docs/guia-instalacion
test/pruebas-modulo-viga
chore/configurar-github-actions
```

---

# Convención de commits

Formato:

```text
tipo: descripción corta en presente - Closes #N
```

| Tipo | Cuándo usarlo |
|---|---|
| `feat:` | Nueva funcionalidad |
| `fix:` | Corrección de error |
| `docs:` | Documentación |
| `test:` | Pruebas |
| `chore:` | Configuración o CI/CD |
| `refactor:` | Mejora sin cambiar comportamiento |
| `security:` | Mejora de seguridad |
| `data:` | Análisis de datos |

Ejemplos:

```text
feat: agregar calculadora de matrices - Closes #10
fix: corregir conversion hexadecimal - Closes #52
docs: agregar guia de instalacion en Windows - Closes #31
test: agregar pruebas unitarias para modulo viga - Closes #44
```

> Siempre referencia el issue correspondiente usando `Closes #N`.

---

# Reglas importantes

 - ❌  Nunca hagas push directo a `main` o `dev` 
 - ❌  Nunca trabajes directamente sobre `main` o `dev` 
 - ✅  Un issue = una rama = un PR 
 - ✅  Todo PR debe referenciar su issue con `Closes #N` 
 - ✅  Todo PR debe pasar CI antes del merge 
 - ✅  Todo PR requiere al menos una revisión aprobada

---

# Estructura de ramas

| Rama | Propósito |
|---|---|
| `main` | Versión estable — solo recibe merges desde `dev` |
| `dev` | Rama principal de desarrollo |
| `feat/*` | Nuevas funcionalidades |
| `fix/*` | Correcciones |
| `docs/*` | Documentación |
| `test/*` | Pruebas |
| `chore/*` | Configuración |

---

# ¿Por dónde empezar?

Si es tu primera vez contribuyendo:

1. Busca issues abiertos etiquetados como `good first issue`
2. Comenta en el issue que deseas trabajar
3. Espera confirmación antes de empezar
4. Crea tu rama desde `dev`
5. Sigue los pasos de este documento

---

# ¡Gracias por contribuir al proyecto!

Toda contribución grande o pequeña ayuda a mejorar Escuadra.