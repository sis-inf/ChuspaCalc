# Estilo de Commits

## Introducción

El proyecto **ChuspaCalc** utiliza la especificación **Conventional Commits** para mantener un historial de cambios claro, consistente y fácil de entender.

Seguir una convención para los mensajes de commit facilita la revisión de cambios, mejora la trazabilidad del proyecto y permite identificar rápidamente el propósito de cada modificación.

Para garantizar que todos los commits cumplan este estándar, el proyecto utiliza un **hook de pre-commit** que valida automáticamente el formato del mensaje antes de aceptar el commit.

---

# Formato del mensaje

Todos los commits deben seguir el siguiente formato:

```text
tipo(ámbito): descripción
```

El **ámbito** es opcional. Si el cambio no pertenece a un componente específico del proyecto, puede omitirse.

Por ejemplo:

```text
tipo: descripción
```

La descripción debe ser breve, clara y estar escrita en presente.

---

# Tipos permitidos

El hook acepta únicamente los siguientes tipos de commit:

| Tipo     | Descripción                                                |
| -------- | ---------------------------------------------------------- |
| feat     | Nueva funcionalidad.                                       |
| fix      | Corrección de errores.                                     |
| docs     | Cambios en la documentación.                               |
| chore    | Tareas de mantenimiento, configuración o dependencias.     |
| test     | Agregar o modificar pruebas.                               |
| refactor | Reestructuración del código sin cambiar su comportamiento. |
| style    | Cambios de formato o estilo sin modificar la lógica.       |
| ci       | Cambios relacionados con integración continua (CI/CD).     |

---

# Uso del ámbito

El ámbito indica qué parte del proyecto fue modificada. Aunque es opcional, se recomienda utilizarlo cuando ayude a identificar el componente afectado.

Algunos ámbitos comunes son:

* cli
* docs
* core
* config
* io
* ui
* civil
* electrica
* geometria
* matematicas
* sistemas

---

# Ejemplos de commits válidos

```text
feat: agregar calculadora de matrices
```

```text
fix(cli): manejar error de módulo no encontrado
```

```text
docs: actualizar guía de instalación
```

```text
fix(docs): actualizar instrucciones de desarrollo local
```

```text
test(math): agregar pruebas para el solucionador lineal
```

```text
refactor(core): simplificar inicialización del proyecto
```

```text
style(ui): aplicar formato al código
```

```text
ci: actualizar flujo de GitHub Actions
```

---

# Ejemplos de commits inválidos

Los siguientes mensajes no cumplen con la convención y serán rechazados por el hook:

```text
arreglo bug
```

```text
Cambios varios
```

```text
nuevo commit
```

```text
bug corregido
```

```text
fix
```

```text
docs
```

```text
actualización
```

---

# Referencias a issues

Si tu commit cierra un issue, sigue incluyendo **`Closes #N`**, tal como se indica en **CONTRIBUTING.md**.

Ejemplo:

```text
fix(cli): manejar error de módulo no encontrado - Closes #52
```

El hook valida únicamente que el mensaje comience con el formato:

```text
tipo(ámbito): descripción
```

Todo el contenido que aparezca después (como `Closes #52`) no afecta la validación del mensaje.

---

# Validación automática

El proyecto utiliza el hook **conventional-pre-commit** para verificar automáticamente el formato del mensaje de commit.

La configuración del hook se encuentra en:

```text
.pre-commit-config.yaml
```

Una vez instalado, Git ejecutará esta validación antes de crear cada commit.

Si el mensaje no cumple con la convención definida, el commit será rechazado.

---

# Instalación del hook

Después de clonar el repositorio e instalar las dependencias de desarrollo, instala los hooks con:

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

El segundo comando instala el hook encargado de validar los mensajes de commit.

---

# Comprobación del funcionamiento

### Ejemplo de mensaje rechazado

```bash
git commit --allow-empty -m "arreglo bug"
```

Resultado esperado:

```text
Commit message validation failed.
```

### Ejemplo de mensaje aceptado

```bash
git commit --allow-empty -m "fix(cli): manejar error de módulo no encontrado"
```

El commit será aceptado porque cumple con el formato definido por Conventional Commits.

---

# ¿Qué hago si mi commit es rechazado?

Si el hook rechaza el mensaje del commit, simplemente corrige el mensaje y vuelve a intentarlo.

Puedes editar el mensaje con:

```bash
git commit --edit --file=.git/COMMIT_EDITMSG
```

O volver a ejecutar el comando `git commit` utilizando un mensaje que siga la convención establecida.

---

# Recomendaciones

* Utiliza descripciones breves y claras.
* Escribe la descripción en presente.
* Mantén un único propósito por commit.
* Usa el tipo de commit que mejor describa el cambio realizado.
* Utiliza un ámbito cuando facilite identificar el componente afectado.
* Incluye `Closes #N` cuando el commit resuelva un issue.
